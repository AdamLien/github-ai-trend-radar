# GitHub AI Trend Radar 分析｜2026-08-11（台灣）

## 結論先行

固定十組查詢各取 10 筆後原有 89 個範圍內專案；本次已把 GitHub Trending daily 的範圍內候選與歷史每日候選累積入池，得到 **152 個**。其中 53 個是過往熱門、目前未再命中固定搜尋的保留項；10 個是首次出現在 Radar 的新進榜：`PrimeIntellect-ai/prime-agent`、`anthropics/skills`、`paperclipai/paperclip`、`semantica-agi/semantica`、`stablyai/orca`、`vitali87/code-graph-rag` 等。新進榜沒有可比較的前一快照，故標為 `new`／成長待量測，**不以 0 當作動能**。既有項目的動能則以相鄰兩次 API 快照計算，約一天的觀測差值，不是 GitHub Trending 的歷史「今日新增 stars」。

本輪訊號集中於三條線：可操作的 coding-agent harness（Pi、Ponytail、agent-skills、Prime Agent）、可查且可追溯的 code/document knowledge graph（Graphify、Semantica、code-graph-rag），以及將工具輸出與 RAG context 控制在預算內（Headroom）。GitHub Trending daily 於 8/12 台灣時間讀取；其「stars today」保留成獨立即時訊號，不能倒推 8/11 的歷史排行，也不混入跨快照 delta。

## 最值得追蹤的專案

| 分類 | 專案與動能 | 用途、維護訊號與風險 | 對 Adam 的可用性 |
| --- | --- | --- | --- |
| Deep research | [earendil-works/pi](https://github.com/earendil-works/pi) — 87,502★，`+777`，MIT，8/11 push，v0.84.1 | 統一 LLM API、agent loop、TUI 與 coding-agent CLI；本輪最大增長且有近期 release。模型成本、工具權限與長任務失控仍要隔離。 | 做「啟動、停止線、觀測、回復」課程 demo；只接假資料與可撤銷 sandbox。 |
| Deep research | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — 100,648★，`+476`，MIT，v4.9.0 | 以先釐清需求、少寫程式為主的 agent 約束。增長強且 release 新鮮，但不能把方法論當成品質保證。 | 與可驗收使用者情境、scope/out-of-scope 寫法結合，量測漏項與返工。 |
| Deep research | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — 86,104★，`+336`，MIT，v0.6.6 | production-grade engineering skills；動能仍高，README 直接對應開發工作流。 | 比對 metabiz skills 的輸入、驗證與停止線；僅採可測的 review/verification 模板，不覆蓋 RTK 與人工核准。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — 105,227★，`+215`，Apache-2.0，8/11 push，v0.9.40 | 本地 AST 將 code、文件、schema、PDF 轉為可查知識圖，主張 edge 可解釋且不依賴 vector store；仍有大量 issue，須驗證可用性。 | 用匿名 sample repo 驗證 source→node→edge、敏感檔排除與 citation；不可直接匯入 metabiz 私密 wiki。 |
| Skill candidate | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) — 65,934★，`+109`，Apache-2.0，8/11 push，v0.34.0 | 壓縮 tool output、log、檔案與 RAG chunk；明確對準 context 成本，但壓縮宣稱須以完整性與答案正確率實測。 | 建立 AI 辦公室 context-budget skill：固定 corpus 記錄 token、延遲、資訊遺失與答案差異。 |
| Demo content | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) — 4,638★，`+128`，Apache-2.0 | Claude Code/Codex 的 Remotion 影片 skill；增幅相對基數高，適合作為可審核產出的示範。 | 做短片從 brief 到素材授權、render 成本與人工核稿的完整 demo。 |
| Watch | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) — 126,448★，`+223`，MIT，8/11 push，v3.19.2 | 多個 coding agent 的桌面切換器；更新新鮮但匯集多 provider、設定與憑證，攻擊面大。 | 僅以無客戶帳號 PoC 比較設定管理 UX，不存正式憑證。 |
| Watch | [affaan-m/ECC](https://github.com/affaan-m/ECC) — 239,410★，`+150`，MIT，8/11 push | 跨 Claude Code、Codex、Cursor 的 harness 優化；注意力很高，但宣稱與整合面廣，需要獨立驗證。 | 隔離環境測 memory/security preset；不直接改正式工作流。 |
| Watch | [langgenius/dify](https://github.com/langgenius/dify) — 152,103★，`+96`，8/11 push，v1.16.1 | Agent/RAG 協作平台，更新與動能都在；API metadata 的 license 是 `NOASSERTION`，且有資料落點、權限與模型供應商風險。 | 先作架構/UX 參考；採用前須釐清 license、資料流、角色權限。 |
| Reference only | [obra/superpowers](https://github.com/obra/superpowers) — 270,644★，`+385`，MIT | 高星且持續增長的 agentic SDLC 方法論；其 worktree/subagent 預設並不必然符合現有治理。 | 萃取 debugging、verification、review practices；不全域啟用。 |

## Trending 新進榜（首次觀測，成長待量測）

| 專案 | Trending 當日訊號 | 為何納入／下一步 |
| --- | --- | --- |
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | 14,131★，當日 +1,138 | self-improving RLM coding 與長任務 agent；列入 Deep research，先隔離驗證自我修改、工具權限與成本上限。 |
| [anthropics/skills](https://github.com/anthropics/skills) | 168,151★，當日 +485 | Agent Skills 公開庫；列入 Reference only，做技能格式與驗證介面的比較，勿因品牌或星數直接採用。 |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 77,188★，當日 +748 | 管理工作中 agents 的開源 app；列入 Watch，先查多租戶、審計、權限與資料落點。 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | 4,917★，當日 +893 | Graph-native context/accountable AI infrastructure；列入 Deep research，對照 Graphify 以 provenance、query 正確率與敏感資料排除測試。 |
| [stablyai/orca](https://github.com/stablyai/orca) | 42,820★，當日 +875 | 並行 coding agents 的 ADE；列入 Demo content，展示 queue、隔離與停止線，不接正式憑證。 |
| [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag) | 3,838★，當日 +341 | monorepo 的 code Graph RAG；列入 Skill candidate，與 metabiz wiki 的 source/citation/audit 要求做最小基準。 |

## 可執行安排

- **Deep research**：以匿名 10–20 篇 Markdown 與小型 repo，檢驗 Graphify 的可追溯 edge 與檔案排除；並讓 Pi、Ponytail、agent-skills 在同一份需求案例上比較漏項、測試與回退品質。
- **Demo content**：以 Pi 講解長任務停止線；以 video-shotcraft 講解可審核短片工作流。兩者只展示量測與流程，不宣稱 production adoption。
- **Skill candidate**：先寫 Headroom 的 context-budget 操作卡，驗收需含 token、延遲、完整性與資料外流檢查四欄。
- **Watch**：追 cc-switch、ECC、Dify 與新進榜 Paperclip 的 README、license、release/issue 活躍度與 secrets/data-flow；未核實前不接客戶資料或正式憑證。
- **Reference only**：superpowers 與各種 awesome 清單只作比較材料；stars 是開發者注意力，不是採購或市場需求證明。

## 風險與假陽性

- 跨資料夾 star 差異是兩個 API 快照的差值，非精確 24 小時，也不是 Trending daily 的 stars today；新進榜顯示 `new`／成長待量測，避免把首次出現誤讀為零動能。
- MCP、wiki、RAG 與 agent 一旦觸及檔案、資料庫或 token，預設應最小權限、唯讀 allowlist、可回復 staging 與人工批准。
- Dify 的 API license 欄位為 `NOASSERTION`；awesome 清單與模板的文件/維護品質不應由星數代替審查。
- Graphify、Headroom 的價值取決於資料可追溯與資訊保真，必須保留 raw source、引用與失敗案例，才可納入 know metabiz wiki 流程。

## 明日追蹤清單

1. 固定十組查詢加 Trending daily 再跑一次，驗證 Pi、Ponytail、superpowers、agent-skills、Graphify 與本輪新進榜是否持續領先。
2. 對 Graphify、Headroom 做隔離基準，輸出可重現 corpus、token/延遲/正確率與敏感資料排除結果。
3. 補 cc-switch、ECC、Dify 的 license、release/issue 健康度與秘密資料流查核。
4. 寫 MCP/wiki 拒絕案例：越權查詢、未授權寫入與缺 audit 均必須被阻擋。

## 資料來源與範圍

- API 搜尋與 repo 快照：[repos.json](./repos.json)；本次執行快照：[snapshots/repos-2026-08-12.json](./snapshots/repos-2026-08-12.json)。
- GitHub Trending daily：https://github.com/trending?since=daily（8/12 台灣時間讀取；範圍內候選已併入，`stars today` 仍是獨立的即時訊號）。
- 本文依相鄰快照的 star 差異、更新/release、README 定位與授權 metadata 排序；Radar 追蹤池採累積制，歷史候選不會因出榜刪除。本文屬研究與內容規劃建議，不構成採購、部署或客戶資料處理授權。
