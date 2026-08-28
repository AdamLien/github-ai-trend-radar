# GitHub AI 趨勢雷達分析（2026-08-28）

## 今日摘要

本次以 GitHub Trending daily 與指定的 10 組搜尋詞交叉收集，保留 AI、MCP、Skills、coding agent、LLM、RAG、知識庫與開發者自動化相關專案。判讀優先順序是今日 Trending 星數、相對前次 snapshot 的 star delta、近期更新/發布、README 可操作性與 issue 活躍度；總 stars 只作規模背景，不作單一排名依據。

今日最強訊號是 agent skill 正在從「提示詞集合」走向可驗證的工作流：Archify 把架構圖生成變成可重複的 agent skill，Scientific Agent Skills 將技能庫與資料庫打包，book-to-skill 則直接把文件轉成可使用的 skill。另一條主線是 Claude Code / MCP 的正式化與瀏覽器自動化：Anthropic 官方 plugins directory 與 Chrome DevTools MCP 都有明顯的當日關注度。

## 值得保留的 repos

| Repo | 用途與訊號 | 總 stars / 動能 | 風險 | 判定 | 對 Adam / metabiz 的價值 |
| --- | --- | ---: | --- | --- | --- |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 將 codebase 或系統描述轉成可驗證、可匯出的互動式架構/流程圖；README 明列 Cursor、Claude Code、Codex CLI、OpenCode。 | 26,316；今日 +4,561 Trending，snapshot +4,240；8/28 更新，v2.15.0。 | 增長非常快，需確認輸出驗證品質、相依服務與長期維護；MIT 是正面訊號。 | Deep research | 可做「AI 產系統圖」課程 demo，也適合示範把複雜專案轉成 metabiz wiki 的架構頁與 onboarding 素材。 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 163 個科學 agent skills、100+ 資料庫，支援 Cursor、Claude Code、Codex 與 Agent Skills 標準。 | 36,104；今日 +720，snapshot +964；8/28 更新，v2.64.0，13 open issues。 | 領域範圍很深，資料庫/外部服務與科學結果的正確性需個別驗證；MIT。 | Skill candidate | 可作為「把專業 SOP 封裝成 skill」的教材範本，啟發 metabiz 內部的報價、知識整理與研究 skill 分層。 |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 以教學/參考手冊方式涵蓋 agent、LLM、MCP、深度學習與從零實作，並有多語 README。 | 50,515；今日 +703，snapshot +523；近期 release v2026.08，98 open issues。 | 教學型 repo 的內容更新速度與正確性要持續抽查；MIT。 | Deep research | 適合拆成 Adam 課程的模組地圖、讀書會與「從概念到可部署 AI office automation」的學習路徑；也可作內容選題對照。 |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Anthropic 維護的 Claude Code plugin directory，含官方與第三方 plugins。 | 34,911；今日 +457，snapshot +342；8/28 更新，1,050 open issues。 | README 明確警告需信任檢查；第三方 plugin 可能執行 MCP/檔案/軟體操作，供應鏈與權限風險高。Apache-2.0。 | Watch | 可做「Claude Code plugin 生態」與安全審核內容；對 metabiz wiki 的 skill/plugin 採購清單很有參考價值，但不宜直接全量採用。 |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | MCP server 讓 coding agent 控制/檢查 live Chrome，支援除錯、效能分析與可靠瀏覽器自動化。 | 49,907；今日 +61；8/28 更新，v1.8.0，94 open issues。 | 需要瀏覽器與本機權限，測試環境/版本相容性與資料外洩邊界要先定義；Apache-2.0。 | Demo content | 很適合示範「AI office automation 的瀏覽器驗證迴圈」：agent 操作、DevTools 觀測、截圖/效能證據回寫 wiki。 |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 以 Claude Code + Obsidian 建立自組織 Markdown second brain、連結圖與 grounded retrieval。 | 14,282；snapshot +468；8/28 更新前一日 push，v2.1.1，141 open issues。 | 知識圖譜整理規則可能造成錯誤連結或 metadata 污染；需評估 vault 備份、權限與 Claude 依賴；MIT。 | Deep research | 與 metabiz wiki、LLM wiki、研究筆記和 Adam 的 know-how 沉澱高度相關，可做「可擁有的 AI 知識庫」實作研究。 |
| [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 把技術書 PDF、文件資料夾或來源集合轉成可供 Claude Code / Copilot CLI 使用的 agent skill。 | 26,582；snapshot +464；8/28 更新與 push，v1.4.0，22 open issues。 | PDF 解析、版權、引用可追溯性與過度壓縮知識是主要風險；MIT。 | Skill candidate | 直接對應 Adam 的課程教材轉 skill、PDF ingestion 與企業 SOP 封裝，亦可作 metabiz wiki 匯入管線的比較基準。 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 高規模、以實際工程工作流為導向的 agent skills 集合。 | 239,962；snapshot +1,174；8/28 更新，v1.2.3，434 open issues。 | 總量與知名度很高但不代表每個 skill 都適合生產；需逐項審核 prompt、工具權限、license 與與本地流程的衝突；MIT。 | Reference only | 可作 skill 架構、命名與內容品質的參考庫，協助設計 Adam 課程的 skill pattern；目前不應只因 stars 高就整庫導入。 |

## 與 Adam 工作的轉譯

- 課程/內容：以 Archify、Chrome DevTools MCP、book-to-skill 組成一條「描述系統 → 產生 skill → 用瀏覽器驗證」的可錄製 demo；以 ai-engineering-from-scratch 做課程章節索引。
- AI office automation：優先研究 Chrome DevTools MCP 的權限邊界與可觀測性，將每次自動化執行留下截圖、log、結果摘要，再回寫 wiki。
- know metabiz wiki：先用 claude-obsidian 的 Markdown-first 思路建立來源、摘要、連結與驗證狀態，再決定是否導入圖譜或 RAG；不要把 star 數當作知識可信度。
- Skill backlog：將「PDF/文件 → 可測試 skill」與「專案描述 → 架構圖」拆成兩個內部 skill candidate，加入 license、來源引用、測試案例與人工審核欄位。

## 明日 watchlist

1. 追蹤 `tt-a1i/archify` 是否仍有高 Trending 星數、release/issue 是否同步增加，並實測一個 metabiz 專案描述的輸出可否驗證。
2. 追蹤 `anthropics/claude-plugins-official` 的 plugin 數量、重大 issue 與安全說明；建立安裝前檢查表，不直接擴大權限。
3. 追蹤 `ChromeDevTools/chrome-devtools-mcp` 的 v1.8.x 後續修正與瀏覽器相容性，設計一個不含敏感資料的 office automation demo。
4. 比較 `book-to-skill`、`K-Dense-AI/scientific-agent-skills` 與現有 PDF/skill workflow：輸入格式、引用保留、測試策略、更新成本。
5. 觀察 `AgriciDaniel/claude-obsidian` 的 issue/release 與 `know metabiz wiki` 現有 Markdown 結構是否能互通，再決定是否做小型 vault 試驗。

## 判讀限制

本報告的 star delta 是相對上一個可用 daily snapshot 的觀測差，不等於真實買方需求；Trending daily 也可能放大短期曝光。404 的既有追蹤項目沿用上一筆 metadata，應在後續 run 重新確認。任何第三方 skill、plugin、MCP server 在課程或公司環境採用前，都必須另做 license、權限、供應鏈與資料處理審查。
