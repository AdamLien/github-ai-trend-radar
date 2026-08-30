# GitHub AI 趨勢雷達分析

分析日期：2026-08-30（Asia/Taipei 前一個日曆日）  
資料快照：2026-08-31；共檢查 226 個候選，來源包含 GitHub Trending daily 與十組指定搜尋。

## 摘要

今日最值得追的是「把 agent 變成可教、可查、可重複工作的系統」：OpenMAIC 把多代理直接放進互動課堂，last30days-skill 把跨平台研究包成 skill，claude-obsidian 與 Graphify 則分別處理個人知識庫和程式／文件知識圖譜。這比單純追逐高星數更貼近 Adam 的課程、AI office automation 與 metabiz wiki 路線。

星數 delta 是相對前一快照的觀測值；「今日星數」只在 Trending daily 提供，不能把兩者直接相加，也不能視為市場購買意願。

## 值得保留的 8 個 repos

### 1. [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — Demo content

- **目的：**一鍵建立多代理互動課堂；最新 `v1.0.0` 於 2026-08-27 發布。
- **動能：**今日 +907 stars，為本次新進 Trending 中最強訊號；總 stars 23,425，當日更新。
- **風險：**新進項目的歷史 delta 尚未建立；課程內容、模型成本、部署穩定性仍需實測。
- **Adam 關聯：**可做「agent 如何共同備課／帶學習者」示範，延伸到 workshop、課程腳本生成與客戶教育自動化。

### 2. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) — Skill candidate

- **目的：**讓 agent 搜尋 Reddit、X、YouTube、HN、Polymarket 與 web，再產出有根據的主題摘要。
- **動能：**今日 +271 stars；總 stars 60,387，版本 `v3.21.1`，但最近 push 為 2026-08-26。
- **風險：**跨平台來源的 API、條款、可重現性與引用品質要逐一驗證；179 個 open issues 代表維護負擔不低。
- **Adam 關聯：**高度適合改造成每日 content radar、課程題材研究與 metabiz wiki 的「來源→摘要→待辦」流程；可與本 skill 的 GitHub 雷達互補。

### 3. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Demo content

- **目的：**Claude Code 將來源整理成使用者擁有的 Obsidian Markdown 知識圖譜，支援擷取、連結、 grounded retrieval 與 vault 維護。
- **動能：**總 stars 14,375、相對 delta +40；最近更新 2026-08-30，`v2.1.1` 於 2026-08-25 發布。
- **風險：**141 個 open issues；需要測試檔案結構遷移、權限邊界、引用正確性與長期 vault 維護。
- **Adam 關聯：**是「AI office automation + know metabiz wiki」最直觀的 demo 候選：展示資料不離開 Markdown、如何自動歸檔，以及如何從 wiki 產生課程素材。

### 4. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research

- **目的：**把 codebase、docs、SQL schema、config 與 PDF 轉成可查詢知識圖譜；主張以 deterministic AST parsing、可解釋 edge、無 vector store 為核心。
- **動能：**總 stars 112,535、delta +328；最近更新並發布 `v0.9.53`（2026-08-30）。
- **風險：**1,143 個 open issues；高星數不能取代對解析覆蓋率、增量更新、查詢品質與大型 repo 成本的驗證。
- **Adam 關聯：**可研究為 metabiz wiki 的程式／文件索引層，也能做「RAG 不一定等於向量資料庫」的深度內容與顧問型比較。

### 5. [anthropics/skills](https://github.com/anthropics/skills) — Reference only

- **目的：**Anthropic 的公開 Agent Skills 實作；以可動態載入的 instructions、scripts、resources 讓 agent 重複完成專門工作。
- **動能：**總 stars 172,596、delta +167；最近更新 2026-08-30，但最近 push 為 2026-08-21。
- **風險：**collector 未辨識到授權；1,189 個 open issues；應先確認條款與可再散布範圍，再借鑑結構。
- **Adam 關聯：**適合作為本 repo skills 設計的標準參照，尤其是文件產製、資料分析、wiki 整理與 AI office workflow 的可重用邊界。

### 6. [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) — Watch

- **目的：**把 Claude Code、Codex、Pi、OpenCode 等終端／IDE agent 接到免費模型與轉送服務。
- **動能：**總 stars 51,821、delta +474；最近更新與 push 均在 2026-08-30，為本次搜尋候選中很強的近期增長訊號。
- **風險：**365 個 open issues；「免費 token」與多 provider 轉送涉及服務可用性、隱私、供應商條款與金鑰安全，不能直接推薦給客戶生產使用。
- **Adam 關聯：**可觀察「低成本 agent 入口」的教學需求，但內容應聚焦威脅模型、成本透明與安全設定，而非免費承諾。

### 7. [53AI/53AIHub](https://github.com/53AI/53AIHub) — Watch

- **目的：**企業 AI portal／知識庫，管理知識、agents、prompts、AI tools，並整合 Coze、Dify、FastGPT、RAGFlow。
- **動能：**總 stars 4,636、delta +1；最近更新 2026-08-30，`v0.5.0` 於 2026-08-19 發布；相對增長弱於本日其他候選。
- **風險：**license 欄位為 `NOASSERTION`；需要核查雲端依賴、中文部署文件、資料隔離與整合維護成本。
- **Adam 關聯：**很貼近 metabiz wiki 與客戶 AI office portal，可作競品／架構觀察，不宜尚未實測就納入交付標準。

### 8. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — Reference only

- **目的：**MCP reference implementations 與社群 server 資源；README 明確提醒它不是完整 server 市集，正式清單應看 MCP Registry。
- **動能：**總 stars 89,968、delta +14；最近更新 2026-08-30，`2026.8.18` 於 2026-08-18 發布；目前更像穩定基礎設施而非爆發型標的。
- **風險：**license 欄位為 `NOASSERTION`；514 個 open issues；個別 server 的權限、資料外洩與供應鏈風險必須分開審查。
- **Adam 關聯：**適合課程中解釋 MCP 的邊界、server／client／registry 與 office automation 的連接方式；不應把 reference server 當成生產 ready 清單。

## 明日 watchlist

1. **追 OpenMAIC 的第二日留存：**記錄 stars delta、issue／PR、文件與 demo 是否持續更新，並實測一個「課程大綱→互動課堂」流程。
2. **追 last30days-skill 的來源品質：**抽查同一題在 Reddit、YouTube、HN 與 web 的引用、時間戳和衝突處理，評估是否能成為 content radar 的研究模組。
3. **追 Graphify 與 claude-obsidian 的可合併工作流：**以一份 metabiz wiki 輸入測試「檔案擁有權→索引→回答→回寫」全鏈路。
4. **追 agent skills 生態：**比較 `anthropics/skills`、`mattpocock/skills`、`addyosmani/agent-skills` 的目錄規範、授權與跨 Codex／Claude Code 相容性。
5. **追安全與成本：**對 free-claude-code、MCP servers、OmniRoute 等多 provider／工具轉送方案做金鑰、資料路由、ToS、失效切換與每月成本檢查。
6. **保持訊號衛生：**明日沿用同十組 query 與 `--include-trending-daily`，分開記錄今日 stars、snapshot delta、release、push 與 issue activity；不要按總 stars 單一排序。

## 判讀限制

本報告的 GitHub stars、Trending 與 repository metadata 是開發者注意力訊號，不等於市場需求、商業成熟度或 Adam 客戶的購買意願。授權為空或 `NOASSERTION` 的專案，在完成法律與安全檢查前只作參考。
