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
    "Leonxlnx/taste-skill": "為 AI coding agent 加入設計品味與反制制式化輸出的 skill。",
    "Vincentwei1021/video-shotcraft": "供 Claude Code 與 Codex 製作產品影片的 Remotion skill，含鏡頭腳本與動態範本。",
    "esengine/DeepSeek-Reasonix": "為終端機打造、針對 prefix cache 穩定性優化的 DeepSeek coding agent。",
    "calesthio/OpenMontage": "把 AI coding assistant 擴充成影片製作工作室的 agentic 影片生產系統。",
    "coreyhaines31/marketingskills": "提供 CRO、文案、SEO、分析與成長工程等行銷 skills 給 AI agent。",
    "ruvnet/ruflo": "可協調多 agent swarm、記憶與 RAG 的 meta-harness 與工作流框架。",
    "t8y2/dbx": "支援 70 多種資料庫的輕量跨平台 client，內建 AI、MCP server、CLI 與桌面版。",
    "CherryHQ/cherry-studio": "整合前沿 LLM、智慧對話、自主 agent 與大量助理的 AI 生產力桌面工作台。",
    "hesreallyhim/awesome-claude-code": "彙整 Claude Code 的 skills、agents、plugins、hooks 與開發工具資源清單。",
    "jnMetaCode/agency-agents-zh": "提供 267 個可插拔 AI 專家角色與 DAG 編排器，涵蓋多工具及中國市場情境。",
    "bytedance/deer-flow": "用 sandbox、memory、tools、skills 與 subagents 處理長任務的開源 SuperAgent harness。",
    "iOfficeAI/AionUi": "可長時間運行並組隊 OpenClaw、Claude Code、Codex 等 CLI agent 的開源 Cowork app。",
    "ComposioHQ/awesome-claude-skills": "彙整可自訂 Claude AI 工作流的 Skills、資源與工具清單。",
    "aaif-goose/goose": "可用任意 LLM 安裝、執行、編輯與測試的可擴充開源 AI agent。",
    "AgriciDaniel/claude-obsidian": "讓 Claude Code 整理來源、連結 Markdown 的 Obsidian AI 第二大腦與知識圖。",
    "luongnv89/claude-howto": "以圖解與可複製模板教授 Claude Code，從入門到進階 agents 的實作指南。",
    "humanlayer/12-factor-agents": "整理可投入正式產品的 LLM 軟體設計原則與工程方法。",
    "modelcontextprotocol/servers": "Model Context Protocol 的官方 server 範例與實作集合。",
    "punkpeye/awesome-mcp-servers": "彙整各類 Model Context Protocol servers 的資源清單。",
    "nashsu/llm_wiki": "把文件增量整理成互連 wiki 的跨平台桌面應用，而非每次從頭檢索的傳統 RAG。",
    "cobusgreyling/loop-engineering": "為 AI coding agent 設計與編排迭代開發流程的 patterns、starter 與 CLI 工具。",
    "MODSetter/SurfSense": "可透過平台、API 或 MCP 搜尋即時網路來源的開源 NotebookLM 替代方案。",
    "0x4m4/hexstrike-ai": "讓 AI agent 操作 150 多種資安工具的 MCP server，面向滲透測試與漏洞研究。",
    "microsoft/mcp-for-beginners": "以多語言實例教學 MCP 基礎、安全設計與可擴充 AI 工作流的開源課程。",
    "activepieces/activepieces": "以約 400 個 MCP servers 串接 AI agents 與工作流自動化的開源平台。",
    "davila7/claude-code-templates": "設定、管理與監控 Claude Code 的 CLI 工具與模板集合。",
    "VectifyAI/OpenKB": "面向 LLM 應用的開源知識庫專案。",
    "modelcontextprotocol/modelcontextprotocol": "Model Context Protocol 的官方規格與文件庫。",
    "GLips/Figma-Context-MCP": "把 Figma 版面資訊提供給 Cursor 等 AI coding agent 的 MCP server。",
    "rohitg00/awesome-claude-code-toolkit": "彙整 Claude Code agents、skills、commands、plugins、hooks 與 MCP 設定的工具包。",
    "breferrari/obsidian-mind": "讓 Claude Code、Codex CLI 等 agent 在 Obsidian vault 中保留持久記憶。",
    "xerrors/Yuxi": "整合 LightRAG、知識圖譜、MCP 與多租戶能力的 Agent Harness 平台。",
    "centminmod/my-claude-code-setup": "提供 Claude Code 起始設定範本與 CLAUDE.md 記憶庫系統。",
    "SamurAIGPT/llm-wiki-agent": "讓 Claude、Codex 或 Gemini 從來源自動維護持久互連 wiki 的個人知識庫。",
    "superset-sh/superset": "可在本機調度大量 Claude Code、Codex 等 agent 的 AI 時代程式編輯器。",
    "modelcontextprotocol/python-sdk": "Model Context Protocol server 與 client 的官方 Python SDK。",
    "DataTalksClub/ai-dev-tools-zoomcamp": "以實作課程教導如何用 AI 開發工具建置、測試、部署與稽核軟體。",
    "modelcontextprotocol/registry": "由社群維護的 Model Context Protocol server registry 服務。",
    "mark3labs/mcp-go": "讓 Go 應用連接 LLM 與外部資料／工具的 Model Context Protocol 實作。",
    "deepset-ai/haystack": "用明確控制 retrieval、routing、memory 與 generation 建置正式 LLM、RAG 與 agent pipeline 的框架。",
    "labring/FastGPT": "提供資料處理、RAG 檢索與視覺化 AI workflow 的 LLM 知識庫應用平台。",
    "chatchat-space/Langchain-Chatchat": "以 LangChain、ChatGLM、Qwen、Llama 等模型建立本地 RAG 與 Agent 應用的平台。",
    "jeecgboot/JeecgBoot": "企業低程式碼平台，支援用 AI Skills 生成流程、表單、報表與 AI 知識庫／MCP 應用。",
    "DevCoreXOfficial/core-termux": "將 Termux 轉成含 AI coding agent、編輯器、資料庫與自動化工具的行動開發工作站。",
    "witchan/ios-mcp": "供開發者與 AI agent 檢視及控制已越獄 iPhone 的 iOS MCP 管理工具。",
    "Zleap-AI/SAG": "為人類與 agent 建置的開源知識庫與新型 RAG retrieval 架構。",
    "FlorianBruniaux/claude-code-ultimate-guide": "涵蓋 agent workflow、hooks、skills、MCP、測驗與正式範本的 Claude Code 完整指南。",
    "mufeedvh/code2prompt": "把程式碼庫連同目錄、模板與 token 計數轉為單一 LLM prompt 的 CLI。",
    "lastmile-ai/mcp-agent": "以 Model Context Protocol 與簡潔 workflow patterns 建立 agent 的框架。",
    "dataelement/bisheng": "整合 GenAI workflow、RAG、Agent、模型管理、評估與可觀測性的企業 LLM DevOps 平台。",
    "modelcontextprotocol/typescript-sdk": "Model Context Protocol server 與 client 的官方 TypeScript SDK。",
    "kdsz001/OpenWiki": "在 Mac 上擷取剪貼簿、建立個人 wiki 並取得 AI 洞察的知識管理工具。",
    "golutra/golutra": "把 Codex、Claude Code 與 OpenClaw 統一為可平行執行與長任務編排的多 agent 工作台。",
    "bytedance/flowgram.ai": "提供 canvas、表單、變數與素材機制的可擴充 AI workflow 平台開發框架。",
    "OpenSPG/KAG": "以邏輯形式引導檢索與推理，為專業領域知識庫建立事實問答的 RAG 框架。",
    "hangwin/mcp-chrome": "以 Chrome extension 暴露瀏覽器操作、內容分析與語意搜尋給 AI assistant 的 MCP server。",
    "tadata-org/fastapi_mcp": "把 FastAPI endpoints 連同驗證機制暴露成 MCP tools 的函式庫。",
    "53AI/53AIHub": "整合企業知識、agents、prompts 與 AI tools 的開源入口網站，支援 Coze、Dify、FastGPT、RAGFlow。",
    "AvdLee/RocketSimApp": "為 Xcode Simulator 提供測試、除錯、網路監控、無障礙與 AI agent automation 的 30 多項工具。",
    "ProfessionalWiki/NeoWiki": "結合協作編輯與知識圖譜、可供 AI 使用的知識管理系統。",
    "ahmedsaadawi13/splash-wiki": "以 PHP／MySQL 建立多租戶、可公開文件與 REST API 的 production-ready wiki 平台。",
    "bulolo/CatWiki": "具內容管理、AI 問答與現代介面的 Agentic RAG 知識庫平台。",
    "cft0808/edict": "以三省六部概念組織九個專職 agent，提供即時 dashboard、模型設定與完整 audit trail。",
    "claude-did-this/claude-hub": "透過 webhook 將 Claude Code 接到 GitHub PR／Issue，支援以提及方式協助分析與改進程式庫。",
    "derrickxu1220/patalaka-wiki": "以 Claude Code 驅動、協助 AI 知識管理的 Obsidian vault framework。",
    "eugenelim/llm-wiki-kit": "供團隊與家庭使用的 LLM Wiki 知識管理套件，含 Obsidian 範本、agent skills 與腳本。",
    "feiskyer/claude-code-settings": "彙整可強化 Claude Code 的 skills、sub-agents 與設定範本，涵蓋研究、圖像與 GitHub 自動化。",
    "googleapis/mcp-toolbox": "把 AI agents、IDE 與應用直接安全連接企業資料庫的開源 MCP server 與自訂工具框架。",
    "hanshaze/Awesome-Prediction-Market-Trading-Tools": "用於 Polymarket 套利、訊號、流動性與高頻執行的 AI 預測市場交易工具包。",
    "harikrishna8121999/antigravity-workflows": "為 Antigravity AI 提供可重用 prompts 與自動化工作流的社群資源。",
    "iflytek/astron-agent": "可商用、面向下一代 SuperAgents 的企業級 agentic workflow 平台。",
    "ishicm/llm-wiki-skills": "讓 LLM 自主建立、消化、整理與維護知識庫的 LLM Wiki 管理 skill。",
    "ouyearllla/obsidian-wiki-manager": "以 Karpathy LLM Wiki pattern 對 Obsidian 知識庫進行掃描、匯入與 lint 的 plugin。",
    "pingcap/autoflow": "以 TiDB Serverless Vector Storage 建置 Graph RAG 對話式知識庫的工具。",
    "swarmclawai/swarmvault": "local-first LLM Wiki，結合知識圖、RAG、agent memory 與長期個人知識管理。",
    "testsigmahq/testsigma": "為 AI-first 工程團隊提供測試與品質智慧的平台，因應快速交付帶來的覆蓋缺口。",
    "zylon-ai/private-gpt": "可接任意 OpenAI-compatible inference server 的私有 AI 應用 API layer，涵蓋 RAG、skills、MCP 與 text-to-SQL。",
}


def purpose_zh(repo: dict, tags: list[str]) -> str:
    name = repo["full_name"]
    if name in PURPOSE_ZH:
        return PURPOSE_ZH[name]
    description = repo.get("description", "").strip()
    return description or "GitHub 專案未提供簡短用途說明。"


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
            "descriptionZh": purpose_zh(repo, tags),
            "readmeExcerpt": repo.get("readme_excerpt", ""),
            "stars": repo["stars"],
            "forks": repo["forks"],
            "issues": repo["open_issues"],
            "delta": delta,
            "relativeGrowth": round(delta / max(repo["stars"], 1) * 100, 3),
            "sources": repo.get("sources", ["search"]),
            "isNew": repo.get("is_new", name not in previous),
            "trendingStarsToday": repo.get("trending_stars_today"),
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
        "source": "GitHub API snapshots plus in-scope GitHub Trending daily candidates. Trending daily stars are kept separate from snapshot deltas.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} with {len(records)} repositories from {len(snapshots)} snapshots.")


if __name__ == "__main__":
    main()
