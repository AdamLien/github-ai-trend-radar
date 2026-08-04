# GitHub AI Trend Radar 分析 — 2026-08-04

## 判讀範圍與訊號

- 本日以 GitHub Trending daily 頁面作為即時趨勢參考，並以十組 AI/MCP/skills/agent/RAG/wiki/developer automation 查詢蒐集 GitHub API 資料；共 89 個去重 repo。
- `repos.json` 的 API snapshot 日期是 **2026-08-05**（collector 的執行日期），但本報告的 editorial target 是台灣時間 **2026-08-04**。GitHub Trending 不提供歷史日快照，故不可把今天看到的 Trending 排名倒推為 8/04 的歷史排名。
- 此目錄是第一份可用完整基線；89 個 repo 僅 5 個有 `stars_delta > 0`，最大為 +2。這不是「沒有成長」，而是缺少同一集合的前日快照；本日不以 delta 排名，優先看 8/04 push、近期 release、README 定位、issue 負荷、授權和與 metabiz 工作的貼合度。
- 以下 README 以即時首段/定位檢查，release、issues、stars 為本次 API snapshot；stars 代表開發者注意力，不等於商業需求或可直接採用。

## 值得追蹤（依工作可用性與維護訊號，不依總 stars 排名）

| 分類 | Repo | 用途與動能 | 指標（stars / 更新 / release / issues） | 風險與 Adam 的可用性 |
| --- | --- | --- | --- | --- |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | README 與描述都明確主打把 code、docs、SQL、config、PDF 轉成可解釋的知識圖譜，並支援 Codex/Claude Code/Cursor；與 know metabiz wiki 的「可追溯企業知識」最貼近。 | 102,327 / 8-01 / v0.9.32（8-01）/ 803 | Apache-2.0，適合先做「一個小型 wiki + codebase」研究；803 open issues 代表不宜直接承接核心資料契約。 |
| Skill candidate | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | README 明確將 senior engineering workflow、quality gates 和 best practice 封裝成 coding-agent skills；8-04 更新且同日有 v0.6.6 release。 | 81,601 / 8-04 / v0.6.6（8-04）/ 142 | MIT。可拆解為 metabiz 的「研究→驗證→交付」skill 設計參考；不可直接複製其工作規則到客戶資料。 |
| Demo content | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 將 tool output、logs、檔案和 RAG chunks 壓縮後再進 LLM；README 與定位可做「AI 辦公室 token 成本」實測主題。 | 64,674 / 8-04 / v0.33.0（7-29）/ 629 | Apache-2.0。先以非機敏 mCRM/文件樣本量測品質與 token；宣稱的節省比例不是本次驗證結果。 |
| Demo content | [earendil-works/pi](https://github.com/earendil-works/pi) | 統一 LLM API、agent loop、TUI 和 coding-agent CLI；8-04 push、issue 相對低，適合拆解 agent loop demo。 | 83,440 / 8-04 / v0.83.0（7-29）/ 77 | MIT。可做「同一任務切換模型與工具」課程材料；需先比對既有 Codex/OpenCodex 選型，避免新增另一套日常入口。 |
| Deep research | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | README 標示 MCP Toolbox for Databases；資料庫 MCP 的 provider、權限與查詢邊界值得深查。 | 16,116 / 8-04 / v1.8.0（7-28）/ 252 | Apache-2.0。可研究作為 Odoo/資料源 read-only MCP 的對照；不得以它直接連 production 或略過 metabiz staged-action 流程。 |
| Watch | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | README 是長時程 SuperAgent，含 sandbox、memory、tools、skills、subagents 和 gateway；是 orchestration 架構參考。 | 79,274 / 8-04 / v2.0.0（6-25）/ 959 | MIT，但 issue 量高且 release 不如前四個新；先畫架構/權限模型，不導入。 |
| Watch | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | README 主張自動建立、持續維護個人 knowledge base，而非每次從零 RAG；很適合對照 know metabiz wiki 的人審與來源證據。 | 15,852 / 8-02 / v0.6.7（8-02）/ 220 | 無明確 SPDX license，且是桌面產品；僅做互動與資料模型研究，不能採用或混入公司知識。 |
| Reference only | [activepieces/activepieces](https://github.com/activepieces/activepieces) | AI agents、MCP 與 workflow automation 的廣泛平台參考；8-04 push，適合拿來比較工作流 product surface。 | 23,574 / 8-04 / 0.86.3（7-17）/ 432 | 授權為 NOASSERTION，且範圍很廣；不列為導入候選，只保留為 AI 辦公室自動化內容的比較案例。 |

## 對 Adam 工作的轉換

- **課程與內容**：做一支「agent skills 不是 prompt：quality gate 如何可重複」短 demo（`agent-skills`），再以 `pi` 做最小 agent loop 對照；`headroom` 可延伸為成本與可觀測性內容，但必須先實測。
- **AI 辦公室自動化**：以 `activepieces` 作為流程編排 UI 的 reference，以 `mcp-toolbox` 檢驗資料 MCP 的 read-only、授權與 audit 設計；兩者都不是 production 導入決策。
- **know metabiz wiki**：優先 deep research `graphify` 的來源關聯與可解釋 edge，並用 `llm_wiki` 反向檢驗「自動維護」是否仍保留來源、人工核准與敏感資料隔離。

## 明日追蹤清單

1. 用同一套 query 與同一輸出目錄重跑，取得第一個可比較的 24 小時 `stars_delta` 與相對成長率。
2. 對 `graphify` 建立一個不含客戶資料的小型 POC；記錄 ingestion、可追溯連結與 query 品質，不作生產連線。
3. 比較 `agent-skills`、現有 Codex skills 與 metabiz quality gates 的重疊，先提出一個可 demo 的「evidence-first research」skill 草案。
4. 追查 `deer-flow` 的 issue 組成與 v2.0.0 後維護節奏；若無明顯收斂，維持 Watch。
5. 在任何 wiki/automation 導入評估前，先確認 SPDX license、資料落點、權限模型與 audit trail。
