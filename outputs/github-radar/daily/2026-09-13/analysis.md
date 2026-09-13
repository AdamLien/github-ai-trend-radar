# GitHub AI 趨勢雷達分析（2026-09-13）

## 方法與解讀

本日以 GitHub 搜尋結果及 GitHub Trending daily 交叉收集 277 個候選，優先看今日星數增量、相對成長、最近 push／release、README 清晰度與 issue 活躍度，而不是只按總 stars 排名。下文的 stars、星數增量、日期與 README 描述是 GitHub 觀測資料；「適合課程／內容／AI 辦公室／metabiz wiki」是本雷達的推論。Stars 代表開發者注意力，不代表安全性、成熟度、買方需求、節省成本或生產環境成效。

## 值得追蹤的研究優先項目

### 1. affaan-m/ECC — Skill candidate

- **用途（GitHub／README 聲稱）：** 面向 Claude Code、Codex、OpenCode、Cursor 的 agent harness，涵蓋 skills、instincts、memory、安全與 research-first development。
- **動能：** 257,543 stars，snapshot star delta **+651**；2026-09-12 有 push，2026-09-13 仍有更新觀測，38,524 forks、194 open issues。日增與 fork 規模同時高，屬本日最值得拆解的 agent 工作法樣本之一。
- **風險／限制：** 功能面很廣，容易把方法論、提示、工具與安全保證混為一談；需要逐項檢查腳本權限、供應鏈與實際相容性，不能因 README 的「performance optimization」描述直接推論效能提升。
- **Adam 相關性：** 可作「AI coding agent 作業系統／研究先行開發」課程案例，並抽取可重用的檢查清單到 AI 辦公室流程；其中 memory、security、research log 也可映射到 metabiz wiki 的工作規範。
- **明日觀察：** 是否持續維持高 star delta；新增 skill 是否有測試與變更說明；檢查 Codex／Claude Code 安裝步驟與可撤銷性。
- **來源：** https://github.com/affaan-m/ECC

### 2. obra/superpowers — Deep research

- **用途（GitHub／README 聲稱）：** 以可組合 skills 與軟體開發方法論，讓多種 coding agent 按 brainstorming、規劃、實作與驗證流程工作；README 列出 Claude、Codex、Cursor 等整合方式。
- **動能：** 286,083 stars，delta **+405**；2026-09-12 push、2026-09-13 更新，25,596 forks、363 open issues。總量高但仍有穩定日增，顯示方法論型 skill 仍在擴散。
- **風險／限制：** 方法論導入可能增加流程成本；363 issues 顯示維護與使用情境很多，需確認版本、平台差異與商業服務邊界，不能把社群採用直接等同於交付品質。
- **Adam 相關性：** 適合做「把 prompt 變成可重複交付流程」的課程主案例；可改寫成 AI 辦公室的需求澄清、執行、review、交付四段式 SOP，並收錄到 metabiz wiki。
- **明日觀察：** 追蹤 Codex 路徑是否有更新；比較其 skill lifecycle 與本 workspace skill 的重疊；留意 breaking changes。
- **來源：** https://github.com/obra/superpowers

### 3. tech-leads-club/agent-skills — Demo content

- **用途（GitHub／README 聲稱）：** 提供給 Antigravity、Claude Code、Cursor、Copilot 等 coding agent 的 secure、validated skill registry。
- **動能：** 本日首次進入 radar 的 Trending daily，新進條目 **215 stars today**；總 stars 5,487，2026-09-12 push、2026-09-13 更新，494 forks、29 open issues。因首次觀測，snapshot delta 尚未可量化。
- **風險／限制：** GitHub license 欄位為 `NOASSERTION`；「secure／validated」是專案定位，尚不是本雷達驗證結果。registry 中的 skill 仍須逐一審查來源、權限、依賴與更新者。
- **Adam 相關性：** 可做「如何評估第三方 agent skill」的 demo：從 metadata、README、權限、測試、版本與撤銷策略建立採用門檻；對 AI 辦公室與 metabiz wiki 的技能目錄很直接。
- **明日觀察：** 確認新進 Trending 是否延續；查看 license 是否補齊；抽查熱門 skill 的內容與 CI／release 證據。
- **來源：** https://github.com/tech-leads-club/agent-skills

### 4. cathrynlavery/diagram-design — Demo content

- **用途（GitHub／README 聲稱）：** 為 Claude Code、Codex、Pi 提供 38 種 editorial diagram，使用 self-contained HTML + SVG；README 展示 architecture、loop 等圖例。
- **動能：** 39,099 stars，delta **+352**；2026-09-10 push、2026-09-13 更新，2,479 forks、42 open issues；相對星增明顯高於成熟的大型平台。
- **風險／限制：** 圖表美感與可讀性仍需依內容驗證；HTML／SVG 輸出要檢查可存取性、品牌一致性與資料外洩風險。MIT 授權降低採用摩擦，但不等於產出必然正確。
- **Adam 相關性：** 很適合課程簡報、AI 辦公室流程圖、客戶提案與 metabiz wiki 的架構說明；可示範「同一份需求由 agent 產生流程圖，再由人校稿」。
- **明日觀察：** 追蹤新增圖型與範例；測試繁中標籤、手機可讀性與品牌樣式；觀察 star delta 是否只是短期曝光。
- **來源：** https://github.com/cathrynlavery/diagram-design

### 5. unclecode/crawl4ai — Skill candidate

- **用途（GitHub／README 聲稱）：** 開源、LLM-friendly 的 web crawler／scraper，主打把網頁資料轉成適合 LLM 使用的內容。
- **動能：** 83,068 stars，delta **+639**；2026-09-09 push、2026-09-13 更新，8,578 forks、196 open issues；Apache-2.0，日增高且仍有社群活動。
- **風險／限制：** 抓取行為受 robots、網站條款、反爬與個資規範約束；196 issues 代表整合面不小。不能把 README 的「LLM friendly」直接推論成所有網站的穩定抽取品質。
- **Adam 相關性：** 可研究成「公開資料→摘要→wiki 索引」的 AI 辦公室 skill，支援課程資料蒐集與 metabiz wiki 更新；教學時必須加入來源、授權、去重與人工查核。
- **明日觀察：** 看 release／breaking change、Python 版本相容性、robots 與 citation 支援；避免對需要登入或含個資頁面做未授權測試。
- **來源：** https://github.com/unclecode/crawl4ai

### 6. n8n-io/n8n — Deep research

- **用途（GitHub／README 聲稱）：** fair-code 的 AI agent 與 workflow automation 平台，可 self-host 或使用 cloud，連接多種整合；README 描述 1,500+ integrations。
- **動能：** 204,163 stars，delta **+76**；2026-09-13 push，60,656 forks、1,158 open issues。絕對日增不如前述 skill 專案，但總量、fork 與當日維護活動都高，代表成熟且競爭激烈的自動化基礎設施。
- **風險／限制：** fair-code／NOASSERTION 需由採用者核對版本與商業使用條款；1,158 issues 反映龐大整合面。AI workflow 的憑證、權限、重試與人工核准仍需自行治理。
- **Adam 相關性：** 是 AI 辦公室自動化與 metabiz 內部流程的主力候選，可做表單→LLM→審核→Odoo／wiki 的示範；課程應把權限、觀測與失敗處理列為核心，而非只展示拖拉畫布。
- **明日觀察：** 追蹤 AI／MCP 節點變更、self-host 升級風險與授權說明；找一個無敏感資料的最小流程做可重現 demo。
- **來源：** https://github.com/n8n-io/n8n

### 7. infiniflow/ragflow — Deep research

- **用途（GitHub／README 聲稱）：** RAG engine，結合 RAG 與 agent capabilities，提供文件理解、檢索與知識層；README 提供繁體中文版本。
- **動能：** 90,608 stars，delta **+35**；2026-09-13 push／更新，10,718 forks、1,560 open issues；Apache-2.0。星增溫和但日常維護明確，較像可深入評估的基礎設施而非短期爆紅。
- **風險／限制：** 1,560 open issues 顯示系統複雜度與維護負擔；RAG 的正確性、權限隔離、索引更新與引用完整性仍需用自己的資料集驗證，README 不能替代 benchmark。
- **Adam 相關性：** 與 metabiz wiki、課程知識庫、內部文件問答高度相關；可比較它與 markdown/wiki-first 做法，形成「何時用 RAG、何時用可讀 wiki」的課程單元。
- **明日觀察：** 查看最新 release、繁中文件品質、引用／權限功能與最低部署成本；只用去識別化文件測試。
- **來源：** https://github.com/infiniflow/ragflow

### 8. modelcontextprotocol/servers — Reference only

- **用途（GitHub／README 聲稱）：** MCP reference implementations 與社群 server 資源；README 明確說明它是 steering group 維護的少量 reference servers，而非完整 server 清單。
- **動能：** 90,287 stars，delta **+14**；2026-09-03 push、2026-09-13 更新，11,626 forks、520 open issues。總量很高但今日增長低，較適合作為規格／介面基準，不是本日熱門採用推薦。
- **風險／限制：** license 欄位為 `NOASSERTION`；reference implementation 不等於 production-ready server。MCP 工具權限、輸入驗證、資料外洩與供應鏈風險必須個別處理。
- **Adam 相關性：** 可支撐 MCP 課程的概念、server／client 邊界與 AI 辦公室工具整合教學，也可成為 metabiz wiki 的協定參考頁；採用前需另做安全 review。
- **明日觀察：** 追蹤規格／reference server 的 breaking changes、license 明確化與安全公告；比較官方 registry 與社群 server 的差異。
- **來源：** https://github.com/modelcontextprotocol/servers

### 9. VectifyAI/OpenKB — Watch

- **用途（GitHub／README 聲稱）：** Open LLM Knowledge Base，主打長文件、多模態、reasoning-based retrieval，並宣稱不需要 vector DB；README 也有近期更新與知識庫格式說明。
- **動能：** 4,503 stars，delta **+4**；GitHub code push 顯示 2026-07-22，但 2026-09-13 有更新觀測，470 forks、80 open issues，Apache-2.0。與高星 RAG 平台相比成長小，且近期程式碼活躍度需再核實。
- **風險／限制：** 「不需要 Vector DB」是架構主張，不是對 Adam 資料的驗證；小型社群、較長的 code push 間隔與部署成熟度都要留意。需測量索引更新、引用、中文與權限行為。
- **Adam 相關性：** 與 metabiz wiki 的長文件、知識頁與 AI 維護流程很貼近，適合拿來做 wiki-first、RAG-first 的對照研究，而非立即採用。
- **明日觀察：** 查最新 release／commit、繁中與 markdown 匯入、權限與引用；若 star delta 仍低，維持 Watch。
- **來源：** https://github.com/VectifyAI/OpenKB

## 明日共同 watchlist

1. **延續性：** `affaan-m/ECC`、`obra/superpowers`、`cathrynlavery/diagram-design`、`unclecode/crawl4ai` 的 star delta 是否連續，而非單日尖峰。
2. **新進項目：** `tech-leads-club/agent-skills` 是否仍在 Trending，並確認 license、skill 審核與 CI 證據。
3. **採用風險：** `n8n`、`ragflow`、`modelcontextprotocol/servers` 的 release／breaking changes、open issues 與安全公告。
4. **wiki 決策：** `OpenKB` 與 `ragflow` 以同一份去識別化 metabiz 文件做小型比較，記錄引用正確性、更新成本、權限模型與繁中表現；在有實測前不宣稱 ROI 或生產就緒。

## 結論

本日最值得轉成 Adam 課程／內容的主題不是「哪個 repo stars 最高」，而是三條可示範的工作流：可審核的 agent skills、可視化與可驗證的 AI 交付流程，以及帶來源與權限治理的文件→RAG／wiki。短期先以 ECC、Superpowers、agent-skills、diagram-design 做技能與教學研究；n8n、RAGFlow、MCP servers 與 OpenKB 則維持受控、可重現、去識別化的評估。
