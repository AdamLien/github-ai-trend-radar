# GitHub AI Trend Radar — 2026-07-17（台灣）

## 結論

本日最強訊號不是再找一個通用 agent framework，而是三條可立刻轉成 Adam 工作流的路線：**coding skill 品質治理（Hallmark / agent-skills / Superpowers）**、**可追溯的知識圖與 code context（Graphify / code-review-graph）**，以及 **agent 可嵌入產品的 SDK 層（Copilot SDK）**。

本次以 GitHub Trending daily 頁（於 2026-07-18 擷取，故 `stars today` 是當下滾動 24 小時訊號）加上 GitHub API 搜尋快照完成。API collector 成功寫入 44 筆 repo；這是 `daily/2026-07-17` 的第一筆基線，所有 `stars_delta=0` 僅代表尚無前一筆快照，**不可解讀為 2026-07-17 的零成長**。

## 今日優先清單

|分類|Repo|動能 / 規模|用途與為何值得看|風險|
|---|---|---:|---|---|
|Skill candidate|[Nutlope/hallmark](https://github.com/Nutlope/hallmark)|Trending +1,486 today；11,752★|給 Claude Code、Codex、Cursor 的 anti-slop 設計 skill；近期 Trending 最強的「把 agent UI 產出拉回可用設計」訊號。|最後 push 為 6/26；先以審查規則/課程 demo 評估，不直接當設計系統。|
|Deep research|[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)|89,944★；API 首基線|把 code、schema、文件、圖片/影片聚成可查詢 knowledge graph，明確涵蓋 Codex、Cursor 與 GraphRAG。對大型 repo 與 wiki 證據鏈最有價值。|527 open issues；不可把 metabiz 私密資料直接送入，先驗證權限、刪除、provenance 與資料外流。|
|Skill candidate|[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)|78,938★；7/17 有更新|production-grade coding-agent skills，涵蓋 Claude Code、Codex、Cursor。可萃取為 Adam 課程的「技能不是 prompt」案例與內部低權限 skill 審查清單。|124 open issues；技能需逐份審核工具權限與 side effect。|
|Deep research|[tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)|Trending +57 today；19,662★；7/17 有更新|local-first code intelligence graph，MCP/CLI 將 agent 讀取範圍縮到必要上下文；很適合和既有 codebase-memory 工作法比較。|131 open issues；需以 Adam 真實 repo benchmark context reduction，勿只採信宣稱。|
|Demo/content idea|[github/copilot-sdk](https://github.com/github/copilot-sdk)|Trending +234 today；9,761★；7/17 有更新|把 Copilot agent 嵌入應用/服務的多平台 SDK；可做「IDE agent 到產品內 agent」教學。|239 open issues；GitHub/Copilot 產品依賴與授權成本需獨立確認。|
|Watch|[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)|Trending +528 today；27,240★|長期個人化教學 agent，熱度高，適合拆成課程互動、學習歷程與知識庫治理的內容題材。|最後 push 7/09；教育成效與資料隱私不能由 stars 推論。|
|Reference only|[openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)|Trending +431 today；66,246★；7/17 有更新|本地/開放模型 coding agent 的重要比較基準。|涉及本機執行與工具權限；不是可無審核導入的辦公室自動化方案。|
|Reference only|[OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)|Trending +1,077 today；74,646★|高熱度開源剪輯器，可作 AI 內容製作工具鏈觀察樣本。|與核心 AI/MCP/knowledge scope 關聯較弱；351 open issues，暫不投入工程評估。|
|Watch|[googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)|15,970★；7/17 有更新|資料庫 MCP server，是「AI 辦公室自動化接企業資料」的可研究參考。|245 open issues；資料庫權限、SQL guardrail、audit log 必須先做。|
|Reference only|[zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)|57,339★；7/17 有更新|local/on-prem RAG、skills、tools、MCP 的整合參考，適合私有知識庫架構比較。|架構面廣；不要因「private」字樣跳過實際模型、向量庫、遙測與資料流審查。|

## 其他重要 API 發現

- [obra/superpowers](https://github.com/obra/superpowers)（256,506★、MIT、7/17 有更新）仍是 agentic skills / SDLC 方法論的高影響力參考；適合比較流程而非直接全量安裝。
- [langgenius/dify](https://github.com/langgenius/dify)（149,159★、7/17 有更新）與 [deepset-ai/haystack](https://github.com/deepset-ai/haystack)（25,925★、7/17 有更新）是 workflow/RAG/orchestration 架構基準；前者偏產品平台，後者偏可組裝 pipeline。
- [kdsz001/OpenWiki](https://github.com/kdsz001/OpenWiki)（590★、MIT）是本機 Mac 知識管理的 watch；規模小，應先確認它是個人工具而非 metabiz wiki 的 source-of-truth 替代品。
- [OpenSPG/KAG](https://github.com/OpenSPG/KAG)（8,913★、Apache-2.0）值得用作 knowledge-graph RAG 的技術參考，但最近 push 為 1/28，優先度低於仍快速更新的 Graphify。

## 對 Adam 的可用行動

1. **課程與內容**：做一支「同一需求下，沒有品質 skill / 使用 Hallmark」的前後對照；再用 agent-skills 解析可審核 skill 的結構。
2. **AI 辦公室自動化**：把 MCP Toolbox 當 database connector 研究樣本，先設計 read-only identity、approved query、audit log、結果遮罩四個 guardrail；不要直接接正式 ERP。
3. **know metabiz wiki**：用去識別化小子集做 Graphify 或 code-review-graph PoC，評估來源連結、權限切割、更新/刪除同步與回答可追溯性。wiki 原始證據仍須保留為 source of truth。
4. **Agent coordination**：Superpowers、Dify、Haystack 均可作流程/編排參考；先以既有 board + human approval 為主，不因單一熱門 repo 改寫任務權責。

## 明日續追

- Hallmark：是否持續在 Trending、是否有新 release / 文件更新。
- Graphify：issue 收斂、私有資料處理與本地/雲端資料流；決定是否啟動去識別 PoC。
- code-review-graph：用一個真實但非敏感 repo 驗證 MCP context reduction。
- agent-skills / Superpowers：挑一個低權限 skill 做安裝前審查樣板。
- Copilot SDK：版本、auth/計費與可嵌入場景是否出現明確範例。
- MCP Toolbox：資料庫 read-only 和 policy/audit 控制是否有可複用實作。

## 資料與限制

- Collector：44 repos，10 組指定 query；輸出見 `repos.json`、`report.md` 與 `snapshots/repos-2026-07-18.json`。
- 初次嘗試 `--limit 10` 在約 50 筆後因遠端斷線失敗；使用已登入 GitHub token 以 `--limit 5` 重跑成功。這不是 rate limit。
- API metrics 是 2026-07-18 擷取時的快照；Trending `stars today` 亦為擷取時的 rolling 24-hour 值，不能回溯重建已結束的 7/17 歷史頁面。
