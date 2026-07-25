# GitHub AI Trend Radar — 2026-07-19（台灣）

> 收集時間：2026-07-20 00:10–00:14（Asia/Taipei）；目標日為前一個台灣日期 **2026-07-19**。
>
> 口徑：GitHub Trending 的 `stars today` 是收集時的滾動 24 小時訊號，**不是可回放的 7/19 歷史頁面**。API 星數則為本次約 00:10 的快照；`star delta` 比對 7/19 與前一輪 7/18 相同候選集的約 24 小時變化。兩種數字不可相加或互換。

## 摘要

- 已透過登入的 GitHub token 完成指定 10 組搜尋，取得 **89 個去重 repository** 的 metadata、release 與 metrics 快照；原始結果在 [repos.json](repos.json)、[report.md](report.md)、[snapshots/repos-2026-07-20.json](snapshots/repos-2026-07-20.json)。未遇 rate limit，維持 `--limit 10`。
- 今日應聚焦兩條線：**agent 的可控上下文**（code intelligence graph、knowledge graph、tool-output compression）與 **可重複的 skills / coding-agent harness**；不要把「多 agent」本身當成足夠的採用理由。
- 最快能產出驗證的是：對去識別 code/wiki 做 `code-review-graph` 或 Graphify 的 source-linked PoC；另以 `wigolo` 做隔離的公開網路 research demo，先驗證權限與來源治理。

## 今日最值得追的專案

| Repo | 分類 | 用途與為何值得看 | 動能 | 風險／採用提醒 |
| --- | --- | --- | --- | --- |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Deep research | Local-first MCP/CLI code intelligence graph；讓 coding agent 只取工作需要的 code context，直接對應大型 repo review 與 source-linked wiki。 | Trending **551 stars today**／20,567（約 **2.7%**）；API 快照稍後為 20,824，MIT。 | 先驗證索引更新、刪除、provenance 與私有碼外流；只用去識別樣本。 |
| [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | Watch | 給 coding agent 的 local-first web search/fetch/crawl/research MCP，主打免 API key。 | Trending **605 stars today**／1,559（約 **38.8%**，小基數爆發）；TypeScript。 | 仍是 public beta；來源品質、robots/合規、SSRF 與內網邊界未驗證，不能直接授予內網權限。 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | Claude Code、Codex、Cursor 可用的 knowledge-graph skill，可納入 code、schema、文件、影像與影音。 | API：91,428 stars、較前輪 **+650**（約 0.7%）；7/18 push 並釋出 v0.9.20，MIT。 | 高成長不是企業治理證明；要實測檢索正確率、metadata 外送、access control 與索引成本。 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Deep research | 在 tool output、log、檔案、RAG chunk 進模型前做壓縮；是 agent 成本與上下文治理層。 | API：60,044 stars、**+234**（約 0.4%）；7/19 push，Apache-2.0。 | token 變少不等於結果正確；需用真實 debug/review 任務量測遺漏率，保留原文可回查。 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Skill candidate | Production-grade engineering skills 範例，適合當 Adam 自建 skill 的審查與驗收基準。 | API：79,266 stars、**+143**；7/18 push，MIT。 | 是通用工程規範，不可未審查就覆蓋專案既有 AGENTS/安全規則。 |
| [obra/superpowers](https://github.com/obra/superpowers) | Reference only | Agentic skills framework 與開發方法論；對「skill 是可執行流程，不是 prompt 收藏」具參考值。 | API：257,463 stars、**+475**；MIT，但最近 push 是 7/17。 | 高注意力且本輪仍增長，卻不是今日最活躍的維護訊號；借鑑流程，勿直接整包採用。 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Watch | Database MCP server；對 ERP／資料庫 agent 的 read-only guardrail 最具參考性。 | API：15,980 stars；7/19 push，v1.7.0，Apache-2.0。 | 不直接連 production ERP：需要最小權限、schema/table allowlist、參數化 query、稽核與人工核准。 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Watch | Long-horizon SuperAgent，涵蓋 research、code、sandbox、memory、tools、skills、subagents。 | API：77,387 stars、**+39**；7/19 push，v2.0.0，MIT。 | 面積太大；先研究 cancellation、handoff、sandbox 與可觀測設計，非直接作為生產編排器。 |
| [github/copilot-sdk](https://github.com/github/copilot-sdk) | Demo/content idea | 把 GitHub Copilot Agent 整合到 app/service 的多平台 SDK，可做 coding-agent runtime 比較。 | Trending **111 stars today**／9,887（約 1.1%）；API 9,910 stars，7/19 push，MIT。 | GitHub/Copilot 帳號與供應商依賴明確；比較時分開 SDK、模型、IDE/CLI 體驗。 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Demo/content idea | Rust coding-agent harness，適合觀察 agent harness 的工具與工作迴圈設計。 | Trending **199 stars today**／8,689（約 **2.3%**）；API 8,746 stars，7/19 push，MIT。 | 不以 Trending 取代安全與可維護性檢驗；需先確認 sandbox、credential 與 repo write 邊界。 |

## 對 Adam 的可用性

### 課程與內容選題

- **「不是塞更多上下文：先把上下文變成可查詢的地圖」**：比較 `code-review-graph`、Graphify 與一般 RAG，示範回答附回原始檔／段落的 provenance。
- **「Skills 是可驗收的工作流，不是 prompt 備忘錄」**：用 `agent-skills`、`superpowers` 與本地 skill 對照 trigger、輸入、驗收、風險、版本與 project override。
- **「免費 web MCP 也要做權限設計」**：以 `wigolo` 示範公開研究環境，刻意不接內網、登入狀態或 production secrets。

### AI 辦公室自動化

- `code-review-graph`／Graphify：優先做小範圍、可刪除的 code/wiki context PoC；回答需保留 source link，而非只給摘要。
- `mcp-toolbox`：可作 ERP data-access guardrail 參考，不是直接安裝到 production 的理由。
- `deer-flow`／`jcode`：研究 agent coordination 時，以「能否暫停、審核、回復與追責」取代「是否能連跑很久」作為評估主軸。

### know metabiz wiki

- 最實用的下一步是 Graphify 或 `code-review-graph` 的**去識別 wiki 子集**：驗證原始來源 → 索引 → 回答引用 → 刪除更新的閉環。
- 對會爬網或遠端服務的工具，先確認 local-only 行為、metadata、索引資料位置與 export／telemetry；不可將私有 wiki 直接上傳。
- `nashsu/llm_wiki` 本輪為概念參考：14,894 stars、跨輪 +51、v0.6.4，但 license 為 `NOASSERTION`，不列採用候選。

## 風險與假陽性

- `wigolo` 的 38.8% 是最強注意力訊號，但小基數的 `stars today` 非品質、資安或維護能力的證明。
- 各日期資料夾自己的首次快照都會顯示 `stars_delta=0`；本頁的 delta 是由前一個日資料夾的重疊 88 個 repo 重新計算，約 24 小時，並非 collector 內建欄位。
- GitHub stars 代表開發者注意力，不代表課程付費需求、企業採購意願或 production readiness。

## 明日續追清單

1. `tirth8205/code-review-graph`：以去識別 repo 測 context reduction、review 漏失率與 provenance。
2. `Graphify-Labs/graphify`：做 source-linked wiki PoC，量測正確引用、刪除與 access-control。
3. `KnockOutEZ/wigolo`：只在隔離環境驗證 web research 的權限、來源與安全邊界。
4. `headroomlabs-ai/headroom`：用真實 coding-agent 任務同時量測壓縮率與決策錯漏。
5. `googleapis/mcp-toolbox`：產出 ERP read-only MCP 的 allowlist、audit、approval 設計清單。
6. `addyosmani/agent-skills`：擇一個可轉為 Adam 本地 skill 的驗收標準，勿直接移植整包規則。
