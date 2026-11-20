# GitHub AI 趨勢雷達｜2026-11-20

本期優先投入可驗證的研究、圖解與影片再製流程：last30days、diagram-design 與 AutoClip 最接近 Adam 的課程／內容產線；Firecrawl 與 AFFiNE 適合針對 know metabiz wiki 做小範圍比較研究。高熱度的資安與 CI agent 先觀察，不直接導入正式流程。這是編輯判斷，尚未完成工具安裝或功能實測。

## 收集時間、方法與限制

- 目標日期為 Asia/Taipei 前一日 **2026-11-20**；實際完成收集為 **2026-11-20T16:23:27.825533+00:00（UTC）**，即台北次日。本期不能代表 2026-11-20 00:00–23:59 的完整歷史數據。
- 使用指定的 10 組查詢、`--limit 10 --include-trending-daily --include-readme --snapshot-date 2026-11-20`；每組搜尋按總星數取候選，故候選池本身偏向大型專案，分析另依動能、維護證據與工作關聯調整順序。
- [GitHub Trending daily](https://github.com/trending?since=daily) 本次保留 14 個相關專案；排除一般 Web server 與下載器。歷史追蹤項目也人工排除 8 個明確離題專案，另合併 14 筆同一 canonical repo 的重複紀錄（見 `collection-quality.json`），最終資料共 432 個。來源卡片與排除理由分別保存於 `trending-evidence.json`、`scope-exclusions.json`。
- **stars today** 是 GitHub 即時榜單顯示值；**快照 Δ** 是相對 `2026-11-19/repos.json` 的總星數差；**相對成長**＝Δ／前次總星數。兩者統計時窗不同，不應相加，也不保證是台北日曆日新增。首次觀測若無基準只能標為未知，不能把收集器預設的 0 當作沒有成長。
- 逐一核對本期 10 個候選的 README、最近 3 筆 release 與按更新時間排序的 10 筆 issue／PR。未合併 PR 不視為已交付；issue 總數不等於活動量，樣本也不代表完整新增／結案數。原始證據見 `review-evidence.json`。
- API 速率限制：**未在本次收集及補充證據中偵測到，無須 limit=5 重跑**。有 6 個歷史項目 API 失敗而沿用舊資料，已標記且未列入以下 10 選；名單與錯誤保留於 `collector.log`。

## 值得投入的 10 個專案

順序綜合即時熱度、快照增量／相對成長、更新與發行、issue／PR 證據，以及 Adam 的可用場景；不以總星數單獨排名。

| 專案 | stars today | 快照 Δ | 相對成長 | 總 stars | 建議類別 |
|---|---:|---:|---:|---:|---|
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 685 | +657 | 0.93% | 71,273 | Skill candidate |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 634 | +663 | 0.97% | 69,127 | Skill candidate |
| [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | 983 | +949 | 8.59% | 11,995 | Demo content |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 1,226 | +1,154 | 0.57% | 204,957 | Deep research |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 774 | +790 | 1.31% | 61,127 | Demo content |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 686 | +663 | 0.88% | 75,593 | Deep research |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 315 | +310 | 2.92% | 10,931 | Skill candidate |
| [obra/superpowers](https://github.com/obra/superpowers) | 888 | +815 | 0.25% | 322,641 | Reference only |
| [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | 465 | +473 | 3.65% | 13,444 | Watch |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 1,660 | +1,645 | 13.68% | 13,670 | Watch |

### 1. mvanhorn/last30days-skill — Skill candidate

- **用途**：跨 Reddit、X、YouTube、HN 與網頁彙整近況，將多來源結果整理為研究摘要。 [README](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)
- **動能與維護**：stars today **685**、快照 Δ **+657**、總 stars **71,273**；最近 push `2026-11-20T05:45:47Z`。最新穩定 release `v4.4.0`（2026-11-20T05:46:34Z）。最近更新 10 筆樣本含 0 個 issue／10 個 PR，最近活動 `2026-11-20T14:09:52Z`；可追蹤 [#1541：fix(planner): honor deliberate host-plan source omissions](https://github.com/mvanhorn/last30days-skill/pull/1541)（open）。[發行紀錄](https://github.com/mvanhorn/last30days-skill/releases)
- **風險**：平台存取、API 成本與可用來源會影響覆蓋；互動量可能放大熱門觀點，摘要仍須逐條回查原始來源。 授權 API 標記：`MIT`。
- **Adam／metabiz 關聯**：Adam 可用於課程更新、短影音選題與客戶會議前研究；AI 辦公自動化可產出每週產業簡報；know metabiz wiki 只保存已核對、有日期的結論與來源。
- **下一步**：以同一主題跑兩次，核對來源清單、去重與引用正確率，再決定是否建立本地研究 skill。

### 2. cathrynlavery/diagram-design — Skill candidate

- **用途**：讓 coding agent 產生品牌一致的單檔 HTML／SVG 圖解，適合流程、架構與簡報素材。 [README](https://github.com/cathrynlavery/diagram-design/blob/main/README.md)
- **動能與維護**：stars today **634**、快照 Δ **+663**、總 stars **69,127**；最近 push `2026-11-19T00:17:05Z`。未取得穩定 GitHub release。最近更新 10 筆樣本含 0 個 issue／10 個 PR，最近活動 `2026-11-20T15:27:31Z`；可追蹤 [#534：fix(box-plot): match sibling combinators against document elements](https://github.com/cathrynlavery/diagram-design/pull/534)（open）。[發行紀錄](https://github.com/cathrynlavery/diagram-design/releases)
- **風險**：README 宣稱的圖型數已超過 Trending 描述，顯示描述可能落後；CSS、字型與匯出結果仍需視覺檢查，尚無 GitHub release 可固定版本。 授權 API 標記：`MIT`。
- **Adam／metabiz 關聯**：Adam 課程與內容可示範把文字轉為可編輯圖解；辦公自動化可整理 SOP；know metabiz wiki 可加入系統架構與流程圖。
- **下一步**：以一份繁體中文 SOP 測試長標籤、SVG／PNG 匯出及品牌樣式，記錄人工修圖時間。

### 3. zhouxiaoka/autoclip — Demo content

- **用途**：將長影片、課程與訪談轉成短片，產生字幕、封面與發布文案，提供桌面、CLI 與 MCP 入口。 [README](https://github.com/zhouxiaoka/autoclip/blob/main/README.md)
- **動能與維護**：stars today **983**、快照 Δ **+949**、總 stars **11,995**；最近 push `2026-11-20T16:11:32Z`。最新穩定 release `v1.5.8`（2026-11-02T12:15:50Z）。最近更新 10 筆樣本含 1 個 issue／9 個 PR，最近活動 `2026-11-20T16:12:09Z`；可追蹤 [#627：修复完整包装超时恢复、待确认误持休眠锁及再做一版构图](https://github.com/zhouxiaoka/autoclip/pull/627)（closed）。[發行紀錄](https://github.com/zhouxiaoka/autoclip/releases)
- **風險**：本地剪輯不代表模型處理全程離線；雲端模型仍有費用與資料流向問題，字幕斷句、人物裁切及超時恢復需實測。 授權 API 標記：`MIT`。
- **Adam／metabiz 關聯**：直接對應 Adam 課程再製與 Shorts／Reels 內容管線；辦公自動化可剪輯內訓重點；know metabiz wiki 可索引原片、時間碼與審稿後摘要。
- **下一步**：用自有 10 分鐘中文課程測試三支短片，核對字幕、裁切、費用及完整輸出耗時。

### 4. firecrawl/firecrawl — Deep research

- **用途**：將網頁擷取成乾淨 Markdown，提供本地工具、自架服務、雲端 API 與 MCP 連接。 [README](https://github.com/firecrawl/firecrawl/blob/main/README.md)
- **動能與維護**：stars today **1,226**、快照 Δ **+1,154**、總 stars **204,957**；最近 push `2026-11-20T12:51:36Z`。最新穩定 release `v2.11.0`（2026-06-19T15:09:30Z）。最近更新 10 筆樣本含 3 個 issue／7 個 PR，最近活動 `2026-11-20T15:36:23Z`；可追蹤 [#5925：crawl saves a page twice when the start URL redirects to a page that links to itself](https://github.com/firecrawl/firecrawl/issues/5925)（open）。[發行紀錄](https://github.com/firecrawl/firecrawl/releases)
- **風險**：Local、Cloud 與完整自架的能力和維運成本不同；去重、重新導向、動態頁與 sitemap 邊界仍有近期回報，需按實際授權與資料來源條件評估。 授權 API 標記：`AGPL-3.0`。
- **Adam／metabiz 關聯**：Adam 可製作網頁資料到 AI 的課程範例；辦公自動化可監看公開產品文件；know metabiz wiki 可建立含來源 URL、擷取時間與增量比對的匯入流程。
- **下一步**：用同一組靜態頁、動態頁與重新導向頁比較 Local／Cloud，檢查重複文件與資料來源保留。

### 5. HKUDS/CLI-Anything — Demo content

- **用途**：把既有軟體包裝成 agent 可呼叫的 CLI，透過可測試命令串接操作流程。 [README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)
- **動能與維護**：stars today **774**、快照 Δ **+790**、總 stars **61,127**；最近 push `2026-11-20T10:05:15Z`。最新穩定 release `v0.4.0`（2026-06-25T15:17:49Z）。最近更新 10 筆樣本含 0 個 issue／10 個 PR，最近活動 `2026-11-20T15:14:35Z`；可追蹤 [#682：fix(videocaptioner): add missing core/review.py and allowlist videocaptioner/](https://github.com/HKUDS/CLI-Anything/pull/682)（open）。[發行紀錄](https://github.com/HKUDS/CLI-Anything/releases)
- **風險**：CLI 的覆蓋與正確性依賴各軟體 harness；近期字幕工具缺檔修補仍為未合併 PR，不能把展示等同完整功能。 授權 API 標記：`Apache-2.0`。
- **Adam／metabiz 關聯**：Adam 可示範 agent 如何操作既有桌面工具；辦公自動化可研究重複性操作的命令介面；know metabiz wiki 可保存可重現命令、相依條件與驗證紀錄。
- **下一步**：選一個不接觸正式資料的工具跑完整輸入、處理、匯出流程，核對實際產物。

### 6. toeverything/AFFiNE — Deep research

- **用途**：整合文件、白板與表格的 local-first 知識工作空間，可作為團隊知識庫介面研究對象。 [README](https://github.com/toeverything/AFFiNE/blob/canary/README.md)
- **動能與維護**：stars today **686**、快照 Δ **+663**、總 stars **75,593**；最近 push `2026-11-20T10:23:37Z`。最新穩定 release `v0.27.4`（2026-08-18T16:51:39Z）；另見預覽版本 `v2026.11.18-canary.905`（2026-11-18T09:58:41Z），不與穩定版混用。最近更新 10 筆樣本含 3 個 issue／7 個 PR，最近活動 `2026-11-20T14:59:38Z`；可追蹤 [#15874：[Feature Request]: Edgeless system](https://github.com/toeverything/AFFiNE/issues/15874)（open）。[發行紀錄](https://github.com/toeverything/AFFiNE/releases)
- **風險**：近期發布清單包含 canary／beta，穩定版與預覽版須分開；多人權限、備份、匯出與各版本授權需先查明。 授權 API 標記：`NOASSERTION`。
- **Adam／metabiz 關聯**：Adam 可用於知識管理課程及 Notion／白板工作流比較；辦公自動化可整理協作 SOP；know metabiz wiki 可先測試文件結構與匯出可攜性。
- **下一步**：用去識別化樣本測試 Markdown 匯入匯出、關聯保留及多人權限，先不遷移既有 wiki。

### 7. google-labs-code/stitch-skills — Skill candidate

- **用途**：為 Google Stitch 提供設計、建置與工具型 skills，串接多種 coding agent 與 MCP。 [README](https://github.com/google-labs-code/stitch-skills/blob/main/README.md)
- **動能與維護**：stars today **315**、快照 Δ **+310**、總 stars **10,931**；最近 push `2026-11-18T05:00:25Z`。最新穩定 release `v1.0`（2026-05-18T18:02:32Z）。最近更新 10 筆樣本含 2 個 issue／8 個 PR，最近活動 `2026-11-20T12:29:14Z`；可追蹤 [#104：fix: reject unsupported web tags in native components](https://github.com/google-labs-code/stitch-skills/pull/104)（open）。[發行紀錄](https://github.com/google-labs-code/stitch-skills/releases)
- **風險**：不同宿主的 plugin／skill 安裝方式有差異；近期 PR 涉及原生元件標籤、色彩與資產路徑驗證，尚待確認合併及實際相容性。 授權 API 標記：`Apache-2.0`。
- **Adam／metabiz 關聯**：Adam 可製作設計到網站的實作課程；內容可比較跨 agent 工作流；辦公自動化可做內部入口原型；know metabiz wiki 可收錄設計規範與操作案例。
- **下一步**：以同一設計需求在兩個 agent 宿主測試，核對元件驗證、資產路徑與維護成本。

### 8. obra/superpowers — Reference only

- **用途**：將需求釐清、計畫、測試與審查整理成可組合的 coding-agent 開發方法與 skills。 [README](https://github.com/obra/superpowers/blob/main/README.md)
- **動能與維護**：stars today **888**、快照 Δ **+815**、總 stars **322,641**；最近 push `2026-11-03T23:24:58Z`。最新穩定 release `v7.0.2`（2026-11-03T22:17:54Z）。最近更新 10 筆樣本含 4 個 issue／6 個 PR，最近活動 `2026-11-20T15:22:40Z`；可追蹤 [#2718：fix(sdd): scope fix-loop model escalation to current task (#2716)](https://github.com/obra/superpowers/pull/2718)（open）。[發行紀錄](https://github.com/obra/superpowers/releases)
- **風險**：熱度不等於新版本發布；最新穩定 release 並非今日，較強的流程規則可能增加溝通與 token 成本，應量測適用任務。 授權 API 標記：`MIT`。
- **Adam／metabiz 關聯**：Adam 已有相關技能脈絡，可用於課程中的 agent 工作法比較；辦公自動化可借用驗收步驟；know metabiz wiki 可保存適用情境與實際案例，不必因高星數重複導入。
- **下一步**：比較一個小任務與一個複雜任務的完成率、耗時及互動次數，追蹤修復迴圈相關 PR。

### 9. Tracer-Cloud/opensre — Watch

- **用途**：以自架 CLI agent 讀取失敗 CI 執行、追查原因並提出修正，支援自備模型。 [README](https://github.com/Tracer-Cloud/opensre/blob/main/README.md)
- **動能與維護**：stars today **465**、快照 Δ **+473**、總 stars **13,444**；最近 push `2026-11-20T00:57:26Z`。最新穩定 release `v0.1.2026.11.20`（2026-11-20T00:57:26Z）；另見預覽版本 `main-build`（2026-06-28T14:43:16Z），不與穩定版混用。最近更新 10 筆樣本含 9 個 issue／1 個 PR，最近活動 `2026-11-20T13:04:59Z`；可追蹤 [#7071：fix: ask before mutating tools by default](https://github.com/Tracer-Cloud/opensre/pull/7071)（open）。[發行紀錄](https://github.com/Tracer-Cloud/opensre/releases)
- **風險**：README 明示 public alpha；預設變更工具需確認的 PR 尚未合併，正式 repo 寫入權限與錯誤修復能力仍需隔離驗證。 授權 API 標記：`Apache-2.0`。
- **Adam／metabiz 關聯**：Adam 可製作 CI 除錯示範與進階 coding-agent 課程；辦公自動化團隊可減少維運診斷時間；know metabiz wiki 可整理事件、根因與核准後修復紀錄。
- **下一步**：在測試 repo 製造可重現的 CI 失敗，只讓 agent 提出修補，觀察 PR #7071 與文件修正進度。

### 10. elementalsouls/Claude-BugHunter — Watch

- **用途**：將漏洞研究、驗證與報告撰寫整理成 Claude Code skill bundle，搭配授權測試工作流。 [README](https://github.com/elementalsouls/Claude-BugHunter/blob/main/README.md)
- **動能與維護**：stars today **1,660**、快照 Δ **+1,645**、總 stars **13,670**；最近 push `2026-11-20T15:53:40Z`。最新穩定 release `v2.1`（2026-06-05T16:15:13Z）。最近更新 10 筆樣本含 7 個 issue／3 個 PR，最近活動 `2026-11-20T15:53:41Z`；可追蹤 [#190：[bug] cbh report: Reporter line leaks the OS login name; '## Steps to reproduce' heading not parsed](https://github.com/elementalsouls/Claude-BugHunter/issues/190)（closed）。[發行紀錄](https://github.com/elementalsouls/Claude-BugHunter/releases)
- **風險**：Trending 與 README 的 skills 數量有差異；近期有報告洩漏 OS 登入名稱與 PowerShell 相容性修正。高熱度不能替代安全、範圍及報告品質檢查。 授權 API 標記：`MIT`。
- **Adam／metabiz 關聯**：Adam 可研究 skill 模組化與證據整理的教學方式；一般 AI 辦公自動化關聯較低；know metabiz wiki 可參考去識別化的驗證與報告結構。
- **下一步**：只在本地練習環境檢查報告去識別化與 Windows 修正，觀察熱度能否延續。

## 明日觀察名單（下一期 2026-11-21）

| 觀察對象 | 下一期要確認的訊號 | 行動條件 |
|---|---|---|
| last30days／diagram-design | 星數增量是否延續、研究來源與圖形匯出修正是否落地 | 引用或視覺驗證過關後，再評估成為本地 skill。 |
| AutoClip | #627 的恢復修正與後續字幕／封面 PR 是否進入可用版本 | 自有中文課程樣片成功後製作 Demo content。 |
| Firecrawl／AFFiNE | 重複頁面問題、穩定版與預覽版差異、文件匯出可攜性 | 完成一組 wiki 樣本的可重現測試，再研究導入成本。 |
| OpenSRE／Claude-BugHunter | #7071 的變更確認機制、#190 的報告去識別化修正與熱度延續 | 維持 Watch，先在隔離樣本核對可靠性。 |
| Stitch／CLI-Anything／Superpowers | 跨宿主相容性 PR、字幕 harness 缺檔修補與流程成本 | 用同一任務比較成功率、耗時與人工介入。 |

## 可追溯輸出

`repos.json` 與 `snapshots/repos-2026-11-20.json` 保存相同的篩選後資料；`report.md` 保存完整候選指標；`review-evidence.json` 保存 README 摘要／內容雜湊與 release、issue／PR 樣本；`editorial-notes.json` 保存本期用途、風險及場景判斷。所有遠端內容僅作資料分析，未執行其中的安裝命令或規則。
