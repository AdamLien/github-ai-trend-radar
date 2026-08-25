# GitHub AI Trend Radar｜2026-08-24（台灣）

## 摘要

本次以 GitHub API 的十組查詢與執行時的 Daily Trending 合併蒐集，共保留 204 個去重候選。排序採用相鄰快照的 stars delta、Trending 當日星數、最近推送／release、README 定位與導入摩擦，而非總 stars 單一排序。`openai/codex` 的 +1,921（Trending 1,994）仍是開發者自動化最強訊號；同時，skills 的可攜格式、可稽核的 agent workspace，以及知識／記憶層是本日最值得驗證的三條主線。

> 資料品質註記：本機沒有 `GITHUB_TOKEN`。第一次以 `--limit 10` 執行時，在部分 repo metadata 階段收到 GitHub API 403 rate limit 與 429 abuse limit；collector 依既有設計保留可用的前次 metadata 並寫出 `repos.json`、`report.md` 與 snapshot。依規則改以 `--limit 5` 重跑後，搜尋端點立即回 429，故本次為「受 rate limit 限制的完整產物」，不是全新即時排行。首次觀測或未重新抓取的 repo，`stars_delta: 0` 代表「未量測」，不是零成長。

## 優先名單

|分類|專案與動能|用途與適用性|風險／判讀|
|---|---|---|---|
|Deep research|[openai/codex](https://github.com/openai/codex) — 116,841 stars；+1,921；Trending 1,994；8/24 release `0.149.1`|終端 coding agent 的真實工作流與權限界線。可作 Adam 的 coding-agent 課程基準，也可反推 AI 辦公室任務如何切小、驗證與交接。|13,654 open issues 代表採用者廣、但也要嚴格鎖定版本與驗收場景；不可把本地測試等同生產自動化。|
|Skill candidate|[mattpocock/skills](https://github.com/mattpocock/skills) — 235,038；+1,594；8/24 更新|以工程實務把可重複提示／流程封裝為 skill。適合比對現有 Codex skill 的內容邊界，挑選「文件驗證、資料檢查、交接」等可重用結構。|MIT，但 391 open issues；不宜整包啟用，須逐項審查工具權限與是否衝突既有 RTK／人工核准規則。|
|Deep research|[stablyai/orca](https://github.com/stablyai/orca) — 52,622；+968；8/22 release `v1.4.188`|平行 coding agents 的 ADE；可做多 agent 分工／觀測／收斂的課程 demo，亦是 AI 辦公室複雜研究任務的候選編排介面。|MIT，但 4,473 open issues；先以隔離、無機密的 repo 做 POC，確認成本、權限與交接紀錄。|
|Deep research|[volcengine/OpenViking](https://github.com/volcengine/OpenViking) — 32,874；+501；8/21 release `v0.4.16`|把 agent memory、RAG 與 skills 統一為 context database。最直接對應 know metabiz wiki 的檢索／來源追溯設計。|AGPL-3.0 與 513 open issues；企業內部／對外服務的授權義務、資料落點與可刪除性要先法務確認。|
|Skill candidate|[virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) — 25,126；+682；8/10 release `v1.4.0`|把技術書 PDF 轉為 Claude Code skill；可做「教材→可驗證工作卡」的課程示範，也可探索知識庫攝取前的結構化步驟。|MIT、23 open issues；來源版權、PDF 品質、引用範圍及產出的事實核驗不可省略，不能直接把轉換結果當作企業知識。|
|Demo content|[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — 31,715；+602；Trending 602；8/24 更新|跨 Claude Code、Codex、Cursor 的 skills 目錄，適合做「如何辨識可移植 skill 與危險自動化」的內容選題。|MIT，集合型專案不等於所有條目安全；以來源、授權、網路／檔案權限逐件篩選。|
|Watch|[apache/maka](https://github.com/apache/maka) — 2,753；+517；Trending 411；8/18 release `v0.1.11`|local-first agent workspace，將 model／tool／permission decisions 留為 append-only log；值得研究作為 AI 辦公室可稽核執行層。|Apache-2.0，但仍是 incubating、248 open issues；先評估日誌是否含敏感 prompt／個資及 retention。|
|Demo content|[freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) — 15,193；+2,631；Trending 2,449|本日最快成長訊號；可做「Prompt as Code＋skill 模板」視覺內容 demo，連結到教材與提案素材產製。|MIT、12 open issues；案例與生成資產的來源／商用權利須另行驗證，熱度不等於企業可採用性。|
|Reference only|[anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) — 1,249；+445；Trending 490|Claude Cowork／Claude Code plugin marketplace 的生態訊號，可追蹤封裝和提交規格。|Apache-2.0，但 README 明示為 read-only mirror、40 open issues；以官方提交入口為準，不作直接整合依據。|
|Watch|[openclaw/openclaw](https://github.com/openclaw/openclaw) — 387,356；Trending 160；首次觀測|個人跨平台 AI assistant，可作 agent 個人化與通訊整合的參考。|首次量測，成長未知；`NOASSERTION` 授權、5,857 open issues，且涉及個人資料與外部 action，暫不列為採用候選。|

## 對 Adam 的可用行動

- **課程**：用 Codex + Orca 做一組「單 agent 與平行 agent 的同一任務」實驗；成功標準包含來源、測試、人工核准點與可重現交接，不以一次跑成功為準。
- **內容**：製作「Skill 不是 prompt 收藏：如何審查權限、可驗證性與資料邊界」；以 `mattpocock/skills`、VoltAgent 目錄與 `book-to-skill` 各示範一個正反案例。
- **AI 辦公室自動化**：研究 Maka 的 append-only permission log，對照現有 mCRM 的 stage → human approval → execution/audit；先只做 read-only 流程。
- **know metabiz wiki**：以 OpenViking 做離線 POC 設計，不直接導入：比較來源引用、chunk／memory 隔離、刪除要求、AGPL 義務與成本；以一份無敏感資料的已公開文件集驗收。

## 明日追蹤清單

1. 重新量測 5 個首次 Trending 專案，將第一個可比較的 stars delta 明確標為「自首次觀測以來」。
2. 檢查 Codex、Orca、OpenViking、Maka 的 release／issue 是否出現權限、資料外洩或重大相容性議題。
3. 從 skills 目錄挑 1 個 read-only、可測試流程，確認授權與本地規則後再製作最小 skill POC。
4. 對 `book-to-skill` 以可公開教材做一次人工抽樣比對：頁碼、引用、遺漏段落與不應被自動化的版權內容。
5. 在下一輪前提供 `GITHUB_TOKEN`；未驗證 API 已觸發 abuse limit，應先等 GitHub 限流解除，再以 limit 5 重新測量本日候選。
