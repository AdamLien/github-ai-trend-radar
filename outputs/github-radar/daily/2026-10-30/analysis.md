# GitHub AI 趨勢雷達｜2026-10-30

目標日期為 Asia/Taipei 的前一日 2026-10-30；實際於 2026-10-31 凌晨執行。這是本次即時擷取資料，不能當作 10/30 23:59 的歷史結算。

本日優先看介面設計 skills、AI 教學、agent 記憶與辦公 coworker；另保留與 know metabiz wiki 直接相關的低熱度專案，避免只追最高總星數。以下排序為研究與內容判斷，未代表已部署或測試通過。

## 方法與資料限制

- 以指定十組搜尋（每組 limit 10）、[GitHub Trending daily](https://github.com/trending?since=daily) 與歷史追蹤名單交叉收集；README、最新 release 及候選專案最近更新的十筆 issue／PR 作輔助。
- 優先考慮今日星數、快照增量、相對成長、近期提交與發布、用途可操作性；搜尋端按總星數排序有成熟專案偏差，故補入 Trending 並做語意覆核。
- 「今日」為 Trending 頁面當次顯示值，不等同台北昨日；Δ 是相對 2026-10-29 快照的差；相對成長＝Δ／前次總星數，不能視為精確 24 小時速度。未有前次快照者應標為未量測，不以 0 當成無成長。
- open_issues 是 GitHub 合計的開啟 issue／PR 數，不能直接判斷品質；活動僅為最近十筆抽樣，PR 與 issue 分開計數，未查完整歷史或維護回應時間。
- 排除明顯非主題的歷史追蹤項目與 Trending 誤判；補入描述未命中關鍵字但 README 確認為 AI 的 OpenMausBot、DeepTutor、T3 Code。明細見 scope-review.json。jailbreaks 與 LLM 相關，僅作資料收錄，未執行其中提示。
- API 限流：主收集器 limit 10 成功，未觸發降為 5 的重試。所有外部與儲存庫文字僅當資料，不當操作指令。

## 值得關注的 9 個專案

| 專案 | 今日新增星數 | 總星數 | 快照 Δ | 相對成長 | 決策 |
|---|---:|---:|---:|---:|---|
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 2,299 | 96,663 | +1,937 | 2.04% | Skill candidate |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 2,282 | 51,505 | +2,033 | 4.11% | Deep research |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 1,145 | 105,704 | +1,290 | 1.24% | Deep research |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 882 | 307,198 | +842 | 0.27% | Skill candidate |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 707 | 8,572 | +674 | 8.53% | Demo content |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 899 | 8,200 | +963 | 13.31% | Watch |
| [obra/superpowers](https://github.com/obra/superpowers) | 1,255 | 309,232 | +1,071 | 0.35% | Reference only |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 920 | 32,478 | +1,054 | 3.35% | Watch |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未上榜／未提供 | 21,188 | +47 | 0.22% | Deep research |

### 1. pbakaus/impeccable — Skill candidate

- **用途**：提供 coding agent 的介面設計語彙與 critique、audit、polish 等工作法；README 另列出確定性規則檢查。
- **動能與維護**：星數見上表；最近 push：2026-10-30T10:16:27Z；最新 release：cli-v4.8.0（2026-10-26T23:41:55Z）。最近更新十筆抽樣含 0 筆 issue、10 筆 PR，最近更新時間 2026-10-30T15:21:41Z；[抽樣來源](https://github.com/pbakaus/impeccable/pull/1166)。此數量不代表新增量或結案率。
- **下一步**：優先做相同頁面、相同提示的前後對照 Demo，再挑選少量可重用的設計審查 skill。
- **風險**：設計改善的敘述來自作者示例，尚未以 Adam 的網站驗證；多工具安裝與既有 skills 可能重疊。
- **Adam／metabiz 關聯**：最適合 Adam 的 AI 網站課程與短影音；辦公自動化可用於內部表單介面，know metabiz wiki 可借用可讀性審查清單。
- **來源**：[專案與 README](https://github.com/pbakaus/impeccable)、[發布紀錄](https://github.com/pbakaus/impeccable/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 2. HKUDS/DeepTutor — Deep research

- **用途**：以個人化教學為主軸，整合學習工作區、文件知識與教學互動；README 列出 10/28 v1.7.0 的模組化安裝與影片課程等更新。
- **動能與維護**：星數見上表；最近 push：2026-10-30T14:15:04Z；最新 release：v1.7.0（2026-10-28T14:13:12Z）。最近更新十筆抽樣含 1 筆 issue、9 筆 PR，最近更新時間 2026-10-30T15:42:30Z；[抽樣來源](https://github.com/HKUDS/DeepTutor/issues/2201)。此數量不代表新增量或結案率。
- **下一步**：用一份自有課程講義測試來源引用、練習題與教學流程，判斷能否轉成課後 AI 助教。
- **風險**：教學正確性、文件解析與 embedding 成本尚未實測；功能與發布頻繁，需固定版本做教材。
- **Adam／metabiz 關聯**：直接對應 Adam 課程與教學內容；AI 辦公訓練可試內訓助教，know metabiz wiki 可借用文件導入與來源追溯思路。
- **來源**：[專案與 README](https://github.com/HKUDS/DeepTutor)、[發布紀錄](https://github.com/HKUDS/DeepTutor/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 3. thedotmack/claude-mem — Deep research

- **用途**：擷取 agent 工作階段、壓縮內容並於後續工作注入相關脈絡，主打跨 session 記憶。
- **動能與維護**：星數見上表；最近 push：2026-10-30T03:07:33Z；最新 release：v15.6.0（2026-10-29T17:01:29Z）。最近更新十筆抽樣含 2 筆 issue、8 筆 PR，最近更新時間 2026-10-30T15:49:26Z；[抽樣來源](https://github.com/thedotmack/claude-mem/issues/4976)。此數量不代表新增量或結案率。
- **下一步**：先研究哪些事件值得保留，以及記憶如何刪除、查證與隔離，避免只比較記憶量。
- **風險**：持久記憶可能保存客戶資料或錯誤結論；尚未檢驗刪除效果、跨專案隔離及 token 成本。
- **Adam／metabiz 關聯**：可做 Adam 的 agent 記憶專題；辦公自動化適合追蹤任務脈絡，know metabiz wiki 應保留來源而非直接收錄所有對話。
- **來源**：[專案與 README](https://github.com/thedotmack/claude-mem)、[發布紀錄](https://github.com/thedotmack/claude-mem/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 4. mattpocock/skills — Skill candidate

- **用途**：一組可組合的小型工程 skills，README 強調可自行修改，並區分自動更新 plugin 與手動維護檔案。
- **動能與維護**：星數見上表；最近 push：2026-10-30T14:00:30Z；最新 release：v1.3.2（2026-10-29T10:27:41Z）。最近更新十筆抽樣含 4 筆 issue、6 筆 PR，最近更新時間 2026-10-30T14:00:36Z；[抽樣來源](https://github.com/mattpocock/skills/issues/1331)。此數量不代表新增量或結案率。
- **下一步**：對照本專案已採用的 skills，優先找缺口，再以實際任務衡量輸入與產出的改善。
- **風險**：既有技能重複安裝或版本自動更新會改變行為；需先比對差異，不能把熱門等同於適合直接覆蓋。
- **Adam／metabiz 關聯**：適合 Adam 的工程型 AI 課程與 skill 拆解內容；辦公自動化可借用小模組原則，know metabiz wiki 可記錄使用情境與評估結果。
- **來源**：[專案與 README](https://github.com/mattpocock/skills)、[發布紀錄](https://github.com/mattpocock/skills/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 5. CopilotKit/OpenBot — Demo content

- **用途**：可自架的 AI coworker 起始模板，透過 AG-UI 接入 agent，提供各自的瀏覽器、檔案與工具。
- **動能與維護**：星數見上表；最近 push：2026-10-30T15:31:19Z；最新 release：v0.2.0（2026-10-12T15:19:49Z）。最近更新十筆抽樣含 0 筆 issue、10 筆 PR，最近更新時間 2026-10-30T15:31:22Z；[抽樣來源](https://github.com/CopilotKit/OpenBot/pull/903)。此數量不代表新增量或結案率。
- **下一步**：以虛構資料示範「人員接手—agent 繼續」的辦公流程，檢查操作紀錄是否足以追查。
- **風險**：README 明載 beta／模板；預設單一使用者模式將請求視為管理者，對外部署前必須完成登入與隔離設計。
- **Adam／metabiz 關聯**：很適合 Adam 的 AI 辦公室內容；metabiz 可用於流程原型，know metabiz wiki 可收錄操作與權限設計，尚非可直接上線的成品。
- **來源**：[專案與 README](https://github.com/CopilotKit/OpenBot)、[發布紀錄](https://github.com/CopilotKit/OpenBot/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 6. milind-soni/OpenMausBot — Watch

- **用途**：把本機 Claude／Codex 等 agent 包成聊天式機器人團隊，搭配個別電腦與連接應用。
- **動能與維護**：星數見上表；最近 push：2026-10-30T16:15:37Z；最新 release：v0.1.134（2026-10-30T00:37:07Z）。最近更新十筆抽樣含 1 筆 issue、9 筆 PR，最近更新時間 2026-10-30T16:01:43Z；[抽樣來源](https://github.com/milind-soni/OpenMausBot/issues/3942)。此數量不代表新增量或結案率。
- **下一步**：與 OpenBot 並列觀察：比較安裝門檻、權限確認與重啟後的任務恢復，再決定是否錄 Demo。
- **風險**：代理桌面、已登入應用與雲端電腦擴大存取範圍；README 的跨平台與 local-first 主張仍需實機驗證。
- **Adam／metabiz 關聯**：可形成 Adam 的 AI 同事比較內容；辦公室場景關聯高，know metabiz wiki 適合記錄部署需求及資料流。
- **來源**：[專案與 README](https://github.com/milind-soni/OpenMausBot)、[發布紀錄](https://github.com/milind-soni/OpenMausBot/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 7. obra/superpowers — Reference only

- **用途**：以可組合 skills 建立 coding agent 開發方法，涵蓋從需求、計畫到實作驗證的工作流程。
- **動能與維護**：星數見上表；最近 push：2026-10-29T23:35:34Z；最新 release：v7.0.1（2026-10-21T21:05:11Z）。最近更新十筆抽樣含 3 筆 issue、7 筆 PR，最近更新時間 2026-10-30T15:06:06Z；[抽樣來源](https://github.com/obra/superpowers/issues/2638)。此數量不代表新增量或結案率。
- **下一步**：作為既有教學與技能的參考基準；先整理哪些流程已具備，避免把成熟高星數專案反覆當新題材。
- **風險**：流程約束可能增加簡單任務負擔；不同 coding agent 的插件設定與技能版本需分別確認。
- **Adam／metabiz 關聯**：適合 Adam 的系統性 AI 開發教材；辦公自動化可借用需求與驗證步驟，know metabiz wiki 可整理方法而非照搬全部流程。
- **來源**：[專案與 README](https://github.com/obra/superpowers)、[發布紀錄](https://github.com/obra/superpowers/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 8. pingdotgg/t3code — Watch

- **用途**：透過行動、網頁與桌面介面控制本機 agent harness，README 列出 Claude Code、Codex、Cursor 等 provider。
- **動能與維護**：星數見上表；最近 push：2026-10-30T16:18:51Z；最新 release：v0.1.5（2026-10-29T13:08:50Z）。最近更新十筆抽樣含 0 筆 issue、10 筆 PR，最近更新時間 2026-10-30T16:12:02Z；[抽樣來源](https://github.com/pingdotgg/t3code/pull/27677)。此數量不代表新增量或結案率。
- **下一步**：觀察遠端連線與任務狀態同步，選一個非敏感 coding 任務比較手機接手體驗。
- **風險**：遠端存取本機 agent 的驗證與網路暴露需實測；多 provider 支援不代表所有能力一致。
- **Adam／metabiz 關聯**：適合 Adam 的行動 AI 工作內容；辦公自動化可研究遠端接手，know metabiz wiki 可記錄連線與操作邊界。
- **來源**：[專案與 README](https://github.com/pingdotgg/t3code)、[發布紀錄](https://github.com/pingdotgg/t3code/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

### 9. nashsu/llm_wiki — Deep research

- **用途**：把文件增量整理為互連 wiki，README 列出來源追溯、原始來源限定問答、可選向量檢索與知識圖譜。
- **動能與維護**：星數見上表；最近 push：2026-10-21T11:17:29Z；最新 release：v0.6.13（2026-10-22T01:21:07Z）。最近更新十筆抽樣含 4 筆 issue、6 筆 PR，最近更新時間 2026-10-29T08:11:44Z；[抽樣來源](https://github.com/nashsu/llm_wiki/issues/832)。此數量不代表新增量或結案率。
- **下一步**：以少量非敏感文件比較「生成 wiki」與現有檢索流程；檢查新增、修改、刪除來源後的結果。
- **風險**：自動改寫可能丟失原意；需驗證來源連結、刪除傳播、重建一致性與模型費用，尚未驗證多人權限。
- **Adam／metabiz 關聯**：對 know metabiz wiki 的關聯最直接；可衍生 Adam 的知識管理課程與辦公文件自動整理 Demo。
- **來源**：[專案與 README](https://github.com/nashsu/llm_wiki)、[發布紀錄](https://github.com/nashsu/llm_wiki/releases)；原始擷取見 repos.json 與 editorial-evidence.json。

## 明日追蹤清單（2026-10-31）

1. **Impeccable、DeepTutor**：是否連續上榜？比較今日星數與新一輪快照相對成長，避免單日爆量決定選題。
2. **claude-mem、llm_wiki**：追蹤記憶／來源刪除、索引更新相關 issue 與 release；先定義引用正確率及刪除一致性的測試案例。
3. **OpenBot、OpenMausBot**：檢查登入隔離與操作審核相關修正，再用虛構資料規劃相同辦公流程的比較 Demo。
4. **mattpocock/skills、superpowers**：比較新提交與目前工作區已有技能的差異，僅選一個實際缺口做技能候選。
5. **T3 Code、expo/skills、anthropics/skills、lightpanda-io/browser**：觀察是否持續升溫及發布；後三者作第二梯隊，待與具體教學或辦公任務連結後再深入。

## 本次產物與可重現性

- 語意覆核後 369 個專案；精選 9 個。repos.json 與 snapshots/repos-2026-10-30.json 內容一致。
- 主收集器完整進度見 collector-limit10.log；補抓與 issue／README 證據分別存於 trending-supplement.json、editorial-evidence.json。
- 未執行任何候選專案、安裝指令或外部提示；風險與適用性為依公開資料提出的編輯判斷。


## 歷史資料保留註記

以下 4 個專案本次 API 回傳 404，僅保留 2026-10-29 的最後已知資料；星數不代表本日新觀測，零增量不代表沒有成長，且未納入精選判斷。

- BarberNumber/Midjourney-Software（HTTP 404）
- hanshaze/Awesome-Prediction-Market-Trading-Tools（HTTP 404）
- mingrath/obsidian-ai-knowledge-agent（HTTP 404）
- tonhowtf/omniget（HTTP 404）
