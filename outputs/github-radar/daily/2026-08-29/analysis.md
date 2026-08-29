# GitHub AI Trend Radar 分析（2026-08-29）

## 摘要

本次以 GitHub Trending daily 與 10 組指定查詢收集 219 個候選，再依「今日星數、相對增長、近期 push/release、README 可用性、issue/PR 維護訊號與採用風險」挑出 8 個值得追蹤的專案。今日資料的強訊號是：Agent Skills 正從提示詞範本走向可重複的工作流；coding agent 開始出現並行協作、token gateway 與知識圖譜等基礎設施；內容生產與學習材料也在快速產品化。

本次未觀察到 GitHub API rate-limit 錯誤；collector 最終以 `--limit 5` 完成，因前景執行時需避免輸出管道阻塞。星數與增量均為 collector 當次快照，不能直接當作買方需求或產品採用量。

## 值得保留的專案

### 1. [tt-a1i/archify](https://github.com/tt-a1i/archify)

- 目的：把架構、流程、sequence、data-flow 與 lifecycle 圖轉成可驗證、可匯出的 HTML agent skill。
- 動能：總星數 30,130；今日 Trending 3,927；相對星增量 +3,814；最近更新 2026-08-28；最新 release v2.15.0（2026-08-17）。這是本次最強的單日增長訊號。
- 風險：高增長但 license、issue 健康度與長期維護仍需人工核查；圖表正確性不能只靠視覺效果判斷。
- 分類：Deep research
- 對 Adam／metabiz：可做「AI 把需求變成架構圖」課程 demo，也適合把 mCRM、mBeauty 或內部流程整理成 wiki 可讀的流程圖；值得研究其 skill 輸入輸出契約。

### 2. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

- 目的：提供 165 個科學研究 skills 與資料庫連接，兼容 Cursor、Claude Code、Codex 等 Agent Skills 標準。
- 動能：總星數 37,613；今日 Trending 1,604；相對星增量 +1,509；最近更新 2026-08-29；最新 release v2.64.0（2026-08-17）。README 的範圍、數量與相容性定位清楚。
- 風險：科學、醫學與藥物領域有高準確性與引用責任；需要檢查各 skill 的來源、測試、license 與外部 API 依賴。
- 分類：Skill candidate
- 對 Adam／metabiz：可作為「如何把專業知識封裝成 skill」課程案例，並映射到 know metabiz wiki 的分類、引用、版本與審核流程；不宜未審核就用於商業或醫療結論。

### 3. [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)

- 目的：讓 coding agent 以較少程式碼與較少過度工程完成任務，主打「不要寫不必要的程式」。
- 動能：總星數 116,170；今日 Trending 1,171；相對星增量 +1,147；最近更新 2026-08-07；最新 release v4.9.0（2026-08-07）。高星基礎上仍有明顯單日增長。
- 風險：理念型工具容易被誤用成省略測試或設計；需檢查規則是否會犧牲可維護性，且目前更新距快照已有一段時間。
- 分類：Demo content
- 對 Adam／metabiz：適合做「AI coding agent 如何避免 over-engineering」前後對照 demo，延伸到 office automation 的最小可行流程；可沉澱為 wiki 的 agent review checklist。

### 4. [mattpocock/skills](https://github.com/mattpocock/skills)

- 目的：分享真實 `.agents` 目錄中的可重用工程 skills。
- 動能：總星數 240,782；相對星增量 +820；最近更新 2026-08-24；最新 release v1.2.3（2026-08-06）；20,477 forks。雖無當日 Trending 數值，社群規模與增量仍具參考性。
- 風險：個人工作流不等於通用標準；需要逐項檢查權限、提示注入、外部命令與適用模型，並確認 license。
- 分類：Skill candidate
- 對 Adam／metabiz：可直接作為 Codex skill 設計與課程教材的參考基線，對照現有 skills/github-trend-radar、文件與影片流程，建立「skill 的輸入、輸出、驗證、失敗處理」模板。

### 5. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

- 目的：以 12 條 production pipeline、100+ tools、700+ agent skill/知識檔案組成開源 agentic 影片製作系統。
- 動能：總星數 53,847；今日 Trending 809；相對星增量 +779；最近更新 2026-08-22。規模與單日增量都高，且與內容生產直接相關。
- 風險：pipeline 數量多代表整合與維護面大；需驗證實際輸出品質、模型成本、素材版權與各工具的 license。
- 分類：Demo content
- 對 Adam／metabiz：可做短影音／課程內容的端到端示範，拆解「brief → 腳本 → 素材 → 剪輯 → 發布」如何變成可觀測的 AI office workflow；其 production knowledge 也可作 know metabiz wiki 的結構參考。

### 6. [stablyai/orca](https://github.com/stablyai/orca)

- 目的：以桌面、手機或 VPS 管理一組平行 coding agents，使用既有模型訂閱。
- 動能：總星數 56,652；相對星增量 +746；最近更新 2026-08-29；最新 release v1.4.192（2026-08-29）。近期更新與 release 同日，是很強的維護訊號。
- 風險：平行 agent 帶來成本、競態、權限與 secrets 隔離問題；需確認資料是否離開自有環境，以及訂閱服務條款。
- 分類：Deep research
- 對 Adam／metabiz：可研究成「AI office 多代理分工」課程案例，對照 Odoo、文件、內容與 wiki 任務如何排程；採用前要做權限模型、審計與失敗回復測試。

### 7. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

- 目的：提供兼容 Claude Code、Codex、Cursor 等工具的多 provider AI gateway，含 fallback、token 壓縮與 MCP/A2A。
- 動能：總星數 57,922；相對星增量 +543；最近更新 2026-08-29；最新 release v3.8.50（2026-08-26）；7,989 forks。更新頻繁且整合面廣。
- 風險：多 provider gateway 會集中 API key、請求內容與計費風險；「免費／大量 provider」宣稱必須實測穩定性、合規、速率與供應商條款。
- 分類：Watch
- 對 Adam／metabiz：值得做 AI office automation 的成本、fallback、模型路由比較實驗，並將 provider、資料分類、token 使用量寫入 know metabiz wiki；暫不建議直接承載正式客戶資料。

### 8. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

- 目的：將 codebase、文件、SQL schema、設定與 PDF 轉成可查詢 knowledge graph，提供 Claude Code、Cursor、Codex、Gemini CLI skill。
- 動能：總星數 112,207；相對星增量 +330；最近更新 2026-08-28；最新 release v0.9.51（2026-08-28）；10,913 forks。近期 release 與高 fork 數顯示工程整合價值。
- 風險：AST/文件解析的覆蓋率與圖邊正確性需抽樣驗證；本地圖譜的權限、敏感資料、增量更新與索引成本也要先釐清。
- 分類：Deep research
- 對 Adam／metabiz：與 know metabiz wiki 最直接相關，可研究「wiki 不只存頁面，而是建立可追溯的知識關係」；也能用 metabiz 專案資料做內部 demo，但須先做脫敏與存取控制。

## 明日 watchlist

明日優先重查以下訊號：`tt-a1i/archify` 是否維持異常高的星增量、`K-Dense-AI/scientific-agent-skills` 是否持續發版、`stablyai/orca` 的平行 agent 權限與成本說明、`OmniRoute` 的 provider/fallback 實測，以及 `Graphify` 對 PDF、SQL 與增量更新的實際案例。另追蹤 `anthropics/claude-plugins-official`、`obra/superpowers`、`virgiliojr94/book-to-skill` 與 `rohitg00/ai-engineering-from-scratch`：它們分別代表官方 plugin 生態、agentic 開發方法、知識轉 skill、以及課程型內容，若星增量與 README/issue 活動同步，應納入下一輪深入分析。

## 行動建議

1. 先以 `archify`、`OpenMontage`、`book-to-skill` 做低風險 demo，產出可重複的課程與短影音素材。
2. 以 `mattpocock/skills`、`scientific-agent-skills` 對照現有 Codex skills，建立 skill QA、權限與版本規範。
3. 以 `Graphify` 做 know metabiz wiki 的小型脫敏 PoC；以 `Orca`、`OmniRoute` 做多 agent／多 provider 的隔離與成本測試，不直接升級為 production 依賴。
