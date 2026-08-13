# GitHub AI Trend Radar 分析 — 2026-08-13

> 蒐集執行於台灣時間 2026-08-14；GitHub Trending daily 是當下注意力訊號，並非可回溯重建的 8/13 歷史榜。以下排名重視同一累積快照下的星數增量、Trending 當日星數、更新與 release 活躍度，不以總 stars 排序。

## 本日判讀

- 本輪保留 165 個累積候選；Daily Trending 新增 6 個範圍內專案。新入榜者沒有同範圍前日基線時，成長一律標為「未量測」，不是 `+0`。
- `diagram-design` 的快照增量 `+4,354`、Trending `+4,504`，是明確的 Claude Code 視覺化工作流訊號；`macro` 雖僅 2,473 stars，卻有 `+1,052` / Trending `+1,180`，代表早期高動能而非成熟度保證。
- 知識工作流呈兩條可互補路線：`kepano/obsidian-skills` 把 agent 接入 Obsidian 開放格式；`Graphify`、`Semantica` 與 `RAGFlow` 則分別代表可查詢程式知識圖、可問責的圖原生 context、企業 RAG context layer。

## 最值得追蹤的專案

| 分類 | 專案與動能 | 為何值得追 | 風險與 Adam 可用性 |
| --- | --- | --- | --- |
| Skill candidate | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — 13,470 stars，`+4,354`，Trending `+4,504`，8/13 有推送 | 29 種可編輯 HTML/SVG 圖解型別，適合把抽象 AI 工作流變成可審閱產物 | MIT、僅 9 open issues；先驗證輸出品質與品牌 token。可做 Codex 圖解 skill、課程「AI 產圖不是 Mermaid」示範。 |
| Deep research | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) — 6,286，`+746`，Trending `+727`，8/11 `v0.6.5` | 圖原生 context 與可問責 AI，對資料來源、關係與證據鏈的設計特別相關 | MIT、70 open issues；需先做小型 corpus 的 provenance/E2E 評估，才可談 metabiz wiki 導入。 |
| Watch | [macro-inc/macro](https://github.com/macro-inc/macro) — 2,473，`+1,052`，Trending `+1,180`，8/12 release | 把郵件、聊天、文件、任務、agents、CRM 與共同記憶放進一個 workspace，具 AI 辦公室流程研究價值 | AGPL-3.0 與早期產品風險；研究其工作流與資料邊界，不直接混入 mCRM 客戶資料。可做「AI office OS」內容比較。 |
| Deep research | [stablyai/orca](https://github.com/stablyai/orca) — 44,720，`+1,130`，8/11 `v1.4.180` | 固定 watchlist；並行 coding agents 的 ADE，與多代理協作實驗直接相關 | MIT，但 3,741 open issues，需區分社群需求與可維護性。可用隔離 demo 比較 agent fleet 成本與可觀測性。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — 105,949，`+370`，8/13 `v0.9.42` | 對程式碼、文件、SQL、設定、PDF 做可查詢知識圖，強調本地 AST 與每條 edge 可解釋 | Apache-2.0，905 open issues；適合作為 know metabiz wiki「程式資產」側的 POC，不取代既有證據庫。 |
| Reference only | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) — 87,892，`+446`，Trending `+473` | 成熟的 RAG + agent context layer 參考實作，可校準檢索、解析與營運能力 | Apache-2.0，但 1,860 open issues、release 為 7/7；先比較架構與成本，不預設採用。可作課程 RAG 對照案例。 |
| Watch | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) — 78,003，`+436`，8/13 有推送 | 面向「管理工作中的 agents」，與 AI 辦公室任務治理題目高度相符 | MIT、5,066 open issues；需先檢查權限、審計、資料隔離與穩定性。可做治理需求清單，不接客戶系統。 |
| Skill candidate | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) — 45,488，Trending `+252`，新觀測、成長未量測 | 將 agent 連至 Obsidian CLI、Markdown、Bases、JSON Canvas；和 Adam 本地知識工作流吻合 | MIT、62 open issues，最近推送為 6/8；先在副本 vault 驗證寫入範圍與 Git diff，再考慮互通。 |
| Demo content | [mattpocock/skills](https://github.com/mattpocock/skills) — 216,095，`+1,284`，8/6 `v1.2.3` | 工程技能的高度注意力指標，適合拿來討論 skills 的可組合、可驗證與治理 | MIT、328 open issues；不應以星數取代本地 skill 審核。可和現有 adam-codex-skills 做「導入前檢核」課程。 |
| Deep research | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) — 15,324，`+593`，8/11 `v0.7.2` | 自我改進的長程 coding agent，值得追蹤可靠性、成本與終止條件 | MIT、615 open issues；僅可做 sandbox benchmark，不能把自主行動擴大到客戶系統。 |

## 對 Adam 的可執行方向

- **課程／內容：** 用 `diagram-design` 做「從需求到可審閱架構圖」短 demo；以 Macro、Paperclip、Orca 對照「AI 辦公室／agent 管理」而非宣稱可直接上線。
- **AI 辦公室自動化：** 優先抽取 Macro 與 Paperclip 的權限、記憶、任務審計模型，形成 mOfficeAI 的需求檢核表；客戶資料、發送與寫入仍維持人工核准。
- **know metabiz wiki：** 先以 Obsidian skills 在隔離 vault 驗證開放格式互通；再用 Graphify/Semantica 各做小樣本 evidence/provenance POC。RAGFlow 留作企業 RAG 能力與成本比較基準。
- **Skill 候選：** `diagram-design` 可先轉成「輸入：已核准流程／輸出：品牌化 HTML/SVG 圖與驗證清單」；`kepano/obsidian-skills` 只在副本 vault 做 read-first 評估。

## 明日追蹤清單

1. 重新量測 `diagram-design`、`macro`、`semantica` 的次日 star delta 與 Trending 是否延續；若快速回落，降為短期內容訊號。
2. 檢查 Orca、Paperclip、RAGFlow 的 release／issue 關閉率與安全公告，而非只看 open issue 絕對數。
3. 在隔離環境各挑一個小型資料集，對 Graphify、Semantica、Obsidian skills 記錄：來源可追溯、寫入權限、失敗可恢復性、成本。
4. 保留 `stablyai/orca` 固定 watchlist；所有首次觀測 Trending 候選待有第二日基線後再計算成長。
