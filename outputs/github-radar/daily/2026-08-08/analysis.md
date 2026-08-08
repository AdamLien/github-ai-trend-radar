# GitHub AI Trend Radar 分析｜2026-08-08（台灣）

## 結論先行

本次以 GitHub Search 的 10 組主題各 10 筆結果去重後取得 89 個專案，並以 `2026-08-07` 同範圍快照比對重疊專案。GitHub Trending daily（執行日讀取）中最直接相關的是 `PrimeIntellect-ai/prime-agent`、`addyosmani/agent-skills` 與 `google/skills`；Trending 是「今天的注意力」訊號，不能倒推成 8/8 的歷史星數。優先追蹤方向是：可驗證的工程流程 skills、可追溯的程式／文件知識圖、以及成本可量測的 context 壓縮。

`stars_delta` 是 8/7 → 8/9 執行快照的可比觀測值，約跨一天，並非 GitHub Trending 的「stars today」。不在前一快照的 Trending 候選標為「未量測」，絕不視為 0。

## 最值得追蹤的專案

| 分類 | 專案與動能 | 已核實用途／風險 | 對 Adam 的可用性 |
| --- | --- | --- | --- |
| Deep research | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — 84,317★，`+356`，8/8 push、MIT、v0.6.6 | README 明列 `/spec → /plan → /build → /test → /review → /ship` 的工程 skills 與驗證關卡；高動能但不可不加審核地匯入既有規範。 | 最適合比對 metabiz 的 skill 生命周期、課程的「先規格後實作」章節與 AI 辦公室 SOP。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — 104,261★，`+205`，8/7 push、Apache-2.0、v0.9.36 | README 證實它以本地 AST 把 code/docs/PDF 映成可追溯知識圖，並區分 extracted/inferred；文件語意處理可能仍使用模型或 API key。 | 可做「從 repo 到可問知識圖」demo；先以匿名化 sample 驗證，不能直接把 metabiz 私密 vault 上雲。 |
| Deep research | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) — 65,480★，`+64`，8/8 push、Apache-2.0、v0.34.0 | README 證實它在 LLM 前壓縮 tool output、log、檔案與 RAG chunk，提供 library/proxy/MCP；60–95% 是專案主張，需用本地基準重測。 | 適合 AI 辦公室與 coding-agent 成本／延遲實驗；先做前後 token、正確率與可逆性驗收。 |
| Demo content | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) — 79,561★，`+32`，8/8 push、MIT、v2.0.0 | README 顯示 2.0 是重寫的長任務 super-agent harness，編排 sub-agent、memory、sandbox 與 skills；同時對特定模型／雲服務有建議。 | 可拍「長任務如何留證據與回復」的架構 demo；不列為 metabiz 直接導入，先釐清 SaaS、資料與模型依賴。 |
| Skill candidate | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) — 16,135★，`-1`，8/8 push、Apache-2.0、v1.8.0 | README 證實它提供資料庫 MCP server 與自訂安全工具框架，可連 Gemini CLI、Claude Code、Codex；負變動不代表衰退，僅是量測窗內的淨差。 | 可萃取「唯讀 schema 探索／參數化查詢／權限界線」skill；禁止以自然語言直接授權生產寫入。 |
| Skill candidate | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) — 3,334★，`+5`，8/3 push、MIT | README 證實它把 `raw/` 來源寫入 interlinked wiki、append-only log 與 graph；主張免 API key，但仍須審查 agent 的寫入品質。 | 與 know metabiz wiki 的來源不可變、操作紀錄與人工審核方向相合；可作差異比較，不取代既有 Vault Guard。 |
| Watch | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) — 8,135★，Trending daily、8/8 push、MIT | README 證實它是 RLM coding/research agent，含持久 REPL、sub-agent、可精煉的 harness 與背景任務；前一同範圍快照沒有它，star delta 未量測。 | 值得研究其 snapshot/rollback 與持久任務設計；自我調整 harness 需要明確變更審核，不能自動套進日常流程。 |
| Watch | [google/skills](https://github.com/google/skills) — 16,553★，Trending daily、8/7 push、Apache-2.0 | README 證實為 Google 產品與技術的 Agent Skills，且明記 active development；前一快照未收錄，star delta 未量測。 | 可作 Google Cloud／RAG 課程的參考素材；只擇取可驗證、可在本機或已授權租戶重現的步驟。 |
| Reference only | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — 89,350★，`+17`，8/5 push、授權欄位未聲明、2026.7.10 | MCP server 範例／集合仍具生態參考價值，但授權欄位未聲明且不是本日最強動能。 | 用於介面與安全模式比較；不能把未核實的範例當 production connector。 |

## 可執行的內容與研究安排

- Deep research：以 `agent-skills` 對照目前的規格、測試、review、發布守門；以 `graphify` 在非機密示例專案驗證「來源 → 節點 → 邊」是否可追溯。
- Demo content：做一支「長任務不是放著跑：DeerFlow 的 sandbox、memory、rollback 要怎麼驗收」短 demo，明確標示是架構展示而不是部署推薦。
- Skill candidate：起草一個 database MCP 安全操作卡：唯讀預設、allowlist、參數化、stage → human approval → audit；另比較 `llm-wiki-agent` 對 raw source、log、結構化 wiki 的實作。
- Watch：Prime Agent 的可持久／自我精煉能力與 Google Skills 的可攜性都先做隔離 PoC；不得連客戶資料、正式憑證或自動寫入。
- Reference only：MCP servers 清單用於發現與相容性盤點，仍以官方規格、README、release 與權限模型為導入門檻。

## 風險與假陽性

- 搜尋結果含大量清單、模板與高星專案；總 stars 是累積注意力，不是採用、品質或商業需求。
- `NOASSERTION`／空白授權（例如部分 wiki、automation 專案）未列為採用候選；須先讀 LICENSE 與相依服務條款。
- 8/8 Trending 在 8/9 抓取，只能提供當前注意力，不能聲稱它是 8/8 歷史榜單；沒有相同專案的前一快照時，成長值是未量測。
- 對資料庫、wiki、agent 的 MCP 一律先做資料分級、最小權限和 staged action；任何能寫入或送出的動作保留人工批准。

## 明日追蹤清單

1. 重抓同一批候選以取得 `prime-agent` 與 `google/skills` 的首個可比 baseline，分開記錄新收錄與成長。
2. 以可丟棄的 repo 測 Graphify：至少驗證 AST edge、文件語意 edge、敏感檔排除與離線行為。
3. 對 headroom 建立 3 組固定 corpus，記錄 token、答案正確率、延遲與可逆性，才判定是否進 AI 辦公室流程。
4. 對 MCP Toolbox 編寫唯讀資料庫測試案例與拒絕案例，確認權限、SQL 範圍與 audit log。
5. 追蹤 DeerFlow 2.0 issue／release 與外部依賴變化；只有在可重現的沙盒內才測多 agent 任務。

## 資料來源與範圍

- API 搜尋與 repo 快照：[repos.json](./repos.json)（89 個去重結果），執行日快照在 [snapshots/repos-2026-08-09.json](./snapshots/repos-2026-08-09.json)。
- GitHub Trending daily：https://github.com/trending?since=daily（執行日讀取）。
- 用途、授權與安裝／架構判讀以上列專案的 README 與 GitHub repo metadata 為準；本文的建議是研究優先序，不是採購或生產導入批准。
