#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import multiprocessing as mp
import re
import time
from pathlib import Path
from queue import Empty
from typing import Callable

import fitz
from pypdf import PdfReader, PdfWriter


def sample_pages(total: int) -> list[int]:
    if total <= 9:
        return list(range(1, total + 1))
    mid = max(2, total // 2)
    return sorted({1, 2, 3, mid - 1, mid, mid + 1, total - 2, total - 1, total})


def safe_stem(path: Path) -> str:
    return re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", path.stem)[:120]


def page_count(path: str) -> int:
    return fitz.open(path).page_count


def pymupdf_extract(path: str, pages: list[int]) -> str:
    doc = fitz.open(path)
    chunks = []
    for page_no in pages:
        chunks.append(f"\n\n<!-- page {page_no} -->\n")
        chunks.append(doc[page_no - 1].get_text("text") or "")
    return "".join(chunks)


def pypdf_extract(path: str, pages: list[int]) -> str:
    reader = PdfReader(path)
    chunks = []
    for page_no in pages:
        chunks.append(f"\n\n<!-- page {page_no} -->\n")
        chunks.append(reader.pages[page_no - 1].extract_text() or "")
    return "".join(chunks)


def make_sample_pdf(path: str, pages: list[int], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(path)
    writer = PdfWriter()
    for page_no in pages:
        writer.add_page(reader.pages[page_no - 1])
    with output.open("wb") as fh:
        writer.write(fh)


def markitdown_extract(path: str, pages: list[int], output: Path) -> str:
    from markitdown import MarkItDown

    make_sample_pdf(path, pages, output)
    return MarkItDown().convert(str(output)).text_content or ""


def worker(fn: Callable, args: tuple, queue: mp.Queue) -> None:
    start = time.perf_counter()
    try:
        text = fn(*args)
        queue.put({"status": "ok", "text": text, "seconds": time.perf_counter() - start, "error": ""})
    except Exception as exc:
        queue.put({"status": "error", "text": "", "seconds": time.perf_counter() - start, "error": repr(exc)})


def run_timeout(fn: Callable, args: tuple, timeout: int) -> dict:
    queue: mp.Queue = mp.Queue()
    proc = mp.Process(target=worker, args=(fn, args, queue))
    proc.start()
    proc.join(timeout)
    if proc.is_alive():
        proc.terminate()
        proc.join(3)
        return {"status": "timeout", "text": "", "seconds": timeout, "error": f"timeout after {timeout}s"}
    try:
        return queue.get_nowait()
    except Empty:
        return {"status": "error", "text": "", "seconds": 0, "error": "worker produced no result"}


def token_set(text: str) -> set[str]:
    return set(re.findall(r"[A-Za-z0-9_]{2,}", text.lower()) + re.findall(r"[\u3400-\u9fff]", text))


def jaccard(left: str, right: str) -> float:
    a, b = token_set(left), token_set(right)
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def metrics(text: str) -> dict:
    return {
        "chars": len(text),
        "cjk_chars": len(re.findall(r"[\u3400-\u9fff]", text)),
        "numeric_tokens": len(re.findall(r"\d+(?:[.,]\d+)*", text)),
        "non_empty_lines": sum(1 for line in text.splitlines() if line.strip()),
    }


def verdict(rows: dict[str, dict]) -> str:
    md = rows.get("markitdown")
    base = rows.get("pymupdf")
    if not md or md["status"] != "ok":
        return "markitdown_failed"
    if md["chars"] == 0:
        return "markitdown_empty"
    if base and base["chars"]:
        ratio = md["chars"] / base["chars"]
        if ratio < 0.55:
            return "markitdown_may_miss_content"
        if ratio > 1.7:
            return "markitdown_may_duplicate_or_hidden_text"
    return "sample_usable"


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark sampled PDF extraction methods.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("outputs/pdf-benchmark"))
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--skip-markitdown", action="store_true")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    total = page_count(str(args.pdf))
    pages = sample_pages(total)
    stem = safe_stem(args.pdf)
    sample_pdf = args.out_dir / "sample_pdfs" / f"{stem}.sample.pdf"

    raw = {
        "pymupdf": run_timeout(pymupdf_extract, (str(args.pdf), pages), args.timeout),
        "pypdf": run_timeout(pypdf_extract, (str(args.pdf), pages), args.timeout),
    }
    if not args.skip_markitdown:
        raw["markitdown"] = run_timeout(markitdown_extract, (str(args.pdf), pages, sample_pdf), args.timeout)

    rows = {}
    for method, result in raw.items():
        row = {
            "file": str(args.pdf),
            "pages": total,
            "sample_pages": ",".join(map(str, pages)),
            "method": method,
            "status": result["status"],
            "seconds": round(float(result["seconds"]), 3),
            "error": result["error"],
            **metrics(result["text"]),
        }
        rows[method] = row
        suffix = "md" if method == "markitdown" else "txt"
        (args.out_dir / method).mkdir(parents=True, exist_ok=True)
        (args.out_dir / method / f"{stem}.{suffix}").write_text(result["text"], encoding="utf-8")

    base_text = raw.get("pymupdf", {}).get("text", "")
    for method, row in rows.items():
        row["jaccard_vs_pymupdf"] = round(jaccard(raw[method]["text"], base_text), 4)
        row["verdict"] = verdict(rows)

    csv_path = args.out_dir / f"{stem}.metrics.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(next(iter(rows.values())).keys()))
        writer.writeheader()
        writer.writerows(rows.values())

    summary = {
        "file": str(args.pdf),
        "pages": total,
        "sample_pages": pages,
        "verdict": verdict(rows),
        "metrics_csv": str(csv_path),
        "methods": rows,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
