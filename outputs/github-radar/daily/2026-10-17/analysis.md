# GitHub AI 趨勢雷達｜2026-10-17

本期優先關注可驗證的檢索、跨 agent 記憶與文件工作流程；其次研究 plugin／skill 的封裝品質。以下十項依短期動能、近期維護與 Adam 的使用情境編排，並非總星數排行。

## 觀測方法與資料限制

- 歸檔目標日：2026-10-17，依 Asia/Taipei 前一日計算；本次開始抓取：2026-10-17T16:10:58.938844+00:00。Trending 原頁保存於 `trending-daily.html`，時間與卡片記錄於 `trending-evidence.json`。這是執行當下的 daily 榜單，不是重建目標日的歷史排名。
- 從專案根目錄執行十組指定查詢，搭配 `--include-trending-daily --include-readme --snapshot-date 2026-10-17`；原始 360 筆，合併 5 組轉址重複並排除 12 個範圍外專案後，共 343 個追蹤專案（見 `scope-review.json`）。來源包括查詢、當日榜單與歷史追蹤。
- API 限流：未觀測到；使用 --limit 10，未啟用 --limit 5 重試。
- stars today 採 GitHub 榜單標示；快照 Δ 採本期總星數減 2026-10-16 快照，相對成長＝Δ／前期星數。觀測間隔不保證剛好 24 小時；未上榜不等於零成長，首次觀測無可用增長率。
- README、最新 release 與每個精選最多五筆近期 issue／PR 互相參照；issue 數含 PR，樣本不能推估完整活動量或缺陷率。PR／issue 僅屬開發訊號，本期沒有安裝專案或重現效能宣稱。原始證據見 `editorial-evidence.json`。
- 本期 4 個歷史專案回傳 404，collector 沿用舊值；這些紀錄以 metadata_freshness 標記，不列精選。沒有 release 資料表示未取得，不能推論沒有維護。

VoiceStudio 屬 AI 語音工具，本期補上 daily 榜單 +2,135 的來源訊號；精選仍以檢索、技能與辦公流程的可用性為主。LLM Wiki 推送時間較舊，但近期有 PR 更新，故列為研究候選而非已完成導入；CLI-Anything 同樣需區分榜單熱度與主分支更新。

## 十個值得投入的專案

### 1. xerj-org/xerj — Deep research

[xerj-org/xerj](https://github.com/xerj-org/xerj)｜stars today：+1,102｜總星數：**7,523**｜快照 Δ：**+880**｜相對成長：**+13.25%**。

最近推送：2026-10-17T16:12:31Z；最新 release：v1.0.0-rc.96（2026-10-16T14:51:29Z）；授權：Apache-2.0；open issues／PR 合計：21。近期樣本：1 個 issue、4 個 PR，最近更新 2026-10-17T16:10:33Z；本期參考 [#1611](https://github.com/xerj-org/xerj/pull/1611)（open）。

- 用途：為程式碼、文件、log、PDF 建立本機搜尋索引，讓 agent 參考既有實作及檢索資料。
- 判斷與風險：README 的 token 節省數字是作者案例，尚未重現；近期 mapping／embedder 修補表示介面與索引語意仍需驗證。應用同一資料集比較召回率、來源定位及總成本。
- Adam 關聯：適合 Adam 的 AI 檢索課程與成本實測內容；辦公文件搜尋與 know metabiz wiki 可測試增量索引、原文回鏈與檔案排除規則。

### 2. MadsLorentzen/ai-job-search — Demo content

[MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)｜stars today：+1,397｜總星數：**49,678**｜快照 Δ：**+1,657**｜相對成長：**+3.45%**。

最近推送：2026-10-15T16:16:00Z；最新 release：v1.7.2（2026-09-29T18:32:55Z）；授權：MIT；open issues／PR 合計：54。近期樣本：0 個 issue、5 個 PR，最近更新 2026-10-17T15:53:59Z；本期參考 [#614](https://github.com/MadsLorentzen/ai-job-search/pull/614)（open）。

- 用途：以 Claude Code 串接職缺評估、履歷調整、求職信與面試準備，將文件工作拆成可重複流程。
- 判斷與風險：近期 tracker 欄位連接與 profile 模板修補，顯示資料結構與輸出驗收比一次生成更重要；職缺入口偏丹麥市場，在地化與個資處理需另測。作者求職成效不是通用保證。
- Adam 關聯：可改編成 Adam 的需求比對→提案草稿→人工審核課程與內容；AI 辦公自動化可示範客戶資料整理，wiki 記錄模板、來源與審核節點。

### 3. anthropics/claude-plugins-official — Skill candidate

[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)｜stars today：+1,383｜總星數：**41,360**｜快照 Δ：**+1,246**｜相對成長：**+3.11%**。

最近推送：2026-10-17T07:36:42Z；最新 release：未取得 release；授權：Apache-2.0；open issues／PR 合計：1164。近期樣本：2 個 issue、3 個 PR，最近更新 2026-10-17T12:22:28Z；本期參考 [#6754](https://github.com/anthropics/claude-plugins-official/pull/6754)（closed）。

- 用途：提供 Anthropic 維護的 Claude Code plugin 目錄，含內部與第三方 plugins，適合研究技能封裝與分發。
- 判斷與風險：官方目錄不代表每個外部 plugin 都有相同信任邊界；需逐項檢查外部服務、授權、hook 與寫入範圍。近期設定文件 PR 是整合活動證據，不是功能驗證。
- Adam 關聯：適合 Adam 的 skill／plugin 封裝教材與辦公小任務範例；know metabiz wiki 可建立評選清單、固定版本與安裝前後驗收紀錄。

### 4. akitaonrails/ai-memory — Deep research

[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)｜stars today：+208｜總星數：**9,783**｜快照 Δ：**+254**｜相對成長：**+2.67%**。

最近推送：2026-10-17T15:56:08Z；最新 release：v3.1.0（2026-10-16T05:43:14Z）；授權：MIT；open issues／PR 合計：28。近期樣本：1 個 issue、4 個 PR，最近更新 2026-10-17T15:56:10Z；本期參考 [#1359](https://github.com/akitaonrails/ai-memory/pull/1359)（closed）。

- 用途：在 Claude Code、Codex 等 coding agent 間保存長期記憶與工作交接，讓不同工具延續任務脈絡。
- 判斷與風險：近期 PR 涉及登入錯誤內容清理與 OIDC HTTPS 限制；是否合併及已發佈需逐版確認。跨 agent 記憶可能帶入過期結論或不該保存的內容，需測刪除、隔離與來源追溯。
- Adam 關聯：適合 Adam 示範跨工具交接與持久記憶；辦公長任務可保存進度，know metabiz wiki 可比較「短期任務記憶」與「經審核公司知識」的維護方式。

### 5. stablyai/orca — Demo content

[stablyai/orca](https://github.com/stablyai/orca)｜stars today：+829｜總星數：**95,065**｜快照 Δ：**+821**｜相對成長：**+0.87%**。

最近推送：2026-10-17T16:12:34Z；最新 release：v1.4.229（2026-10-17T06:54:05Z）；授權：MIT；open issues／PR 合計：8532。近期樣本：0 個 issue、5 個 PR，最近更新 2026-10-17T16:12:03Z；本期參考 [#30080](https://github.com/stablyai/orca/pull/30080)（open）。

- 用途：以多 worktree 並行執行 Codex、Claude Code 等 agent，提供任務管理、終端、瀏覽器設計互動與手機伴隨介面。
- 判斷與風險：README 功能清單尚未實測；並行 agent 仍可能在外部系統產生共享副作用，worktree 不會隔離所有狀態。遠端連線、同步、合併成本與訂閱需求都要納入測試。
- Adam 關聯：適合 Adam 的多 agent 比較與任務拆解課程；辦公自動化可比較同一文件任務的不同方案，wiki 留存任務分工與採用理由。

### 6. HKUDS/CLI-Anything — Demo content

[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)｜stars today：+580｜總星數：**53,879**｜快照 Δ：**+568**｜相對成長：**+1.07%**。

最近推送：2026-09-22T02:01:29Z；最新 release：v0.4.0（2026-06-25T15:17:49Z）；授權：Apache-2.0；open issues／PR 合計：184。近期樣本：1 個 issue、4 個 PR，最近更新 2026-10-17T15:25:43Z；本期參考 [#577](https://github.com/HKUDS/CLI-Anything/pull/577)（open）。

- 用途：為既有軟體提供可由 agent 操作的 CLI／harness，社群 registry 涵蓋圖形、影音、文件等操作。
- 判斷與風險：近期 FreeCAD 輸出與 VLC harness PR 顯示整合仍逐工具演進；有 PR 不等於已發佈。CLI 包裝的成熟度、讀回驗證與錯誤回復需分別確認，先以副本測試重複執行。
- Adam 關聯：適合 Adam 的「既有軟體如何接上 AI」內容；辦公文件與影音流程可做可重現 demo，wiki 記錄每個 wrapper 的版本、限制及驗收方式。

### 7. affaan-m/ECC — Watch

[affaan-m/ECC](https://github.com/affaan-m/ECC)｜stars today：+1,145｜總星數：**282,108**｜快照 Δ：**+1,002**｜相對成長：**+0.36%**。

最近推送：2026-10-15T19:17:01Z；最新 release：v2.2.3（2026-10-01T23:00:36Z）；授權：MIT；open issues／PR 合計：237。近期樣本：2 個 issue、3 個 PR，最近更新 2026-10-17T14:58:00Z。

- 用途：將規劃、測試、review、記憶、skills 與 hooks 整合成 coding agent 工程流程，README 區分原生支援與能力有限的 adapters。
- 判斷與風險：功能與設定面大，跨 harness 並非完全等價；近期 UTF-8 BOM 設定讀取討論顯示平台差異。先拆出單一流程驗證，避免將目錄數量當品質。
- Adam 關聯：Adam 課程可比較不同 agent 工作流的可驗收性；AI 辦公自動化借用規劃→產出→驗證，wiki 整理可抽成內部 skill 的部分與版本依賴。

### 8. nashsu/llm_wiki — Deep research

[nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)｜stars today：未上榜｜總星數：**20,722**｜快照 Δ：**+15**｜相對成長：**+0.07%**。

最近推送：2026-09-28T01:43:23Z；最新 release：v0.6.12（2026-09-28T02:58:13Z）；授權：NOASSERTION；open issues／PR 合計：285。近期樣本：5 個 issue、0 個 PR，最近更新 2026-10-17T08:02:16Z；本期參考 [#821](https://github.com/nashsu/llm_wiki/issues/821)（open）。

- 用途：把來源文件增量整理成有來源追溯的 wiki，支援多格式匯入、模型配置、知識圖與來源限定檢索。
- 判斷與風險：近期 Pi 唯讀 WikiToolServer／Chat 開發值得追蹤，但 PR 標題不代表功能已上線。需檢查匯入正確性、刪除同步、權限、模型外送資料及原文引用；wiki 生成仍可能誤述。
- Adam 關聯：與 know metabiz wiki 最直接相關：用公開文件測試匯入→更新→問答→引用→刪除全流程；適合 Adam 的 AI 知識管理課程與辦公 SOP 示範。

### 9. android/skills — Skill candidate

[android/skills](https://github.com/android/skills)｜stars today：+368｜總星數：**8,321**｜快照 Δ：**+390**｜相對成長：**+4.92%**。

最近推送：2026-10-16T10:07:27Z；最新 release：v1.0.15（2026-10-14T11:24:10Z）；授權：Apache-2.0；open issues／PR 合計：41。近期樣本：5 個 issue、0 個 PR，最近更新 2026-10-17T15:26:14Z；本期參考 [#240](https://github.com/android/skills/issues/240)（open）。

- 用途：提供針對 Android 特定任務的模組化 agent skills；README 表示優先處理評測顯示 LLM 較弱的流程。
- 判斷與風險：近期 issue 回報 testing-setup 引入額外 DI 框架與 Compose 範例截斷；這是待核實回報，不能直接當成已證實缺陷。技能仍需配合實際專案版本驗證。
- Adam 關聯：Adam 可用來教「如何以失敗案例與評測設計 skill」；辦公自動化與 wiki 不直接依賴 Android，但可借用範例驗證、來源依據與技能驗收方法。

### 10. K-Dense-AI/scientific-agent-skills — Reference only

[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)｜stars today：+879｜總星數：**52,061**｜快照 Δ：**+829**｜相對成長：**+1.62%**。

最近推送：2026-10-15T23:57:39Z；最新 release：v2.72.0（2026-10-01T22:42:08Z）；授權：MIT；open issues／PR 合計：48。近期樣本：2 個 issue、3 個 PR，最近更新 2026-10-17T15:27:58Z；本期參考 [#331](https://github.com/K-Dense-AI/scientific-agent-skills/pull/331)（open）。

- 用途：彙整科學研究工作流程 skills 與資料庫串接，README 宣稱支援開放 Agent Skills 標準與多種 agent。
- 判斷與風險：技能數量、使用者數與驗證程度是作者描述，本期未重現。專業分析與資料庫使用條件需由領域人員核對；近期數值擬合修補凸顯計算正確性不能由敘述取代。
- Adam 關聯：適合 Adam 參考大型技能庫如何分類、附來源與維護；辦公研究流程可借用資料整理模式，know metabiz wiki 記錄來源及適用限制，暫不列為直接導入項目。

## 明日觀察清單

- **XERJ × LLM Wiki**：以同一組公開文件比較檢索召回、來源引用與增量更新，追蹤 XERJ mapping 修補及 LLM Wiki 唯讀 Pi 介面的合併／發佈狀態。
- **ai-memory × Orca**：觀察跨 agent 交接與並行工作是否有可重現案例；確認驗證修補發佈版本、記憶隔離與 worktree 合併成本。
- **AI Job Search × CLI-Anything**：挑選一條文件流程做 demo，測繁體中文、資料欄位、重跑與輸出讀回；追蹤近期修補是否進入 release。
- **官方 plugins × Android skills × ECC**：追蹤安裝文件、範例品質與跨工具相容性，選一個小型 skill 做可驗收任務；科學技能庫暫作封裝參考。
- **動能檢查**：重新抓取 stars today 與快照 Δ，觀察高相對成長是否延續；新進專案累積至少第二次觀測後再評成長。保留低星數但有實際工作價值的候選。

## 查詢與來源

[GitHub Trending daily](https://github.com/trending?since=daily)；各專案連結、release metadata 與近期 issue／PR 證據如上。完整十組查詢：

- `mcp server ai`
- `model context protocol`
- `agent skills coding agent`
- `claude code template`
- `codex skills`
- `coding agent llm`
- `rag knowledge base`
- `ai wiki knowledge management`
- `llm orchestration agent`
- `developer automation ai`
