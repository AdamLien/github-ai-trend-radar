# GitHub AI 趨勢雷達｜2026-11-09

目標日期：**2026-11-09（Asia/Taipei 前一日）**。本次觀測完成：2026-11-10T00:22:48.859158+08:00。

本次精選 9 個專案。Astryx 的設計系統與 OpenMausBot、agent-browser 適合示範；Auto Ontology、GBrain 與 LLM Wiki 對應 know metabiz wiki 的語意、記憶與來源管理。Skills 則優先考慮可驗收性與跨 agent 可用性。以下為編輯優先順序，不是總星數排行榜。

## 觀測口徑與資料完整性

- 已以指定十組查詢、--limit 10、--include-trending-daily、--include-readme 從專案根目錄執行收集器，原始 425 筆；清理 7 筆過期 metadata、11 筆轉址重複及 16 筆範圍外工具後保留 391 個專案。細節見 collection-audit.json。
- [GitHub Trending daily](https://github.com/trending?since=daily) 共解析 11 張卡片，人工保留 8 個；排除原因與原始頁面見 trending-daily.json、trending-daily.html。補上簡單關鍵字可能漏判的 OpenMausBot 來源標記。
- 今日星數是 Trending 當次頁面的滾動窗口值；快照增量是本次總星數減去 2026-11-08 快照；相對成長是增量／前次總星數。未上榜標「—」，不等於零；首次觀測無前日基準，不把零增量解讀成沒有成長。
- 本次即時觀測歸檔至前一個台北日曆日，並非還原昨日午夜或精確 24 小時資料。搜尋結果按總 stars 取得，存在大型專案偏差；精選另比較今日星數、增量、相對成長、push、README、release 與近期 issue／PR 樣本。
- API rate limit：**未觀察到 API rate-limit 錯誤；以 --limit 10 完成，未啟動 --limit 5 重試。**
- 9 個精選的完整 README、metadata、最近 3 筆 release、最近更新的 8 筆 issue／PR 已存於 readmes/ 與 editorial-evidence.json。總 stars 統一採 repos.json；補查時間可能略有不同。open_issues_count 包含 PR；樣本活動不等於所有 issue 的活躍度。
- 用途來自第一方 README；課程、內容與導入建議為本次分析判斷。候選工具未安裝、未執行；issue 回報未重現，PR 尚未合併時不宣稱問題已修復。

## 精選與動能

| 專案 | 總 stars | 今日星數 | 快照增量 | 相對成長 | 建議 |
| --- | ---: | ---: | ---: | ---: | --- |
| [meta/astryx](https://github.com/meta/astryx) | 19,009 | 3,324 | +3,342 | +21.33% | **Demo content** |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 19,402 | 1,589 | +1,493 | +8.34% | **Demo content** |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 48,254 | 914 | +883 | +1.86% | **Demo content** |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | 10,890 | — | +797 | +7.90% | **Deep research** |
| [garrytan/gbrain](https://github.com/garrytan/gbrain) | 31,973 | 215 | 無基準 | 無基準 | **Watch** |
| [anthropics/skills](https://github.com/anthropics/skills) | 190,476 | 1,052 | +1,169 | +0.62% | **Skill candidate** |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 319,377 | — | +1,092 | +0.34% | **Skill candidate** |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 21,528 | — | +34 | +0.16% | **Deep research** |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | 19,838 | 560 | +575 | +2.98% | **Reference only** |

## 逐項判斷與應用

### 1. meta/astryx — Demo content

**用途：** 為人與 coding agent 協作設計的 React／StyleX 元件、主題與設計系統。

**動能與維護：** 總 stars 19,009；今日星數 3,324；相較前次快照 +3,342、+21.33%。最近 push（UTC）：2026-11-09T16:17:56Z；release：v0.7.11／2026-11-07T15:00:47Z。未關閉項目（含 PR）627；最近更新的 8 筆樣本中，0 個 issue、8 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** Adam 可示範以同一份設計規格產出 AI 辦公室後台；metabiz 可評估 CRM 與 wiki 介面一致性。

**風險：** README 標示 Beta，依賴 React 19+ 與 StyleX；元件可用性與升級成本須實測，不能因高熱度直接遷移。

**下一步：** 用表格、表單、側欄各做一個案例，驗證鍵盤操作及繁中排版。

來源：[專案與 README](https://github.com/meta/astryx)、[release 紀錄](https://github.com/meta/astryx/releases)、[具體 issue／PR](https://github.com/meta/astryx/pull/10821)。

### 2. milind-soni/OpenMausBot — Demo content

**用途：** 聊天式多 bot 工作台；README 描述 Claude／Codex agent 各自使用電腦與連接應用。

**動能與維護：** 總 stars 19,402；今日星數 1,589；相較前次快照 +1,493、+8.34%。最近 push（UTC）：2026-11-09T16:12:52Z；release：v0.1.150／2026-11-09T03:26:23Z。未關閉項目（含 PR）918；最近更新的 8 筆樣本中，0 個 issue、8 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** 適合 Adam 的 AI 辦公室多代理分工內容，示範研究、整理及報告交接；metabiz 先以匿名 wiki 資料測試。

**風險：** 快速版本更新與電腦、連接器權限提高維護面；近期討論涉及大型 workspace 遷移與跨電腦交接，不能預設長任務穩定完成。

**下一步：** 跑兩個 agent 交接任務，記錄權限、等待、取消與結果驗證。

來源：[專案與 README](https://github.com/milind-soni/OpenMausBot)、[release 紀錄](https://github.com/milind-soni/OpenMausBot/releases)、[具體 issue／PR](https://github.com/milind-soni/OpenMausBot/pull/5102)。

### 3. vercel-labs/agent-browser — Demo content

**用途：** 以 CLI 讀取瀏覽器無障礙樹並操作元素，適合可重複的網站自動化。

**動能與維護：** 總 stars 48,254；今日星數 914；相較前次快照 +883、+1.86%。最近 push（UTC）：2026-11-09T14:24:19Z；release：v0.41.2／2026-11-03T23:46:27Z。未關閉項目（含 PR）536；最近更新的 8 筆樣本中，2 個 issue、6 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** Adam 可製作查詢、填表、驗證結果的辦公自動化教案；metabiz 可用測試後台檢驗流程可靠性。

**風險：** issue #1612 回報 action policy 與文件分類不符；#2505 回報 file access 旗標影響後續頁面。需驗證允許清單，不能把工具回傳成功當工作完成。

**下一步：** 以測試頁驗證 action policy、檔案頁與頁面重載後元素定位。

來源：[專案與 README](https://github.com/vercel-labs/agent-browser)、[release 紀錄](https://github.com/vercel-labs/agent-browser/releases)、[具體 issue／PR](https://github.com/vercel-labs/agent-browser/issues/1612)。

### 4. NVIDIA/auto-ontology — Deep research

**用途：** 從企業 metadata 建立語意與知識圖譜脈絡層，透過 MCP、CLI、API 提供資料定義、關係與來源。

**動能與維護：** 總 stars 10,890；今日星數 —；相較前次快照 +797、+7.90%。最近 push（UTC）：2026-11-07T21:54:29Z；release：本次未取得 release；不代表沒有其他發行方式。未關閉項目（含 PR）94；最近更新的 8 筆樣本中，5 個 issue、3 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** 直接對應 know metabiz wiki 的業務名詞與跨系統欄位定義；Adam 可比較一般 RAG 與具語意定義的查詢。

**風險：** issue #472 回報非 ASCII 同義詞搜尋無法匹配，對繁中尤其相關；README 表示目前不接受外部貢獻，修復仍依賴維護者。

**下一步：** 用繁中、英文同義詞及跨 schema 關係建立小型匿名測試集。

來源：[專案與 README](https://github.com/NVIDIA/auto-ontology)、[release 紀錄](https://github.com/NVIDIA/auto-ontology/releases)、[具體 issue／PR](https://github.com/NVIDIA/auto-ontology/issues/472)。

### 5. garrytan/gbrain — Watch

**用途：** 為既有 agent 提供可控記憶，保存明確事實、來源、修正與撤回，支援跨 agent 共用。

**動能與維護：** 總 stars 31,973；今日星數 215；相較前次快照 無基準、無基準。最近 push（UTC）：2026-11-09T16:15:51Z；release：v0.60.623.0／2026-11-09T14:34:14Z。未關閉項目（含 PR）777；最近更新的 8 筆樣本中，3 個 issue、5 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** 可作為 know metabiz wiki 的來源記憶與撤回機制參考；Adam 可示範同一知識在不同 agent 間如何維持一致。

**風險：** 本日首次納入、沒有前日基準；release 頻繁不等於成熟。近期 file-drift 修復 PR 尚未合併，需測試同步、撤回與個人內容界線。

**下一步：** 測試一筆事實新增、修正、撤回後，兩個 agent 的檢索結果。

來源：[專案與 README](https://github.com/garrytan/gbrain)、[release 紀錄](https://github.com/garrytan/gbrain/releases)、[具體 issue／PR](https://github.com/garrytan/gbrain/pull/9009)。

### 6. anthropics/skills — Skill candidate

**用途：** 提供可動態載入指令、腳本與資源的 skills 範例，涵蓋文件、設計、開發與企業流程。

**動能與維護：** 總 stars 190,476；今日星數 1,052；相較前次快照 +1,169、+0.62%。最近 push（UTC）：2026-11-06T22:32:32Z；release：本次未取得 release；不代表沒有其他發行方式。未關閉項目（含 PR）1,504；最近更新的 8 筆樣本中，2 個 issue、6 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** Adam 可用來教可重複工作法與驗收；metabiz 可挑選文件輸出流程，再補公司範本與人工檢查。

**風險：** 各目錄授權不同，須逐項查閱；#2167 回報 PDF 轉圖保留全部頁面造成記憶體問題，相關 PR 不等於已修復。

**下一步：** 選一個文件 skill 用長 PDF 測試記憶體、版面與輸出驗收。

來源：[專案與 README](https://github.com/anthropics/skills)、[release 紀錄](https://github.com/anthropics/skills/releases)、[具體 issue／PR](https://github.com/anthropics/skills/issues/2167)。

### 7. mattpocock/skills — Skill candidate

**用途：** 將需求釐清、工程設計與開發方法拆成小型、可組合的 agent skills。

**動能與維護：** 總 stars 319,377；今日星數 —；相較前次快照 +1,092、+0.34%。最近 push（UTC）：2026-11-09T14:03:07Z；release：v1.3.2／2026-10-29T10:27:41Z。未關閉項目（含 PR）227；最近更新的 8 筆樣本中，8 個 issue、0 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** 適合 Adam 的 coding-agent 課程設計與內容案例；metabiz 可用於需求拆解、驗收與 wiki 術語整理。

**風險：** #1123 涉及 harness 專用 Skill tool 依賴；#1405 回報實作需多次提示才繼續。先驗證現用 agent 的工具與持續執行行為。

**下一步：** 比較需求到實作的一輪完成率，確認輸出可追溯到驗收條件。

來源：[專案與 README](https://github.com/mattpocock/skills)、[release 紀錄](https://github.com/mattpocock/skills/releases)、[具體 issue／PR](https://github.com/mattpocock/skills/issues/1405)。

### 8. nashsu/llm_wiki — Deep research

**用途：** 將多格式來源增量整理成互連 wiki，包含來源追溯、來源限定檢索與知識圖譜。

**動能與維護：** 總 stars 21,528；今日星數 —；相較前次快照 +34、+0.16%。最近 push（UTC）：2026-10-21T11:17:29Z；release：v0.6.13／2026-10-22T01:21:07Z。未關閉項目（含 PR）300；最近更新的 8 筆樣本中，4 個 issue、4 個 PR，其中 3 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** 與 know metabiz wiki 最直接相關；Adam 可用同一組文件比較臨時 RAG 回答與持久 wiki 的更新、查證成本。

**風險：** 近期 push 較慢且授權 API 回傳 NOASSERTION；#806 回報 PDF 內容解析偏差，#848 回報頁面操作未真正寫回，須實測來源與持久化。

**下一步：** 用繁中 PDF、含表格文件與來源刪改測試引用正確率及 wiki 更新。

來源：[專案與 README](https://github.com/nashsu/llm_wiki)、[release 紀錄](https://github.com/nashsu/llm_wiki/releases)、[具體 issue／PR](https://github.com/nashsu/llm_wiki/issues/806)。

### 9. anthropics/claude-quickstarts — Reference only

**用途：** 提供客服知識庫、資料分析、computer use 與瀏覽器操作等 Claude 應用起始範例。

**動能與維護：** 總 stars 19,838；今日星數 560；相較前次快照 +575、+2.98%。最近 push（UTC）：2026-11-06T19:37:57Z；release：本次未取得 release；不代表沒有其他發行方式。未關閉項目（含 PR）238；最近更新的 8 筆樣本中，6 個 issue、2 個 PR，其中 8 筆於觀測前 48 小時內更新。

**Adam／metabiz 關聯：** 可為 Adam 的教學與 AI 辦公自動化 demo 提供結構參考，metabiz 可借鏡客服連接知識庫的流程。

**風險：** #519 回報 read_page 暴露密碼欄位值，#545 是尚未合併的遮罩 PR；範例仍需權限、依賴與輸出遮罩設計後才適合實際資料。

**下一步：** 追蹤密碼遮罩與安裝版本固定的修復狀態，先用合成資料示範。

來源：[專案與 README](https://github.com/anthropics/claude-quickstarts)、[release 紀錄](https://github.com/anthropics/claude-quickstarts/releases)、[具體 issue／PR](https://github.com/anthropics/claude-quickstarts/issues/519)。

## 明日觀察清單

- **Astryx：** 今日星數 3,324 的熱度能否延續；v0.7.12 的發布準備是否成為正式 release，鍵盤與繁中排版測試是否通過。
- **OpenMausBot／agent-browser：** 相對成長與今日星數是否同步持續；大型 workspace、交接及 action policy 的問題是否有合併修復與實測。
- **Auto Ontology：** 非 ASCII 同義詞 #472 是否修復；用繁中業務詞彙和來源追溯作為 know metabiz wiki 進入實驗的門檻。
- **GBrain：** 建立下一次 star delta 基準，驗證記憶修正、撤回與同步；發布頻率之外也看回歸狀況。
- **anthropics/skills／mattpocock/skills：** 長 PDF 記憶體、跨 harness 依賴與實作持續性回報是否改善，再決定吸收哪些 skill 方法。
- **LLM Wiki／Claude Quickstarts：** 追蹤 PDF 來源偏差、寫回持久化與密碼欄位遮罩修復；以合成資料驗證後才規劃企業示範。
