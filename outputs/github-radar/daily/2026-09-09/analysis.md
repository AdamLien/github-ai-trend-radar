# GitHub AI Trend Radar 分析（2026-09-09）

## 今日判讀

本次掃描 263 個候選 repository，涵蓋 MCP、agent skills、coding agent、LLM、RAG、wiki/knowledge base 與 developer automation。判斷優先順序是今日 star 增長、相對增長、最近 push/update、README 可操作性與 issue 維護訊號，而不是總 stars 排名。值得注意的是：大量 stars 代表開發者注意力，不等於產品成熟度或商業需求；下列「風險」需在採用前重新驗證。

## 值得追蹤的 repositories

### 1. [affaan-m/ECC](https://github.com/affaan-m/ECC) — Skill candidate

- **用途：** 面向 Claude Code、Codex、OpenCode、Cursor 的 agent harness；整理 skills、instincts、memory、安全與 research-first development。
- **動能：** 254,903 stars，今日約 +985；2026-09-09 有 push，forks 38,190、open issues 198。高增長且 README 對使用方式有完整定位。
- **風險：** 功能面很廣，採用整套 harness 可能把團隊流程綁在作者的工作法；需逐項審查安全規則與相容性。
- **對 Adam / metabiz：** 最接近把 AI office automation 的重複流程變成可移植 skill 的參考，可拆成「研究、報價、wiki handoff、QA」等模組。

### 2. [obra/superpowers](https://github.com/obra/superpowers) — Deep research

- **用途：** 可組合 agent skills 加上軟體開發方法論，支援多種 coding agent，包括 Codex、Claude Code 與 Cursor。
- **動能：** 283,857 stars，今日約 +668；2026-09-08 有 push，forks 25,403、open issues 344。跨工具支援與清晰的安裝/工作流說明是強訊號。
- **風險：** 方法論層較重，導入後可能增加流程與提示詞成本；高人氣也代表需防止照單全收。
- **對 Adam / metabiz：** 適合做「AI 辦公室作業系統」課程的流程骨架，尤其是需求澄清、規劃、執行、驗證與交付的標準循環。

### 3. [openai/codex](https://github.com/openai/codex) — Reference only

- **用途：** 可在 terminal 執行的輕量 coding agent，README 也指向 IDE、desktop 與 web agent 使用場景。
- **動能：** 122,790 stars，今日約 +292；2026-09-09 有 push，forks 18,880、open issues 16,217。官方 repo 的更新與周邊生態仍很活躍。
- **風險：** open issues 數量很高；功能與產品介面快速變動，且 repository 本身不等於穩定的企業部署承諾。
- **對 Adam / metabiz：** 作為 Codex skill、plugin、repo workflow 的基準參考；可用於課程示範「從自然語言需求到可驗證交付」。

### 4. [openai/skills](https://github.com/openai/skills) — Skill candidate

- **用途：** Codex skills catalog，提供可重複任務的 instructions、scripts 與 resources 範例。
- **動能：** 26,750 stars，今日約 +366；2026-09-08 有 push，forks 1,794、open issues 294。README 明確標示 repository deprecated，並導向 OpenAI Plugins。
- **風險：** 已 deprecated，不能直接當成長期依賴；license 欄位未明確，應依新 plugin 文件與官方範例重建。
- **對 Adam / metabiz：** 對本 workspace 的 skill monorepo 最直接；可作為 migration/watch reference，檢查現有 PDF、video、quotation、wiki skills 的封裝方式。

### 5. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) — Demo content

- **用途：** MCP server，讓 Claude、Cursor、Copilot 等 coding agent 控制與檢查 live Chrome，支援可靠瀏覽器自動化、debug 與效能分析。
- **動能：** 51,447 stars，今日約 +103；2026-09-09 有 push，forks 3,615、open issues 105，Apache-2.0，README 有 npm、tool reference、troubleshooting 與 changelog 路徑。
- **風險：** 瀏覽器控制涉及權限、登入 session、外部資料與網站條款；demo 必須使用測試帳號與非敏感資料。
- **對 Adam / metabiz：** 很適合示範「AI agent + browser + MCP」如何做表單驗證、後台巡檢與內容 QA，是 AI office automation 的可視化案例。

### 6. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Deep research

- **用途：** Obsidian + Claude Code 的 self-organizing AI second brain，把來源轉成連結筆記、knowledge graph 與可檢索的 Markdown；MIT。
- **動能：** 14,766 stars，今日約 +28；2026-08-26 push、2026-09-09 update，forks 1,470、open issues 142。README 對 capture、grounded answers、vault health 的流程描述清楚。
- **風險：** 最新 push 與 update 之間可能有自動化/issue 活動而非程式變更；需驗證 Claude Code 版本、資料匯入品質與隱私邊界。
- **對 Adam / metabiz：** 與 metabiz wiki、課程研究資料、客戶知識交接高度相關；可研究「來源 → 原子筆記 → backlinks → grounded answer」的最小流程。

### 7. [infiniflow/ragflow](https://github.com/infiniflow/ragflow) — Deep research

- **用途：** 具 agent capabilities 的開源 RAG engine，處理文件解析、context layer、retrieval 與 knowledge compilation；Apache-2.0。
- **動能：** 90,384 stars，今日約 +93；2026-09-09 有 push，forks 10,672、open issues 1,556。提供繁中 README，且近期 agent/context-engineering 定位清楚。
- **風險：** 系統較重、部署與維護成本高；1,556 個 open issues 代表需做版本與運維評估，不宜直接承諾 production SLA。
- **對 Adam / metabiz：** 可作 metabiz wiki 的 RAG 對照組，拿來教「向量相似度之外的文件解析、權限、引用與評測」；先做小型 proof-of-concept。

### 8. [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) — Skill candidate

- **用途：** TypeScript fullstack MCP framework，用來建立 MCP servers、MCP Apps、ChatGPT plugins、Claude connectors 與 agent experience；MIT。
- **動能：** 10,596 stars，今日約 +4；2026-09-09 有 push，forks 1,443、open issues 46。增長不快，但更新與文件/Inspector 路徑完整。
- **風險：** MCP 生態仍在快速演變，framework abstraction 可能落後 protocol 或 SDK 變更；需鎖版本並測試 client 相容性。
- **對 Adam / metabiz：** 適合作為內部「把常用 office API 包成 MCP」的候選，先從 wiki search、quotation lookup、CRM read-only 查詢等低風險工具開始。

### 9. [Tencent/teamai-cli](https://github.com/Tencent/teamai-cli) — Watch

- **用途：** 團隊級管理 skills、rules、MCP 與 knowledge，定位為讓團隊 AI-native；README 提供英文/簡中與 npm 路徑。
- **動能：** 今日首次被 daily trending 觀測，今日約 +563；目前 2,809 stars、176 forks、22 open issues，2026-09-09 有 push。首次觀測代表尚無可比 snapshot delta。
- **風險：** license metadata 顯示 NOASSERTION，雖 README badge 指向 MIT，仍應確認實際 LICENSE；團隊治理、權限與 secrets handling 尚需實測。
- **對 Adam / metabiz：** 直接對應「公司共用 skills/rules/knowledge」問題，值得觀察是否能補上 metabiz wiki handoff 與 AI office automation 的治理層。

## 明日 watchlist

1. **Tencent/teamai-cli：** 確認第二日 star delta、實際 LICENSE、skill/rule/MCP/knowledge 的同步與權限模型。
2. **ECC、superpowers：** 比較兩者的 skill lifecycle、memory、review gate 與 Codex 相容性，決定是否做一個 metabiz 版最小 harness。
3. **openai/codex、openai/plugins：** 追蹤官方 skill/plugin 方向，避免繼續依賴已 deprecated 的 `openai/skills`。
4. **Chrome DevTools MCP：** 做隔離環境 demo，測試 browser automation 的登入、截圖、console/performance QA 與資料外洩風險。
5. **claude-obsidian、RAGFlow：** 用同一批 metabiz wiki 文件比較 Markdown graph、agentic retrieval、引用與更新成本。
6. **MCP 生態：** 追蹤 `modelcontextprotocol/servers`（90,185 stars、今日約 +24）與 `mcp-use/mcp-use` 的 protocol/SDK 變動；reference repo 不應直接當 production server 清單。
7. **新 trending 候選：** `vastsa/PI-Desktop`（今日約 +393）與 `earthtojake/text-to-cad`（今日約 +97）先看 README、release 與 license，再決定是否納入課程 demo。

## 結論

今日最可轉成行動的是：以 ECC/superpowers 研究可重用 agent workflow，以 Chrome DevTools MCP 做可視化 office automation demo，以 claude-obsidian/RAGFlow 建立 metabiz wiki 的知識流 proof-of-concept；Codex 與官方 plugin 生態則作為基準與相容性 watch。所有採用決策仍應補做安全、授權、版本鎖定與實際資料測試。
