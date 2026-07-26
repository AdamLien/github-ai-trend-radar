# GitHub AI Trend Radar 分析 — 2026-07-26

> 分析基準：GitHub Trending `daily` 的 **stars today** 是 7/26 的注意力訊號；API `star delta` 是 7/25 快照到本次蒐集的可比增長，兩者不能相加。本次以已登入 GitHub 憑證蒐集，十組查詢各取 10 筆後去重為 89 個 repo，未遇 rate limit；README 摘要、release、push、issue 與 license 已收進 API 快照。Trending 原始頁只保留與 AI／agent／coding automation 範圍相符的五個補充 repo。

## 結論

今天最值得追的不是再選一個通用 agent framework，而是三條可直接轉成 Adam 工作成果的線：

1. **可查詢的專案／知識脈絡**：`graphify` 的 `+1,190` 與當日 release，使「code + 文件 + schema + PDF」的 knowledge graph POC 成為 know metabiz wiki 的第一優先研究。
2. **把代理工作方式變成可驗收技能**：`superpowers`、`ECC`、`claude-obsidian` 分別覆蓋開發 SOP、agent harness 與 Markdown 知識工作流；可抽取規範，不應整包安裝。
3. **有治理邊界的開發自動化**：Trending 的 `open-code-review`（840 today）適合示範「規則兜底＋LLM 輔助」；`mcp-toolbox` 適合另做唯讀資料 POC，而非直接連 production。

## 最值得追的 repo

| Repo | 分類 | 動能／總 stars | 用途與可用性 | 風險／判讀 |
| --- | --- | --- | --- | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | API `+1,190`／96,255；7/26 push、v0.9.27 release | 將 code、文件、SQL schema、config、PDF 變成可問的 knowledge graph；最貼近 know metabiz wiki 的「跨資產脈絡」需求。 | Apache-2.0 是正面訊號；先用非敏感 repo 驗證索引時間、答案可追溯性與權限隔離。 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Deep research | API `+1,035`／77,982；7/26 push、v0.82.1（7/25） | 統一 LLM API、agent loop、TUI 與 coding-agent CLI；可作為課程中「agent harness 的最小組成」對照。 | MIT、issue 僅 81，維護訊號佳；仍須把模型成本、工具權限與長任務可靠性分開實測。 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Deep research | API `+14`／16,023；v1.7.0（7/16） | 資料庫 MCP server，是 AI 辦公室自動化「能查資料但不裸連 DB」的治理候選。 | 動能非最高且有 256 issues；POC 僅可用唯讀帳號、查詢白名單、audit log，禁止 production 寫入。 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skill candidate | API `+992`／261,462；v6.2.0（7/24） | 可組合的 coding-agent skills 與開發方法；很適合反推 Adam 課程的任務定義、驗收與回退模板。 | MIT；先挑「研究→變更→測試」單一工作流萃取，避免把外部方法論直接覆蓋既有 repo 規範。 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skill candidate | API `+770`／233,541；7/26 push | 對 skills、memory、security、research-first 的 agent harness 操作系統；可用於 AI 辦公室自動化的 SOP 素材。 | MIT、issue 88；高星數不等於每個規則都適配，需特別審閱其權限與記憶處理。 |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Skill candidate | API `+74`／9,952；最近 code push 5/28 | Obsidian + Claude Code 的自組織 second brain；可借鏡 ingest、連結、歸檔規則，直接服務 know metabiz wiki。 | MIT；維護新鮮度偏弱，採「設計參考」而非 vault 的核心依賴。 |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Demo content | Trending **840 today**／13,579；7/26 push | deterministic pipeline + LLM agent 的行級 code review，可做「AI code review 不該全自動」的課程／內容 demo。 | Apache-2.0；需實測中文程式碼、CI 整合與 false positive，Alibaba 規模不可直接外推中小團隊。 |
| [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | Demo content | Trending **189 today**／15,341；7/25 push | 多家生成式 AI provider 的統一介面，適合一支「模型供應商替換層」的入門 demo。 | MIT；只適合作為 API abstraction 參考，需另驗證 streaming、tool calling、成本與 provider capability 落差。 |
| [block/buzz](https://github.com/block/buzz) | Watch | Trending **1,705 today**／12,817；7/26 push | hive-mind communication platform，是 agent coordination 的強注意力訊號。 | Apache-2.0，但 674 open issues、定位仍抽象；先看架構與實際協作流程，不列入採用或課程承諾。 |
| [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | Reference only | API `+9`／8,684；最近 push 7/23 | MCP 規格與 schema 的權威參考；所有 MCP POC 的 protocol 對照來源。 | license 欄位為 `NOASSERTION`；它是標準／文件來源，不是要直接部署的產品。 |

## 對 Adam 的可用行動

### 課程與內容

- 做一個「skills 不是 prompt」單元：用 `superpowers`、`ECC` 對照輸入、工具權限、驗收、回退與記憶邊界。
- 做一支 hybrid code review demo：先跑可解釋規則，再讓 `open-code-review` 類型 agent 補脈絡，最後保留人工合併門檻。
- 做顧問式比較內容：`graphify`／knowledge graph 和一般 RAG 的差別，是依賴關係、schema、變更影響這類可追溯問題。

### AI 辦公室自動化

- `mcp-toolbox` 只開唯讀、最小權限的 sandbox database；記錄每個 query，先驗證資料分級與審計是否足夠。
- 用 `pi` 的 components 畫出 internal agent 的最小架構，但不要直接把具寫入能力的工具接進工作系統。
- 將 `ECC`／`superpowers` 抽成「研究先行、明確驗收、變更後驗證」三段式內部模板。

### know metabiz wiki

- 第一個 POC：以一個非敏感 repo + Markdown 文件 + 已知 10 題，評估 `graphify` 的引用可追溯性、索引成本與權限分區。
- 從 `claude-obsidian` 借鏡 ingestion 與 linking 規則；由既有 wiki 工作流掌握寫入，避免新增必經外部服務。

## 風險與假陽性

- Trending 是滑動日窗注意力，不是付費需求、資安通過或長期維護承諾；`stars today` 不能和 API delta 相加。
- 清單／方法論 repo（例如 skills 集合）容易高速成長，仍要逐一檢查下游 skill 的 license、工具權限和可驗收性。
- `block/buzz` 的高 Trending 注意力與大量 open issues 同時存在，故維持 Watch；`mcp-toolbox` 的價值在治理設計而非今日最高增長。

## 明日追蹤清單

1. `graphify`：release 後 issue 回覆、索引 POC 與可追溯回答品質。
2. `pi`：v0.82.1 後的 CLI／tool permission 變化與持續 star delta。
3. `superpowers`、`ECC`：哪些 skill 有清楚輸入／輸出／安全界線，可轉成自家 SOP。
4. `open-code-review`：CI installation、規則與 LLM 結果的可控性。
5. `mcp-toolbox`：read-only database、query allowlist、audit log 是否能落在 metabiz 邊界。
6. `block/buzz`：issue 收斂與是否有可重現的 agent coordination demo。

## 資料產物

- [GitHub API 合併快照](./repos.json)：89 個去重 repo，使用 7/25 快照計算可比 delta。
- [Collector 原始報告](./report.md) 與 [快照](./snapshots/)：可重跑、可比對的 API 證據。
- [GitHub Trending 原始頁](./trending.html) 與 [相關 Trending 補充結果](./trending-runs/)：當日 attention signal 與五個範圍內 repo 的 API metadata。
