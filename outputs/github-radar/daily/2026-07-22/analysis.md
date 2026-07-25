# GitHub AI Trend Radar｜2026-07-22（台灣）

> 收集時間：2026-07-23 00:12–00:16（Asia/Taipei）。本輪以 10 組 GitHub API 搜尋收集 89 個去重 repo，已使用已登入的 GitHub token，未遇 rate limit。
>
> **數字閱讀方式**：GitHub Trending 只提供「當下的 daily」頁面，無法回查 7/22 的歷史頁；文中的 `stars today` 是 7/23 00:12 擷取到的即時日增星，不可當成 7/22 的歷史值。`snapshot delta` 是本輪 API 快照相對 7/21 上一輪 API 快照的差異（約 15 小時），用於長期追蹤。

## 今日判讀

本日不是單一模型或單一 agent framework 的熱潮，而是三個明顯方向：

1. **Context engineering 落地**：code-review-graph 與 Graphify 把大型 codebase／文件變成可查的圖譜，對降低 coding agent context 成本最直接。
2. **Skills 產品化**：從小而明確的輸出規範（i-have-adhd）到工程技能庫（agent-skills），大家開始將可複用工作法封裝成 agent 可執行單位。
3. **可控的長任務與自動化**：DeerFlow、MCP Toolbox、n8n-as-code 分別補上長任務編排、資料庫工具安全邊界、workflow-as-code。

## 最值得追的 repo（依動能、適配度與可驗證性排序）

| Repo | 分類 | 用途與為什麼現在值得看 | 動能／規模 | 風險與採用立場 |
| --- | --- | --- | --- | --- |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Deep research | MCP/CLI 的 local-first code intelligence graph；讓 AI 只讀與 review 有關的 context。這正是 Codex 大型 repo 導航與 token 控制的痛點。 | Trending **+872 stars today**；25,160 stars；MIT；v2.3.7（7/18）。 | 86 open issues，先用獨立測試 repo 量測 context/review 品質，不直接取代現有 codebase-memory 流程。 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 將 code、docs、SQL schema、設定、PDF 轉可查詢 knowledge graph，並主打 Claude Code/Cursor/Codex skill；對 metabiz wiki 與產品 repo 的跨資料探索很貼合。 | 93,672 stars；snapshot delta **+503**；7/22 有 push；MIT；v0.9.23。 | 607 open issues；先驗證索引時間、資料外洩邊界與本機資源成本。 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Skill candidate | 面向 AI coding agent 的 production-grade engineering skills，可作為 Adam 現有 skills 的評估 checklist 與測試設計參考。 | 79,822 stars；snapshot delta **+130**；7/22 有 push；MIT；v0.6.4。 | 非即插即用的產品規格；只擷取可驗證流程，勿直接全量安裝或覆蓋既有 skill 邊界。 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Deep research | 壓縮工具輸出、log、檔案與 RAG chunks，主打 coding agent token 節省，並提供 library/proxy/MCP。 | 61,168 stars；snapshot delta **+149**；7/22 有 push；Apache-2.0；v0.32.0。 | 497 open issues；壓縮可能遺失 debugging 關鍵訊息，須用 RTK、repo log、RAG 三種真實輸入做準確率測試。 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Watch | 長時間 SuperAgent harness，含 sandbox、memory、tools、skills、subagents 與訊息閘道；很適合拆解 agent coordination 的產品設計。 | 77,606 stars；snapshot delta **+60**；7/22 有 push；MIT；v2.0.0。 | 973 open issues；系統面積大，先讀 architecture/安全模型，不建議直接作為 production orchestration layer。 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Deep research | Google 的 database MCP server，代表 MCP 從 demo 走向資料庫工具治理；適合作為 Odoo/ClickHouse 等資料工具 expose 設計的參考。 | 15,997 stars；snapshot delta **+4**；7/22 有 push；Apache-2.0；v1.7.0。 | 248 open issues；資料庫權限、query allowlist、audit 是前置條件，禁止把 production credential 直接交給 agent。 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Demo/content idea | Skills 生態的即時熱點與素材索引，適合做「技能不是 prompt：如何評估可重用 agent workflow」課程/影片選題。 | Trending **+155 stars today**；68,612 stars。 | License 為 `NOASSERTION`；只能作 discovery/reference，個別 skill 要回到原 repo 查授權與安全性。 |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Demo/content idea | 很小但清楚的 coding-agent 輸出 skill：避免把答案埋在冗長說明中。可作「好 skill 的最小規格」反例/正例示範。 | Trending **+1,682 stars today**；7,878 stars；7/22 有 push；MIT。 | 無 release、概念較窄；適合作為 UX pattern，不是完整工程工作流。 |
| [EtienneLescot/n8n-as-code](https://github.com/EtienneLescot/n8n-as-code) | Skill candidate | 把 n8n 節點 schema、範本與 Git-like sync 交給 AI agent；非常接近 AI 辦公室自動化「可版本控管 workflow」需求。 | 1,458 stars；7/22 有 push；MIT；v2.4.1。 | 規模較小、13 open issues；先以不含機密的單一 n8n workflow 做 round-trip 測試。 |

## 對 Adam 的可用行動

### 課程與內容選題

- **內容主題 A：**「AI Coding Agent 不是讀整個 repo：用 graph/skill/context compression 做出可量測的工作流」——比較 code-review-graph、Graphify、Headroom；驗收指標是 token、定位時間與 review 漏檢率，不是 star 數。
- **內容主題 B：**「Skill 的三個粒度」——i-have-adhd（輸出 UX）、agent-skills（工程規程）、n8n-as-code（可執行業務流程），示範何時該做 prompt、skill 或正式 automation。
- **內容主題 C：**「MCP 連資料庫前必問的五題」——以 MCP Toolbox 為骨架，帶出最小權限、read-only、allowlist、audit、資料遮罩。

### AI 辦公室自動化

- 近期 PoC 優先順序：`n8n-as-code` 的 workflow 版本控管 → `MCP Toolbox` 的 read-only 資料查詢 → `DeerFlow` 的長任務編排研究。
- 不要一次導入大型 multi-agent framework；先選一個可回復、無 production credential 的流程，定義成功率、人工接手點與成本上限。

### know metabiz wiki

- 先深研 Graphify 的本地索引與引用可追溯性；它比「再建一個向量庫」更接近既有 Obsidian/專案文件的可解釋探索。
- 可比較 [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)（3,244 stars、snapshot delta +6、MIT）與 [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)（9,802 stars、snapshot delta +43、MIT），但兩者都先在資料副本驗證連結、來源引用與錯誤寫回保護，不能直接對正式 vault 自動寫入。

## 明天持續追蹤

1. `tirth8205/code-review-graph`：每日 Trending 是否續強、release 後 issue 回應、真實 context reduction。
2. `Graphify-Labs/graphify`：snapshot delta、索引範圍和 Codex skill 的可重現性。
3. `headroomlabs-ai/headroom`：壓縮後 debugging/RAG 答案是否保持正確。
4. `addyosmani/agent-skills`：新增/調整的 skill 是否附可驗證 acceptance criteria。
5. `googleapis/mcp-toolbox`：database connector 與安全策略的 release/issue 變化。
6. `EtienneLescot/n8n-as-code`：schema 覆蓋、匯入匯出與 Git sync 是否能穩定 round-trip。
7. `bytedance/deer-flow`：sandbox、權限、human handoff 與 subagent coordination 設計。

## 資料與限制

- 完整 API 原始資料：[repos.json](repos.json)、機器摘要：[report.md](report.md)、本輪快照：[snapshots/repos-2026-07-23.json](snapshots/repos-2026-07-23.json)。
- 本資料夾是首次快照，collector 內部 `stars_delta=0` 屬正常基線；本報告另與 7/21 的同範圍快照交叉計算 `snapshot delta`。明日若對同一輸出目錄重跑，collector 即可產生原生 delta。
- GitHub stars/trending 反映開發者注意力，**不等於**課程付費需求、商業成熟度或可安全導入生產環境。
