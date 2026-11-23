# GitHub AI 趨勢雷達｜2026-11-23

> 目標日期依 Asia/Taipei 前一個曆日計算。執行於 2026-11-24；Trending 與 API 為執行當下觀測，並非回溯重建 11 月 23 日整日行情。

## 收集範圍與判讀

- 使用指定 10 組查詢，每組 `--limit 10`，含 daily Trending 與 README。共更新 441 個專案（含歷史追蹤），其中 14 個來自本次範圍內 Trending。
- 排序依近期動能、相對成長、README 的具體用途、推送、release、Issue／PR 與 Adam 的應用關聯，由編輯判斷安排，並非總星數排名。
- Trending 今日增星是 [GitHub daily Trending](https://github.com/trending?since=daily) 的觀測視窗；快照增量是本次總星數減 2026-11-22 快照，兩者時間窗不同。相對成長＝快照增量／前次總星數。
- 首次觀測而無有效基準的增量標示「未測」；未上 Trending 標示「—」，不代表增星為零。
- 補抓每個入選專案最近更新的 5 筆 Issue／PR；這是活動樣本，不代表完整 bug 趨勢。open_issues 為 GitHub 的 Issue／PR 合計，不能當成 bug 數。PR closed 不等於已合併或發佈。
- README、描述及 Issue 是來源陳述；本次未安裝或實測專案。採用建議與應用方式為編輯推論。
- API 限流：未發生；無須重跑 `--limit 5`。原始狀態見 `collection-status.json`。

## 優先關注的 10 個專案

| 優先 | 專案 | 總星數 | Trending 今日 | 快照增量 | 相對成長 | 建議 |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 63,351 | 783 | +784 | 1.25% | Deep research |
| 2 | [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | 14,220 | 908 | +938 | 7.06% | Demo content |
| 3 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 12,166 | 425 | +365 | 3.09% | Skill candidate |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 70,781 | 624 | +633 | 0.90% | Skill candidate |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 73,252 | 790 | +725 | 1.00% | Deep research |
| 6 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 207,611 | 920 | +870 | 0.42% | Deep research |
| 7 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 77,204 | 593 | +564 | 0.74% | Watch |
| 8 | [cursor/plugins](https://github.com/cursor/plugins) | 18,722 | 395 | +389 | 2.12% | Reference only |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | 324,800 | 838 | +849 | 0.26% | Watch |
| 10 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 19,186 | 2037 | +2,002 | 11.65% | Watch |

### 1. HKUDS/CLI-Anything｜Deep research

**用途：**把既有軟體封裝成 agent 可呼叫的 CLI，README 展示從軟體操作到產出實際檔案的流程。

**動能：**總星數 63,351；Trending 今日 783；快照增量 +784；相對成長 1.25%。兼具高今日增星與直接辦公應用，列為優先研究。

**維護與版本：**最近推送 `2026-11-20T10:05:15Z`；API 最新 release `v0.4.0`（2026-06-25T15:17:49Z）；open_issues 合計 284；授權欄位 `Apache-2.0`。
近期 [GIMP 3 相容性 PR #694](https://github.com/HKUDS/CLI-Anything/pull/694) 與 [Calc 公式 PR #691](https://github.com/HKUDS/CLI-Anything/pull/691)；均為 open，修正尚不能視為已發佈。

**風險：**CLI 與軟體版本相依；GIMP 3 批次處理與 Calc 公式仍有修正提案，不能把所有軟體均可用的宣傳視為驗證結果。

**Adam／metabiz 關聯（編輯推論）：**Adam 的 AI 辦公自動化課程可用 LibreOffice 報表或圖像處理做端到端案例；將指令、輸入與結果驗證寫進 know metabiz wiki。

**下一步：**以固定輸入跑一份試算表，檢查公式計算與產物可重現性。

來源：[README](https://github.com/HKUDS/CLI-Anything#readme)、[releases](https://github.com/HKUDS/CLI-Anything/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 2. zhouxiaoka/autoclip｜Demo content

**用途：**將長影片切成短影音並生成字幕、封面與發布文案，提供桌面、CLI 與 MCP 工作流。

**動能：**總星數 14,220；Trending 今日 908；快照增量 +938；相對成長 7.06%。基數較小、熱門程度高且能直接產出內容，適合先做可驗收 demo。

**維護與版本：**最近推送 `2026-11-23T15:24:28Z`；API 最新 release `v1.5.9`（2026-11-22T23:45:38Z）；open_issues 合計 30；授權欄位 `MIT`。
[1.6.0-rc 發版 PR #677](https://github.com/zhouxiaoka/autoclip/pull/677) 仍 open；[字幕斷行 PR #669](https://github.com/zhouxiaoka/autoclip/pull/669) 顯示字幕相容性仍在調整。

**風險：**雲端模型另有成本；中文字幕斷行、人物取景及成片品質需人工驗收，RC 提案不代表穩定版已推出。

**Adam／metabiz 關聯（編輯推論）：**直接對應 Adam 課程與訪談的 Shorts／Reels 內容再製；可在 know metabiz wiki 記錄每支素材的剪輯、校稿與發布 SOP。

**下一步：**以一段自有繁中課程測試三支短片，量測校字幕及調整取景時間。

來源：[README](https://github.com/zhouxiaoka/autoclip#readme)、[releases](https://github.com/zhouxiaoka/autoclip/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 3. google-labs-code/stitch-skills｜Skill candidate

**用途：**將 Google Stitch 設計與元件工作流整理成可供多種 coding agent 使用的 skills／plugins。

**動能：**總星數 12,166；Trending 今日 425；快照增量 +365；相對成長 3.09%。較小基數的相對成長比總星數更有參考價值，但近期主線及安裝修正仍需追蹤。

**維護與版本：**最近推送 `2026-11-20T18:08:01Z`；API 最新 release `v1.0`（2026-05-18T18:02:32Z）；open_issues 合計 27；授權欄位 `Apache-2.0`。
[路徑解析 PR #112](https://github.com/google-labs-code/stitch-skills/pull/112) 仍 open，處理從 plugin root 或 repo clone 找 uploader 的問題。

**風險：**依賴 Stitch 服務與宿主 plugin 結構；安裝成功不代表各種宿主、工作目錄都能運作。

**Adam／metabiz 關聯（編輯推論）：**適合 Adam 的跨工具 Agent Skills 課程；可研究如何把 metabiz 辦公系統畫面設計、元件與驗收連成可重用流程。

**下一步：**在獨立測試專案檢查跨工作目錄的腳本路徑與輸出，不直接安裝到正式環境。

來源：[README](https://github.com/google-labs-code/stitch-skills#readme)、[releases](https://github.com/google-labs-code/stitch-skills/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 4. cathrynlavery/diagram-design｜Skill candidate

**用途：**以單一 HTML＋SVG 產出品牌化圖解，README 現列 52 種圖表類型。

**動能：**總星數 70,781；Trending 今日 624；快照增量 +633；相對成長 0.90%。今日熱度配合具體封裝改進，適合做圖解產物驗收。

**維護與版本：**最近推送 `2026-11-23T11:00:38Z`；API 最新 release `未取得正式 release`（—）；open_issues 合計 39；授權欄位 `MIT`。
[Desktop ZIP PR #531](https://github.com/cathrynlavery/diagram-design/pull/531) 與 [Windows／路徑 PR #540](https://github.com/cathrynlavery/diagram-design/pull/540) 已 closed；closed 本身不證明已合併或發佈。

**風險：**HTML／SVG 的字型、匯出、列印與跨平台效果需驗證；README 的圖種數量屬作者陳述。

**Adam／metabiz 關聯（編輯推論）：**可製作 Adam 課程架構圖、AI 辦公流程圖與 know metabiz wiki 的系統關係圖；適合比較圖解品質與人工調整成本。

**下一步：**用同一份中文流程規格產圖，檢查溢字、箭頭語義、SVG／PNG 匯出。

來源：[README](https://github.com/cathrynlavery/diagram-design#readme)、[releases](https://github.com/cathrynlavery/diagram-design/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 5. mvanhorn/last30days-skill｜Deep research

**用途：**跨社群與網路來源研究近期話題，以互動訊號輔助彙整。

**動能：**總星數 73,252；Trending 今日 790；快照增量 +725；相對成長 1.00%。今日熱度之外亦有近期 release，值得檢查研究品質是否跟上功能擴張。

**維護與版本：**最近推送 `2026-11-23T01:00:01Z`；API 最新 release `v4.6.0`（2026-11-22T04:31:36Z）；open_issues 合計 24；授權欄位 `MIT`。
[cookie 同意 PR #1440](https://github.com/mvanhorn/last30days-skill/pull/1440) 已 closed；[日期解析 PR #1570](https://github.com/mvanhorn/last30days-skill/pull/1570) 仍 open，研究時間窗需抽查。

**風險：**互動量不能代表資訊正確；來源 API、登入與 cookie 使用影響可用性及資料界線。

**Adam／metabiz 關聯（編輯推論）：**可支援 Adam 課程選題、影片腳本前置研究與公司競品觀察；know metabiz wiki 應保留來源、日期和可追溯主張。

**下一步：**用同一選題比對來源完整度、日期正確率與結論引文，不只比較摘要流暢度。

來源：[README](https://github.com/mvanhorn/last30days-skill#readme)、[releases](https://github.com/mvanhorn/last30days-skill/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 6. firecrawl/firecrawl｜Deep research

**用途：**把網站轉成可供 agent 與 RAG 使用的資料，README 區分 Local、Cloud 與完整自架服務。

**動能：**總星數 207,611；Trending 今日 920；快照增量 +870；相對成長 0.42%。絕對增星高，但應同時看大基數下的相對增幅，以及資料攝取實用性。

**維護與版本：**最近推送 `2026-11-23T14:59:30Z`；API 最新 release `v2.11.0`（2026-06-19T15:09:30Z）；open_issues 合計 924；授權欄位 `AGPL-3.0`。
[Python SDK 文件 PR #5990](https://github.com/firecrawl/firecrawl/pull/5990) 仍 open；[API routing PR #5984](https://github.com/firecrawl/firecrawl/pull/5984) 已 closed。近期樣本也有宣傳型 Issue，不能把所有活動都當成維護成果。

**風險：**AGPL-3.0 與不同部署模式需分別確認使用條件；動態頁、重導向、雲端用量與內容更新都會影響品質。

**Adam／metabiz 關聯（編輯推論）：**可作 know metabiz wiki 的公開來源攝取層；Adam 課程可展示擷取、清理、來源標記與知識更新的完整流程。

**下一步：**用一組公開文件測來源 URL、重複內容與增量更新；比較 Local／自架需求。

來源：[README](https://github.com/firecrawl/firecrawl#readme)、[releases](https://github.com/firecrawl/firecrawl/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 7. toeverything/AFFiNE｜Watch

**用途：**整合文件、白板及表格的知識工作空間，涵蓋 wiki 與數位資產管理。

**動能：**總星數 77,204；Trending 今日 593；快照增量 +564；相對成長 0.74%。知識庫需求與近期協作功能 PR 有直接關聯，先觀察權限及資料可攜性。

**維護與版本：**最近推送 `2026-11-23T16:11:47Z`；API 最新 release `v0.27.4`（2026-08-18T16:51:39Z）；open_issues 合計 702；授權欄位 `NOASSERTION`。
[逐頁讀寫權限 PR #15522](https://github.com/toeverything/AFFiNE/pull/15522) 與 [台灣繁中 PR #15852](https://github.com/toeverything/AFFiNE/pull/15852) 仍 open，與公司協作落地直接相關。

**風險：**API 的 license 為 NOASSERTION，不能直接當成無限制商用；權限、匯出及現有 wiki 搬遷成本仍需評估。

**Adam／metabiz 關聯（編輯推論）：**適合評估 know metabiz wiki 的編輯及視覺化入口；Adam 可做「文件＋白板如何接到 AI 知識工作」的案例。

**下一步：**以小型非敏感文件測讀寫權限、繁中與 Markdown 匯出完整度。

來源：[README](https://github.com/toeverything/AFFiNE#readme)、[releases](https://github.com/toeverything/AFFiNE/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 8. cursor/plugins｜Reference only

**用途：**Cursor 官方 plugin 與 manifest 範例集合，含教學、持續學習與團隊工作流。

**動能：**總星數 18,722；Trending 今日 395；快照增量 +389；相對成長 2.12%。相對增幅值得注意，但授權及宿主相容性證據不足，維持參考用途。

**維護與版本：**最近推送 `2026-11-22T01:02:38Z`；API 最新 release `未取得正式 release`（—）；open_issues 合計 689；授權欄位 `未提供`。
[多宿主 ports PR #1322](https://github.com/cursor/plugins/pull/1322) 已 closed；[新 plugin PR #1256](https://github.com/cursor/plugins/pull/1256) 仍 open。

**風險：**API 未提供明確 SPDX 授權；不同 plugin 的授權、腳本與 MCP 權限須個別查驗，不宜整包搬用。

**Adam／metabiz 關聯（編輯推論）：**作 Adam 跨宿主 plugin 教學與 metabiz skill 包裝的參考；know metabiz wiki 可記錄 manifest、宿主差異與移植限制。

**下一步：**挑單一 teaching 或 compatibility 範例比較結構，先補授權與宿主相容性證據。

來源：[README](https://github.com/cursor/plugins#readme)、[releases](https://github.com/cursor/plugins/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 9. obra/superpowers｜Watch

**用途：**把需求釐清、規劃與開發驗證組成可重複使用的 coding agent skills 方法。

**動能：**總星數 324,800；Trending 今日 838；快照增量 +849；相對成長 0.26%。總星數領先，但主線推送較久，搭配成本回報後採觀察，不因規模直接排首位。

**維護與版本：**最近推送 `2026-11-03T23:24:58Z`；API 最新 release `v7.0.2`（2026-11-03T22:17:54Z）；open_issues 合計 361；授權欄位 `MIT`。
[Issue #2612](https://github.com/obra/superpowers/issues/2612) 回報多次 session limit 與大量 context；[Issue #2723](https://github.com/obra/superpowers/issues/2723) 回報腳本執行權限問題，皆為使用者回報，尚未獨立重現。

**風險：**總星數高但不能證明適合長任務；額外協調、執行權限與 context 成本可能抵消效益。

**Adam／metabiz 關聯（編輯推論）：**可供 Adam Agent 工程課程比較開發工作法；metabiz 團隊可評估較小任務的採用成本，將實測結果寫入 wiki。

**下一步：**以固定小任務比對耗時、token 與缺陷數，追蹤 #2612 的維護者回覆。

來源：[README](https://github.com/obra/superpowers#readme)、[releases](https://github.com/obra/superpowers/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

### 10. elementalsouls/Claude-BugHunter｜Watch

**用途：**面向安全研究的 Claude Code skill bundle，將漏洞案例與 scope 控制整理成工作流。

**動能：**總星數 19,186；Trending 今日 2037；快照增量 +2,002；相對成長 11.65%。今日增星最高且小基數放大相對成長，但與日常辦公適配較低，安全邊界修正比熱度更重要。

**維護與版本：**最近推送 `2026-11-23T15:45:22Z`；API 最新 release `v2.1`（2026-06-05T16:15:13Z）；open_issues 合計 10；授權欄位 `MIT`。
[scope import PR #208](https://github.com/elementalsouls/Claude-BugHunter/pull/208) 仍 open；[fail-open PR #182](https://github.com/elementalsouls/Claude-BugHunter/pull/182) 與 [redirect PR #181](https://github.com/elementalsouls/Claude-BugHunter/pull/181) 已 closed，不能只由狀態推定修正已發佈。

**風險：**高熱度與大量技能不等於可靠；近期 scope fail-open、重導向越界修正顯示控制邊界仍是重點。

**Adam／metabiz 關聯（編輯推論）：**適合 Adam 進階課程講解安全 agent 的邊界設計；metabiz 可參考 scope 控制與稽核紀錄，不將其當成通用辦公工具。

**下一步：**只閱讀 scope 設計與公開測試紀錄，觀察修正版本及回歸證據。

來源：[README](https://github.com/elementalsouls/Claude-BugHunter#readme)、[releases](https://github.com/elementalsouls/Claude-BugHunter/releases)。近期活動連結見上；擷取樣本存於 `activity-evidence.json` 與 `readme-evidence.json`。

## 明日觀察清單（2026-11-24）

- **CLI-Anything／AutoClip：**觀察今日動能是否持續，分別追蹤 Calc／GIMP 相容性、RC 與字幕修正；準備固定輸入的辦公與繁中影片驗收案例。
- **Stitch Skills／diagram-design：**追蹤跨目錄路徑、Desktop／Windows 封裝；檢查 skill 可攜性與中文輸出的品質。
- **last30days／Firecrawl：**追蹤最新 release 與主線差距，建立帶日期與來源 URL 的小型知識攝取／研究品質測試。
- **AFFiNE：**追蹤逐頁權限、台灣繁中與 Markdown 匯出，評估 know metabiz wiki 的入口及移轉成本。
- **Superpowers／Claude-BugHunter：**追蹤 context 成本、scope 邊界修正的維護者回覆及發佈證據，避免把星數當成穩定性。
- **擴展觀察：**[Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) 本次仍在 Trending；明日補查 CI/CD 故障診斷的 release 與修復驗證，評估開發自動化課程價值。

## 資料與限制

- `repos.json`、`snapshots/repos-2026-11-23.json`：完整快照；`report.md`：收集器自動摘要，其規則分類與本篇編輯建議可能不同。
- `trending-evidence.json` 保留原始卡片供稽核；完整原始卡片可能含範圍外專案，最終 Trending 候選已由收集器篩選。
- `activity-evidence.json` 與 `readme-evidence.json` 為分析證據；查詢與執行狀態見 `collection-status.json`。
- 既有收集器在歷史專案讀取失敗時可能沿用舊資料；本次檢查執行紀錄，沿用情形見下。
- 歷史資料沿用：6 筆。詳見 collector log，不能把沿用資料視為本次即時更新。
- 本次原始快照有 457 筆紀錄、441 個唯一 full_name，差異來自既有追蹤名稱經 GitHub 重新導向至相同 canonical 名稱；本篇與 dashboard 依 full_name 合併判讀，原始快照保留收集器輸出。
- 404 沿用舊資料：`BarberNumber/Midjourney-Software`、`BrickOrioleLoad/aion-2-trainer-tool`、`HunYiSage/dsh-purge`、`YuJunZhiXue/dsh-purge`、`hanshaze/Awesome-Prediction-Market-Trading-Tools`、`mingrath/obsidian-ai-knowledge-agent`。這些資料不代表本次即時觀測，均未列入上述 10 個推薦。
