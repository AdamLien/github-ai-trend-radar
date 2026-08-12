# GitHub AI Trend Radar 分析（2026-08-12，台灣時間）

## 本日判讀

本輪以十組範圍查詢、累積候選池與 GitHub Trending daily 合併後，取得 **159** 個專案；其中 **6** 個是本雷達首次觀測的 Trending 項目。以下的「快照增量」是相鄰執行日（2026-08-11 與本次 API 快照）的差異，並非歷史 Trending 的單日 stars；`Trending 今日` 才是此次頁面可見的當日注意力訊號。排序優先考慮注意力、增量、更新與可落地性，不以總 stars 單獨排名。

## 最值得追蹤的專案

| 分類 | 專案與動能 | 用途與對 Adam 的價值 | 風險／下一步 |
| --- | --- | --- | --- |
| Deep research | **cathrynlavery/diagram-design**：9,116 stars；快照 +1,542；Trending +2,951；8/12 更新；MIT。 | Claude Code 的 29 種自含 HTML/SVG 圖解型別。很適合做「把課程／提案／wiki 證據轉為非模板化圖解」的 demo，並研究其可重用的提示與輸出品質規則。 | 高速成長但仍需檢查圖表生成在中文、品牌與可存取性上的穩定性；先以一篇 metabiz wiki 條目做離線對照測試。 |
| Deep research | **stablyai/orca**：43,590 stars；快照 +417；Trending +1,215；8/12 更新；v1.4.180（8/11）；MIT；固定 watchlist。 | 可用既有訂閱調度平行 coding agents，對 AI 辦公室自動化的「多代理任務拆分／可視化」有直接研究價值。 | 不授權其代替既有執行與審核邊界；比較多代理成本、權限隔離、失敗回收後再決定是否試作。 |
| Deep research | **semantica-agi/semantica**：5,540 stars；快照 +323；Trending +834；8/12 更新；v0.6.5（8/11）；MIT。 | Graph-native context 與可追責 AI 基礎設施；與 know metabiz wiki 的來源、關聯與可追溯回答需求高度相關。 | 尚需做資料模型、索引成本與中文檢索 benchmark；先研究，不直接導入既有 wiki。 |
| Demo content | **paperclipai/paperclip**：77,567 stars；快照 +212；Trending +573；8/12 更新；MIT。 | 主打在工作場所管理 agents；可做「代理工作台與人工核准」內容對照，幫助說明 AI Office 的治理層。 | 產品敘事強於可驗證的企業適配；需審核權限模型、資料外流與審計輸出才可評估。 |
| Skill candidate | **Graphify-Labs/graphify**：105,579 stars；快照 +142；8/12 更新；v0.9.41（8/12）；Apache-2.0。 | 本地 AST 解析把程式、文件、SQL、設定轉成可查詢知識圖；可補強 codebase／metabiz wiki 的證據導覽，且不依賴向量庫。 | 需先量測大型 repo 的時間、記憶體與機敏檔案排除；可考慮封裝成「先建圖、再查證」的受控 skill。 |
| Skill candidate | **addyosmani/agent-skills**：86,508 stars；快照 +138；8/11 更新；v0.6.6（8/04）；MIT。 | 工程型 coding-agent skills，可挑選驗證、測試、文件化等原子流程作為 Adam 課程案例與內部工作流素材。 | 不宜整包啟用或覆蓋既有 RTK／審核規範；逐一檢查指令副作用與相容性。 |
| Watch | **PrimeIntellect-ai/prime-agent**：14,731 stars；快照 +257；8/12 更新；v0.7.2（8/11）；MIT。 | 自我改進 RLM coding agent，適合探索長任務與反思循環的課程內容。 | 「self-improving」需以可重現 eval 驗證；禁止直接碰 production 或客戶資料，先做沙箱基準。 |
| Watch | **infiniflow/ragflow**：87,446 stars；首次觀測，Trending +182；8/12 更新；Apache-2.0。 | 成熟 RAG/Agent context layer，是 know metabiz wiki 的外部比較基準。 | 因首次觀測，快照成長未量測；部署複雜度、資料治理與檢索品質均要先做 POC，暫不視為導入建議。 |
| Reference only | **msitarzewski/agency-agents**：144,385 stars；快照 +457；Trending +1,969；最後 push 8/06。 | 大量角色與交付物很適合作為課程「角色設計」靈感。 | 高 stars／Trending 不代表可運營；角色包較偏內容資產，且近期程式活動較弱，僅作參考。 |
| Reference only | **hugohe3/ppt-master**：45,384 stars；首次觀測，Trending +364；8/12 更新。 | 文件轉原生 PowerPoint 的 demo 角度值得關注。 | 與本日核心 AI agent / knowledge-base 範圍較邊緣，且快照成長未量測；不列為技術採用候選。 |

## 對課程、內容與 AI 辦公室自動化的建議

- **課程主題**：以 diagram-design 對比一般 Mermaid 輸出，示範「來源證據 → 觀眾導向圖解 → 人工校稿」；以 Prime Agent／Orca 說明長任務不可省略沙箱、成本上限與人工 stop line。
- **內容題材**：做一支「Trending 很熱，不等於能導入」短片：用 Orca、Paperclip、Agency Agents 比較執行面、治理面、角色素材面三種不同價值。
- **AI 辦公室自動化**：優先研究 Graphify 的本地解析與 Semantica 的可追責上下文；共同驗收情境是能從指定 wiki／repo 找到回答所依據的檔案與關係，不能以未驗證摘要取代來源。
- **know metabiz wiki**：RAGFlow 僅作外部基準。先以去識別樣本比較 Graphify / Semantica / 現有 evidence 流程的中文檢索、來源引用、更新增量與權限隔離。

## 明日追蹤清單

1. **diagram-design**：確認 +1,542 是否持續，以及中文／品牌圖解的可用性。
2. **Orca**：追蹤 v1.4.180 後的 release／issue 訊號與多代理成本控制。
3. **Semantica、Graphify**：選一個最小去識別 wiki／repo benchmark，紀錄可追溯性與資源成本。
4. **Paperclip、Prime Agent**：追蹤活躍度與權限／審計設計，再判斷是否進入 POC。
5. **RAGFlow**：取得第二日快照後再比較成長；先閱讀部署與資料隔離文件。

## 資料限制

GitHub Trending daily 是本次執行日讀取的當前注意力，不能回溯成 2026-08-12 的完整歷史榜單。API 快照增量也受兩次蒐集時間差、API 可見資料與累積候選池影響；它是排序訊號，不是市場需求或商業採用證明。
