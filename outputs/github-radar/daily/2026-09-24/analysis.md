# GitHub AI 趨勢雷達分析｜2026-09-24

## 今日結論

本次以 GitHub API 搜尋、每日 Trending 與 README 快照交叉篩選 319 個範圍內專案；以下保留 8 個值得投入注意力的標的。排序依據是今日 Trending 星數、相較前一日快照的星數增量與相對成長、推送／release 新鮮度、README 可驗證性，以及 issue 負荷，而非只看累積星數。API 收集未遇到 rate-limit，因此未執行 `--limit 5` 的降載重跑。

| 專案 | 用途與動能 | 累積星數 | 風險 | 分類（擇一） | 與 Adam 課程／內容／AI 辦公自動化／know metabiz wiki 的關聯 |
| --- | --- | ---: | --- | --- | --- |
| [google/ax](https://github.com/google/ax) | Google 的宣告式 agent 編排 runtime；今日 Trending +1,376、快照 +1,285（約 12.9%），9/24 仍有推送，README 明示核心概念與協定在穩定版前可能有破壞性變更。 | 9,930 | 尚未穩定，產品／協定可能大改；不宜直接作為課程唯一基底。 | Deep research | 可拆成「受 sandbox、workspace 與 network fence 約束的 agent」課程段落；也適合評估 Metabiz 自動化工作流的隔離與稽核設計。 |
| [dream-num/univer](https://github.com/dream-num/univer) | 可嵌入的 Sheets、Docs、Slides、Base、Board 辦公 runtime，定位為 AI agent 的 Office Harness；今日 Trending +1,060、快照 +1,142（約 6.6%），9/24 推送並發布 v1.0.2，README 有繁中入口。 | 17,300 | 是 SDK／runtime 而非完整 SaaS；導入仍要自行處理權限、儲存與 agent guardrails。 | Demo content | 最貼近 AI 辦公自動化：可做「agent 在表格、文件、簡報間讀寫」實作示範，也可成為 Metabiz 報表／提案文件自動化的技術評估點。 |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 會學習的 agent memory；本雷達新進 Trending，今日 +1,607，9/24 有推送、9/21 發布 v0.10.1，README 提供文件、整合、cookbook、benchmark 與論文連結。 | 27,274 | 首日加入沒有可比快照 delta；長期記憶的資料保留、可刪除性與成本需先驗證。 | Watch | 適合作為 know metabiz wiki 的「任務記憶 vs. 可治理知識庫」比較素材；先以非敏感課程內容做小型記憶品質測試。 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Python／TypeScript 生產級 agent harness SDK，支援任意模型與雲；今日 Trending +463、快照 +432（約 5.3%），9/24 推送並發布 MCP v0.3.0。 | 8,148 | 814 個 open issues，社群與維護負荷高；跨雲／模型抽象層可能增加除錯面積。 | Deep research | 可作為 AX 的務實對照案例，延伸成「MCP、可觀測性與多模型 agent」進階內容，並評估 Metabiz 工作流的可攜性。 |
| [obra/superpowers](https://github.com/obra/superpowers) | 以可組合 skills 和初始指令組成的 coding-agent 開發方法；今日 Trending +606、快照 +554，README 明列 Codex App、Codex CLI、Claude Code、Cursor 等安裝面。 | 291,082 | 高熱度不等於適合原樣採用；401 個 open issues，且方法論可能與既有團隊 SOP 衝突。 | Skill candidate | 最適合萃取可重複的技能結構、驗證關卡與 handoff 做法，轉化為 Adam 課程實作與 Metabiz 內部技能規範，而非整包複製。 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 將程式碼索引為持久知識圖譜的 MCP server，主打 158+ 語言與低 token 查詢；快照 +408，9/24 推送，v0.11.0 於 9/15 發布，README 有 CI 與測試訊號。 | 44,811 | 606 個 open issues；效能宣稱須以 Metabiz 真實 monorepo 與權限模型驗證。 | Deep research | 可把專案、文件、SQL schema 與 repo 知識連到 coding agent，適合「know metabiz wiki × 開發知識」的檢索與脈絡化實驗。 |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 將原始文件做成 RAG、推理 agent 與自我維護 wiki 的知識平台；快照 +382，9/24 推送且發布 v0.8.2，README 直接定位 Q&A、任務與 wiki。 | 29,654 | 授權欄位為 `NOASSERTION`，商用／再散布前必須核實；653 個 open issues。 | Watch | 與 know metabiz wiki 的目標高度相符，可研究「文件入庫→問答→持續維護」鏈路；先釐清授權與資料治理才試作。 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 將程式、文件、SQL schema、設定與 PDF 轉為可查詢的知識圖譜，提供 Claude Code、Cursor、Codex skill；快照 +323，9/23 推送與發布 v0.9.67，README 有多語文件。 | 121,132 | 1,459 個 open issues；需實測大型知識圖譜的建置時間、更新一致性與資料外流邊界。 | Demo content | 可做成「讓 coding agent 先理解 codebase／文件圖譜再修改」的高辨識度示範，並為 Metabiz wiki 的結構化關聯提供實驗方向。 |

## 明日觀察清單

- **google/ax**：持續追蹤 GitHub Trending 日星數與 release／協定變更；若成長放緩，仍應保留其 sandbox 模型作為設計參考，而非立即採用。
- **dream-num/univer**：檢查 v1.0.2 的 changelog、AI agent API 範圍與 Docs／Slides 的可用程度；可安排一個小型「表格到簡報」自動化 POC。
- **vectorize-io/hindsight**：明天取得第二個快照以建立可比較的 star delta；優先檢視 memory 寫入、忘記／刪除與資料隔離文件。
- **strands-agents/harness-sdk**：觀察 MCP v0.3.0 release 後 issue 的新增／關閉節奏，確認高 issue 數是活躍迭代或未清償負債。
- **Tencent/WeKnora**：先核實 repo 的正式授權文件，再決定是否允許進入 Metabiz wiki 的試驗清單。
- **DeusData/codebase-memory-mcp** 與 **Graphify-Labs/graphify**：以同一個非敏感 Metabiz 範例 repo 比較索引時間、查詢正確性、token 節省與更新成本，避免僅依 README 效能主張決策。

## 資料註記

- `stars today` 為 GitHub Trending 當日訊號；`快照 +N` 為與此前一個日資料夾的星數差，不可混為同一指標。
- 新進 Trending 的 Hindsight 尚無本雷達前日基線，故以每日 +1,607 與 README／release／推送訊號列為觀察，不假稱其快照成長。
- open issues 只反映未關 issue 數，不能單獨推論品質；本報告把它列為後續驗證與維護負荷訊號。
