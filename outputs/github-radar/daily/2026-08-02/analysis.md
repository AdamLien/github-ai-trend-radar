# GitHub AI Trend Radar 分析（目標日：2026-08-02）

## 本次判讀

- 本次 collector 以已登入的 GitHub token 執行；原本 `--limit 10` 的第一輪未寫出完整產物，依流程改以 `--limit 5` 完成，產出 44 個去重 repository。這是搜尋樣本，不是完整 GitHub Trending 歷史榜單。
- 快照實際建立於 2026-08-03（台灣時間），所以檔名為 `snapshots/repos-2026-08-03.json`；目標目錄仍為 2026-08-02。GitHub Trending 的 daily 頁面只能取得執行當日內容，無法回溯目標日，故不把它當成 8/2 的歷史 stars-today 證據。
- 所有 `stars_delta=0` 都是此目錄的首次有效快照基線，**不是**「沒有成長」。本輪排序改看問題契合度、近期 push／release、文件定位、授權與維運訊號；下一輪同目錄快照才可比較可用的 delta。

## 最值得追的 8 個項目

| 分類 | Repo | 用途與動能 | 總 stars | 風險／採用判斷 |
| --- | --- | --- | ---: | --- |
| Deep research | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 面向 Codex、Claude Code、Cursor 的 production engineering skills；MIT，v0.6.5（7/26），topics 直接覆蓋 skills 與 coding agents。 | 81,326 | 7/26 後未見 push，且 144 open issues；先拆解其 skill 邊界與授權，再挑 1–2 個工作流做本地對照。 |
| Deep research | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | 資料庫 MCP server，Apache-2.0；v1.8.0（7/28）且 8/1 有 push，適合研究受控資料查詢與工具治理。 | 16,102 | 246 open issues；不可直接接 production 或 customer database，先以唯讀、假資料的 mOfficeAI／metabiz wiki demo 驗證。 |
| Deep research | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 長任務 SuperAgent harness，8/2 有 push，涵蓋 sandbox、memory、tools、skills、subagents，適合評估 Deep Research 的架構切分。 | 78,946 | 940 open issues，整合面大；先做架構研究，不把它視為可直接導入的產品底座。 |
| Demo content | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Obsidian + Claude Code 的本機 Markdown knowledge graph；MIT，v2.1.0（7/31），與 know metabiz wiki 的「來源→連結→歸檔」示範高度貼合。 | 10,284 | 124 open issues；內容 demo 應用非敏感範例 vault，不能把客戶資料或未核准內容交給外部模型。 |
| Demo content | [activepieces/activepieces](https://github.com/activepieces/activepieces) | AI agents、MCP 與 workflow automation；8/2 有 push，約 400 MCP server 的定位，適合做「AI 辦公室自動化」選型內容。 | 23,551 | 授權欄位為 `NOASSERTION`、437 open issues；先確認商業授權、雲端與憑證邊界，不直接宣稱為 n8n 替代。 |
| Skill candidate | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Claude Code 設定與監控 CLI；8/2 有 push，適合萃取「初始化、規範、檢核」可重複的 coding-agent onboarding 工作流。 | 30,057 | 最近 release 顯示 2025-11，217 open issues；只借鑑流程與模板，需以 Codex 現有 SKILL/AGENTS 邊界重新驗證。 |
| Watch | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | Apache-2.0 的 agentic RAG／orchestration；v3.0.0（7/20）、8/1 有 push，適合研究可控 retrieval、routing、memory。 | 26,090 | 110 open issues，框架導入成本高；先以單一「知識庫問答→來源證據」垂直流程 benchmark。 |
| Reference only | [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Agent production 原則與 context／memory 思考框架，適合作為課程與架構審查的 checklist。 | 25,033 | Repo 最後 push 為 2025-09，且授權欄位 `NOASSERTION`；僅作方法論參考，不當成執行依賴。 |

## 對 Adam 工作的可用性

- **課程／內容：** 用 Claude Obsidian 做「自己的 Markdown 知識庫如何讓 coding agent 可讀、可追溯」；再以 agent-skills 對照「可重複流程」與「不可外包的產品決策／資料契約」。
- **AI 辦公室自動化：** Activepieces 先做沙箱流程，例如表單→摘要→人工核准→草稿；MCP Toolbox 僅研究唯讀資料庫工具與最小權限模式。
- **know metabiz wiki：** Haystack/KAG 可作後續 RAG 與知識圖譜的技術參考，但本輪不建議把現有 wiki 搬遷或接入任何 production connector。
- **Deep research：** DeerFlow 值得拆成「長任務規劃、子代理協作、記憶／sandbox 隔離」三個設計議題，與現行 Codex 工作流逐項比對，而不是直接採用。

## 明日追蹤清單

1. 同一目錄重跑 collector，取得可比較的 `stars_delta`、fork delta；以 delta、近期 push/release 重新排序。
2. 追蹤 agent-skills 的 issue/PR 活躍度與 skill 格式，選一個低風險工程流程做本地 PoC。
3. 檢查 Activepieces 的正式授權條款、self-hosted 安全模型與 MCP credential handling。
4. 為 MCP Toolbox 設計「唯讀資料庫→可審計回答」的小型 demo，不連 production。
5. 在非敏感 Obsidian vault 比較 Claude Obsidian 與 metabiz wiki 的來源、連結、審核與回寫責任邊界。

## 證據與限制

- Repository 數字、topics、授權、push、release、issues 來自本次 collector 的 `repos.json` 快照；README 本輪未另抓取，故不據此主張 README 品質。
- Live GitHub Trending daily 頁於 2026-08-03 可存取，但 GitHub 不提供目標日 2026-08-02 的歷史 daily 清單；因此 stars-today 無法作為本報告的歷史排名訊號。
