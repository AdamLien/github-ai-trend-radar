# GitHub AI Trend Radar — 2026-07-23（台灣）

> 本報告的目標日期為 **2026-07-23**；資料實際在台灣時間 2026-07-24 約 00:10 後取得。GitHub Trending 的 `daily` 頁不能回放歷史日期，故下文「Trending 即時」一律是 7/24 的觀測，不將它冒充為 7/23 的歷史 star 數。

## 資料品質與判讀方法

- Collector：10 個指定搜尋式、`--limit 10`、已驗證 GitHub token、含 README 摘要；取得 **89** 個去重 repo，未降為 limit 5、未遇 rate limit。
- API 星數差：以 7/23 快照與本次 7/24 快照相減；87 個 repo 可比較。這是約一天的快照差，不是 GitHub Trending 的 `stars today`。
- 優先序結合：短期星數差、Trending 即時熱度、最近 push/release、README 對實際工作流的清晰度、授權與維護風險。GitHub attention 並不等於商業需求或可直接採用。

## 今日值得追的 repo

| 類別 | Repo | 訊號 | 用途與為何值得看 | 主要風險 |
| --- | --- | --- | --- | --- |
| Deep research | [Graphify](https://github.com/Graphify-Labs/graphify) | API **+735**；94,407 stars；7/22 push/release | 把程式碼、文件、SQL schema、設定與 PDF 做成可查詢的可解釋知識圖；明確支援 Claude Code、Cursor、Codex。這正對應 know metabiz wiki 的「有根據、跨資料源」檢索需求。 | 616 open issues；先以小型、去識別化 repo 驗證索引時間、權限與圖譜品質，勿直接掃入營運 vault。 |
| Deep research | [Headroom](https://github.com/headroomlabs-ai/headroom) | API **+367**；61,535 stars；7/23 push | 壓縮 tool output、log、檔案與 RAG chunk，並提供 library/proxy/MCP server；是 agent context cost 與長輸出的基礎設施候選。 | 效能宣稱須以 mSHOP/UV100 的真實 tool traces 重跑；中介層可能截斷關鍵證據或洩漏內容。 |
| Deep research | [Obsidian Mind](https://github.com/breferrari/obsidian-mind) | API **+281**；3,772 stars；7/19 push/release | 為 Claude Code/Codex CLI/Gemini CLI 提供可持久化的 Obsidian vault memory。小而聚焦，適合研究「agent 寫回 Markdown」的最小產品面。 | 只有 3 open issues 不等於成熟；先檢查其檔案改寫規則、衝突處理與資料外送。 |
| Skill candidate | [agent-skills](https://github.com/addyosmani/agent-skills) | API **+198**；80,020 stars | Production-grade coding-agent skills。可當作 Adam 現有 skill 的品質基準與課程案例：任務邊界、驗證、failure mode。 | 不應整包匯入；逐一比對現有 `/skills`、權限與依賴後才萃取模式。 |
| Skill candidate | [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | API **+633**；69,245 stars；Trending 即時 **+637 today** | Skills 類發現入口今日熱度很高，適合把「如何挑、測、治理 skills」做成課程或內容主題。 | 收藏清單不是安全審核；本次 API 顯示 license 空白，且連出專案品質與權限差異大。僅作發現來源。 |
| Watch | [ponytail](https://github.com/DietrichGebert/ponytail) | API **+554**；88,295 stars；7/15 push | 主張讓 coding agent 以「少寫、先判斷」的資深工程方法工作；README 定位清楚，能形成 code-review / cost-control 內容角度。 | 快速成長不代表方法可量化；先做 A/B task 成功率、diff 大小與 token 成本實驗。 |
| Watch | [ECC](https://github.com/affaan-m/ECC) | API **+329**；232,472 stars；7/23 push | Agent harness 的 skills、memory、security、research-first 綜合包，支援 Claude Code/Codex/Cursor。可用於觀察 agent developer-experience 的主流設計。 | 範圍很廣，避免把它當單一權威框架；先做威脅模型與最小可逆試用。 |
| Reference only | [LLM Wiki](https://github.com/nashsu/llm_wiki) | API **+53**；15,180 stars | 將資料持續建成可互連 wiki，而非每次即時 RAG；對 know metabiz wiki 的產品敘事很有啟發。 | API 為 `NOASSERTION` license，且 7/20 後未見近期 release；只研究資訊架構，不直接整合。 |
| Demo/content idea | [Open Code Review](https://github.com/alibaba/open-code-review) | Trending 即時 **+265 today**；11,238 stars | 將 deterministic pipeline 與 LLM agent 結合做行級 code review，能做「Agent 不是只聊天，如何可驗證地檢查程式」的示範。 | Trending 快，但不在本次指定 API 搜尋結果內；先讀授權、部署模型與規則更新方式。 |
| Demo/content idea | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Trending 即時 **+1,925 today** | 面向 Claude Code/Codex/Cursor 的多模型 gateway，含 fallback、壓縮、MCP/A2A；是今日最大開發者自動化訊號。 | 目前是 Trending 單點訊號、未列入 API 搜尋候選；provider/key routing、隱私、費用與可用性都必須獨立驗證。 |

## 對 Adam 的可用行動

### 課程與內容選題

1. **「Skills 不是 Prompt：用可驗證工作流挑選 Coding Agent Skills」**：以 `agent-skills` 的工程化做法對照 `awesome-claude-skills` 的發現入口；示範審核授權、外部命令、測試與可逆安裝。
2. **「Context engineering 的下一站：從 RAG 到可追溯知識圖」**：Graphify 對照 Headroom，展示「先保留證據關係、再節省 context」而不是盲目摘要。
3. **「LLM code review 要能落地」**：以 Open Code Review 解釋 deterministic 規則與 LLM judgement 的責任分工；勿把 demo 表現宣稱為 production 成效。

### AI 辦公室自動化

- 優先研究 Headroom：拿 3 組已去識別的 tool/log payload 比較 token、答案完整度、錯誤率；產出量化 gate 再考慮 MCP proxy。
- `awesome-claude-skills` 可作每週候選來源，但要經「授權 → 權限 → 外部存取 → 小測 → 文件品質」五關，不以 stars 決定安裝。
- OmniRoute 屬於觀察項；任何 gateway 接進工作流前，先確認 key 不落地、可切換、可稽核，並對比原生 API 成本。

### know metabiz wiki

- 最佳深研順序：**Graphify → Obsidian Mind → LLM Wiki**。Graphify 可驗證跨 code/docs/schema 的 evidence graph；Obsidian Mind 值得借鑑 agent memory 的 Markdown 互動；LLM Wiki 用於比較持續建構而非即問即答的 wiki 模式。
- 先建立獨立測試 vault（不含客戶資料），設下 writeback diff review、來源連結、roll-back 與資料保留規則；不可讓任何 agent 直接改寫正式 metabiz vault。

## 明日續追清單

- **Graphify、Headroom、Obsidian Mind**：看 7/25 快照 delta、release、issue/PR 新增與是否仍有清楚 README。
- **agent-skills、awesome-claude-skills、ponytail、ECC**：判斷今天的 growth 是否持續；針對 skills repo 抽查授權與會執行的命令。
- **OmniRoute、Open Code Review**：下一次 collector 加入明確 repo seed 後再取得可比較的 API 指標；目前僅有 Trending live signal。
- **LLM Wiki**：追蹤 license 是否補齊與近期 release，未改善前維持 reference only。

## 成果檔

- API 原始資料：[repos.json](repos.json)
- Collector 摘要：[report.md](report.md)
- 可供下次比較的快照：[repos-2026-07-24.json](snapshots/repos-2026-07-24.json)

