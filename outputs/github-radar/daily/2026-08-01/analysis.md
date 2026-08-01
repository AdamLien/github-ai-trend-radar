# GitHub AI Trend Radar 分析 — 2026-08-01

## 結論

今天值得投入的不是再找一個「全能 Agent 平台」，而是驗證三個可落地的 seam：**受治理的 coding-agent skills**、**MCP 的資料庫存取邊界**、以及 **可追溯的企業知識檢索**。首選小型實驗是：用既有非 production 資料，分別驗證 `agent-skills` 的工程 gate、`mcp-toolbox` 的 read-only DB query，以及 KAG 的引用回鏈；三者都必須保留 human approval 和 audit evidence。

- collector 以本機已登入 GitHub token、每 query `--limit 10` 成功完成，產生 **94 個去重 repo** 與 README 摘要；未發生 rate limit，也沒有降為 limit 5。
- 此 target directory 是第一次快照，collector 的 `stars_delta` 全為 0；這代表缺少同一路徑的前次基準，**不是**沒有 star 成長。因此本日依最近 push / release、issue 負荷、README 定位與實際整合摩擦排序，而非總 stars。
- GitHub Trending daily 在本次（台灣時間 2026-08-02）擷取，GitHub 不提供 2026-08-01 的可回溯 daily 頁面。其可篩選訊號是 `microsoft/AI-For-Beginners`（869 stars today）與 `bytedance/deer-flow`（204）；僅作「執行日注意力」參考，未把它誤標為 8/01 的歷史增量。
- 快照檔名為 `snapshots/repos-2026-08-02.json`，是 8/01 radar 在 8/02 執行時所寫的 API snapshot；保留原始日期以維持資料可追溯性。

## 最值得追的 10 個 repo

| 分類 | Repo | 用途與動能 | 本次指標 | 對 Adam 的可用性與風險 |
| --- | --- | --- | --- | --- |
| Skill candidate | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Coding agent 的 production engineering skills；7/26 發布 0.6.5。 | 81,223 stars；7/26 push/release；140 issues；MIT | 適合比對並抽取可遷移的 review、測試與交付 gate；不可覆寫既有 AGENTS/RTK、或不審核就安裝第三方 skill。 |
| Deep research | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | 將資料庫能力經 MCP 提供給 agent；7/28 發 v1.8.0，8/01 仍有 push。 | 16,093 stars；246 issues；Apache-2.0 | 最貼近 AI 辦公室的 governed data-access seam。先用唯讀帳號、allowlist SQL、查詢審計與無客戶資料的 POC。 |
| Deep research | [earendil-works/pi](https://github.com/earendil-works/pi) | 統一 LLM API、agent loop、TUI 與 coding-agent CLI；近期仍活躍。 | 81,843 stars；7/29 v0.83.0；8/01 push；93 issues；MIT | 可拿來比較 Codex/Pi 的任務交接、工具權限與可驗證交付。只在沙盒測試，不接私有憑證或 production。 |
| Demo content | [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | 多語言 MCP 入門教材，包含安全與 orchestration 範例。 | 16,873 stars；7/29 push；僅 7 issues；MIT | 可轉成繁中「MCP 是連接協定，不是直接授權 agent 寫資料」課程模組，配合 mOfficeAI 實例。 |
| Deep research | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 長任務 SuperAgent harness，涵蓋 sandbox、memory、tools、skills、subagents。 | 78,603 stars；8/01 push；v2.0.0（6/25）；932 issues；MIT | 可研究 AI 辦公室的研究→草稿→核准流程；高 issue 數與重 runtime 表示只能做隔離 POC，不能直接當企業底座。 |
| Deep research | [OpenSPG/KAG](https://github.com/OpenSPG/KAG) | 以 logical form / knowledge graph 補足純向量 RAG 的專業知識問答。 | 8,949 stars；174 issues；Apache-2.0；最後 push 1/28 | 對 know metabiz wiki 的多跳、可回鏈問題最有價值。先用有來源版本的 20 題 benchmark，成功條件是能回到原始證據。 |
| Demo candidate | [labring/FastGPT](https://github.com/labring/FastGPT) | RAG、資料處理與可視化 workflow 的快速 demo 平台。 | 29,221 stars；7/31 v4.15.6/push；167 issues；license API=NOASSERTION | 可作企業知識問答的速度比較 demo；採用前需讀實際 LICENSE、部署需求、資料保留與升級責任。 |
| Watch | [langgenius/dify](https://github.com/langgenius/dify) | Agentic workflow、RAG 與多模型協作 workspace。 | 150,990 stars；8/01 push；7/28 security release；922 issues；license API=NOASSERTION | 市場基準與課程比較很有用；龐大平台與 issue 負荷表示不可取代私有證據鏈與權限/核准機制。 |
| Skill candidate | [obra/superpowers](https://github.com/obra/superpowers) | Agentic skills framework 與軟體交付方法。 | 264,715 stars；7/24 v6.2.0；7/31 push；316 issues；MIT | 可把 planning/TDD/review 的精神映射進 `agent-delivery-gates`；不要整包取代本地 skill 治理或自動授權行為。 |
| Reference only | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP server reference implementations。 | 89,118 stars；7/10 release；480 issues；license API=NOASSERTION | 是協定與範例參照，不是可直接選型的 production catalog；對 mOffice / wiki 串接先看 boundary，再選個別 server。 |

## 可轉成 Adam 的行動

### Deep research

1. **MCP Toolbox × governed office data**：用假資料與唯讀 DB 帳號做「自然語言 → allowlisted 查詢 → evidence log」；驗收是每次 query 都能看見身份、SQL/工具呼叫、結果摘要與人工核准點。
2. **KAG × know metabiz wiki**：選一個已有版本與來源欄位的商務資料夾，建立 20 題多跳問題。量測引用正確率、無答案拒答、索引成本與更新流程；不要只比較回答流暢度。
3. **Pi / DeerFlow**：各跑一條隔離的「研究→草稿→human approval」工作流，記錄工具權限、失敗復原、時間與 token 成本，再決定是否值得擴大。

### Demo content

1. 「MCP server 能查資料，不等於 agent 可以任意寫資料」：以 MCP Toolbox 的唯讀/審計設計做 10 分鐘 demo。
2. 「企業 wiki 的答案要能回到哪一份文件？」：比較向量 RAG 與 KAG 的 3 個多跳問題，公開成功與失敗案例。
3. 「熱門 skills 要不要直接裝？」：以 agent-skills / Superpowers 對照現有 Codex AGENTS/RTK，示範審核與最小採用，而非一鍵覆蓋。

### Skill / backlog candidate

1. `governed-mcp-readonly-poc`：輸入資料源、帳號權限、SQL allowlist、審計欄位與 human approval，輸出可重跑的驗證報告。
2. `wiki-evidence-benchmark`：固定題庫、原始來源、答案引用、拒答理由、成本與版本；用於比較 RAG/KAG，不允許無來源的「看似正確」答案。
3. `agent-delivery-gates`：把 planning、TDD、review、變更範圍、驗證證據做成不可略過的可攜 gate，與既有規範並存。

## 風險與非訊號

- **總 stars 不是採用排序。** 首次快照沒有可靠 `stars_delta`；本報告明確不把 0 當作日增量，也不把 GitHub 搜尋排序當作熱度。
- **Trending 日份不可回填。** 本次 live Trending 是執行日（8/02），不能聲稱代表 8/01；後續應在 00:10 當下保存榜單，才能有精確的前日歷史訊號。
- **授權欄位仍需實讀。** GitHub API 的 `NOASSERTION` 不是「無授權」結論，也不是商用許可。FastGPT、Dify、MCP servers 的採用前要讀 repo LICENSE、相依授權與部署條款。
- **高 issue 數是維運訊號，不是品質判決。** DeerFlow 932、Dify 922、MCP servers 480、Superpowers 316 個 open issues，代表需要用隔離環境、版本鎖定與 rollback 設計驗證。
- **安全邊界優先。** `reverse-skill` 今日 1,360 stars 與 `hexstrike-ai` 的攻防自動化定位均不納入採用清單；第三方 skills/MCP 先審查指令、下載、網路與憑證行為。

## 明日追蹤清單

1. 在下一次 00:10 立即保存 Trending 清單與 stars-today，讓「前一日」訊號有原始證據。
2. 對固定清單（agent-skills、MCP Toolbox、Pi、DeerFlow、KAG）保留同一份基準快照，才可得到真正的 `stars_delta`。
3. 追蹤 MCP Toolbox、Pi、FastGPT、Dify 的 release/安全公告與 issue 處理速度，而非只追星數。
4. 先寫 `governed-mcp-readonly-poc` 的一頁驗收 spec；明確列出唯讀帳號、資料遮罩、審計與人工核准，再做任何連線。
