# GitHub AI Trend Radar — 2026-07-18（台灣）

> 收集時間：2026-07-19 01:18–01:20（Asia/Taipei）；目標日為前一個台灣日期 2026-07-18。
>
> 訊號口徑：GitHub Trending 的 `stars today` 是收集當下的滾動 24 小時訊號，不是可回放的 7/18 歷史頁面；API `star delta` 則比較 7/18 與本次相同候選集的快照，約 25 小時。不要把兩者混為同一數字。

## 摘要

- 已以 GitHub 登入 token 跑完 10 組指定搜尋，產出 89 個去重後的 API/README metrics 快照；詳見 [repos.json](repos.json) 與 [collector report](report.md)。
- 這輪最清楚的訊號不是「又一個 agent framework」，而是三條可落地的工作流：**把程式／文件轉為可查詢上下文**、**把技能規格化**、以及**壓縮 agent 的工具輸出與研究上下文**。
- Adam 最值得先做的是：以去識別資料做 `code-review-graph`／Graphify 的 provenance PoC；以 `ui-skills` 做一支「設計也可 skill 化」課程／短影音 demo；把 `headroom` 當作 coding-agent token 成本與輸出治理的評估標的。

## 今日最值得追的專案

| Repo | 分類 | 用途與為何值得看 | 動能 | 風險／採用提醒 |
| --- | --- | --- | --- | --- |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Deep research | Local-first MCP/CLI code intelligence graph；把 codebase 建成持久地圖，讓 coding agent 只讀需要的上下文。最直接對應大型 repo review 與 source-linked wiki。 | Trending **356 stars today**；總 20,062（約 1.8%）。 | 尚須驗證索引更新、私有碼資料外流、刪除與 provenance；先只用去識別樣本。 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | Claude Code、Codex、Cursor 等可用的 knowledge-graph skill，可納入程式、schema、文件、影音。 | API：90,778 stars；相對前次快照 **+834**；7/18 push，v0.9.19。 | 高速成長不等於企業級治理；要測真正的檢索品質、權限與索引成本。 |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | Demo/content idea | Design Engineer 用的 skills，能把 UI 品味／規範轉成 agent 可執行的指令。 | Trending **242 stars today**；總 4,848（約 5.0%，本輪最高比例之一）。 | 偏前端設計工作流；不可把它當成通用產品設計方法論。 |
| [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | Skill candidate | 給 coding agent 的 local-first search/fetch/crawl/research MCP；主打不需 API key。 | Trending **192 stars today**；總 1,093（約 17.6%，小基數爆發）。 | Public beta；宣稱與安全／資料來源品質都必須實測，不能直接接觸內部網路。 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Deep research | 在 tool output、log、檔案、RAG chunk 進 LLM 前壓縮，是 agent 成本、上下文與可讀性治理層。 | API：59,810 stars；跨日快照 **+172**；7/18 push，v0.32.0。 | 壓縮可能漏掉 review 關鍵細節；要以任務正確率和可追溯原文，而非 token 節省單獨驗收。 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Skill candidate | Production-grade engineering skills 範例／規範，適合作為 Adam 自建 skill 的審查基準。 | API：79,123 stars；跨日 **+185**；7/18 push，0.6.4。 | 內容是通用工程技巧，不應未審查就覆蓋本地專案規則或敏感流程。 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Watch | Long-horizon SuperAgent：research、coding、sandbox、memory、tools、subagents 與 message gateway。 | API：77,348 stars；跨日 **+65**；7/18 push，v2.0.0。 | 範圍很大，操作與安全面積也大；先研究其協調模型，不要直接當生產編排器。 |
| [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | Demo/content idea | Kimi Code CLI，代表 coding-agent CLI 競爭仍在升溫，可做 Claude Code/Codex/Cursor 的定位比較。 | Trending **48 stars today**；總 9,365。 | 供應商、模型與帳號依賴；比較時要切開 CLI 體驗與模型能力。 |
| [PostHog/posthog](https://github.com/PostHog/posthog) | Reference only | AI observability/analytics 與 MCP 導向的 developer automation 平台。 | Trending **337 stars today**；總 36,472（約 0.9%）。 | 平台廣、導入重；作為「agent 可觀測性」案例，不是本輪優先部署。 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Watch | Database MCP server，對 ERP／資料庫連接的 guardrail 研究很相關。 | API：15,973 stars；跨日 **+3**；7/18 push，v1.7.0。 | 資料庫權限、query allowlist、審計與 PII 邊界需先完成；不直接連 production ERP。 |

## 對 Adam 的可用性

### 課程與內容選題

- **「AI agent 不是多讀檔，而是先建上下文地圖」**：比較 `code-review-graph`、Graphify 與傳統 RAG；示範 context 選擇如何影響 code review。
- **「Skills 從 prompt 集合變成可維護作業規範」**：以 `agent-skills` + `ui-skills` 拆出觸發條件、輸入、驗收、風險與版本控制。
- **「token 節省不等於答案正確」**：用 `headroom` 做壓縮前後的 review／debug 實驗，強調 source link 與完整性測試。

### AI 辦公室自動化

- `wigolo` 可研究為「公開網路 research MCP」候選，但只能置於低權限、隔離的研究層。
- `mcp-toolbox` 只適合做 database MCP guardrail 的設計參考：read-only role、允許的 schema/table、參數化查詢、審計與人工核准都要在前。
- `deer-flow` 可拿來研究長任務的 sandbox/memory/subagent handoff；協調層的真實價值在可觀測、可中止與可審核，不只是自動連跑。

### know metabiz wiki

- Graphify／`code-review-graph` 值得以**去識別的 wiki 子集**做 PoC，驗證「原始來源 → 抽取索引 → 回答引用」是否能保持可追溯。
- 不把私有 wiki 或 production code 直接餵入外部服務；先確認 local-only、metadata、索引刪除、權限切分與 export 行為。
- `nashsu/llm_wiki` 本輪僅作概念參考：雖有 14,843 stars、v0.6.4，但 license 是 `NOASSERTION`，不列為採用候選。

## 風險與假陽性

- `stars today` 對小基數專案很敏感；`wigolo` 的 17.6% 很吸睛，但不代表其安全性或可維護性已被驗證。
- 本資料夾第一次快照的 collector `stars_delta` 全為 0；本文的跨日 delta 是與 `2026-07-17` 資料夾中相同 repo 的快照相減，不是本次資料夾的內建欄位。
- GitHub star 是開發者注意力，不是課程付費需求、企業採購意願或 production readiness。

## 明日續追清單

1. `tirth8205/code-review-graph`：README、MCP 工具邊界、索引與 provenance 實測。
2. `Graphify-Labs/graphify`：去識別資料集的檢索正確率、刪除與 access-control PoC。
3. `headroomlabs-ai/headroom`：以真實 coding-agent 任務測量壓縮率與答案／review 漏失率。
4. `ibelick/ui-skills`：做一個課程 demo，判斷是否能複用為 Adam 的 UI 審查 skill。
5. `KnockOutEZ/wigolo`：只做隔離環境的 public-web research 安全評估。
6. `googleapis/mcp-toolbox`：整理 ERP read-only MCP 的 allowlist、audit、approval guardrails。
