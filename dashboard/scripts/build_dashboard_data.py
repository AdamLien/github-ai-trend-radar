#!/usr/bin/env python3
"""Build compact browser data from daily GitHub radar snapshots."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DAILY = ROOT / "outputs" / "github-radar" / "daily"
OUT = ROOT / "dashboard" / "src" / "generated" / "radarData.json"


def tags_for(repo: dict) -> list[str]:
    text = " ".join([
        repo.get("description", ""),
        " ".join(repo.get("topics", [])),
        repo["full_name"],
    ]).lower()
    checks = [
        ("MCP", ("mcp", "model context protocol")),
        ("Agent", ("agent", "claude-code", "codex", "cursor")),
        ("Skills", ("skill",)),
        ("RAG", ("rag", "retrieval", "knowledge graph")),
        ("Wiki", ("wiki", "knowledge-management", "obsidian", "knowledge base")),
        ("LLM", ("llm", "language model")),
    ]
    return [label for label, needles in checks if any(needle in text for needle in needles)] or ["AI"]


def category_for(repo: dict, delta: int, tags: list[str]) -> str:
    if not repo.get("license") or repo.get("license") == "NOASSERTION":
        return "Watch"
    if delta >= 400:
        return "Deep research"
    if "Skills" in tags and delta >= 80:
        return "Skill candidate"
    if delta >= 100:
        return "Demo/content idea"
    return "Reference only"


def main() -> None:
    snapshots: list[tuple[str, dict[str, dict]]] = []
    for path in sorted(DAILY.glob("*/repos.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        snapshot_date = payload.get("snapshot_date") or path.parent.name
        snapshots.append((snapshot_date, {repo["full_name"]: repo for repo in payload["repos"]}))
    if not snapshots:
        raise SystemExit(f"No snapshots found in {DAILY}")

    history: dict[str, list[dict]] = defaultdict(list)
    for snapshot_date, repos in snapshots:
        for name, repo in repos.items():
            history[name].append({"date": snapshot_date, "stars": repo["stars"]})

    latest_date, latest = snapshots[-1]
    previous = snapshots[-2][1] if len(snapshots) > 1 else {}
    records = []
    for name, repo in latest.items():
        prior = previous.get(name, repo)
        delta = max(0, repo["stars"] - prior["stars"])
        tags = tags_for(repo)
        series = history[name]
        records.append({
            "name": name,
            "url": repo["html_url"],
            "description": repo.get("description", ""),
            "stars": repo["stars"],
            "forks": repo["forks"],
            "issues": repo["open_issues"],
            "delta": delta,
            "relativeGrowth": round(delta / max(repo["stars"], 1) * 100, 3),
            "tags": tags,
            "category": category_for(repo, delta, tags),
            "license": repo.get("license") or "Unclear",
            "pushedAt": (repo.get("pushed_at") or "")[:10],
            "releaseAt": (repo.get("latest_release", {}).get("published_at") or "")[:10],
            "series": series,
        })
    records.sort(key=lambda item: (item["delta"], item["relativeGrowth"]), reverse=True)
    output = {
        "updatedAt": latest_date,
        "historyDates": [item[0] for item in snapshots],
        "repoCount": len(records),
        "records": records,
        "source": "GitHub API snapshots. GitHub Trending is intentionally excluded from time-series deltas.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} with {len(records)} repositories from {len(snapshots)} snapshots.")


if __name__ == "__main__":
    main()
