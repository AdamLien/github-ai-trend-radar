# GitHub AI 趨勢雷達分析

日期：2026-09-03（Asia/Taipei）

## 今日摘要

本次從 10 組關鍵字與 GitHub Trending daily 收集 244 個候選 repository。今日訊號最明顯的不是單純「誰的星星最多」，而是 agent skill 正在從零散 prompt 走向可安裝、可重複驗證的工作流；同時 MCP、瀏覽器控制、知識庫與多代理教學場景正快速靠攏。下列 8 個項目兼顧 stars_delta、今日 stars、最近更新、release、README 可理解度與維護風險。

## 值得追蹤的 repositories

### 1. [mattpocock/skills](https://github.com/mattpocock/skills)

- **用途：** 將真實工程工作的 agent skills 整理成可重用目錄，README 明確定位為日常工程技能集合。
- **動能：** 246,670 stars；snapshot 增加 1,796，今日 Trending 約 1,576 stars；2026-09-03 更新並有 `v1.2.3` release。這是本日最強的 skill 生態訊號之一。
- **風險：** MIT、文件清楚，但 454 個 open issues 代表規模大、採用前仍需確認每個 skill 的品質與相容性。
- **分類：** **Skill candidate**
- **對 Adam／metabiz 的關聯：** 可作為 Adam 課程中「把個人做事方法產品化為 skill」的核心案例，也適合對照本 workspace 的 PDF、影片、wiki 與報價流程，找出可抽象的 AI office automation 模式。

### 2. [affaan-m/ECC](https://github.com/affaan-m/ECC)

- **用途：** 為 Claude Code、Codex、Cursor 等 coding agent 提供 skills、記憶、安全與研究優先的 agent harness 方法。
- **動能：** 246,862 stars；snapshot +762、今日 Trending 約 +749；2026-09-03 更新，`v2.2.0` release，README 直接展示跨 agent 使用情境。
- **風險：** MIT 且成熟度高，但 138 個 open issues、功能面很廣；「harness 改善」的效果需要以可重現任務測試，不宜只看宣稱。
- **分類：** **Deep research**
- **對 Adam／metabiz 的關聯：** 適合研究成「AI 辦公室作業系統」課程單元：如何把研究、審查、記憶、安全與交付串成可衡量的工作流程，並回饋 know metabiz wiki 的 skill 設計。

### 3. [obra/superpowers](https://github.com/obra/superpowers)

- **用途：** 以可組合 skills 和明確軟體開發方法，讓 coding agents 遵循 brainstorming、規劃、實作與驗證流程。
- **動能：** 281,196 stars；snapshot +445、今日 Trending 約 +470；2026-09-03 更新，`v6.3.0` release，且 README 列出 Claude、Codex、Cursor 等多個入口。
- **風險：** MIT；354 個 open issues，方法論可能增加流程成本，應以小型 metabiz 任務比較「有／無 workflow」的交付品質與時間。
- **分類：** **Deep research**
- **對 Adam／metabiz 的關聯：** 很適合做課程 demo：同一個內容企劃或 wiki 整理任務，展示 agent 是否先澄清需求、拆解、驗證與交付；也可作為 Hermes handoff 的流程參考。

### 4. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

- **用途：** 以 MCP server 讓 coding agent 控制與檢查 live Chrome，執行瀏覽器自動化、除錯與效能分析。
- **動能：** 50,820 stars；snapshot +276；2026-09-03 更新，Apache-2.0，README 有 npm、CLI、tool reference 與 troubleshooting 入口。
- **風險：** 需要瀏覽器權限與本機環境整合；MCP 工具若授權過寬，可能造成誤操作或資料外洩，demo 應使用測試站與最小權限。
- **分類：** **Demo content**
- **對 Adam／metabiz 的關聯：** 可示範 AI office automation 的「觀察—操作—驗證」閉環，例如檢查網站表單、測試課程 landing page、產出可重現的瀏覽器 QA 報告。

### 5. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)

- **用途：** 讓 Claude Code 把來源整理成由 Markdown 擁有的 Obsidian 連結知識圖譜，涵蓋擷取、連結、檢索與 vault 維護。
- **動能：** 14,588 stars；snapshot +35；2026-09-03 更新，最近 release `v2.1.1`；README 有 MIT badge、Agent Skills 相容性與清楚的 second-brain 定位。
- **風險：** 目前 star delta 小於前述 coding-agent 項目，且 140 個 open issues；知識圖譜的自動連結仍需人工抽查，避免錯誤關聯污染 wiki。
- **分類：** **Demo content**
- **對 Adam／metabiz 的關聯：** 與 know metabiz wiki 直接相關，可做「來源 → 原子筆記 → 關聯 → grounded answer」示範，並研究哪些規則應沉澱成 workspace skill。

### 6. [53AI/53AIHub](https://github.com/53AI/53AIHub)

- **用途：** 開源 AI portal／企業知識庫，集中管理知識、agents、prompts 與 AI 工具，並串接 Coze、Dify、FastGPT、RAGFlow。
- **動能：** 4,640 stars；snapshot +0，但 2026-09-03 有更新與 `v0.5.1` release；搜尋命中與整合面顯示其中文企業 AI 知識入口定位值得觀察。
- **風險：** license 顯示 `NOASSERTION`，且只有 21 個 open issues 不代表治理完整；雲端服務、部署文件與各整合的維護責任需先查清楚。
- **分類：** **Watch**
- **對 Adam／metabiz 的關聯：** 可作為 metabiz wiki 與 AI office automation 的產品形態參考，特別是「知識、prompt、agent、工具」同一入口；不宜在 license 釐清前直接採用。

### 7. [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)

- **用途：** 一鍵啟動多代理互動教室，讓學習者以沉浸式方式與多個 agent 協作學習。
- **動能：** 30,963 stars；snapshot +577；2026-09-03 更新並有 `v1.0.0` release，MIT，README 提供中英文使用指南入口。
- **風險：** 226 個 open issues，且多代理教學效果可能高度依賴模型、prompt 與課程設計；要用實際學習任務驗證，而非把互動感當成學習成效。
- **分類：** **Deep research**
- **對 Adam／metabiz 的關聯：** 可研究成 AI 課程的互動式模組：同一主題由研究員、教練、審稿員與實作 agent 分工，再接到課程作業與 wiki 知識沉澱。

### 8. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

- **用途：** 將 research → write → review → revise → finalize 變成 Claude Code skills，README 同時提供繁體中文入口。
- **動能：** 45,914 stars；snapshot +467、今日 Trending 約 +498；2026-09-03 更新，`v3.21.1` release，18 個 open issues，維護訊號相對集中。
- **風險：** repository license 欄為 `NOASSERTION`，README 顯示 CC BY-NC 4.0，商業課程或 metabiz 內部改作前必須確認授權範圍；學術引用與查證仍需人工把關。
- **分類：** **Skill candidate**
- **對 Adam／metabiz 的關聯：** 可拆出「研究型內容生產」課程案例，並借鏡其階段化流程來強化 know metabiz wiki 的來源查證、內容審稿與版本化。

## 明日 watchlist

明天優先重查以下項目與訊號：

1. `mattpocock/skills`、`affaan-m/ECC`、`obra/superpowers`：確認今日高 star delta 是否延續，並比較新增 skill、release 與 issue 變化。
2. `ChromeDevTools/chrome-devtools-mcp`：追蹤 MCP 工具權限、安裝相容性、release/changelog 與實際 browser QA demo 可行性。
3. `AgriciDaniel/claude-obsidian`、`53AI/53AIHub`：確認知識庫匯入、權限、資料擁有權、license 與中文部署文件是否成熟。
4. `THU-MAIC/OpenMAIC`、`Imbad0202/academic-research-skills`：觀察課程／研究 workflow 是否有新版本、案例與可重現評估；先處理後者的商業授權疑問。
5. 新進 Trending 項目 `ByteByteGoHq/system-design-101` 與 `magnitudedev/magnitude`：確認是否持續進入本雷達，避免只因單日曝光就過早採用。

## 使用判讀

stars 與 star delta 代表開發者注意力，不等於產品需求、教學成效或商業採購意願。任何導入 metabiz workflow 的決定，仍需補做 license、資料安全、安裝摩擦、維護者回應與小型任務驗證。
