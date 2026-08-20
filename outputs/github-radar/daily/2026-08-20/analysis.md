# GitHub AI Trend Radar 分析 — 2026-08-20

## 摘要

本次累積追蹤 186 個 AI／MCP／Skills／Agent／RAG／開發自動化專案；13 個出現在 GitHub Trending daily。排序採相鄰日快照 star delta、Trending 當日 stars、近期 push、README 定位與可落地性，而不是總 stars。新增 Trending 項目 `RyanCodrai/turbovec`、`PostHog/posthog`、`Tencent/AI-Infra-Guard`、`agent-substrate/substrate` 均是雷達首次觀測，故其 snapshot delta 為**未量測**，不可解讀為 +0。

## 今日優先追蹤

| 優先 | Repo | 分類 | 動能與證據 | 總 stars | 風險／採用判斷 |
| --- | --- | --- | --- | ---: | --- |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | +1,662；Trending 2,267；8/20 仍更新。真實工程團隊 skill 組合，最適合作為工作流拆解樣本。 | 225,542 | MIT；374 open issues，不能整包全域啟用，需挑選可驗收流程。 |
| 2 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Deep research | +621；Trending 955；8/20 更新。將 agent memory、knowledge RAG、skills 收斂為 context database，直接對應 know metabiz wiki。 | 30,861 | AGPL-3.0 與 472 open issues；先做隔離 POC，勿直接進客戶資料流。 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Demo content | +690；8/20 更新。提供 Claude Code／Codex／Pi 的 38 種編輯式圖表，能立刻做課程前後對比。 | 24,100 | MIT；需用真實簡報與中文標籤驗證版面品質。 |
| 4 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Demo content | +1,785；Trending 2,774；8/20 更新。題目到短影音的自動化鏈路，適合 Deep research 與內容 demo。 | 112,595 | MIT；生成內容、模型與素材授權要逐項檢查，不能把 demo 視為商用產製承諾。 |
| 5 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Skill candidate | +201；Trending 335；8/20 更新。聚焦 coding CLI 跨 agent 長期記憶與 handoff，適合補強 Codex 任務交接。 | 3,449 | MIT；先以去識別測試 repo 驗證，避免把客戶上下文寫入未核准儲存。 |
| 6 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | Watch | +318；Trending 517；8/20 更新。本地 multi-agent harness，值得觀察代理協調最小實作。 | 3,027 | 無明確授權（NOASSERTION）；67 open issues，暫不納入正式自動化。 |
| 7 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Skill candidate | +213；Trending 286；8/20 更新。以精簡提示降低 token 的 Claude Code skill，能作 AI 辦公室成本／品質實驗。 | 99,459 | NOASSERTION；宣稱的節省率需用同一任務基準重測。 |
| 8 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Deep research | +219；8/20 更新。Graph-native context 與可追責 AI 的基礎層，適合研究 wiki evidence/來源追溯。 | 9,760 | MIT；148 open issues，先評估資料模型與既有 Obsidian/Git evidence 相容性。 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | +228；8/19 更新。以 deterministic AST 將 code/docs/SQL/PDF 轉可查知識圖，適合 codebase 與 wiki 的可解釋檢索。 | 108,600 | Apache-2.0；1,013 open issues，需先在小型 repo 驗證效能與維護成本。 |
| 10 | [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | Watch | 首次觀測，Trending 28；8/19 更新。涵蓋 Agent／Skills／MCP 掃描與 jailbreak 評測，切合上線前供應鏈檢查。 | 4,836 | Apache-2.0；尚無基線增長，先檢查掃描範圍、誤報率與資料外送。 |

## 對 Adam 的落地建議

- **課程**：以 `mattpocock/skills`、`diagram-design` 做「把模糊需求變成可驗收 skill 與圖解」單元；比較產出品質、修改輪數、人工覆核點。
- **Demo／內容**：用 `MoneyPrinterTurbo` 示範內容管線，但標記為實驗，不宣稱商用素材／成效；`OpenViking` 可做「RAG、memory、skills 何時該分層」的架構拆解。
- **AI 辦公室自動化**：將 `ai-memory` 的 handoff 概念映射到任務摘要、來源、待決策與 stop line；`caveman` 僅用於 token 成本 A/B test，不改寫正式提示規範。
- **know metabiz wiki**：優先用 `Semantica` 和 `Graphify` 各挑一個無敏感資料的資料夾，驗證來源可追溯、更新增量、權限邊界與中文檢索，不匯入客戶內容。

## Reference only 與風險訊號

- `stablyai/orca` +681、`earendil-works/pi` +497、`diegosouzapw/OmniRoute` +495，皆有高動能與近期更新，但分別有 4,196／134／347 open issues；先當能力地圖，不直接成為 production 依賴。
- `obra/superpowers` +470、Trending 749，是成熟方法論訊號；它的完整工作流與既有 RTK、顯式 staging、人工核准邊界存在重疊，僅選擇性採用可驗證做法。
- 新項目 `turbovec`（Trending 251）與 `PostHog/posthog`（Trending 100）屬首次觀測，前者可作向量索引效能參考，後者可作 AI observability／MCP 可觀測性參考；兩者都需下一日資料確認動能。PostHog 的授權欄位未明確，暫不做採用推薦。

## 明日追蹤清單

1. 重測 `OpenViking`、`ai-memory`、`Semantica` 的相鄰日 delta、release 與 issue 變化，決定一個 wiki POC。
2. 檢查 `mattpocock/skills`、`diagram-design` 的 README 安裝路徑與可抽取、可驗收的單一流程。
3. 為 `MoneyPrinterTurbo` 製作 1 支去商標、去客戶資料的短片 demo，逐步記錄模型／素材授權。
4. 為 `AI-Infra-Guard`、`turbovec`、`PostHog`、`agent-substrate` 補第二日快照；首次觀測前不以 delta 排名。
5. 對 NOASSERTION 專案（`munder-difflin`、`caveman`）先完成 license 核查，再決定是否可進入內部試用。

## 蒐集註記

collector 以可用的 GitHub CLI token 執行 10 組查詢、`--limit 10`、`--include-trending-daily`、`--include-readme`；未觸發 rate limit，因此未採用 limit 5 降級。兩個既有追蹤 repo 在讀取時回傳 404，系統保留最後已知中繼資料，未影響本日完整產物；它們不作今日推薦依據。
