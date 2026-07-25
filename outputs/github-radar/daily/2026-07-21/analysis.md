# GitHub AI Trend Radar 分析｜2026-07-21（台灣目標日）

> 收集時間：2026-07-22 09:27（Asia/Taipei）。API 使用 GitHub 已登入帳號，10 組查詢、每組 10 筆，共 **89 個去重 repo**；未遇 rate limit。
>
> 指標註記：`stars today` 是 7/22 09:27 讀取 GitHub Trending daily 頁面時顯示的即時日增星，屬於強動能訊號、不是可回溯的 7/21 歷史頁面。`API delta` 是指定輸出資料夾內 7/22 00:18 與 09:27 兩個快照的差異（約 9 小時）；多數為 0，不能解讀為全天沒有成長。

## 結論

今天最清楚的主線是「**讓 coding agent 更少讀、讀得更準、以明確 skill 執行**」：code intelligence graph、agent harness、輸出規格 skill，以及本機研究／搜尋 MCP 同時升溫。對 Adam 而言，優先做可驗收的小型內部試驗，不要直接把高成長 repo 當成團隊標準。

- **優先深研：** `code-review-graph`、`Graphify`、`open_deep_research`。
- **最快可示範：** `i-have-adhd`（輸出契約）、`llmfit`（本機模型選型）、`wigolo`（本機 MCP research）。
- **策略訊號：** `jcode` 的 843、`code-review-graph` 的 1,925 daily stars 均很高；先看 README、issue 和本機可重現性，再判定採用。

## 今日最值得追的 repo

| 分類 | Repo | 用途與為何紅 | 動能／健康 | 風險與建議 |
| --- | --- | --- | --- | --- |
| Deep research | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | MCP/CLI 的 local-first 程式碼 intelligence graph，讓 coding agent 只讀需要的 context；非常貼合大型 repo code review 與 context 壓縮。 | Trending **+1,925 today**／24,576 stars（約 **7.8%**）；MIT；7/21 有 push；117 open issues。 | daily 成長異常高，先以一個真實 repo 量測索引時間、召回品質與 token 節省；目前沒有看到正式 release 訊號。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 將 code、docs、SQL schema、config、PDF 做為可查詢 knowledge graph；直接提供 Claude Code、Codex、Cursor 等 skill。 | API **+0**（短時窗）／93,169 stars；MIT；7/21 push，7/21 發布 v0.9.23；README 定位清楚。 | 597 open issues，先確認索引成本、資料邊界與現有 codebase-memory 工作流的重疊。 |
| Deep research | [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | 可參照的深度研究 agent 實作，適合拆解「研究計畫→搜尋→來源→綜合」的可教學流程。 | Trending **+23 today**／12,242 stars；MIT；69 open issues；最近 push 為 7/17。 | 不是最新 daily mover；應視為 workflow reference，驗證來源可追溯性與成本，不直接當 production framework。 |
| Demo/content idea | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Rust coding-agent harness；可做「輕量 coding agent 對比重型框架」的內容實驗。 | Trending **+843 today**／10,331（約 **8.2%**）；MIT；7/22 有 push；108 open issues。 | 成長快且描述很短；先跑最小任務、檢查 provider／sandbox／資料外送行為，再決定是否追蹤。 |
| Skill candidate | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 讓 coding agent 不埋沒結論的輸出 skill；本質是可驗收的回覆結構，而非模型能力。 | Trending **+1,866 today**／6,891（約 **27.1%**）；MIT；7/21 有 push；僅 14 open issues。 | 高日增可能受社群擴散影響；值得萃取成 Adam 自用的「結論、證據、下一步」skill 規格，不必直接安裝。 |
| Skill candidate | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 面向 Claude Code、Codex、Cursor 的 production-grade engineering skills，可作為既有 skill 的品質比較基準。 | API **+1**（短時窗）／79,692 stars；MIT；7/18 push；v0.6.4（7/12）。 | 非今日 Trending 訊號；先挑一個可量測 workflow 比對，避免整包導入後與既有規範衝突。 |
| Demo/content idea | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | 用單一命令按硬體條件找可執行的 model/provider；很適合 Apple Silicon 本機 LLM 選型教學。 | Trending **+129 today**／30,205（約 **0.4%**）；MIT；7/21 有 push；51 open issues。 | 只能提供相容性／推薦起點，仍需實測 token/s、RAM、模型品質與授權。 |
| Watch | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | local-first MCP 搜尋、抓取與 research，主張無 API key／無雲端；適合 AI 辦公室 research prototype。 | Trending **+642 today**／3,160（約 **20.3%**）；7/21 有 push；28 open issues。 | Public beta、授權為 **NOASSERTION**；不得導入客戶或 metabiz 敏感資料，先確認授權與 crawler 合規性。 |
| Watch | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | 整合 IM、LLM、plugins 的 agent assistant；可作為「AI 辦公室自動化／多通路 bot」架構觀察樣本。 | Trending **+416 today**／37,475（約 **1.1%**）；7/22 有 push；AGPL-3.0；1,335 open issues。 | AGPL 與大量 issue 代表部署、客製、商用責任均要先評估；只作架構參考。 |
| Reference only | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | AI Agent 設計與工程實作的開源書與章節程式，可用作中文課程選題的素材池。 | Trending **+4,624 today**／14,614（約 **31.6%**）。 | 不等同可採用工具；應逐章核實內容、版權與實作更新狀態。 |

## 對 Adam 的可用性

| 方向 | 可做的下一步 | 優先 repo |
| --- | --- | --- |
| 課程／內容選題 | 做一集「為何 Agent 不是多讀 context，而是讀對 context」：以 code-review-graph 對照 Graphify，展示同一 PR 的 context 篩選。 | code-review-graph、Graphify |
| AI 辦公室自動化 | 用非敏感公開資料試作 research chain：問題定義、來源抓取、引用輸出；本機優先，保留每一步 provenance。 | wigolo、open_deep_research |
| know metabiz wiki | 不直接全庫索引。先以單一受控專案／匿名文件測試 schema、權限、更新增量與可追溯引用，再決定是否採 graph 層。 | Graphify、code-review-graph |
| Codex skill 強化 | 把 `i-have-adhd` 的意圖轉為內部回覆驗收：先結論、再證據、最後可執行下一步；以既有 skill 的驗證規範為主。 | i-have-adhd、agent-skills |
| 本機模型教學 | 在 M1 Max 實測 llmfit 推薦值與 Ollama 基準，輸出實測速度、RAM、品質，而非只引用推薦。 | llmfit |

## 風險與假陽性

- Trending 的 `stars today` 是 GitHub 頁面的 live signal，可能包含社群傳播／短期曝光，不能推導市場付費需求。
- `wigolo` 未宣告 SPDX license；`AstrBot` 為 AGPL-3.0，兩者都不應未審查就納入商業或客戶資料流程。
- 高 issue 數不必然是壞訊號，但須用 release 節奏、可重現安裝與最小任務成功率判斷維護品質。
- API collector 的 snapshot delta 僅約九小時，且早前基準已在同一輸出目錄；本輪不以 `+0/+1` 排名。

## 明日繼續追蹤

1. `tirth8205/code-review-graph`：連續兩日 daily stars、release 與 issue 回應，及其 context/token benchmark 是否可重現。
2. `Graphify-Labs/graphify`：v0.9.23 後的問題回報、Codex skill 安裝與增量索引體驗。
3. `1jehuang/jcode`：快速成長是否延續，及 sandbox／provider 使用界線。
4. `ayghri/i-have-adhd`：將其 output contract 與既有 Codex 回覆品質規則對照後的實測收益。
5. `KnockOutEZ/wigolo`：授權補齊、公開 beta 穩定性，以及本機 research 的來源品質。
6. `AlexsJones/llmfit`：Apple Silicon 的推薦與實測是否一致。
7. `langchain-ai/open_deep_research`：引用／provenance 與成本控制的實作差異。

## 產物與驗證

- API 原始快照：[repos.json](repos.json)
- collector 報告：[report.md](report.md)
- 本輪快照：[snapshots/repos-2026-07-22.json](snapshots/repos-2026-07-22.json)
- GitHub Trending daily 讀取：2026-07-22 09:27（Asia/Taipei），AI 相關條目已人工篩選；無法從 live 頁面回溯到 7/21 歷史排名。
