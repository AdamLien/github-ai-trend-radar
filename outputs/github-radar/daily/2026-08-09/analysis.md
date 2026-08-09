# GitHub AI Trend Radar 分析｜2026-08-09（台灣）

## 結論先行

本輪以 10 組固定搜尋詞各取 10 筆、去重後取得 89 個專案；與前一輪 `2026-08-08` 資料夾的同範圍快照全數重疊，可量測約一天的星數淨增。此值是兩個 API 快照的差異，不是 GitHub Trending 的「今日新增 stars」。GitHub Trending daily 於 8/10 台灣時間讀取，範圍內的當前注意力訊號為 `PrimeIntellect-ai/prime-agent`、`vitali87/code-graph-rag`、`msitarzewski/agency-agents`、`addyosmani/agent-skills`、`google/skills` 與 `pingdotgg/t3code`；不能倒推為 8/9 歷史排行榜。

優先研究三條線：可驗證工程 workflow（skills / harness）、可追溯的程式與文件知識圖、以及 context 與工具輸出的成本控制。星數只代表開發者注意力；授權、資料流、寫入權限、README 可操作性、release 與 issue 健康度才是是否進入 PoC 的門檻。

## 最值得追蹤的專案

| 分類 | 專案與動能 | 用途、維護訊號與風險 | 對 Adam 的可用性 |
| --- | --- | --- | --- |
| Deep research | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — 84,948★，`+631`，8/8 push，MIT，v0.6.6 | README 定位為 production-grade engineering skills；高增速與已發版是正向訊號，但 workflow 不應覆蓋既有 RTK、人工核准與 staging 邊界。 | 對照 metabiz skill 生命週期，做「spec → plan → build → test → review」課程案例。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — 104,526★，`+265`，8/8 push，Apache-2.0，v0.9.37 | README／描述主張以本地 AST 將 code、文件、SQL schema 與 PDF 轉為可查知識圖；867 open issues，且文件語意處理與模型/API 使用需另驗證。 | 在匿名 sample repo 驗證來源→節點→edge 的可追溯性；不可直接上傳 metabiz 私密 vault。 |
| Deep research | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) — 65,611★，`+131`，8/9 push，Apache-2.0，v0.34.0 | 在 LLM 前壓縮 tool output、log、檔案與 RAG chunk；最近有 release 與 push，但 629 issues，節省率屬專案主張，必須用固定 corpus 重測完整性。 | AI 辦公室／coding agent 的 token、延遲與答案品質基準實驗候選。 |
| Demo content | [earendil-works/pi](https://github.com/earendil-works/pi) — 85,913★，`+371`，8/9 push，MIT，v0.84.1 | 統一 LLM API、agent loop、TUI 與 coding-agent CLI；高增長且新鮮，但 connector、模型成本與工具權限要隔離驗證。 | 可拍「agent loop 如何可觀測與可停止」的 demo，避免連入客戶憑證。 |
| Demo content | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — 99,183★，`+509`，8/7 push，MIT，v4.9.0 | 主張以少寫程式、先驗證需求來約束 agent；動能高，但方法論需以缺陷率、返工與驗收案例量測，不能當成品質保證。 | 適合課程中的需求拆解與「不做什麼」案例，與可驗收情境結合。 |
| Skill candidate | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) — 16,135★，`-1`，8/8 push，Apache-2.0，v1.8.0 | 資料庫 MCP server 與自訂工具框架，負淨差只是短觀測窗，不等同衰退；最大風險是自然語言到資料庫的權限擴張。 | 萃取唯讀 schema 探索、allowlist、參數化、stage → human approval → audit 的安全 skill。 |
| Skill candidate | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) — 3,334★，`+5`，8/3 push，MIT | 將 raw source 建成 interlinked wiki、log 與 graph 的方向與 evidence-grounded wiki 一致；較低動能且寫回品質需實測。 | 比較其 raw/source/log 模式與 know metabiz wiki；只在可丟棄副本測寫入 diff。 |
| Watch | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) — Trending daily、8/8 push、MIT | RLM coding/research agent，含持久 REPL、sub-agent 與背景任務；本輪搜尋未收錄，沒有此範圍的可比星數。 | 追蹤 snapshot、rollback 與長任務停止線；先在無機密沙盒 PoC。 |
| Watch | [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag) — Trending daily | Trending 的 code/RAG 訊號直接呼應 Graphify；尚未進固定搜尋結果，缺少同範圍 delta、授權與 issue 健康度核實。 | 先讀 README、license 與資料流，再決定是否進 code knowledge graph 比較。 |
| Reference only | [obra/superpowers](https://github.com/obra/superpowers) — 269,621★，`+453`，8/8 push，MIT，v6.2.0 | 高注意力的 agentic SDLC 方法論；其自動化 worktree／subagent 取向與本工作區的 RTK、明確授權及小範圍 staging 需逐項相容性評估。 | 取用 debugging、verification 與 review 模板；不全域啟用其流程。 |

## 可執行安排

- Deep research：用匿名化 10–20 篇 Markdown 與小型 repo，驗證 Graphify 的 AST edge、文件 edge、敏感檔排除與可追溯來源；對 Headroom 以三組固定 tool/RAG corpus 同時記錄 token、完整性、答案正確率與延遲。
- Demo content：以 Pi 或 Ponytail 做「長任務如何設停止線、驗收與回復」示範；展示架構與可量測指標，不宣稱推薦生產導入。
- Skill candidate：先起草資料庫 MCP 安全操作卡（read-only default、allowlist、parameterized query、人工核准、audit）；另比對 llm-wiki-agent 的 raw source、append-only log、寫回 diff。
- Watch：Prime Agent、code-graph-rag、agency-agents、Google Skills 與 t3code 均先補 README、license、release/issue 活躍度及隔離 PoC，未核實前不接觸客戶資料或正式憑證。
- Reference only：superpowers、MCP server 清單與其他高星模板作為比較素材；不以星數直接轉為採用決策。

## 風險與假陽性

- 高星清單、模板與 awesome repo 容易掩蓋實際維護成本；例如 `ComposioHQ/awesome-claude-skills` 授權欄位空白，`langgenius/dify`、`hesreallyhim/awesome-claude-code` 為 `NOASSERTION`，不可當成已核實的採用許可。
- wiki、RAG、database MCP 與 agent 均可能讀寫敏感資料；先做資料分級、最小權限、可回復的 stage action 與人工批准。
- 本輪 `stars_delta` 是 8/8 → 8/10 執行快照的差異，非精確 24 小時，也不等同 Trending 的新增 stars；範圍外 Trending 候選一律標示為未量測。

## 明日追蹤清單

1. 用相同十組查詢再抓一次，確認 agent-skills、Pi、Ponytail、Graphify 的動能是否延續，並保留負成長與新收錄的原始值。
2. 補 Prime Agent、code-graph-rag、agency-agents、Google Skills、t3code 的 README/license/release/issue 健康度，再決定是否納入固定候選。
3. 跑 Graphify 與 Headroom 的隔離基準，輸出可重現測試資料、失敗案例與資料外流檢查。
4. 寫 database MCP 的拒絕案例，驗證越權 SQL、未授權寫入與 audit 缺失都會被阻擋。

## 資料來源與範圍

- API 搜尋及 repo 快照：[repos.json](./repos.json)；本次執行快照：[snapshots/repos-2026-08-10.json](./snapshots/repos-2026-08-10.json)。
- GitHub Trending daily：https://github.com/trending?since=daily（8/10 台灣時間讀取，僅作當前注意力訊號）。
- 本文依 GitHub metadata、專案描述及上述候選 README 定位形成研究優先序；不是採購、部署或客戶資料處理授權。
