# GitHub AI Trend Radar 分析｜2026-08-11（台灣）

## 結論先行

固定十組查詢各取 10 筆，去重後得到 89 個範圍內專案，且與 `2026-08-10` 資料夾的 89 筆全數重疊。collector 在新目標資料夾中第一次寫入，故其 `stars_delta` 為 0；以下動能改以相鄰兩次 API 快照計算，約一天的觀測差值，**不是 GitHub Trending 的歷史「今日新增 stars」**。

本輪訊號集中於三條線：可操作的 coding-agent harness（Pi、Ponytail、agent-skills）、可查且可追溯的 code/document knowledge graph（Graphify），以及將工具輸出與 RAG context 控制在預算內（Headroom）。GitHub Trending daily 已於 8/12 台灣時間讀取作為當前注意力來源；其頁面是即時榜，不能倒推 8/11 的歷史排行，故不混入本表的跨快照 delta。

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

## 可執行安排

- **Deep research**：以匿名 10–20 篇 Markdown 與小型 repo，檢驗 Graphify 的可追溯 edge 與檔案排除；並讓 Pi、Ponytail、agent-skills 在同一份需求案例上比較漏項、測試與回退品質。
- **Demo content**：以 Pi 講解長任務停止線；以 video-shotcraft 講解可審核短片工作流。兩者只展示量測與流程，不宣稱 production adoption。
- **Skill candidate**：先寫 Headroom 的 context-budget 操作卡，驗收需含 token、延遲、完整性與資料外流檢查四欄。
- **Watch**：追 cc-switch、ECC、Dify 的 README、license、release/issue 活躍度與 secrets/data-flow；未核實前不接客戶資料或正式憑證。
- **Reference only**：superpowers 與各種 awesome 清單只作比較材料；stars 是開發者注意力，不是採購或市場需求證明。

## 風險與假陽性

- 跨資料夾 star 差異是兩個 API 快照的差值，非精確 24 小時，也不是 Trending daily 的 stars today；collector 本資料夾 `stars_delta=0` 代表首次寫入而非沒有動能。
- MCP、wiki、RAG 與 agent 一旦觸及檔案、資料庫或 token，預設應最小權限、唯讀 allowlist、可回復 staging 與人工批准。
- Dify 的 API license 欄位為 `NOASSERTION`；awesome 清單與模板的文件/維護品質不應由星數代替審查。
- Graphify、Headroom 的價值取決於資料可追溯與資訊保真，必須保留 raw source、引用與失敗案例，才可納入 know metabiz wiki 流程。

## 明日追蹤清單

1. 固定十組查詢再跑一次，驗證 Pi、Ponytail、superpowers、agent-skills、Graphify 是否持續領先。
2. 對 Graphify、Headroom 做隔離基準，輸出可重現 corpus、token/延遲/正確率與敏感資料排除結果。
3. 補 cc-switch、ECC、Dify 的 license、release/issue 健康度與秘密資料流查核。
4. 寫 MCP/wiki 拒絕案例：越權查詢、未授權寫入與缺 audit 均必須被阻擋。

## 資料來源與範圍

- API 搜尋與 repo 快照：[repos.json](./repos.json)；本次執行快照：[snapshots/repos-2026-08-12.json](./snapshots/repos-2026-08-12.json)。
- GitHub Trending daily：https://github.com/trending?since=daily（8/12 台灣時間讀取，僅為當前注意力訊號）。
- 本文依相鄰快照的 star 差異、更新/release、README 定位與授權 metadata 排序，屬研究與內容規劃建議，不構成採購、部署或客戶資料處理授權。
