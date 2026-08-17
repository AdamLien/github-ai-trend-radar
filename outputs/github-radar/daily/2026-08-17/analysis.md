# GitHub AI Trend Radar 分析｜2026-08-17

> 蒐集執行：2026-08-18 00:10 後（台灣時間）。`snapshot delta` 是與 2026-08-16 同範圍快照的差異；GitHub Trending daily 則為執行時的即時榜單，不能倒推成 8/17 的歷史榜單。首次觀測項目一律標示「未量測」，不把它寫成 `+0`。

## 今日結論

- 本輪維持「只增不減」的歷史池，共 **178** 個候選；執行時 Daily Trending 有 **7** 個 in-scope 項目，當中 `akitaonrails/ai-memory` 連續第二日可量測，其餘 5 個新增 Trending 候選先列 Watch。
- 強動能集中在可重用工作規範（`mattpocock/skills`）、可視化交付（`diagram-design`）、平行 coding agents（`Orca`）、模型路由（`OmniRoute`）和本地／可追溯知識圖譜（`Graphify`、`Semantica`）。這些都比總 stars 更能轉譯為 Adam 的課程、Demo 與 AI 辦公室實驗。
- 先做隔離、可回復的 POC：sample repo 測知識圖譜、假資料測 agent handoff、隔離帳號測瀏覽器／模型路由。不得交付客戶憑證、登入 session 或 know metabiz wiki 原始內容給第三方服務。

## 優先追蹤（按動能與可用性，不按總 stars 排名）

| 優先 | Repo | 分類 | 本次訊號 | 可用場景 | 主要風險 |
| --- | --- | --- | --- | --- | --- |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 220,081 ★；快照 **+1,057**；8/17 更新；MIT；359 issues | 可用來定義 metabiz skill 的輸入、驗收輸出與權限 stop line；適合「把流程變成技能」課程素材。 | 不可整包全域啟用；逐個檢查指令、資料權限和授權。 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Demo content | 20,332 ★；**+1,004**；MIT；24 issues | 以 Claude Code 產生編輯式 HTML/SVG 圖，適合 mCRM 人工核准流程、Wiki 架構的內容與課程 demo。 | 無正式 release；產出必須人工核對事實、版權和品牌。 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | Watch | 47,192 ★；固定 watchlist；**+751**；8/17 更新；v1.4.184 | 平行 coding-agent 的 ADE，值得研究任務切分、審核和執行證據如何呈現。 | 4,034 issues；介面成功不等於 production orchestration 穩定。 |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Deep research | 49,637 ★；**+646**；8/17 更新；MIT；414 issues | 單端點多模型路由，可做 Codex／Claude Code／Cursor 的成本、fallback 對照 demo。 | provider、API key、配額與資料外送邊界；免費額度不可當長期承諾。 |
| 5 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | Demo content | 73,074 ★；**+705**；8/17 更新；v0.1.800-beta；Apache-2.0 | 做「Prompt / RAG / fine-tune 何時該選哪一種」的實作對照教材。 | beta release、GPU 成本及模型授權差異大；1,264 issues。 |
| 6 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 107,401 ★；**+410**；8/16 release v0.9.45；Apache-2.0 | 將程式、文件、SQL、設定和 PDF 變成本地可查詢知識圖譜，最貼近 know metabiz wiki 的來源可追溯需求。 | 980 issues；先用無敏感 repo 驗證索引品質、資源耗用及清除流程。 |
| 7 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Deep research | 8,435 ★；**+314**；8/17 更新；v0.6.5；MIT | 可研究 accountable AI 的圖譜式 context、主張與證據連結。 | 早期資料模型可能與既有 Obsidian evidence schema 不合；103 issues。 |
| 8 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Watch | 1,855 ★；**+197**；Daily Trending **207 stars today**；8/17 release v1.28.0；MIT | 適合驗證 Claude Code 與 Codex 的任務 handoff：可否找回已試方案、失敗路徑及待決策。 | 跨 agent 記憶可能洩露 repo／任務脈絡；先驗證儲存位置、隔離、清除和 team boundary。 |
| 9 | [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) | Reference only | 40,377 ★；**+543**；8/17 更新；v3.20.212-lts | AI-native internal tools、dashboard、workflow 的產品與內容比較參考。 | AGPL-3.0 對商業整合有 copyleft 影響；未完成法務與部署判定前不採用。 |

## 對 Adam 工作的可執行轉譯

### 課程與 Demo content

1. 用 `diagram-design` 將「讀取客戶資料 → 草稿 → 人工核准 → 執行／稽核」畫成圖；只用假資料，驗收是學員能指出四個權限界線。
2. 用 `OmniRoute` 比較同一 coding 任務的模型路由、token、失敗與 fallback；保留 provider、成本和失敗原因，不承諾免費額度。
3. 用 `unsloth` 與 RAG 做同資料包比較：更新速度、成本、可稽核性及模型授權，而非只比回答效果。

### AI 辦公室自動化與 Skill candidate

1. 從 `mattpocock/skills` 抽取「明確輸入、可驗收輸出、權限 stop line」為既有 metabiz skills 的最低準則；優先補來源驗證、報告整理和人工核准草稿。
2. `Orca` 只作多 agent 協作介面研究；以一個非敏感 coding 任務驗證 Given/When/Then：任務拆分、人工審核、失敗重試各自有可回看的證據。
3. `ai-memory` 可做單一 sample repo handoff POC；boundary case 是人工清除記憶後不得復原敏感脈絡。

### know metabiz wiki

1. 用 `Graphify`／`Semantica` 研究「來源檔 → 主張 → 任務／系統 → 驗證時間 → 擁有者」的最小 schema；圖譜是導覽／查詢層，原始 evidence 仍是事實依據。
2. POC 必測引用能否回鏈到原始檔、能否排除敏感來源、重建索引後是否可正確清除舊資料。

## 新增 Trending 與反訊號

- 新增 Trending `AlexsJones/llmfit`（239 today）、`harry0703/MoneyPrinterTurbo`（1,275）、`jundot/omlx`（96）、`mukul975/Anthropic-Cybersecurity-Skills`（156）、`santifer/career-ops`（147）、`usestrix/strix`（656）皆為首次觀測，成長尚未量測；先不將當日注意力等同長期趨勢或採用建議。
- 大量 issues（Orca、Unsloth、Graphify、ToolJet）不等於拒用，但明確要求在 demo 成功後仍做維運、升級與失敗復原測試。
- GitHub stars 是開發者注意力，不可推論課程購買、客戶需求、production 安全或商業可行性。

## 明日追蹤清單

1. 追 `mattpocock/skills`、`diagram-design`、`Orca`、`OmniRoute` 的第二日 delta；快速收斂則改列內容參考。
2. 比較 `ai-memory` 的第二日 delta、README 及記憶清除／workspace 隔離設定，未通過前維持 Watch。
3. 以非敏感 repo 對 `Graphify` 和 `Semantica` 測來源回鏈、索引時間、查詢品質及刪除後重建。
4. 為新增 Trending 六項建立第二日基線；只在 README、release／issue 活躍度與範圍吻合時進入優先清單。
5. 持續保留 `stablyai/orca` 固定 watchlist 與所有歷史候選，避免搜尋結果變動而遺失趨勢曲線。
