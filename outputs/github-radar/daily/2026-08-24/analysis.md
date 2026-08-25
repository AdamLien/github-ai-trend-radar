# GitHub AI Trend Radar 分析（2026-08-24）

本次資料夾以 Asia/Taipei 前一日 2026-08-24 命名；collector 於 2026-08-25 執行，檢查 204 個去重後專案。判斷以 stars_delta、相對成長、最近 push/release、README、fork/issue 活動綜合，不以總星數單獨排名。數字為 collector 當次快照，`stars_delta` 是相對前一快照的變化。

## 值得追蹤的專案

### 1. [openai/codex](https://github.com/openai/codex) — Skill candidate / Deep research

- **用途：** Apache-2.0 的本機終端 coding agent；README 同時指向 IDE、desktop 與 cloud agent 入口。
- **動能：** 117,716 stars、`+2,796`；2026-08-25 有更新，並在 2026-08-24 發布 `0.149.1`。17,957 forks、13,745 open issues 顯示關注度與維護/回報量都很高。
- **風險：** issue 量極大，版本與 CLI 行為變動快；需實測權限、成本、資料外流與不同 IDE 整合，不能直接視為企業 production default。
- **Adam 關聯：** 可作「coding agent 基礎工作流」課程主線，並把本工作區的 radar、文件整理、wiki handoff 做成 Codex skill 範例；對 AI office automation 的可重複終端流程特別 relevant。

### 2. [mattpocock/skills](https://github.com/mattpocock/skills) — Skill candidate

- **用途：** MIT、以 `.agents` 目錄呈現真實工程技能，README 強調日常可用的 engineering skills。
- **動能：** 236,011 stars、`+2,567`；最近 push 為 2026-08-24，20,106 forks、394 issues，代表範式擴散且仍有實際維護訊號。
- **風險：** skill 品質與適用情境不一；把別人的規則直接帶入工作區可能造成過度自動化、上下文污染或不必要的命令執行。
- **Adam 關聯：** 適合拆解成「如何設計可重用 skill」課程與 know metabiz wiki 的標準模板；優先研究 skill metadata、觸發條件、驗證與回滾方式。

### 3. [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — Reference only / Demo content

- **用途：** MIT 的 agent skills 集合；README 顯示 1,497+ skills，涵蓋 Claude Code、Codex、Gemini CLI、Cursor 等。
- **動能：** 32,117 stars、`+1,004`；2026-08-25 更新，3,414 forks、僅 8 open issues，且有清楚的 curated/非 AI-slop 定位。
- **風險：** curated list 不等於每個 skill 都經過同等深度的安全與相容性審查；沒有 release 也表示版本治理需自行確認。
- **Adam 關聯：** 適合做「跨 agent skill 生態地圖」demo，挑出 3–5 個與報價、PDF、CRM、wiki 最接近的項目做隔離測試，再決定是否成為本地 skill candidate。

### 4. [stablyai/orca](https://github.com/stablyai/orca) — Demo content / Watch

- **用途：** MIT 的 parallel-agent 工作台，支援用既有訂閱執行不同 coding agent，涵蓋 desktop、mobile、VPS。
- **動能：** 53,178 stars、`+1,524`；2026-08-25 持續 push，最近 release `v1.4.188`，3,678 forks。相對成長強，且 orchestration、worktree、Claude Code/Codex/Cursor 整合主題貼近市場。
- **風險：** 4,517 open issues 偏高；多 agent 平行執行會放大成本、權限與衝突管理風險，需驗證訂閱條款與 secrets 隔離。
- **Adam 關聯：** 可做「AI office automation 多代理分工」示範：研究、草稿、QA、wiki 更新各自隔離，再比較單 agent；不建議未審核就導入 metabiz 生產環境。

### 5. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Deep research

- **用途：** MIT 的 Claude Code + Obsidian second brain；把來源轉成互相連結的 Markdown 知識圖譜，強調檔案由使用者持有。
- **動能：** 12,226 stars、`+958`；快照更新訊號很強，1,357 forks、135 issues，最近 release `v2.1.0` 並加入 Windows 相容性。
- **風險：** 上次 repo push 較早，快照的更新活動可能包含 metadata/外部同步；需檢查 ingest、連結與權限邊界，避免將敏感 wiki 送入模型。
- **Adam 關聯：** 與 know metabiz wiki 最直接：可研究「來源→原子筆記→連結→grounded answer→vault health」流程，轉成課程中的企業知識庫案例。

### 6. [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) — Demo content / Skill candidate

- **用途：** MIT，把技術書 PDF、文件資料夾或來源集合轉成可供 agent 使用的 skill；含 RAG、knowledge base 與自學定位。
- **動能：** 25,376 stars、`+932`；2026-08-24 push、最近 release `v1.4.0`，2,630 forks、23 issues。
- **風險：** PDF 抽取、版權、引用正確性與 prompt injection 都是主要風險；生成 skill 仍需人工審稿與測試，不能把摘要當成原文依據。
- **Adam 關聯：** 可做「課程教材轉內部 skill」demo，直接連到 PDF ingestion、課程內容維護與 metabiz wiki onboarding；是值得建立隔離試驗的 skill candidate。

### 7. [volcengine/OpenViking](https://github.com/volcengine/OpenViking) — Deep research / Watch

- **用途：** AGPL-3.0 的 context database，將 agent memory、knowledge RAG 與 skills 統一管理，並提供文件、中文 README 與 live demo 入口。
- **動能：** 33,133 stars、`+760`；2026-08-25 push，最近 release `v0.4.16`，2,525 forks、521 issues，屬於 RAG/agent context 的高相關成長項目。
- **風險：** AGPL 對 SaaS/衍生整合有合規影響；仍需驗證資料模型、遷移成本、self-evolving 行為與可觀測性。
- **Adam 關聯：** 可作 know metabiz wiki 的 context layer 研究對照組，評估它與現有 Markdown/wiki、向量檢索及 MCP 的邊界；先做小型非敏感資料 benchmark。

### 8. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research / Demo content

- **用途：** Apache-2.0，把 codebase、文件、SQL schema、設定與 PDF 轉成可查詢 knowledge graph；支援 Claude Code、Cursor、Codex、Gemini CLI，主打 deterministic AST 與不依賴 vector store。
- **動能：** 110,266 stars、`+522`；2026-08-24 發布 `v0.9.49`，10,727 forks、1,112 issues，更新與社群規模都強。
- **風險：** issue 量高且版本仍在 0.x；圖譜正確性、schema 覆蓋率與大型 repo 成本要以實際資料驗證，不能只因 stars 高而採用。
- **Adam 關聯：** 很適合做「讓 AI 理解 metabiz 專案與 wiki 的關係」demo，並比較 knowledge graph 與一般 RAG；若可控，可成為 coding agent onboarding skill 的參考實作。

## 明日 watchlist

1. **Codex、mattpocock/skills、Orca：** 觀察 stars_delta 是否連續兩日為正、release 是否持續，以及 issue 增長是否超過使用者價值訊號。
2. **claude-obsidian、book-to-skill、OpenViking、Graphify：** 以同一批非敏感 metabiz wiki/PDF 樣本測試引用可追溯性、更新成本、權限與 license 邊界。
3. **VoltAgent/awesome-agent-skills：** 追蹤清單新增哪些官方/高品質 skills，篩選可轉成 AI office automation 課程模組的項目。
4. **新進候選：** 留意今日高相對成長但尚未納入深研的 `apache/maka`、`hugohe3/ppt-master`、`citrolabs/ego-lite`，明日以 README、release、issue 與安全模型複核。

## 結論

今日最值得投入研究資源的是 Codex 的 coding-agent 工作流、book-to-skill/claude-obsidian 的「內容→知識→skill」鏈，以及 OpenViking/Graphify 的 context/knowledge layer。這些訊號能直接轉成 Adam 課程、AI office automation 與 know metabiz wiki 的實驗；高星但 license、issue 或資料安全邊界未釐清者先維持 Watch 或 Reference only。
