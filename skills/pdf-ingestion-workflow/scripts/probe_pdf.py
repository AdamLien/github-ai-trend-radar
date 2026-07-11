#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import fitz


def sample_pages(total: int) -> list[int]:
    if total <= 9:
        return list(range(1, total + 1))
    mid = max(2, total // 2)
    return sorted({1, 2, 3, mid - 1, mid, mid + 1, total - 2, total - 1, total})


def probe(path: Path) -> dict:
    doc = fitz.open(path)
    total = doc.page_count
    pages = []
    for page_no in sample_pages(total):
        text = doc[page_no - 1].get_text("text") or ""
        pages.append(
            {
                "page": page_no,
                "chars": len(text),
                "cjk_chars": len(re.findall(r"[\u3400-\u9fff]", text)),
                "numeric_tokens": len(re.findall(r"\d+(?:[.,]\d+)*", text)),
                "low_text": len(text.strip()) < 80,
            }
        )
    low = sum(1 for page in pages if page["low_text"])
    return {
        "file": str(path),
        "bytes": path.stat().st_size,
        "pages": total,
        "sample_pages": [page["page"] for page in pages],
        "sample_low_text_pages": low,
        "sample_low_text_ratio": round(low / len(pages), 3) if pages else 0,
        "likely_needs_ocr": bool(pages and low / len(pages) > 0.25),
        "pages_detail": pages,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Probe PDF page text density.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = probe(args.pdf)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print(f"file: {result['file']}")
    print(f"pages: {result['pages']}")
    print(f"sample_pages: {','.join(map(str, result['sample_pages']))}")
    print(f"low_text_ratio: {result['sample_low_text_ratio']}")
    print(f"likely_needs_ocr: {result['likely_needs_ocr']}")


if __name__ == "__main__":
    main()
