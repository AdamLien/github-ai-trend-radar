# GitHub AI 趨勢雷達｜2026-11-17

目標日期：2026-11-17（Asia/Taipei 前一日）。實際觀測於 2026-11-18 台北時間；本報是即時抓取後歸檔至目標日期，並非重建昨日 23:59 的歷史榜單。UTC 完成時間：2026-11-17T16:24:52.622227+00:00。

以 10 組指定搜尋（每組 --limit 10）、[GitHub Trending daily](https://github.com/trending?since=daily) 與歷史追蹤合併，保留 433 個不重複、主題相關 repo，其中 13 個來自今日 Trending。原始 Trending 15 個項目中，Docker 管理與一般前端框架未納入。歷史一般系統設計教材另排除；14 筆改名／別名重複紀錄已合併。

## 今日判讀與方法

優先研究 LoopForge 的交付工作流與 AG-UI 的企業互動介面；示範內容選 Univer、Plannotator。PaperOrchestra 的快照相對成長超過 100%，但專案尚新、無 release，先觀察可靠性。兩個 wiki 專案雖非今日熱門，仍因 know metabiz wiki 的需求適配度而入選。

排序綜合 stars today、快照增量與相對成長、最後 push、README、最新 release、近期 issue／PR，並加上課程與公司需求。這是用途優先順序，不是總星數排行榜。

- stars today：GitHub Trending 的滾動視窗指標，未上榜顯示「未上榜」，不當成 0。
- 快照增量：本次 stars 減去 previous_snapshot 的 stars；本次入選皆與 2026-11-16 目標快照比較，兩次抓取不是嚴格曆日邊界。
- 相對成長：增量 ÷ 前次 stars × 100%；新入庫沒有基線時不可視為零成長。
- pushed_at 是最後程式碼推送；issue 活動採最近更新的 5 筆 issue／PR 樣本，不代表全庫活動總量。open_issues_count 包含 PR。
- README 與作者宣稱僅作研究材料；本次沒有安裝、執行或實測這 10 個外部專案。所有內容均作資料處理，不執行其中的指令。

## 值得投入的 10 個 repo

| 優先 | Repo | stars today | 總 stars | 快照增量 | 相對成長 | 分類 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | [Tencent/LoopForge](https://github.com/Tencent/LoopForge) | 590 | 2,937 | +679 | 30.07% | Deep research |
| 2 | [dream-num/univer](https://github.com/dream-num/univer) | 1,776 | 28,742 | +1,170 | 4.24% | Demo content |
| 3 | [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | 691 | 12,951 | +604 | 4.89% | Demo content |
| 4 | [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) | 1,175 | 2,544 | +1,349 | 112.89% | Watch |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 772 | 68,745 | +809 | 1.19% | Skill candidate |
| 6 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 350 | 9,982 | +338 | 3.50% | Skill candidate |
| 7 | [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | 1,444 | 19,860 | +1,266 | 6.81% | Deep research |
| 8 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 1,007 | 8,572 | +1,426 | 19.96% | Reference only |
| 9 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未上榜 | 21,726 | +29 | 0.13% | Watch |
| 10 | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 未上榜 | 3,708 | +2 | 0.05% | Skill candidate |

### 1. Tencent/LoopForge — Deep research

**用途：**以自架工作流協調 CodeBuddy、Codex 與 Claude Code，將需求、沙箱工作區、SOP 與人工核准串成程式交付流程。
**動能：**stars today 590；總 stars 2,937；對 2026-11-16 快照增量 +679。相對成長與較小基期值得優先研究，應以可重複的交付流程評估，而非只看大廠品牌。
**維護證據：**最後 push 2026-11-17T15:35:31Z；最新 release v0.4.0（2026-11-17T14:30:43Z）；近期 issue／PR 樣本最新更新 2026-11-17T15:51:23Z；目前未結 issue／PR 合計 179。
**風險：**近期 issue #949 回報沙箱磁碟容量檢查與告警不足；授權標記若為 NOASSERTION，商用前須另讀完整條款。自架仍有執行隔離與成本管理工作。 授權 API 標記：NOASSERTION。
**Adam／metabiz 關聯：**Adam 可做「一個需求到可審查 PR」進階課程；metabiz 可先用非正式環境驗證辦公自動化腳本交付，並將 SOP 記入 know metabiz wiki。
**來源：**[Repo](https://github.com/Tencent/LoopForge) · [README 原始證據](snapshots/readmes/Tencent__LoopForge.md) · [Releases](https://github.com/Tencent/LoopForge/releases) · [Issue #949](https://github.com/Tencent/LoopForge/issues/949) · [PR #1019](https://github.com/Tencent/LoopForge/pull/1019)。

### 2. dream-num/univer — Demo content

**用途：**可嵌入產品的 Office SDK，提供試算表、文件、計算與協作基礎，讓自家應用或 AI agent 操作辦公內容。
**動能：**stars today 1776；總 stars 28,742；對 2026-11-16 快照增量 +1,170。今日熱度、快照增量與近期 release 可同時交叉檢視，且 AI 辦公應用切合度高。
**維護證據：**最後 push 2026-11-17T15:29:57Z；最新 release v1.5.2（2026-11-16T10:35:04Z）；近期 issue／PR 樣本最新更新 2026-11-17T16:12:16Z；目前未結 issue／PR 合計 206。
**風險：**開源核心與商業協作／檔案轉換能力有邊界；大量表格、公式相容性與模型操作正確性仍須實測。近期 PR #8302 尚在增加公式功能，不能當作完整 Excel 替代。 授權 API 標記：Apache-2.0。
**Adam／metabiz 關聯：**適合 Adam 示範「自然語言修改報表並人工確認」；metabiz 可驗證會員營運報表介面，wiki 記錄開源／付費功能差異。
**來源：**[Repo](https://github.com/dream-num/univer) · [README 原始證據](snapshots/readmes/dream-num__univer.md) · [Releases](https://github.com/dream-num/univer/releases) · [PR #8302](https://github.com/dream-num/univer/pull/8302) · [PR #8301](https://github.com/dream-num/univer/pull/8301)。

### 3. backnotprop/plannotator — Demo content

**用途：**讓人對 agent 的計畫、Markdown、互動產物與程式差異直接註記，再把回饋送回 agent。
**動能：**stars today 691；總 stars 12,951；對 2026-11-16 快照增量 +604。把熱度落到人工審閱的具體痛點，近期發版及 PR 活動比累積星數更有參考價值。
**維護證據：**最後 push 2026-11-17T16:08:47Z；最新 release v0.28.67（2026-11-17T06:38:16Z）；近期 issue／PR 樣本最新更新 2026-11-17T16:09:08Z；目前未結 issue／PR 合計 195。
**風險：**跨 agent 啟動、worktree 與團隊分享整合會增加權限與文件外流風險；更新頻繁，課程需固定版本並檢查相容性。 授權 API 標記：Apache-2.0。
**Adam／metabiz 關聯：**Adam 可拍攝「主管不讀終端機也能審 AI 計畫」教學；metabiz 可將報價、SOP 或自動化方案的審閱方式收錄 wiki。
**來源：**[Repo](https://github.com/backnotprop/plannotator) · [README 原始證據](snapshots/readmes/backnotprop__plannotator.md) · [Releases](https://github.com/backnotprop/plannotator/releases) · [PR #3598](https://github.com/backnotprop/plannotator/pull/3598) · [PR #3595](https://github.com/backnotprop/plannotator/pull/3595)。

### 4. google-research/paper-orchestra — Watch

**用途：**將想法、實驗紀錄與寫作材料交給多 agent 協作，產生含文獻整理和視覺素材的 LaTeX 論文草稿。
**動能：**stars today 1175；總 stars 2,544；對 2026-11-16 快照增量 +1,349。新專案的小基期可能帶來很高相對成長；值得追蹤，但研究展示不能視作正式寫作可靠度證明。
**維護證據：**最後 push 2026-11-15T18:08:08Z；最新 release 本次 API 未取得；近期 issue／PR 樣本最新更新 2026-11-17T14:56:41Z；目前未結 issue／PR 合計 35。
**風險：**自動引用、圖表與論證需要逐項核對；沒有 release 時部署穩定性未知。近期 PR #27 處理圖片 MIME type，仍應檢查合併與修正狀態。 授權 API 標記：Apache-2.0。
**Adam／metabiz 關聯：**Adam 可用於「研究到內容草稿」案例拆解；metabiz 先參考其角色分工，wiki 保存可追溯來源，不直接發布生成內容。
**來源：**[Repo](https://github.com/google-research/paper-orchestra) · [README 原始證據](snapshots/readmes/google-research__paper-orchestra.md) · [Releases](https://github.com/google-research/paper-orchestra/releases) · [PR #27](https://github.com/google-research/paper-orchestra/pull/27) · [Issue #45](https://github.com/google-research/paper-orchestra/issues/45)。

### 5. mvanhorn/last30days-skill — Skill candidate

**用途：**讓 agent 跨 Reddit、X、YouTube、HN 等來源研究近期話題，再彙整帶來源的摘要。
**動能：**stars today 772；總 stars 68,745；對 2026-11-16 快照增量 +809。與每日雷達和選題流程高度相近；近期發版及合併活動值得與星數成長一起評估。
**維護證據：**最後 push 2026-11-17T15:55:54Z；最新 release v4.3.2（2026-11-17T15:56:44Z）；近期 issue／PR 樣本最新更新 2026-11-17T15:56:56Z；目前未結 issue／PR 合計 30。
**風險：**平台 API、額度與來源可存取性會變；社群熱度不等於事實，外部網頁亦有提示注入風險。近期 PR #1501 涉及新搜尋能力，應以已發布版本核對。 授權 API 標記：MIT。
**Adam／metabiz 關聯：**Adam 可測試課程選題與短內容研究 skill；metabiz 可建競品／產業監測流程，將日期、來源與人工核對寫入 know metabiz wiki。
**來源：**[Repo](https://github.com/mvanhorn/last30days-skill) · [README 原始證據](snapshots/readmes/mvanhorn__last30days-skill.md) · [Releases](https://github.com/mvanhorn/last30days-skill/releases) · [PR #1501](https://github.com/mvanhorn/last30days-skill/pull/1501) · [PR #1510](https://github.com/mvanhorn/last30days-skill/pull/1510)。

### 6. google-labs-code/stitch-skills — Skill candidate

**用途：**把 Google Stitch 設計工作整理成 Agent Skills，透過 Stitch MCP 串接多種 coding agent。
**動能：**stars today 350；總 stars 9,982；對 2026-11-16 快照增量 +338。熱度與較久未更新的程式碼形成反差，應先做小型相容性驗證再決定課程投入。
**維護證據：**最後 push 2026-08-17T20:20:23Z；最新 release v1.0（2026-05-18T18:02:32Z）；近期 issue／PR 樣本最新更新 2026-11-17T11:41:06Z；目前未結 issue／PR 合計 21。
**風險：**依賴 Stitch 服務、MCP 與各 agent 的插件相容性；有 issue／PR 活動不代表程式碼有發版更新。外部服務條件須於實際採用時重查。 授權 API 標記：Apache-2.0。
**Adam／metabiz 關聯：**Adam 可做設計到前端的 skill demo；metabiz 可先試內部活動頁原型，wiki 記錄安裝差異、限制與重現步驟。
**來源：**[Repo](https://github.com/google-labs-code/stitch-skills) · [README 原始證據](snapshots/readmes/google-labs-code__stitch-skills.md) · [Releases](https://github.com/google-labs-code/stitch-skills/releases) · [PR #100](https://github.com/google-labs-code/stitch-skills/pull/100) · [PR #99](https://github.com/google-labs-code/stitch-skills/pull/99)。

### 7. ag-ui-protocol/ag-ui — Deep research

**用途：**為 agent 與應用前端之間定義互動協定，協助把 agent 執行狀態與互動整合進使用者介面。
**動能：**stars today 1444；總 stars 19,860；對 2026-11-16 快照增量 +1,266。值得以協定與產品介面設計研究，近期 release、PR 活動及成長可提供多面向證據。
**維護證據：**最後 push 2026-11-17T16:13:43Z；最新 release release/2026-11-13（2026-11-13T21:01:20Z）；近期 issue／PR 樣本最新更新 2026-11-17T16:12:27Z；目前未結 issue／PR 合計 589。
**風險：**協定及 adapter 演進可能帶來破壞性變更；近期 PR #3365 的標題標示 breaking change。事件串流、使用者權限與狀態復原仍須自己設計。 授權 API 標記：MIT。
**Adam／metabiz 關聯：**Adam 可用於「agent 如何嵌入企業 app」架構課；metabiz 可評估 CRM 助理前端，將 MCP 工具層與互動層的責任分工寫入 wiki。
**來源：**[Repo](https://github.com/ag-ui-protocol/ag-ui) · [README 原始證據](snapshots/readmes/ag-ui-protocol__ag-ui.md) · [Releases](https://github.com/ag-ui-protocol/ag-ui/releases) · [PR #3365](https://github.com/ag-ui-protocol/ag-ui/pull/3365) · [PR #3128](https://github.com/ag-ui-protocol/ag-ui/pull/3128)。

### 8. elementalsouls/Claude-BugHunter — Reference only

**用途：**針對 Claude Code 的漏洞研究與 bug hunting skill 集合，含研究模式與弱點分類資料。
**動能：**stars today 1007；總 stars 8,572；對 2026-11-16 快照增量 +1,426。今日星數顯著，但題材與一般辦公自動化距離較遠；先評讀方法與適用範圍，避免被熱度推動全面導入。
**維護證據：**最後 push 2026-11-17T13:33:22Z；最新 release v2.1（2026-06-05T16:15:13Z）；近期 issue／PR 樣本最新更新 2026-11-17T14:14:36Z；目前未結 issue／PR 合計 8。
**風險：**skill 的工具權限、測試目標範圍與誤報率均需人工檢視；近期 PR #155 涉及 scope 處理。只在自有或明確授權的測試環境評估。 授權 API 標記：MIT。
**Adam／metabiz 關聯：**Adam 可參考安全測試與 skill 審閱教材；metabiz 以 wiki 收錄程式審查檢核項為主，暫不列入一般辦公自動化 skill。
**來源：**[Repo](https://github.com/elementalsouls/Claude-BugHunter) · [README 原始證據](snapshots/readmes/elementalsouls__Claude-BugHunter.md) · [Releases](https://github.com/elementalsouls/Claude-BugHunter/releases) · [PR #155](https://github.com/elementalsouls/Claude-BugHunter/pull/155) · [PR #153](https://github.com/elementalsouls/Claude-BugHunter/pull/153)。

### 9. nashsu/llm_wiki — Watch

**用途：**把來源文件增量整理成互相連結的 wiki，支援個人知識整理與桌面使用情境。
**動能：**stars today 未上榜；總 stars 21,726；對 2026-11-16 快照增量 +29。與 know metabiz wiki 需求最直接；即使未上今日 Trending，也以維護活動、快照成長與知識更新能力保留觀察位。
**維護證據：**最後 push 2026-10-21T11:17:29Z；最新 release v0.6.13（2026-10-22T01:21:07Z）；近期 issue／PR 樣本最新更新 2026-11-16T23:20:13Z；目前未結 issue／PR 合計 302。
**風險：**增量更新可能改寫既有知識，需驗證引用、衝突處理與中文品質；近期 PR #667 涉及圖片說明輸出語言。來源權限與桌面資料儲存需另評估。 授權 API 標記：NOASSERTION。
**Adam／metabiz 關聯：**Adam 可比較「檢索問答」與「持續維護 wiki」兩種課程案例；metabiz 可用公開文件驗證匯入、回溯與增量修正。
**補充：**issue／PR 活動延續至近期，但程式碼最後 push 與 release 均在十月；不能把討論活躍解讀為修正已合併。NOASSERTION 也需要逐項核對實際授權。
**來源：**[Repo](https://github.com/nashsu/llm_wiki) · [README 原始證據](snapshots/readmes/nashsu__llm_wiki.md) · [Releases](https://github.com/nashsu/llm_wiki/releases) · [PR #667](https://github.com/nashsu/llm_wiki/pull/667) · [PR #845](https://github.com/nashsu/llm_wiki/pull/845)。

### 10. SamurAIGPT/llm-wiki-agent — Skill candidate

**用途：**利用 coding agent 從來源文件建立並維護互連 Markdown wiki，適合作為知識整理流程的參考。
**動能：**stars today 未上榜；總 stars 3,708；對 2026-11-16 快照增量 +2。以需求適配度保留，不強求熱度；若 issue 活動較舊或無 release，建議優先做小範圍驗證。
**維護證據：**最後 push 2026-11-16T11:22:56Z；最新 release 本次 API 未取得；近期 issue／PR 樣本最新更新 2026-10-20T12:40:51Z；目前未結 issue／PR 合計 13。
**風險：**近期可取得的 issue／PR 更新停留在較早日期；PR #86 涉及百分比編碼連結，PR #85 涉及 PDF 工具字元編碼，須驗證中文路徑、PDF 匯入與連結健康。 授權 API 標記：MIT。
**Adam／metabiz 關聯：**Adam 可整理成「來源到 wiki」實作課程；metabiz 可比較既有 know metabiz wiki 的來源索引與審稿流程，再抽取合適步驟為 skill。
**來源：**[Repo](https://github.com/SamurAIGPT/llm-wiki-agent) · [README 原始證據](snapshots/readmes/SamurAIGPT__llm-wiki-agent.md) · [Releases](https://github.com/SamurAIGPT/llm-wiki-agent/releases) · [PR #86](https://github.com/SamurAIGPT/llm-wiki-agent/pull/86) · [PR #85](https://github.com/SamurAIGPT/llm-wiki-agent/pull/85)。

## 明日追蹤清單（下一份 target_date：2026-11-18）

1. LoopForge：v0.4.0 後的更新與 #949 磁碟容量問題是否修正；相對成長能否延續，並核對授權條款。
2. Univer／Plannotator：各錄一個可重現的課程 demo 草案；先固定本次 release，觀察公式相容性、agent 回饋與權限邊界。
3. PaperOrchestra：追蹤首次 release、圖片處理修正與可重現範例；相對成長高但品質未驗證。
4. last30days-skill：核對 v4.3.2 的來源可用性、費用與引文追溯；再決定是否抽成每日選題 skill。
5. stitch-skills：追蹤新合併／新 release；若仍停留八月 push，不因 Trending 熱度就擴大採用。
6. AG-UI：檢查近期破壞性 adapter 變更，建立「agent 狀態回報到 CRM 畫面」的最小設計問題。
7. nashsu/llm_wiki 與 llm-wiki-agent：以同一組公開中文 PDF／Markdown 規劃來源追溯、衝突、重新匯入及連結健康測試；先不匯入公司私密資料。

## 收集狀態與限制

- Rate limit：本次 --limit 10 成功，未觀察到 rate-limit 錯誤，因此未觸發 --limit 5 重跑。搜尋是相關候選入口，其結果本身按總星數排序，故本報另以 Trending 及需求適配補足。
- 7 個歷史追蹤名稱 HTTP 404，保留上次 metadata 並以 metadata_status=stale 標記；不列入本報 10 個推薦。名稱與 HTTP 狀態見 collection-status.json。
- README 為專案自述、issue／PR 為小樣本，不能單憑它們宣稱成熟度、安全性或商用適用性。release 未取得可能是沒有正式 release，不直接判斷無維護。
- 收藏數不等於使用率、品質或採購建議；相對成長尤其受低基期影響。
- 原始 Trending、收集紀錄、完整 README、近期活動樣本與收集狀態均保存在本日資料夾，便於重查。
