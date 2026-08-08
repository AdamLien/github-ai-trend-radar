# GitHub AI Trend Radar 分析 — 2026-08-07（台灣）

## 結論先行

本日最值得投入「可驗證試作」的不是單純高星專案，而是把 AI coding agent 的工作流程、知識脈絡與 MCP 介面接起來的四條線：`addyosmani/agent-skills`／`obra/superpowers`（工程方法與 skills）、`Graphify-Labs/graphify`（可解釋的程式碼知識圖譜）、`GLips/Figma-Context-MCP`（設計到程式的上下文）、`diegosouzapw/OmniRoute`（多供應商模型 gateway）。

這一批資料不應被解讀為 8/7 的 GitHub Trending 歷史排名：collector 於 2026-08-08 以 GitHub API 取得 89 個搜尋結果，並建立首個 8/8 快照；8/6 沒有同範圍快照，故 `stars_delta` 與「stars today」均無可比較基線，標示為**未量測**而非 0。執行當下觀察的 `https://github.com/trending?since=daily` 則出現 `addyosmani/agent-skills`、`obra/superpowers`、`mattpocock/skills`、`google/skills` 等，作為當日趨勢交叉訊號，不回填為 8/7 歷史事實。

## 資料品質與篩選

- 搜尋：10 組 AI／MCP／skills／agent／RAG／wiki／developer automation 查詢，每組最多 10 筆，去重後 89 repo；另依人工 watchlist 加入 OmniRoute，合計 90 repo。
- 動能：原始 89 個 repo 中 25 個的 `pushed_at` 落在 8/7 UTC；OmniRoute 在納入時的 API 快照為 8/8 UTC。沒有前一日可比集合，因此不以總 stars 排名，也不假造日增星。
- 維護與風險：84/89 有 SPDX license；五個 license 不明項目只保留觀察。release、push、issue 數為 API 擷取時的快照；README 用途依 repo 描述與既有公開定位交叉判讀，採用前仍需讀完整 README、授權與安全模型。

## 優先追蹤（按策略價值，不按總 stars）

| 分類 | Repo | 目前訊號 | 對 Adam 的可用性與風險 |
| --- | --- | --- | --- |
| Deep research | [Graphify](https://github.com/Graphify-Labs/graphify) | 104,056 stars、8/7 push 與 release、Apache-2.0；定位為把程式、SQL、文件與 PDF 轉為可查詢且可解釋的知識圖譜。 | 最貼近 know metabiz wiki 與程式碼理解；先以一個非敏感 repo 驗證圖譜品質、增量更新與資料外送邊界。不要直接將客戶／生產資料匯入。 |
| Deep research | [agent-skills](https://github.com/addyosmani/agent-skills) | 83,961 stars、8/6 push、MIT，且在執行當下 Trending daily 出現。 | 可拆成 Adam 課程的「技能如何約束 agent」示範，亦可比對既有 Codex skills；風險是通用工程準則不等同 metabiz 的商業規則。 |
| Deep research | [superpowers](https://github.com/obra/superpowers) | 268,797 stars、8/8 push、MIT，Trending daily 交叉訊號。 | 很適合做「方法論 vs. 專案 skill」的內容比較與開發流程研究；高採用不代表與現行工具鏈、授權或資料契約相容。 |
| Demo content | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 42,888 stars、5,719 forks、8/8 push、MIT；v3.8.49 於 7/30 發布，提供 OpenAI-compatible gateway、quota-aware routing、MCP/A2A 與多種 coding CLI 整合。 | 很適合做「自動路由與模型成本控制」的受控 demo；460 open issues（含 PR）與龐大功能面代表採用負擔。先用無敏感資料的本機 sandbox，逐項檢查 API keys、供應商資料流、fallback、免費額度與可選 MITM/憑證設定；不要接入客戶或生產環境。 |
| Demo content | [Figma Context MCP](https://github.com/GLips/Figma-Context-MCP) | 15,609 stars、8/7 push、MIT；將 Figma layout 交給 Cursor 等 coding agent。 | 可做 10 分鐘設計→前端上下文 demo；需先確認 Figma token、檔案權限與生成程式碼品質，不將 demo 視為產品設計驗收。 |
| Skill candidate | [MCP Registry](https://github.com/modelcontextprotocol/registry) | 7,121 stars、8/6 push/release；社群 MCP registry。 | 可萃取為「MCP 安裝前審核」skill：來源、權限、授權、網路與 secrets checklist；目前 license 欄位為 NOASSERTION，不能當成已完成授權審查。 |
| Demo content | [SurfSense](https://github.com/MODSetter/SurfSense) | 15,800 stars、8/7 push；NotebookLM 替代品、含 API/MCP 與多平台研究來源。 | 可作 AI 辦公室的研究來源比較 demo；license 為 NOASSERTION，且外部平台連接與資料保留需先審核。 |
| Watch | [Yuxi](https://github.com/xerrors/Yuxi) | 6,409 stars、8/7 push、MIT；LightRAG、knowledge graph、PDF/Neo4j/MCP 的多租戶 agent harness。 | 與知識庫產品方向吻合，但面向很廣；先確認多租戶隔離、權限模型、索引成本與中文文件成熟度，再做小範圍評估。 |
| Watch | [NeoWiki](https://github.com/ProfessionalWiki/NeoWiki) | 20 stars、8/7 push、GPL-2.0，宣稱協作 wiki＋知識圖譜。 | 可觀察 wiki 資料模型；星數低、120 open issues 相對高且 GPL-2.0 可能影響嵌入策略，暫不導入。 |
| Reference only | [llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 3,329 stars、MIT；主打以 Claude/Codex/Gemini 維護持久互連 wiki。 | 適合用來對照「agent 維護知識」的內容敘事；最後 push 為 8/3，尚不足以作為近期採用判斷。 |

## 對課程、內容與 AI 辦公室的可行題目

1. **課程／demo：一個 Figma 畫面到可檢查元件的 agent 流程。** 以 Figma Context MCP 提供局部 layout context，再用既有前端實作與可視驗收比較；成功條件是可指出差異與權限需求，不是生成畫面看起來相似。
2. **內容：Skills 到底是提示詞集合還是可驗證流程？** 對照 agent-skills 與 superpowers，示範「適用範圍、輸入、停損線、驗證證據」；避免把社群方法直接宣稱為企業流程。
3. **AI 辦公室／know metabiz wiki 深研：Graphify 的本地知識圖譜 POC。** 只使用可公開、可丟棄的樣本 repo／文件；驗證問題回答能否連回可解釋的來源邊，而不是僅評估回答流暢度。
4. **Skill 候選：MCP 來源與權限審核卡。** 固化「來源、權限、授權、秘密資料、資料出境、回滾」六欄；這是重複流程，適合做成 project-local skill，尚不自動安裝任何 server。
5. **Demo：單一 agent 任務的 provider fallback 與成本帳。** 以 OmniRoute 在本機、無敏感提示詞下比較固定模型與 `auto`；驗收是可重現地列出實際路由、失敗切換、延遲、token／成本與資料外送，而不是只證明請求成功。

## 明日追蹤清單

- 以相同輸出資料夾再跑一次，取得首個可比較的 `stars_delta`；優先看上述 9 個 repo 的絕對增星與相對增長。
- 對 Graphify、agent-skills、superpowers 各讀 README、最新 release／issue，記錄安裝面、授權、外部服務與資料處理限制。
- 對 OmniRoute 驗證最小本機安裝：不匯入既有金鑰、不開啟 MITM、不用免費額度宣稱作生產成本預測；記錄單一可丟棄任務的路由與供應商資料流。
- 比對 GitHub Trending daily 與 API 搜尋集合的交集；僅把交集當作「當下注意力」訊號，不倒灌成歷史日榜。
- 若要啟動 POC，先寫一個可驗收情境：使用者、非敏感樣本、預期可見結果、權限限制與 stop line；未達者不進入產品或客戶資料。
