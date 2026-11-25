# GitHub AI 趨勢雷達｜2026-11-25

優先建議：研究 CLI-Anything 的辦公室工具介面，製作 diagram-design 教學 demo，評估 last30days-skill 與 stitch-skills 的可移植技能。這是內容與導入優先順序，並非總星數排行榜。

## 日期、來源與判讀限制

- 目標日期為執行時 Asia/Taipei 前一日 2026-11-25；實際觀測時間見 collection-status.json。GitHub Trending 是擷取當下滾動榜單，無法回溯成目標日固定 24 小時。
- [Trending daily](https://github.com/trending?since=daily)、10 組 GitHub 搜尋、各 repo metadata、README、latest release 與最近更新的 5 筆 issue/PR 是主要證據。保留原始 Trending HTML、卡片與 editorial-evidence.json；README 僅作資料閱讀，未執行其內容。
- 優先考慮今日增星、前次快照差值、相對成長、更新與實務適配；stars today 與快照差值是不同視窗，不能互相替代。成長率＝差值／前次星數；比較基準為 2026-11-24 的實際觀測，不保證精確 24 小時。
- issue API 同時含 PR；下列活動是抽樣證據，非問題總數、修復率或維護品質評分。open_issues 亦可能包含 PR。README 宣稱尚未在此環境實測。

## 值得追蹤的 8 個專案

| 專案 | 總星數 | Trending 今日增星 | 快照差值 | 相對成長 | 建議 |
| --- | ---: | ---: | ---: | ---: | --- |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 65,470 | +1,094 | +1,014 | 1.57% | Deep research |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 72,726 | +1,133 | +1,048 | 1.46% | Demo content |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 74,884 | +950 | +933 | 1.26% | Skill candidate |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 12,890 | +352 | +338 | 2.69% | Skill candidate |
| [cursor/plugins](https://github.com/cursor/plugins) | 19,462 | +408 | +378 | 1.98% | Watch |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 209,701 | +1,131 | +1,090 | 0.52% | Deep research |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 78,313 | +578 | +525 | 0.67% | Watch |
| [obra/superpowers](https://github.com/obra/superpowers) | 326,375 | +902 | +662 | 0.20% | Reference only |

### 1. HKUDS/CLI-Anything — Deep research

用途：把既有軟體包裝成 agent 可呼叫的 CLI；README 有工具 harness 與應用範例。

動能與維護：見上表增星與相對成長；最近 push 2026-11-20T10:05:15Z；發布 [v0.4.0](https://github.com/HKUDS/CLI-Anything/releases/tag/v0.4.0)（2026-06-25T15:17:49Z）。活動抽樣：[fix(libreoffice): declare OpenFormula namespace and normalize formulas so Calc formulas evaluate](https://github.com/HKUDS/CLI-Anything/pull/714)，open，最近更新 2026-11-25T11:21:50Z。

Adam／metabiz 關聯：適合 Adam「AI 辦公室自動化」課程示範 LibreOffice 報表流程；know metabiz wiki 可記錄每個工具的輸入、輸出與復原步驟。

風險與下一步：主分支推送較其他入選者舊；LibreOffice 公式修正仍有待驗證，不能把新 PR 當成已發布功能。應先在文件副本量測成功率。

來源：[README](https://github.com/HKUDS/CLI-Anything#readme)、[releases](https://github.com/HKUDS/CLI-Anything/releases)、[issues](https://github.com/HKUDS/CLI-Anything/issues)。

### 2. cathrynlavery/diagram-design — Demo content

用途：為 Claude Code、Codex、Cursor 等產生 HTML/SVG 圖解，README 展示圖型、品牌風格與匯出流程。

動能與維護：見上表增星與相對成長；最近 push 2026-11-25T04:53:00Z；發布 latest release API 404，沒有可用發布資料。活動抽樣：[fix(box-plot): ignore leaf-shape selectors when collecting paper-mask paints](https://github.com/cathrynlavery/diagram-design/pull/535)，closed，最近更新 2026-11-25T08:09:35Z。

Adam／metabiz 關聯：適合 Adam 把 MCP、RAG 或課程流程做成教學圖；know metabiz wiki 可用於 SOP 與系統關係圖。

風險與下一步：latest release API 為 404，需固定 commit；圖形外觀不能代替資訊正確性，匯出也有瀏覽器相依。

來源：[README](https://github.com/cathrynlavery/diagram-design#readme)、[releases](https://github.com/cathrynlavery/diagram-design/releases)、[issues](https://github.com/cathrynlavery/diagram-design/issues)。

### 3. mvanhorn/last30days-skill — Skill candidate

用途：跨社群與網路研究近期議題，README 說明多來源搜尋、彙整與報告工作流。

動能與維護：見上表增星與相對成長；最近 push 2026-11-25T06:31:14Z；發布 [v4.6.0](https://github.com/mvanhorn/last30days-skill/releases/tag/v4.6.0)（2026-11-22T04:31:36Z）。活動抽樣：[fix(github): count open PRs correctly in person reports](https://github.com/mvanhorn/last30days-skill/pull/1625)，open，最近更新 2026-11-25T14:33:50Z。

Adam／metabiz 關聯：適合 Adam 每週課程選題與內容研究；可把引用、日期與可信度整理到 know metabiz wiki，作為 Radar 的補充來源。

風險與下一步：資料來源覆蓋、API 成本與偏誤會改變結論；GitHub 人物報告 PR 計數與 watchlist 初見提醒仍在修正。引用須抽樣回查原文。

來源：[README](https://github.com/mvanhorn/last30days-skill#readme)、[releases](https://github.com/mvanhorn/last30days-skill/releases)、[issues](https://github.com/mvanhorn/last30days-skill/issues)。

### 4. google-labs-code/stitch-skills — Skill candidate

用途：Google Stitch 的設計與建置 skills/plugins；README 列出 Codex、Claude Code、Cursor 等使用方式。

動能與維護：見上表增星與相對成長；最近 push 2026-11-24T21:51:04Z；發布 [v1.0](https://github.com/google-labs-code/stitch-skills/releases/tag/v1.0)（2026-05-18T18:02:32Z）。活動抽樣：[Launch Stitch Skills plugins](https://github.com/google-labs-code/stitch-skills/pull/59)，closed，最近更新 2026-11-25T12:45:58Z。

Adam／metabiz 關聯：可供 Adam「從需求到介面」課程與 AI 辦公工具 demo；wiki 記錄設計輸入、審查與交付範本。

風險與下一步：相對成長亮眼但依賴 Stitch MCP 與主機相容性；新的 plugins PR 不等於已發布穩定版。先做跨工具重現。

來源：[README](https://github.com/google-labs-code/stitch-skills#readme)、[releases](https://github.com/google-labs-code/stitch-skills/releases)、[issues](https://github.com/google-labs-code/stitch-skills/issues)。

### 5. cursor/plugins — Watch

用途：Cursor 官方 plugins 與規格集合；README 展示 teaching、continual-learning、團隊工作流等範例。

動能與維護：見上表增星與相對成長；最近 push 2026-11-24T23:17:05Z；發布 latest release API 404，沒有可用發布資料。活動抽樣：[Skill authoring audit: suggested fixes for 1 skill](https://github.com/cursor/plugins/issues/1342)，open，最近更新 2026-11-25T11:45:10Z。

Adam／metabiz 關聯：適合 Adam 比較 Cursor、Claude Code、Codex 的 plugin/skill 封裝；know metabiz wiki 可建立主機能力對照。

風險與下一步：API 未回傳根目錄授權且 latest release 為 404，需逐項查閱 plugin 授權；近期 skill audit、程序清理與批准邊界議題顯示相容性仍需驗證。

來源：[README](https://github.com/cursor/plugins#readme)、[releases](https://github.com/cursor/plugins/releases)、[issues](https://github.com/cursor/plugins/issues)。

### 6. firecrawl/firecrawl — Deep research

用途：提供搜尋、擷取與網站資料存取的 agent 知識基礎設施；README 提供 API 與自架入口。

動能與維護：見上表增星與相對成長；最近 push 2026-11-25T13:29:58Z；發布 [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0)（2026-06-19T15:09:30Z）。活動抽樣：[perf(native): drop non-main-content tags in one document walk](https://github.com/firecrawl/firecrawl/pull/6070)，open，最近更新 2026-11-25T14:46:44Z。

Adam／metabiz 關聯：對 know metabiz wiki 的外部來源匯入、RAG 前處理與來源更新直接相關；Adam 可示範來源到可引用知識頁的流程。

風險與下一步：AGPL-3.0、自架維運、API 費用與擷取品質都需評估；近期內容清理效能 PR 仍不能視為已發版承諾。

來源：[README](https://github.com/firecrawl/firecrawl#readme)、[releases](https://github.com/firecrawl/firecrawl/releases)、[issues](https://github.com/firecrawl/firecrawl/issues)。

### 7. toeverything/AFFiNE — Watch

用途：將文件、白板與規劃整合的知識庫；README 主打 local-first 與隱私導向工作空間。

動能與維護：見上表增星與相對成長；最近 push 2026-11-25T16:22:05Z；發布 [v0.27.4](https://github.com/toeverything/AFFiNE/releases/tag/v0.27.4)（2026-08-18T16:51:39Z）。活動抽樣：[[Bug]: Mermaid flowchart text labels are not rendered; only empty diagram boxes are visible](https://github.com/toeverything/AFFiNE/issues/15861)，open，最近更新 2026-11-25T12:32:58Z。

Adam／metabiz 關聯：適合 Adam 比較辦公室知識協作工具；可作 know metabiz wiki 的介面與資料可攜性參考。

風險與下一步：授權 API 為 NOASSERTION，部署與商用前需查實際條款；現有 Mermaid 標籤渲染 bug 提醒匯入圖解需測試，尚未驗證取代現有 wiki。

來源：[README](https://github.com/toeverything/AFFiNE#readme)、[releases](https://github.com/toeverything/AFFiNE/releases)、[issues](https://github.com/toeverything/AFFiNE/issues)。

### 8. obra/superpowers — Reference only

用途：整理 agent 軟體開發的方法與 skills，README 涵蓋多主機安裝與規劃、執行、驗證流程。

動能與維護：見上表增星與相對成長；最近 push 2026-11-24T23:59:04Z；發布 [v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2)（2026-11-03T22:17:54Z）。活動抽樣：[fix(sdd,executing-plans): harden workspace claims, task-brief boundaries, review-package, and task-done](https://github.com/obra/superpowers/pull/2744)，open，最近更新 2026-11-25T15:34:41Z。

Adam／metabiz 關聯：供 Adam agent 課程的流程設計參考；know metabiz wiki 可整理可重複的需求、驗收與交接格式。

風險與下一步：總星最多但相對成長較低；近期 task boundary 與 adapter 修正仍在 PR 中。既有方法可作參考，導入成本與過度流程化需以實測判斷。

來源：[README](https://github.com/obra/superpowers#readme)、[releases](https://github.com/obra/superpowers/releases)、[issues](https://github.com/obra/superpowers/issues)。

## 範圍與明日觀察清單

Trending 卡片中的 nginx/nginx 與 Ghost-Downloader-3 不符合本次 AI／agent／開發自動化主題，排除於推薦。Claude-BugHunter 今日 +1,644 為高動能，但以資安攻防為主，與本次辦公室與知識工作內容適配較低；保留觀察，不因增星最高直接置頂。OpenVINO、minimind、opensre 等符合主題但未進入本次 8 項優先名單。

- CLI-Anything：追蹤 LibreOffice #714 合併與版本資訊，再設計文件副本 demo 的成功率／復原評估。
- diagram-design：追蹤今日 +1,133 能否延續；用同一份 MCP 架構內容評估文字正確、排版與 SVG 匯出。
- last30days-skill：追蹤 #1624／#1625；評估引用可回查率及每次研究成本，不把 PR 當成已交付功能。
- stitch-skills／cursor/plugins：追蹤 plugin 發布與主機相容性、授權及批准邊界議題，更新課程比較矩陣。
- firecrawl／AFFiNE：觀察來源擷取品質與 Mermaid 問題是否改善；先驗證知識匯入、引用與匯出，再評估 know metabiz wiki。
- Claude-BugHunter：只觀察 stars today、相對成長與維護回應是否持續，再判斷是否值得另做安全課程研究。

## 收集與限流狀態

未在收集器輸出偵測到 API 限流；使用 --limit 10。

## 完整性與資料品質註記

收集器原始取得 458 項，人工範圍核對排除 11 項，當日 repos.json／快照／report.md 最終保留 447 項（含 14 個 Trending 項目）；排除理由見 scope-exclusions.json，歷史資料未改動。遊戲作弊工具的 README 與 AI 描述不一致，未納入雷達。

收集器有 6 項 metadata API 404，沿用先前觀測；其中 1 項已因主題不符排除，剩餘 5 項只作歷史參考，並非今日有效更新：BarberNumber/Midjourney-Software、HunYiSage/dsh-purge、YuJunZhiXue/dsh-purge、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent。本次 8 項推薦不含這些沿用項目。punkpeye/awesome-mcp-servers 未取得 README 摘要，未納入推薦。
