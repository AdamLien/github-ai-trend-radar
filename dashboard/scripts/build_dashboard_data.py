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
        ("Agent", ("agent", "claude-code", "codex", "cursor", "openclaw")),
        ("Skills", ("skill",)),
        ("Coding", ("coding", "codebase", "code review", "ast parsing")),
        ("Automation", ("workflow", "automation", "orchestrat", "harness")),
        ("Research", ("research", "deep research")),
        ("RAG", ("rag", "retrieval", "knowledge graph")),
        ("Knowledge", ("wiki", "knowledge-management", "obsidian", "knowledge base", "knowledge graph")),
        ("LLM", ("llm", "language model")),
    ]
    return [label for label, needles in checks if any(needle in text for needle in needles)] or ["AI"]


PURPOSE_ZH = {
    "Graphify-Labs/graphify": "把程式碼、文件、SQL schema、設定與 PDF 轉成可查詢的知識圖譜，提供 Claude Code、Cursor、Codex 等工具使用。",
    "earendil-works/pi": "提供統一 LLM API、agent loop、終端介面與 coding agent CLI 的 AI agent 工具組。",
    "obra/superpowers": "將 agentic 開發方法整理成可重複使用的 skills 與軟體開發工作法。",
    "DietrichGebert/ponytail": "讓 AI agent 採取更精簡、偏資深工程師式的程式設計決策。",
    "affaan-m/ECC": "面向 Claude Code、Codex、Cursor 等的 agent harness 效能優化系統，涵蓋 skills、記憶、安全與 research-first 開發。",
    "nextlevelbuilder/ui-ux-pro-max-skill": "提供跨平台專業 UI/UX 設計智慧的 AI skill。",
    "farion1231/cc-switch": "整合 Claude Code、Codex、OpenCode、OpenClaw、Grok 等工具的跨平台桌面助手。",
    "headroomlabs-ai/headroom": "在內容送入 LLM 前壓縮工具輸出、log、檔案與 RAG chunks，以降低 coding agent 的 token 成本。",
    "addyosmani/agent-skills": "為 AI coding agent 提供可上線使用的工程技能與工作流程。",
    "JCodesMore/ai-website-cloner-template": "用 AI coding agent 一個指令複製網站的開發模板。",
    "langgenius/dify": "在雲端、VPC 或自架環境建立 agent workflow 與 RAG pipeline 的協作平台。",
    "shareAI-lab/learn-claude-code": "用 Bash 從零理解並實作精簡版 Claude Code 類 agent harness 的學習專案。",
}


def purpose_zh(name: str, tags: list[str]) -> str:
    if name in PURPOSE_ZH:
        return PURPOSE_ZH[name]
    tag_names = {
        "MCP": "MCP", "Agent": "AI agent", "Skills": "skills", "Coding": "開發工具",
        "Automation": "自動化", "Research": "研究", "RAG": "RAG", "Knowledge": "知識管理",
        "LLM": "LLM", "AI": "AI",
    }
    focus = "、".join(tag_names[tag] for tag in tags[:3])
    return f"聚焦 {focus} 的開源工具；可切換 English 查看專案原始 README 用途說明。"


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
            "descriptionZh": purpose_zh(name, tags),
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
