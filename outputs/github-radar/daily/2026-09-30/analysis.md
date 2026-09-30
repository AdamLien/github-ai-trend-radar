# GitHub AI 趨勢雷達｜2026-09-30

## 今日判讀

優先深研 OpenRig、OpenShell 與 PageIndex：分別對應多代理協作、執行環境及文件檢索。VoiceStudio、DBX 適合先做小型展示；Skills 類要以可驗證流程與相容性決定採用。以下排序結合今日星數、相對成長、最近 push、release、README 與 issue／PR，並非總星數排行。

## 資料口徑

- 目標日期為台北時間前一天 2026-09-30；實際收集於 2026-10-01 台北時間。GitHub Trending 是執行當下滾動榜單，不是該日午夜封存值。
- 今日星數來源：[GitHub Trending daily](https://github.com/trending?since=daily)。總星數、README、release 與最近五筆 issue／PR 的查核資料保存在 `review-evidence.json`；因此與較晚完成的 collector 快照可能有少量差異。
- 星數增量以 2026-09-29 的本地快照為基準，相對成長＝增量／前次總星數。首次觀察標示無基準，不把零當成無成長。
- GitHub open_issues_count 含 PR，不能當成未解決 bug 數；最近五筆只是活動樣本，不能據此推算整體解決率。README 的效果宣稱尚未實測。

## 值得追蹤的 9 個專案

### mvschwarz/openrig — Deep research

[GitHub／README](https://github.com/mvschwarz/openrig) · **總星數 2,811** · **今日 +622** · 快照增量 +603（+27.31%）

- 用途：把 Claude Code 與 Codex 組成持續運作的代理團隊，以 YAML 定義角色與協作。README 有 starter rigs、工作區及升級流程。
- 動能：小基數配合高單日關注度，優先研究團隊恢復與任務交接，不以總星數排位。 最近 push：2026-09-30T16:08:45Z；release：[v0.6.2](https://github.com/mvschwarz/openrig/releases)，發布 2026-09-30T05:32:32Z。
- 活動證據：最近樣本 [fix: recognize managed Claude seats behind launch wrappers](https://github.com/mvschwarz/openrig/pull/220)，狀態 open，更新 2026-09-30T16:11:39Z。API 未關閉 issue／PR 合計 116。
- 風險：安全修正 PR #149 仍開啟，涉及通知及 API 邊界；升級與代理程序恢復也需實測。
- Adam／metabiz 關聯：適合 Adam 多代理課程：以小型文件整理任務示範兩種 coding agent 分工，後續評估 AI 辦公流程。

### NVIDIA/OpenShell — Deep research

[GitHub／README](https://github.com/NVIDIA/OpenShell) · **總星數 11,831** · **今日 +1,280** · 快照增量 +1,599（+15.63%）

- 用途：提供自主 AI agent 的執行環境；README 涵蓋運作方式、agent skills、SDK 與 telemetry。
- 動能：今日關注度高，且 release 與 push 都近期更新，適合驗證辦公代理的隔離及網路政策。 最近 push：2026-09-30T16:08:39Z；release：[v0.1.2](https://github.com/NVIDIA/OpenShell/releases)，發布 2026-09-28T03:58:00Z。
- 活動證據：最近樣本 [bug: Restore GCP metadata server support](https://github.com/NVIDIA/OpenShell/issues/3860)，狀態 open，更新 2026-09-30T16:08:24Z。API 未關閉 issue／PR 合計 511。
- 風險：GCP metadata server 支援回報 #3860 尚開啟；安全定位不是已經完成環境隔離驗證的保證。
- Adam／metabiz 關聯：可成為 Adam AI 辦公自動化課程的執行環境案例，評估存取 know metabiz wiki 前的權限邊界。

### VectifyAI/PageIndex — Deep research

[GitHub／README](https://github.com/VectifyAI/PageIndex) · **總星數 37,963** · **今日 +1,095** · 快照增量 +971（+2.62%）

- 用途：以文件結構與推理進行 RAG；README 比較向量 RAG，提供本機索引與查詢成本章節。
- 動能：高今日星數搭配近期 release；直接命中文件知識檢索需求，優先於泛用大型 agent 清單。 最近 push：2026-09-30T08:22:36Z；release：[v0.2.20](https://github.com/VectifyAI/PageIndex/releases)，發布 2026-09-28T14:03:36Z。
- 活動證據：最近樣本 [Restructure repo layout](https://github.com/VectifyAI/PageIndex/pull/539)，狀態 closed，更新 2026-09-30T08:22:37Z。API 未關閉 issue／PR 合計 108。
- 風險：README 的 benchmark 不能直接外推到繁中內部文件；必須測頁碼引用、正確率、延遲及模型費用。
- Adam／metabiz 關聯：know metabiz wiki 可用已公開文件做樹狀檢索對照；Adam 可製作「向量 RAG 與文件推理」課程內容。

### t8y2/dbx — Demo content

[GitHub／README](https://github.com/t8y2/dbx) · **總星數 22,951** · **今日 +1,133** · 快照增量 +1,171（+5.38%）

- 用途：資料庫客戶端，提供 AI SQL assistant、MCP 整合與多種資料庫管理功能。README 明列查詢、schema 與連線功能。
- 動能：今日關注度高且當日有 release，適合具體的資料查詢示範。 最近 push：2026-09-30T13:55:29Z；release：[v0.6.29](https://github.com/t8y2/dbx/releases)，發布 2026-09-30T10:26:10Z。
- 活動證據：最近樣本 [[Bug] 新建postgresql数据库，sql预览窗口无法关闭](https://github.com/t8y2/dbx/issues/10819)，狀態 open，更新 2026-09-30T15:43:28Z。API 未關閉 issue／PR 合計 1,303。
- 風險：資料庫種類多不代表每個操作成熟；PostgreSQL 視窗回報 #10819 尚未解決，AI SQL 需先用唯讀測試資料庫。
- Adam／metabiz 關聯：Adam 可錄製「自然語言到唯讀 SQL 報表」；AI 辦公自動化可評估報表流程，wiki 記錄 schema 與操作 SOP。

### debpalash/VoiceStudio — Demo content

[GitHub／README](https://github.com/debpalash/VoiceStudio) · **總星數 49,982** · **今日 +3,481** · 快照增量 +2,904（+6.17%）

- 用途：本機語音生成、配音、轉錄與有聲書工具；README 提供桌面版使用途徑與責任使用章節。
- 動能：今日星數在本次候選中最高，但先做可重現示範，再考慮導入內容生產。 最近 push：2026-09-29T15:45:28Z；release：[v0.5.6](https://github.com/debpalash/VoiceStudio/releases)，發布 2026-09-23T08:53:32Z。
- 活動證據：最近樣本 [[Crash] Backend died (exit code -1073741819)](https://github.com/debpalash/VoiceStudio/issues/2394)，狀態 open，更新 2026-09-30T16:10:10Z。API 未關閉 issue／PR 合計 76。
- 風險：後端崩潰 issue #2394 與修正 PR #2467 尚開啟；繁中品質、硬體需求與聲音授權仍須實測或確認。
- Adam／metabiz 關聯：適合 Adam 課程旁白與短片配音內容，亦可探索會議轉錄後寫入 know metabiz wiki 的人工審稿流程。

### mattpocock/skills — Skill candidate

[GitHub／README](https://github.com/mattpocock/skills) · **總星數 272,757** · **今日 +736** · 快照增量 +881（+0.32%）

- 用途：日常工程使用的 agent skills，README 以需求理解、輸出長度、程式正確性與架構等問題組織。
- 動能：星數基盤大，相對成長應一起看；近期 push 比較舊 release 更能反映內容維護。 最近 push：2026-09-29T12:38:37Z；release：[v1.2.3](https://github.com/mattpocock/skills/releases)，發布 2026-08-06T14:05:28Z。
- 活動證據：最近樣本 [Has anyone created a Codex version?](https://github.com/mattpocock/skills/issues/178)，狀態 closed，更新 2026-09-30T14:30:27Z。API 未關閉 issue／PR 合計 537。
- 風險：wizard 執行中修改腳本的問題 #1142 尚開啟；不要整包覆蓋既有 skills，需逐項比較與試用。
- Adam／metabiz 關聯：Adam 的技能設計課程可挑一個工程流程做前後對照；將可驗證步驟轉成辦公流程 Skill，wiki 保存採用理由。

### colbymchenry/codegraph — Deep research

[GitHub／README](https://github.com/colbymchenry/codegraph) · **總星數 72,501** · **今日 +159** · 快照增量 無可比較基準

- 用途：本機程式碼知識圖譜，提供 agent 語意程式碼查詢與變更同步；README 列出語言支援與 MCP 工具。
- 動能：今日星數較溫和，但近期 Kotlin 修正 PR 已合併，功能維護證據比排行更有用。 最近 push：2026-09-30T15:52:26Z；release：[v1.6.1](https://github.com/colbymchenry/codegraph/releases)，發布 2026-09-29T05:08:55Z。
- 活動證據：最近樣本 [fix(kotlin): record infix calls as calls](https://github.com/colbymchenry/codegraph/pull/2174)，狀態 closed，更新 2026-09-30T15:52:27Z。API 未關閉 issue／PR 合計 511。
- 風險：Markdown 文件圖譜 PR #361 尚未合併，不能視為已成熟的通用 wiki 索引；宣稱省 token 需用本專案重測。
- Adam／metabiz 關聯：適合 Adam coding agent 課程，比較搜尋與圖譜查詢；know metabiz wiki 可先收錄程式庫架構索引，不等同一般文件 RAG。

### DietrichGebert/ponytail — Watch

[GitHub／README](https://github.com/DietrichGebert/ponytail) · **總星數 148,822** · **今日 +675** · 快照增量 +818（+0.55%）

- 用途：讓 coding agent 偏向較少程式碼與避免過度設計的提示／插件；README 有 before/after、多平台安裝及指令。
- 動能：仍有今日熱度，但最近 push 停在 9/14，需等待平台相容性修正落地。 最近 push：2026-09-14T14:34:56Z；release：[v4.10.0](https://github.com/DietrichGebert/ponytail/releases)，發布 2026-09-14T14:38:56Z。
- 活動證據：最近樣本 [Plugin fails to load on OpenCode v2: v1 plugin API (default export is a function, not an object)](https://github.com/DietrichGebert/ponytail/issues/941)，狀態 open，更新 2026-09-30T14:20:41Z。API 未關閉 issue／PR 合計 318。
- 風險：OpenCode v2 載入問題 #941 與遷移 PR #943 尚開啟；減少程式碼不等於功能正確。
- Adam／metabiz 關聯：可作 Adam 課程中「提示風格是否改善品質」的對照案例；先不作為 AI 辦公流程的預設策略。

### mksglu/context-mode — Watch

[GitHub／README](https://github.com/mksglu/context-mode) · **總星數 24,366** · **今日 +88** · 快照增量 +150（+0.62%）

- 用途：透過 MCP、hooks、工具輸出沙箱與工作階段記憶管理 coding agent context；README 詳列知識庫及路由機制。
- 動能：今日關注度不高但與長文件工作流相關；持續 push 與較舊 release 存在落差，先查相容性。 最近 push：2026-09-30T12:07:33Z；release：[v1.0.169](https://github.com/mksglu/context-mode/releases)，發布 2026-06-29T18:18:53Z。
- 活動證據：最近樣本 [fix(claude-code): restore external-MCP hook routing with `mcp__.*` (#1222)](https://github.com/mksglu/context-mode/pull/1231)，狀態 open，更新 2026-09-30T15:59:45Z。API 未關閉 issue／PR 合計 304。
- 風險：路由修正 PR #1231 與 hook timeout PR #1228 尚開啟；98% 壓縮屬專案宣稱，另需確認 NOASSERTION 的實際授權文本。
- Adam／metabiz 關聯：適合 Adam 長任務與 token 成本課程；know metabiz wiki 的大量檢索輸出可作測試，需量測重要資訊是否遺失。

## 明日觀察清單

1. OpenRig：追蹤 #149 是否合併、v0.6.2 恢復流程，以及小基數今日熱度是否持續。
2. OpenShell：確認 #3860 與網路／sandbox 修正，設計最小權限文件任務。
3. PageIndex：用相同繁中文件題組比較引用正確率與查詢成本，確認雲端與本機邊界。
4. VoiceStudio：追蹤 #2394／#2467；先完成一段繁中配音與轉錄品質檢查。
5. DBX：追蹤 #10819，設計唯讀 SQL 報表示範。
6. Skills／CodeGraph：確認 wizard 修正及 Markdown 圖譜 PR 的進度，再決定 Skill 採用或 wiki 整合。
7. Ponytail／Context Mode：等待 OpenCode v2、MCP 路由及 timeout 修正；以實測成功率而非 token 宣稱決定採用。

## 收集與範圍

collector 使用指定十組查詢、`--limit 10`、daily Trending、README 與目標日期。完整完成狀態及 rate-limit 紀錄見 `collection-status.json`。本文只選 AI、代理、Skills、MCP、RAG 與開發／辦公自動化項目；通用人生指南與無關 SDK／硬體排行不列入推薦。

收集完成：API rate limit 未發生，limit 10 成功，無須降至 5。保留 318 個主題內專案；Trending 保留 14 個。4 個歷史倉庫 404 已標記 `metadata_stale`，不納入本日推薦；名單見 `collection-status.json`。
