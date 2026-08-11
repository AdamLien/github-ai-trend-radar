# GitHub AI Trend Radar 分析｜2026-08-10（台灣）

## 結論先行

本輪以固定十組查詢各取 10 筆，去重後取得 89 個專案；與 `2026-08-09` 同範圍 API 快照全數重疊，可比較約一天的星數淨增。這是兩次 API 觀測值的差異，不是 GitHub Trending 的「今日新增 stars」，而 collector 在本資料夾內的 `stars_delta` 仍為首次成功寫入的 0，故以下採跨資料夾計算的 delta。

最強訊號不是單純大星數，而是「可驗證工程 workflow／agent harness」、「可追溯的程式與文件知識圖」與「context 成本控制」三條線同時增長。GitHub Trending daily 於 8/11 台灣時間讀取，範圍內的當前注意力包括 `semantica-agi/semantica`（967 stars today）、`PrimeIntellect-ai/prime-agent`（2,356）、`addyosmani/agent-skills`（680）及 `paperclipai/paperclip`（167）；這只是當前訊號，不可倒推為 8/10 的歷史排行。

## 最值得追蹤的專案

| 分類 | 專案與動能 | 用途、維護訊號與風險 | 對 Adam 的可用性 |
| --- | --- | --- | --- |
| Deep research | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — 100,172★，`+989`，MIT，8/7 push，v4.9.0 | 以「少寫、先釐清」約束 agent；動能居首，但方法論須以缺陷率、返工與驗收案例量測，不能當品質保證。 | 課程中用作需求拆解、scope 與「不做什麼」示範，接入可驗收使用者情境。 |
| Deep research | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — 85,768★，`+820`，MIT，v0.6.6 | production-grade engineering skills；Trending 亦有 680 stars today，且 issue 數低（107），是強烈注意力訊號。 | 對照 metabiz skill 生命週期；只採納可驗證、review 模板，不覆蓋 RTK、人工核准與 scoped staging。 |
| Demo content | [earendil-works/pi](https://github.com/earendil-works/pi) — 86,725★，`+812`，MIT，8/10 push | 統一 LLM API、agent loop、TUI 與 coding agent CLI；活躍，但模型成本與工具權限必須隔離。 | 製作「長任務如何設停止線、觀測與回復」demo，不連接客戶憑證。 |
| Reference only | [obra/superpowers](https://github.com/obra/superpowers) — 270,259★，`+638`，MIT | Agentic SDLC 方法論，總星與增量都高；但其 worktree／subagent 預設流程不必然符合既有工作區治理。 | 萃取 debugging、verification、review 模板；不全域啟用。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — 105,012★，`+486`，Apache-2.0，8/10 push，v0.9.39 | 本地 AST 將 code、文件、SQL schema、PDF 轉為可查知識圖；宣稱每條 edge 可解釋、無 vector store。877 open issues，仍須實測。 | 用匿名 sample repo 驗證 source→node→edge；不可直接送入 metabiz 私密 wiki/vault。 |
| Skill candidate | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) — 65,825★，`+214`，Apache-2.0，8/10 push | 壓縮 tool output、log、檔案與 RAG chunk；節省率為專案主張，且 656 issues，需測完整性與失真。 | 以固定 corpus 記錄 token、延遲、答案正確率，形成 AI 辦公室的 context-budget skill。 |
| Skill candidate | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) — 3,342★，`+5`，MIT，8/10 push | 將來源整理成持久的 interlinked wiki，方向貼近 evidence-grounded wiki；低動能但可操作。 | 在可丟棄副本比對 raw source、append-only log、寫回 diff 與引用保留。 |
| Demo content | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) — 4,510★，`+221`，Apache-2.0 | Claude Code/Codex 的 Remotion 影片 skill；issues 僅 2、內容示範性強。 | 可作產品短片制作流程的案例；先檢查資產授權與渲染成本。 |
| Watch | [affaan-m/ECC](https://github.com/affaan-m/ECC) — 239,260★，`+304`，MIT，8/11 push | 對 Claude Code、Codex、Cursor 等的 harness 優化；更新新鮮，但 high-level claims 及整合範圍很大。 | 僅在隔離 PoC 測其記憶／安全設定；不導入 production workflow。 |
| Watch | [langgenius/dify](https://github.com/langgenius/dify) — 152,007★，`+152`，NOASSERTION，8/11 push | 成熟的 agent/RAG workflow workspace；熱度與更新均佳，但授權欄位未核實，且多模型、工具與資料流風險較高。 | 僅作架構／UX 參考，採用前先釐清 license、資料落點與角色權限。 |

## 可執行安排

- **Deep research**：以匿名化 10–20 篇 Markdown 加小型 repo，檢驗 Graphify 的 AST/document edge、敏感檔排除與來源可追溯；同時測 Ponytail／agent-skills 對需求漏項、測試覆蓋與 review 品質的效果。
- **Demo content**：用 Pi 展示「長任務從啟動到停止線」；用 video-shotcraft 展示可審核的短片製程。示範架構與量測結果，不宣稱生產推薦。
- **Skill candidate**：起草 Headroom 的 context-budget 操作卡；另為 llm-wiki-agent 建立「raw source → citation → diff → human approval」驗收腳本。
- **Watch**：追 Prime Agent、semantica、paperclip、ECC、Dify 的 README、license、release／issue 健康度，再決定是否進固定候選；未核實前不接觸客戶資料或正式憑證。
- **Reference only**：superpowers、awesome 清單與高星模板僅提供比較素材；不將 stars 直接視為採用或市場需求證明。

## 風險與假陽性

- 高星數與短期成長是開發者注意力，不是安全、品質、商業需求或維護承諾；模板／清單更容易掩蓋維護成本。
- Wiki、RAG、MCP database 與 agent 都可能存取敏感資料；預設應為最小權限、唯讀、allowlist、可回復 staging 與人工批准。
- `Dify` 的 API license 欄位為 `NOASSERTION`；`awesome-claude-skills` 沒有可辨識 license。未核實前不可視為可併入或再散布的依據。
- 本輪跨資料夾 delta 是 8/10 與 8/11 執行快照的差異，非精確 24 小時；Trending 的 stars today 是不同的頁面訊號，兩者不得混用。

## 明日追蹤清單

1. 固定十組查詢再跑一次，驗證 Ponytail、agent-skills、Pi、superpowers 與 Graphify 的動能是否延續。
2. 補 Prime Agent、semantica、paperclip、ECC、Dify 的 README、license、release／issue 活躍度與資料流。
3. 跑 Graphify 與 Headroom 的隔離基準，輸出可重現資料、失敗案例、token／完整性／延遲與資料外流檢查。
4. 寫出 MCP／wiki 寫入拒絕案例：越權查詢、未授權寫入與 audit 缺失均必須被阻擋。

## 資料來源與範圍

- API 搜尋與 repo 快照：[repos.json](./repos.json)；本次執行快照：[snapshots/repos-2026-08-11.json](./snapshots/repos-2026-08-11.json)。
- GitHub Trending daily：https://github.com/trending?since=daily（8/11 台灣時間讀取，僅為當前注意力訊號）。
- 本文依 GitHub metadata、專案描述、版本／更新時間與相鄰快照排序，為研究與內容規劃建議，不構成採購、部署或客戶資料處理授權。
