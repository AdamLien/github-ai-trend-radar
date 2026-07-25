# GitHub AI Trend Radar — 2026-07-14

> 執行時間：2026-07-15 00:12–00:16（Asia/Taipei）；趨勢資料取自 GitHub Trending `daily` 頁面。目標日為台灣時間 2026-07-14。

## 執行摘要

- 今日最強的實務訊號不是新的 agent framework，而是 **coding-agent skills 的可安裝、可治理、可做出差異化結果**：Graphify、mattpocock/skills、Hallmark、DCG 都落在這條線上。
- **優先深研：Graphify、DCG、mattpocock/skills。** 前者可改善跨 repo／文件的脈絡探索，DCG 對 agent 自動化的安全護欄很直接，Skills 則適合作為課程的工程化技能庫參考。
- **最容易做內容或課程 demo：Hallmark、Awesome LLM Apps。** Hallmark 有明確的「反 AI 味」可視化前後對照；Awesome LLM Apps 是可挑選案例的教材目錄，但不應整包導入。
- **知識庫／metabiz wiki 值得追的只有 Graphify。** 它宣稱能將程式、SQL schema、文件、論文、圖片和影片收進可查詢 knowledge graph；先以一個非敏感 wiki／repo 做小型 POC，驗證索引品質、來源追溯和成本。

## 資料限制

- `GITHUB_TOKEN` 不存在，collector 已依規定降至 `--limit 5`，仍在第 20 個 repo metadata 請求收到 GitHub API `403 rate limit exceeded`。因此本次 **沒有 `repos.json`、snapshot 或可比較的 API star delta**。
- 下表的「stars today」與總 stars 是 GitHub Trending 畫面擷取時的數值；它們是日榜動能，**不是** collector 的跨日 `star delta`。README、授權與可見的 issue／PR 計數則以各 repo 公開頁面核對。
- GitHub Trending daily 是滾動的當日頁面；凌晨執行時它是目標日的最佳可得近似訊號，不能回溯為完整、固定的台灣日結資料。

## 今日最值得追的 repo

| Repo | 分類 | 用途與為什麼紅 | stars today／總 stars | 動能判讀與風險 |
| --- | --- | --- | ---: | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 給 Claude Code、Codex、Cursor 等 coding agent 的 knowledge-graph skill；把 code、SQL、文件、圖像／影片等變成可查詢關聯。跨資料源的 context engineering 很貼近實務痛點。 | 1,858／85,890 | 約 2.16%，且 README、tests、architecture、benchmarks、security 文件齊全。風險：233 issues、289 PR，需 POC 驗證維護負荷、索引品質與敏感資料邊界。MIT。 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 工程師日常使用的 agent skills，定位是保留工程控制權、而非由大型流程框架接管。可作為「技能包如何帶入真實工程」的課程對照樣本。 | 1,559／169,761 | 約 0.92%，仍是很大的日榜增量。風險：158 issues、僅 2 PR；不能把高 stars 視為每個 skill 都可直接採用。MIT。 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Demo/content idea | 100+ 可執行的 agent、skills、MCP、RAG 範例；README 有 MCP router、Notion MCP、knowledge-graph RAG、OpenAI Agents SDK 等可拆題材。 | 1,104／120,511 | 約 0.92%，教材面廣且 README 清楚。風險：範例庫不是統一生產級架構，且需各自 API key／相依套件；挑單一例子重做與測試。Apache-2.0。 |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Demo/content idea | Claude Code、Cursor、Codex 的設計 skill；以多種結構、20 themes、slop-test gates 和 pre-emit critique 來壓低制式 AI 視覺感。 | 1,010／5,906 | 約 17.1%，是今日效率最高的訊號。風險：視覺品味／門檻未等於商業轉換率；先用同一 brief 做 A/B 截圖。MIT。 |
| [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Deep research | Rust 製 agent shell／git 破壞性指令防護；repo 具 AGENTS.md、SKILL.md、tests、安裝／解除安裝腳本。對自動化代理的「安全執行層」很具體。 | 481／4,214 | 約 11.4%，新且強。風險：攔阻規則可能誤擋日常流程，必須先以 audit／非 production 環境驗證；可見 7 issues、6 PR。授權檔存在，採用前仍須核對條款與平台覆蓋。 |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Watch | 個人交易 agent；Docker、compose、tests、security 與多語 README 都在，能當 multi-agent／資料流程案例。 | 1,265／22,621 | 約 5.59%，動能高。風險：金融決策與回測／實盤是兩件事；不作投資建議，也不適合作為 metabiz 辦公室自動化的優先採用項。MIT。 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | Reference only | AI hedge fund team 的多 agent 示範，程式含 tests、roadmap 與 vision。 | 156／61,754 | 約 0.25%，今天不是主要動能。風險：金融情境很容易被 demo 效果誤導；保留作 agent team 架構參考，非投資工具。MIT。 |
| [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | Reference only | AI/ML research engineer 的學習資源地圖，包含 AI inference、ML systems design、applied／bleeding-edge AI 等章節。 | 69／5,029 | 約 1.37%，偏知識整理而非可直接部署工具。風險：需逐篇檢查更新性與難度；作課程延伸閱讀即可。 |

## 對 Adam 的可行動轉譯

### Deep research

1. **Graphify POC**：取一個可公開測試的 repo + 少量文件，驗證「問跨程式／schema／文件的問題」是否有可追溯回答；不先接觸 metabiz 私有 wiki 或客戶資料。
2. **DCG 防護評估**：列出 Codex／Claude Code 在日常自動化會觸發的 `git`、刪檔、shell 指令，測 false-positive、bypass 與 rollback；安全護欄在課程和 AI 辦公室都比又一個 agent demo 更有差異化。
3. **Skills 的工程化規範**：以 mattpocock/skills 對照既有 Codex skill：何時需要 SKILL.md、可驗證產物、scope boundary、失敗回復，形成自己的 skill acceptance checklist。

### Demo／內容選題

- **「同一份 brief，Codex 做出 AI 味頁面 vs Hallmark 做出有個性的頁面」**：保留 prompt、skill、截圖和人工評分規準，不只展示好看的結果。
- **「不是再裝 100 個 agent：把 Awesome LLM Apps 的一個 Notion／RAG 範例改成可驗證的小流程」**：挑一個資料源、一個輸出、一個失敗情境。
- **「讓 coding agent 知道整個系統，而不是只讀目前檔案」**：Graphify knowledge graph 對照傳統 `rg`／README 探索，量測回答可追溯性與設定成本。

### AI 辦公室自動化與 know metabiz wiki

- **可用方向**：Graphify 的跨 code／文件 graph POC、Awesome LLM Apps 的 Notion MCP 與 knowledge-graph RAG 範例，可作研究素材。
- **不可直接導入**：不要直接讓外部 skill 索引私有 wiki、客戶文件或憑證；先做資料分類、最小讀取權限、可刪除的測試索引、引用／來源驗證及人工核准出口。
- **可包裝為 skill 的流程**：`資料夾盤點 → 允許來源清單 → 建圖／索引 → 問題集評測 → 引用與缺失資料檢查 → 清理索引`。這比單純「裝 Graphify」更適合內部可重複使用。

## 明天追蹤清單

1. `Graphify-Labs/graphify`：daily stars 是否持續；issues／PR 是否收斂；實作 POC 的索引成本與引用品質。
2. `Dicklesworthstone/destructive_command_guard`：release、授權條款、平台支援及 false-positive 設定方式。
3. `Nutlope/hallmark`：高比例 stars today 是否延續；挑兩份真實 brief 跑視覺 A/B。
4. `mattpocock/skills`：挑 1–2 個 skills 讀完其指令與驗證方式，而非整包安裝。
5. `Shubhamsaboo/awesome-llm-apps`：只挑 Notion MCP／knowledge-graph RAG／deep research 三個候選，看實際 requirements、API 成本與測試涵蓋。
6. `HKUDS/Vibe-Trading`：僅追蹤其 agent orchestration／資料管線設計；不納入金融建議或正式交易流程。

## 下次執行建議

- 設定 `GITHUB_TOKEN` 後重跑 10 個 prescribed queries、`--limit 10` 與 `--include-readme`，使 collector 能落下 `repos.json` 與 snapshot，從下一日開始提供真正的 `star delta`。
- 若仍只能匿名執行，限制為今日 5 個 watchlist repo，而非先搜尋再逐 repo metadata 讀取，避免在產生任何檔案前耗盡 60 次／小時 quota。
