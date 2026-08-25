# GitHub AI Trend Radar 分析

- 目標日期：2026-08-25（Asia/Taipei 前一日）
- 收集完成時間：2026-08-26（collector snapshot date）
- 範圍：GitHub Trending daily 與指定的 10 組 AI／MCP／skills／agent／LLM／RAG／wiki／coding-agent／developer-automation 查詢
- 判讀原則：先看今日 stars、snapshot star delta、相對成長與近期 push／release，再交叉 README、issues、license 與採用摩擦；stars 只是注意力訊號，不等於產品品質或付費需求。

## 值得追蹤的 repositories

### 1. [openai/codex](https://github.com/openai/codex)

- **用途**：在 terminal 執行的輕量 coding agent，可作為 Codex 工作流、repo 維護與自動化開發的基準案例。
- **動能**：117,937 stars；snapshot delta **+211**；GitHub Trending daily **+1,183**；2026-08-25 有 push，2026-08-24 發布 `rust-v0.149.1`。高總量仍有很強的當日注意力。
- **風險**：open issues 13,777，數量很大；專案快速演進，CLI 行為與模型／權限整合可能變動，需要固定版本與安全邊界。
- **判定**：**Deep research**。
- **對 Adam 的關聯**：可直接轉成「coding agent 如何進入 AI office automation」課程主軸，示範把 wiki、proposal、內容產製與 repo 任務串成可重複流程；也是 metabiz wiki 的 agent 操作基準。

### 2. [mattpocock/skills](https://github.com/mattpocock/skills)

- **用途**：面向真實工程工作的 agent skills 集合，展示如何以可重用指令與工作規範提升 coding agent 行為。
- **動能**：236,393 stars；snapshot delta **+369**；2026-08-25 更新，最近 release 為 `v1.2.3`（2026-08-06）。本日 delta 高於 Codex，且文件定位清楚。
- **風險**：open issues 396；不同 skill 的品質、適用模型與授權邊界要逐項檢查，不能整包直接採用。
- **判定**：**Skill candidate**。
- **對 Adam 的關聯**：最適合拆解成 metabiz 的 skill 設計教材：輸入／輸出契約、驗證步驟、失敗處理與可組合的 office automation skill；可與現有 monorepo skill 目錄對照。

### 3. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)

- **用途**：Claude Code 驅動的 Obsidian second brain，將來源整理成互相連結的 Markdown knowledge graph，包含檢索與 vault 維護。
- **動能**：12,461 stars；snapshot delta **+229**；Trending daily **+810**；2026-08-25 更新，README 明確且最近 release `v2.1.0` 支援 Windows。
- **風險**：open issues 135，最近 push 為 2026-08-01，熱門度增長快於近期程式活動；需要驗證資料隱私、索引品質與升級相容性。
- **判定**：**Deep research**。
- **對 Adam 的關聯**：與 metabiz wiki、LLM wiki、課程研究資料庫高度重疊，可做「本地 Markdown 知識庫 + coding agent」demo，也能測試內容雷達到 wiki 的落地路徑。

### 4. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

- **用途**：長任務 SuperAgent harness，結合 sandbox、memory、tools、skills、subagents 與 message gateway，處理研究、coding 與內容產出。
- **動能**：80,853 stars；snapshot delta **+22**；2026-08-25 push；最近 major release 為 `v2.0.0`。總量大且架構訊號完整，但今日增幅低於 skills／Codex 類專案。
- **風險**：open issues 890；長任務 orchestration 的成本、權限、可觀測性與失敗恢復仍需實測，release 與日常 push 之間也要持續觀察。
- **判定**：**Demo content**。
- **對 Adam 的關聯**：可示範「研究 → 草稿 → wiki → 任務派送」的多 agent pipeline，對 AI office automation 與課程中的端到端案例很有價值。

### 5. [53AI/53AIHub](https://github.com/53AI/53AIHub)

- **用途**：企業 AI portal／knowledge base，整合 agents、prompts、AI tools 與 Coze、Dify、FastGPT、RAGFlow。
- **動能**：4,632 stars；snapshot delta **+1**；2026-08-25 更新，2026-08-19 發布 `v0.5.0`。絕對增長不強，但產品定位與 metabiz wiki 的企業知識入口很貼近。
- **風險**：license 顯示 `NOASSERTION`；開源版、雲端服務與整合依賴需拆開評估，不能只依 README 判定可商用。
- **判定**：**Watch**。
- **對 Adam 的關聯**：可作為「企業知識入口」對照組，研究如何把課程內容、prompt library、agent 與 RAG 資料源放到同一個操作面；先做架構比較，不急著導入。

### 6. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

- **用途**：MCP server 參考集合，提供把外部資料與工具接到 agent 的常見整合模式。
- **動能**：89,849 stars；snapshot delta **+9**；2026-08-20 push，最近 release `2026.8.18`。總量與生態重要性很高，但本日與近期增幅已不是本批最強。
- **風險**：license 顯示 `NOASSERTION`，且不同 server 的維護狀態、權限需求與第三方依賴差異很大；open issues 542。
- **判定**：**Reference only**。
- **對 Adam 的關聯**：適合用來教 MCP 的概念、server 選型與安全審查，並作為 AI office automation、metabiz wiki connector 的參考索引；個別 server 仍需另行 QA。

### 7. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

- **用途**：集中整理 100+ AI agents、agent skills 與 RAG apps，適合快速找 demo 題材與課程案例。
- **動能**：134,080 stars；snapshot delta **0**；Trending daily **+161**；2026-08-25 更新，首次出現在本次 radar snapshot。
- **風險**：awesome list 的收錄品質與範例維護不一；容易把「可展示」誤當成「可生產」，需要對每個子專案確認 license、成本與安全性。
- **判定**：**Demo content**。
- **對 Adam 的關聯**：可作為 AI 工具雷達、課程選題與內容比較的素材池，尤其適合把一個 RAG／agent demo 改寫成 office automation 的情境教學。

### 8. [n8n-io/n8n](https://github.com/n8n-io/n8n)

- **用途**：具原生 AI 能力的 workflow automation 平台，提供視覺化流程、custom code、400+ integrations 與 self-host／cloud 選項。
- **動能**：202,383 stars；snapshot delta **+19**；2026-08-25 push 並發布 `n8n@2.36.7`。增長不如熱門 coding-agent，但更新頻率與整合生態穩定。
- **風險**：open issues 1,089；license 顯示 `NOASSERTION`，fair-code 條款與商業使用方式必須先確認；自架部署也帶來 secrets、權限與維運責任。
- **判定**：**Deep research**。
- **對 Adam 的關聯**：是 AI office automation 最直接的流程編排候選，可做 lead intake、proposal、內容雷達、wiki 更新與通知的課程實作；應與 Codex／MCP 形成互補而非二選一。

### 9. [1jehuang/jcode](https://github.com/1jehuang/jcode)

- **用途**：以 Rust 實作、重視 RAM 效率的 coding-agent harness，支援 terminal／TUI、LLM 與 MCP。
- **動能**：18,537 stars；snapshot delta **+34**；2026-08-25 更新並發布 `v0.80.1`。絕對 stars 較小，但 release 與近期 push 同日，具效率型工具的觀察價值。
- **風險**：open issues 351；生態與文件成熟度仍需和 Codex／Claude Code 實測比較，Rust binary、模型供應商與 MCP 相容性可能增加導入門檻。
- **判定**：**Watch**。
- **對 Adam 的關聯**：可作為「低資源 coding agent」與 token／runtime 效率的比較案例，也呼應 dashboard 建置時採用 rtk 的 developer automation 方向。

## 綜合判斷

本日最值得深入的訊號不是單一高星 repo，而是三條互相接上的路徑：

1. **Skills 正在成為 agent 的可移植工作層**：`mattpocock/skills` 提供工程化樣本，Codex／Claude Code 則提供執行入口。
2. **知識庫正從被動儲存轉成可執行上下文**：`claude-obsidian`、`53AIHub` 與 MCP servers 分別代表本地 Markdown、企業入口與工具連接層。
3. **Orchestration 正往長任務與流程自動化延伸**：`deer-flow` 偏多 agent 研究／產出，n8n 偏可視化企業流程；兩者都比單純聊天 demo 更接近 AI office automation。

## 明日 watchlist

- **先看當日 star delta**：`openai/codex`、`mattpocock/skills`、`AgriciDaniel/claude-obsidian` 是否維持高於本批平均的增長；若下降，檢查是否只是 Trending 曝光造成的短脈衝。
- **追 release／相容性**：Codex、Claude Code、jcode 的新版本是否改變 skill、MCP、permission 或 terminal workflow；同步記錄 breaking change。
- **追真實可用性**：n8n 與 deer-flow 是否有新的 workflow／sandbox／memory 文件與 issue 修復，特別是 secrets、權限、重試與可觀測性。
- **追 knowledge-base 採用**：`claude-obsidian` 的 push／release 是否恢復，以及 53AIHub 的 license 與本地部署文件是否明確。
- **追新進熱門**：`Shubhamsaboo/awesome-llm-apps` 的 Trending 訊號是否轉成 snapshot delta；若持續，從清單挑一個 RAG 或 agent app 做可重現 demo。
- **維持風險監測**：對 `NOASSERTION` 或 license 空白專案，不進入商業交付或課程標準工具鏈，直到完成授權與依賴審查。

