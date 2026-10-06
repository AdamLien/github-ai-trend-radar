# GitHub AI 趨勢雷達｜2026-10-06

本次精選 9 個專案。優先研究首次入榜的 REA、工程 Skills 與可持續維護的 wiki；圖解和設計工具適合近期內容示範。順序依動能、維護證據與 Adam／Metabiz 用途判斷，不是總 stars 排行。

## 資料時間與方法

- 目標日期為 Asia/Taipei 前一日 **2026-10-06**。實際完成時間（UTC）：2026-10-06T16:21:50.256647+00:00；GitHub Trending 與 API 是此次執行當下的觀測，並非 10 月 6 日歷史榜單重建。
- 來源：[GitHub Trending daily](https://github.com/trending?since=daily)、十組指定搜尋、repo API、README、release，以及候選最新五筆 issue／PR。原始證據保存在 `snapshots/`。
- 今日 stars 為 Trending 頁面數值；Δ stars 與 `2026-10-05` 資料夾快照比較，並非固定 24 小時。相對成長＝Δ÷上一快照 stars；兩種時間窗不能混用。
- 新入榜沒有前值時，collector 的 0 delta 不代表零成長，下表列「無基準」。未上 Trending 不代表今日新增零 stars。未結 issue 數包含 PR；近期五筆只作活動樣本，不代表全量健康度。
- 保留 341 個搜尋／Trending／歷史追蹤項目；Trending 人工複核保留 9 個。排除健身追蹤 openGym；另外兩個非範圍 Trending 原本就未收錄。
- 三個歷史 repo 回傳 404，metadata 沿用舊值並標示未驗證，delta 設為 null，不作推薦或成長排名。
- API rate limit：**未偵測到**；維持 `--limit 10`，未重試 `--limit 5`。README 功能仍待實際驗證。

## 精選動能比較

| 優先 | Repo | stars today | Δ stars | 相對成長 | 總 stars | 決策 |
|---|---|---:|---:|---:|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | 2,963 | 無基準 | 無基準 | 7,721 | Deep research |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 1,028 | +936 | 0.34% | 277,770 | Skill candidate |
| 3 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 609 | +596 | 0.78% | 77,499 | Demo content |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 227 | +381 | 0.88% | 43,784 | Skill candidate |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 536 | +516 | 0.53% | 96,983 | Watch |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 621 | +583 | 0.37% | 157,651 | Demo content |
| 7 | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 未上榜 | +2 | 0.06% | 3,602 | Deep research |
| 8 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未上榜 | +24 | 0.12% | 20,243 | Watch |
| 9 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 未上榜 | +36 | 0.04% | 91,730 | Reference only |

REA 的 stars today 約占目前總 stars 的 38.38%，只作熱度占比，不代替實測成長率。diagram-design 的相對成長高於幾個更大型專案；llm-wiki-agent 則因知識流程適配度而入選，與熱門度分開判斷。

## 個別判斷

### 1. [morluto/rea](https://github.com/morluto/rea)｜Deep research

**用途：**以 MCP 串接二進位、應用程式與執行行為的逆向分析；README 有 agent、CLI、Ghidra 分析提供者與可追溯調查證據。

**動能與維護：**今日 2,963 stars，首次入榜且總量只有 7,721。近期有 NativeAOT 支援、JavaScript 修正與 4.1.0 發布準備 PR。 最近推送：`2026-10-06T16:09:14Z`；最新 release：rea-agents-4.0.1（2026-10-05T18:54:59Z）；未結 issue／PR：70；API license：`MIT`。

**風險：**大型 Electron ASAR 存在零輸出／結果格式失敗（#746）；分析環境與依賴須先驗證。

**Adam／Metabiz 關聯：**Adam 可用自有樣本做「agent 如何以證據理解黑箱」課程；Metabiz 可研究舊系統整合，先做隔離示範。

證據：[README](https://github.com/morluto/rea/blob/HEAD/README.md)、[Releases](https://github.com/morluto/rea/releases)。
近期活動樣本：[PR #748](https://github.com/morluto/rea/pull/748)、[PR #635](https://github.com/morluto/rea/pull/635)、[PR #749](https://github.com/morluto/rea/pull/749)、[Issue #746](https://github.com/morluto/rea/issues/746)、[Issue #747](https://github.com/morluto/rea/issues/747)。

### 2. [mattpocock/skills](https://github.com/mattpocock/skills)｜Skill candidate

**用途：**將需求澄清、領域模型、TDD、模組設計與 code review 整理為 coding agent Skills。README 以需求落差、冗長輸出與不可用程式等問題組織方法。

**動能與維護：**今日 1,028 stars、快照增加 936；有版本更新 PR，也有規格矛盾與工具權限紀錄問題。 最近推送：`2026-10-06T13:41:41Z`；最新 release：v1.3.1（2026-10-04T12:48:18Z）；未結 issue／PR：419；API license：`MIT`。

**風險：**大量未結 issue／PR 不等於大量故障，但整套引入容易造成提示衝突、流程過重；宜逐一驗證。

**Adam／Metabiz 關聯：**Adam 可挑需求澄清、TDD、review 各做前後對照；作 Metabiz 工程 Skills 候選，將驗證心得整理到 wiki。

證據：[README](https://github.com/mattpocock/skills/blob/HEAD/README.md)、[Releases](https://github.com/mattpocock/skills/releases)。
近期活動樣本：[PR #1161](https://github.com/mattpocock/skills/pull/1161)、[Issue #124](https://github.com/mattpocock/skills/issues/124)、[Issue #1178](https://github.com/mattpocock/skills/issues/1178)、[Issue #1129](https://github.com/mattpocock/skills/issues/1129)、[Issue #966](https://github.com/mattpocock/skills/issues/966)。

### 3. [pbakaus/impeccable](https://github.com/pbakaus/impeccable)｜Demo content

**用途：**透過設計 Skill 與 critique、polish 等命令改善 AI UI，並支援可重用元件與設計 token。

**動能與維護：**今日 609 stars、快照增加 596；近期 PR 在漸層、透明背景與畫面描述上持續修補。 最近推送：`2026-10-06T15:37:13Z`；最新 release：skill-v4.5.0（2026-10-02T02:35:11Z）；未結 issue／PR：57；API license：`Apache-2.0`。

**風險：**效果仍受模型與品牌素材影響；主分支修正不代表已納入 skill-v4.5.0 正式 release。

**Adam／Metabiz 關聯：**適合 Adam 製作 AI 頁面改版前後比較；可改善 Metabiz 課程頁、客戶簡報與辦公 dashboard。

證據：[README](https://github.com/pbakaus/impeccable/blob/HEAD/README.md)、[Releases](https://github.com/pbakaus/impeccable/releases)。
近期活動樣本：[PR #928](https://github.com/pbakaus/impeccable/pull/928)、[PR #930](https://github.com/pbakaus/impeccable/pull/930)、[PR #961](https://github.com/pbakaus/impeccable/pull/961)、[PR #962](https://github.com/pbakaus/impeccable/pull/962)、[PR #806](https://github.com/pbakaus/impeccable/pull/806)。

### 4. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)｜Skill candidate

**用途：**以 agent Skill 產出獨立 HTML／SVG 圖解，並重繪 draw.io、Mermaid、Excalidraw 素材；README 提供品牌與版型流程。

**動能與維護：**今日 227 stars、快照增加 381，相對成長高於數個總 stars 更高的專案；近期修補幾何解析、結構限制與重複 ID。 最近推送：`2026-10-06T16:12:51Z`；最新 release：未取得正式最新 release；未結 issue／PR：27；API license：`MIT`。

**風險：**圖解事實仍需核對；輸入解析正在修補。README 的版本文字不能代替 GitHub 正式 release。

**Adam／Metabiz 關聯：**直接支援 Adam 課程圖解、短影音流程圖；know metabiz wiki 可試作架構與流程圖並保留可編輯來源。

證據：[README](https://github.com/cathrynlavery/diagram-design/blob/HEAD/README.md)、[Releases](https://github.com/cathrynlavery/diagram-design/releases)。
近期活動樣本：[PR #283](https://github.com/cathrynlavery/diagram-design/pull/283)、[PR #281](https://github.com/cathrynlavery/diagram-design/pull/281)、[PR #282](https://github.com/cathrynlavery/diagram-design/pull/282)、[PR #280](https://github.com/cathrynlavery/diagram-design/pull/280)、[PR #199](https://github.com/cathrynlavery/diagram-design/pull/199)。

### 5. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)｜Watch

**用途：**保存 agent 工作歷程、壓縮記憶並在後續 session 注入上下文；README 包含記憶生命週期與 MCP 搜尋工具。

**動能與維護：**今日 536 stars、快照增加 516；此次取得 v13.33.0 release，近期有 worker 工作回收與 observer 批次釋放修補。 最近推送：`2026-10-06T16:18:15Z`；最新 release：v13.33.0（2026-10-06T14:49:05Z）；未結 issue／PR：93；API license：`Apache-2.0`。

**風險：**issue #4559 回報 SQLite 狀態錯誤，#4558 關注 server 模式 worker 行為。歷程可能含客戶資料，需先驗證保留、隔離與刪除。

**Adam／Metabiz 關聯：**Adam 可做持久記憶與 wiki 的比較內容；Metabiz 跨日辦公任務有潛力，修補與資料邊界確認前列 Watch。

證據：[README](https://github.com/thedotmack/claude-mem/blob/HEAD/README.md)、[Releases](https://github.com/thedotmack/claude-mem/releases)。
近期活動樣本：[PR #4560](https://github.com/thedotmack/claude-mem/pull/4560)、[Issue #4559](https://github.com/thedotmack/claude-mem/issues/4559)、[PR #4557](https://github.com/thedotmack/claude-mem/pull/4557)、[Issue #4558](https://github.com/thedotmack/claude-mem/issues/4558)、[PR #4553](https://github.com/thedotmack/claude-mem/pull/4553)。

### 6. [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)｜Demo content

**用途：**提供工程、設計、行銷等角色化 agent 與多工具整合；README 有角色名冊和交接使用方式。

**動能與維護：**今日 621 stars、快照增加 583；近期有 Hermes 設定、runbook roster 與 eval 解析 PR。 最近推送：`2026-10-06T12:47:44Z`；最新 release：未取得正式最新 release；未結 issue／PR：184；API license：`MIT`。

**風險：**角色數量不證明協作效率；整套啟用容易重複工作。此次沒有正式最新 release，示範宜固定 commit。

**Adam／Metabiz 關聯：**Adam 可示範研究、撰稿、檢核三角色的辦公案例；Metabiz 可挑少數職能，將交付格式及評估結果寫入 wiki。

證據：[README](https://github.com/msitarzewski/agency-agents/blob/HEAD/README.md)、[Releases](https://github.com/msitarzewski/agency-agents/releases)。
近期活動樣本：[PR #1030](https://github.com/msitarzewski/agency-agents/pull/1030)、[PR #1056](https://github.com/msitarzewski/agency-agents/pull/1056)、[PR #1055](https://github.com/msitarzewski/agency-agents/pull/1055)、[PR #1054](https://github.com/msitarzewski/agency-agents/pull/1054)、[PR #1053](https://github.com/msitarzewski/agency-agents/pull/1053)。

### 7. [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)｜Deep research

**用途：**讓 coding agent 讀 raw 來源，增量整理來源、概念、實體頁，持續維護互相連結的 Markdown wiki。

**動能與維護：**未在此次 Trending；快照只增加 2 stars，但直接符合 know metabiz wiki。最新五筆 issue／PR 更新停在 9 月 24 日，不能用 pushed_at 代替議題處理活躍度。 最近推送：`2026-10-05T10:29:09Z`；最新 release：未取得正式最新 release；未結 issue／PR：11；API license：`MIT`。

**風險：**來源轉換可能覆寫同名 Markdown（#83／#84），也有絕對路徑問題（#80／#81）；先在複本測試來源引用與重複匯入。

**Adam／Metabiz 關聯：**優先研究 know metabiz wiki 的來源→摘要→概念→實體流程；Adam 可做「持續累積知識，不只即時問答」課程。

證據：[README](https://github.com/SamurAIGPT/llm-wiki-agent/blob/HEAD/README.md)、[Releases](https://github.com/SamurAIGPT/llm-wiki-agent/releases)。
近期活動樣本：[PR #84](https://github.com/SamurAIGPT/llm-wiki-agent/pull/84)、[Issue #83](https://github.com/SamurAIGPT/llm-wiki-agent/issues/83)、[PR #82](https://github.com/SamurAIGPT/llm-wiki-agent/pull/82)、[PR #81](https://github.com/SamurAIGPT/llm-wiki-agent/pull/81)、[Issue #80](https://github.com/SamurAIGPT/llm-wiki-agent/issues/80)。

### 8. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)｜Watch

**用途：**將文件匯入桌面應用並增量維護 wiki；README 描述來源追溯、知識圖譜、持久佇列與人工審閱。

**動能與維護：**未在此次 Trending；快照增加 24 stars。推送與 v0.6.12 release 停在 9 月 28 日，但近期仍有 UI／匯入 PR 和 issue。 最近推送：`2026-09-28T01:43:23Z`；最新 release：v0.6.12（2026-09-28T02:58:13Z）；未結 issue／PR：271；API license：`NOASSERTION`。

**風險：**issue #806 回報 PDF 解析偏差，#805 指出匯入輸出上限。API license 為 NOASSERTION，需核對 LICENSE，不能據此判定沒有授權。

**Adam／Metabiz 關聯：**可評估非工程同事建立 know metabiz wiki 的桌面流程；Adam 可比較 Markdown agent wiki 與桌面工具，先列 Watch。

證據：[README](https://github.com/nashsu/llm_wiki/blob/HEAD/README.md)、[Releases](https://github.com/nashsu/llm_wiki/releases)。
近期活動樣本：[PR #704](https://github.com/nashsu/llm_wiki/pull/704)、[PR #711](https://github.com/nashsu/llm_wiki/pull/711)、[Issue #806](https://github.com/nashsu/llm_wiki/issues/806)、[Issue #805](https://github.com/nashsu/llm_wiki/issues/805)、[PR #796](https://github.com/nashsu/llm_wiki/pull/796)。

### 9. [infiniflow/ragflow](https://github.com/infiniflow/ragflow)｜Reference only

**用途：**提供文件處理、附引用的檢索與 agent 工作流；README 描述企業 context engine、異質來源與 RAG 部署。

**動能與維護：**未在此次 Trending；快照增加 36 stars，相對成長很低。近期有 wiki graph 參數與 DNS rebinding 修補 PR；最新 release 是 v1.0.0-rc1。 最近推送：`2026-10-06T14:30:41Z`；最新 release：v1.0.0-rc1（2026-09-29T05:52:57Z）；未結 issue／PR：1,617；API license：`Apache-2.0`。

**風險：**版本仍是 RC，部署、升級、來源權限與檢索品質需一起評估。未結 issue／PR 數不等於故障數。

**Adam／Metabiz 關聯：**Adam 可作持久 wiki 與 RAG 的教學比較基準；Metabiz 多來源文件搜尋可參考其架構，今日不安排正式導入。

證據：[README](https://github.com/infiniflow/ragflow/blob/HEAD/README.md)、[Releases](https://github.com/infiniflow/ragflow/releases)。
近期活動樣本：[PR #20408](https://github.com/infiniflow/ragflow/pull/20408)、[PR #20483](https://github.com/infiniflow/ragflow/pull/20483)、[PR #20538](https://github.com/infiniflow/ragflow/pull/20538)、[PR #20550](https://github.com/infiniflow/ragflow/pull/20550)、[PR #20569](https://github.com/infiniflow/ragflow/pull/20569)。

## 明日追蹤清單（下一次目標：2026-10-07）

1. **REA**：建立第一個可比較的 stars 快照；追蹤 4.1.0 正式 release 與 #746，拿自有樣本驗證調查證據可重現性。
2. **工程 Skills／diagram-design**：查看版本與解析修補是否合併，選一個需求→測試案例及一張課程圖解，記錄人工修改量與正確性。
3. **claude-mem**：追蹤 #4559／#4558 與新 release，先以無客戶資料的環境驗證跨 session 記憶及刪除。
4. **llm-wiki-agent**：追蹤 #83／#84 與 #80／#81；以 know metabiz wiki 複本測試同名匯入、來源引用、繁中內容與衝突處理。
5. **llm_wiki**：追蹤 PDF 解析 #806、token 上限 #805，核對 LICENSE，再判斷是否適合非工程同事試用。
6. **impeccable／agency-agents**：各做一個有評估標準的示範，前者看品牌與可讀性，後者看交付正確率、重複工作及成本。
7. **RAGFlow**：觀察 RC 後續與檢索／網路修補；若沒有新用途或成長訊號，繼續作參考。

## 收集狀態

十組查詢均使用 `--limit 10 --include-trending-daily --include-readme`。未偵測到 rate-limit 錯誤。404 沿用項目：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。既有未提交的 collector 程式碼變更維持原狀。
