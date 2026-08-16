# GitHub AI Trend Radar 分析｜2026-08-16

> 蒐集執行：2026-08-17 00:10 後（台灣時間）。本報告的 `snapshot delta` 與 2026-08-15 前一份快照相比；GitHub Trending daily 是執行時讀取的即時榜單，不能回溯重建 8/16 的歷史榜單。第一天觀測的新項目一律標示「未量測」，不把它誤寫成 `+0`。

## 今日結論

- 本輪保留 **172** 個歷史＋新候選（只增不減），其中 **1** 個是本 Radar 首次觀測的 in-scope Daily Trending 專案：`akitaonrails/ai-memory`；Daily Trending in-scope 共 3 個。
- 動能最強的仍是把 AI 工作流直接產品化的四條線：**技能資產化**（`mattpocock/skills`）、**多模型／多 agent 路由**（`OmniRoute`）、**agent 可用瀏覽器**（`ego-lite`）與**可查詢知識圖譜**（`Graphify`／`Semantica`）。這比單看總 stars 更貼近 Adam 的課程與 AI 辦公室機會。
- 本日應先做可驗證的小試驗，而不是直接導入：用隔離帳號測 `ego-lite`，用非機敏 sample repo 測 `Graphify`，用假資料檢驗 `ai-memory` 的跨 agent handoff。不得把客戶憑證、瀏覽器 session 或 know metabiz wiki 原始內容直接交給第三方服務。

## 優先追蹤（按動能與可用性，不按總 stars 排名）

| 優先 | Repo | 分類 | 本次訊號 | 為何值得追／可用場景 | 主要風險 |
| --- | --- | --- | --- | --- | --- |
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Demo content | 19,328 ★；快照 **+1,065**；8/14 更新；MIT | Claude Code 可直接產生 29 種編輯式圖表；適合做「把方案／Wiki 架構變成可讀圖」短片與課程作業。 | 無 release；成品仍要人工校對事實、版權與品牌視覺。 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 219,024 ★；**+852**；8/16 更新；v1.2.3、MIT | 高動能 skills 目錄是課程中「何時做成可重用技能」的素材，也可比對 metabiz 現有 skill 邊界。 | 不可整包全域啟用；每個 skill 的指令、資料權限與授權要逐項審核。 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Deep research | 48,991 ★；**+564**；8/16 更新；v3.8.49、MIT | 單一端點路由 340 providers，直接涵蓋 Codex／Claude Code／Cursor；可作「模型路由、成本與 fallback」課程 demo。 | gateway／API key／配額與資料外送邊界；401 open issues 表示採用前需做穩定性測試。 |
| 4 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | Deep research | 11,278 ★；**+545**；8/16 更新；v1.2.3、MIT | 提供 agent 瀏覽器自動化且保留登入狀態，適合研究 AI 辦公室的人工核准前整理流程。 | session 與客戶資料風險最高；只能以隔離帳號／最小權限測試，禁止無審核的外發操作。 |
| 5 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 106,991 ★；**+417**；8/15 更新；v0.9.44、Apache-2.0 | 把 code、文件、SQL、設定與 PDF 轉成可解釋的本地知識圖譜；最貼近 know metabiz wiki 的「證據可追溯」需求。 | 948 open issues；先用非敏感 repo 驗證索引品質、資源耗用與資料清理。 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | Watch | 46,441 ★；**+458**；8/16 更新；v1.4.183、MIT | 平行 coding agents 的 ADE，適合作為多 agent 任務分解與審核站的介面研究。 | 3,971 open issues 是維運訊號；不可把 dashboard 體驗等同 production orchestration 保證。 |
| 7 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Deep research | 8,121 ★；**+286**；8/16 更新；v0.6.5、MIT | Graph-native、accountable AI 基礎設施，可研究可追蹤來源、關係與決策的 wiki／RAG 設計。 | 產品早期且 70 open issues；資料模型與既有 Obsidian evidence schema 要先做 mapping。 |
| 8 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Watch | 1,658 ★；Daily Trending **41 stars today**；8/16 更新；v1.27.0、MIT；**首次觀測，成長未量測** | 主打 Claude Code 中斷後由 Codex 接續，不必重講架構與失敗路徑；很適合做「可移交 agent 工作記憶」實驗。 | 跨 agent 記憶可能洩露 repository／任務脈絡；先查儲存位置、加密、清除與 team boundary。 |
| 9 | [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) | Reference only | 39,834 ★；**+457**；Daily Trending **446**；8/14 更新；AGPL-3.0 | AI-native internal tools／workflow 是 AI 辦公室 dashboard 的參考案例，可做低碼產品比較內容。 | AGPL-3.0 對商業整合有強 copyleft 影響；未完成授權審查前不列為直接採用。 |
| 10 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | Demo content | 72,369 ★；**+530**；Daily Trending **580**；8/16 更新；v0.1.800-beta、Apache-2.0 | 本地／低資源 LLM 訓練話題仍有明顯注意力，適合做「何時該 fine-tune、何時該 RAG」的教學對照。 | beta release、GPU／模型授權與成本差異大；不應以 GitHub 動能推論商業需求。 |

## 對 Adam 工作的可執行轉譯

### 課程與 Demo content

1. 用 `diagram-design` 做一個「mCRM 人工核准流程」圖表 demo；輸入只用假資料，驗收是學員能指出資料讀取、草稿、核准、執行四個界線。
2. 用 `OmniRoute` 示範同一 coding 任務的模型路由與 token／fallback 取捨；保留每次 provider、成本與失敗原因，避免宣稱任何免費額度可長期使用。
3. 用 `unsloth` 對照 RAG：以同一份知識包比較 prompt／retrieval／fine-tune 的成本、更新速度與可稽核性。

### AI 辦公室自動化與 Skill candidate

1. 對照 `mattpocock/skills` 與既有 metabiz skills，抽出「明確輸入、可驗收輸出、權限 stop line」三項最低準則；優先補可重複的報告整理、來源驗證與人工核准草稿技能。
2. `ego-lite` 僅能列為瀏覽器自動化研究，不授權對登入系統執行客戶動作；設計需有隔離帳號、人工確認和可稽核 action payload。
3. `ai-memory` 可做單一 sample repo 的 handoff POC：Given Codex 已完成一半任務，When 改由另一 agent 接手，Then 能找回已試方案與待決策；boundary case 是手動清除後不得還原敏感脈絡。

### know metabiz wiki

1. 以 `Graphify`／`Semantica` 研究「文件與程式的可解釋關係圖」，但來源仍以現有 evidence 文件為準，圖譜只是導覽與查詢層。
2. 先定義最小 schema：`來源檔 → 主張 → 任務／系統 → 驗證時間 → 擁有者`；任何自動抽取關係都必須能回鏈到原始證據。

## 風險與反訊號

- 本輪快照 delta 是相鄰日資料差，不是 GitHub 官方「今日新增 stars」；Daily Trending 的 `stars today` 只有 3 個當下 in-scope 卡片可觀測。
- `ToolJet` 的 AGPL-3.0 必須在任何產品／客戶環境採用前完成法務與部署方式判定。
- 大量 open issues（例如 Orca 3,971、Unsloth 1,240、Graphify 948）不是單獨的拒用理由，但表示 demo 成功不能外推為可上線。
- 高 stars 是開發者注意力，不能推論課程購買、客戶需求或 production 安全性。

## 明日追蹤清單

1. 追 `diagram-design`、`mattpocock/skills`、`OmniRoute`、`ego-lite` 的連續第二日 delta；若增幅快速收斂，從趨勢改列內容參考。
2. 檢查 `ai-memory` 的 README／設定，確認記憶保存位置、跨 workspace 隔離、移除流程和授權；未通過前保持 Watch。
3. 選一個無敏感資料的 sample repo，分別試 `Graphify` 與 `Semantica` 的來源追溯、索引時間與查詢品質。
4. 對 `Orca` 與 `ToolJet` 看 release／issue 回應品質與授權限制，不以熱度作採用決策。
5. 持續保留固定 watchlist `stablyai/orca` 與所有歷史候選，避免只留當日搜尋結果而遺失趨勢曲線。
