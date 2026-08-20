# GitHub AI Trend Radar 分析｜2026-08-19（台灣）

## 摘要

本輪以 182 個去重後的 AI／MCP／Skills／Agent／RAG／developer automation 專案為母體，優先看相鄰快照的 stars 增量、Daily Trending 當日 stars、更新與 release，而非只看累積 stars。完整蒐集的第一次嘗試在單一 GitHub release 請求逾時，重試相同 authenticated `--limit 10` 後成功；並非 rate limit，因此未降為 limit 5。

Daily Trending 是於 8/20 台灣 00:10 左右取得的當前訊號，不能反推 8/19 的歷史排名；下列 `Trending today` 只作注意力佐證。新首見的 `choiyounggi/dev-loop` 未量得相鄰快照增量，明確標示為 unmeasured，而非 +0。

## 本日優先清單

| 優先 | 專案 | 分類 | 動能與目前總 stars | 為何值得追／風險 | 對 Adam 的可用性 |
| --- | --- | --- | --- | --- | --- |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | +2,661；223,880；Trending 1,894；8/19 更新 | 工程導向 skill 集合、MIT；371 open issues，應挑選可驗證工作流而非整包採用。 | 把可重複的課程製作、程式審查、知識整理流程萃為 metabiz/Codex skill。 |
| 2 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Deep research | +1,059（約 3.5%）；30,240；Trending 804；8/18 release | 將 agent memory、knowledge RAG、skills 放入同一 context database；AGPL-3.0 是商用整合的主要門檻，且 459 issues。 | 對 know metabiz wiki 做隔離式 PoC：資料編目、檢索、記憶三者的界線與可觀測性。 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Demo candidate | +1,937（約 8.3%）；23,410；8/20 仍活躍 | 為 Claude Code、Codex、Pi 提供可直接產生的 SVG/HTML 圖解；MIT、僅 26 issues。 | 將課程架構、mOfficeAI 流程、MCP 架構改成可展示的圖解；先檢查品牌與可讀性規範。 |
| 4 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Skill candidate | +676（約 20.8%）；3,248；8/19 release | 面向跨 agent coding CLI 的長期記憶與 handoff；MIT、僅 3 issues，成長率高但規模仍小。 | 可作為 Codex 任務交接／記憶摘要格式的參考；先確認不會把客戶或 tenant 資料自動寫出工作區。 |
| 5 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Demo candidate | +2,748；110,810；Trending 2,221；8/12 release | 題目到短影音的自動化工作流、MIT、31 issues，當日注意力最強。 | 用於「AI office 到內容交付」示範題材；須獨立驗證素材授權、模型成本、繁中品質，不能直接當商用承諾。 |
| 6 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | +581；108,372；8/19 更新 | 可把 code、文件、SQL、設定與 PDF 轉成可查詢 knowledge graph；需要檢查索引成本與資料邊界。 | 可比較 LLM Wiki 的 evidence／provenance 路線與 codebase graph，但先以非敏感資料做 ingestion。 |
| 7 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | Watch | +898（約 33.2%）；2,709；Trending 795；8/18 release | local multi-agent harness 的爆發式早期訊號；`NOASSERTION` license、56 issues，尚不能導入。 | 可作「多 agent 本地協調」教學研究樣本；先釐清授權、隔離與失敗復原。 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | Watch | +1,120（約 2.3%）；49,157；8/19 release | 支援平行 coding agents 的 ADE、MIT；但 4,169 open issues 是明顯維護/支援風險。 | 可研究多 agent 編排與訂閱帳號操作模型，不應接觸客戶環境或當成團隊標準。 |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | Reference only | +757；274,300；Trending 557；8/19 更新 | 方法論與 skill 框架仍有強動能、MIT；既有評估已指出其強制流程不宜覆蓋目前 Codex/RTK 規範。 | 保留 systematic debugging、驗證等可移植做法；不全域啟用其 worktree/subagent 儀式。 |
| 10 | [jundot/omlx](https://github.com/jundot/omlx) | Demo candidate | +565（約 2.9%）；19,851；Trending 472；8/19 release | Apple Silicon 本機 LLM server，有持續 release；963 issues，需要量測資源與模型相容性。 | 可在 Mac 做本地模型／推論成本內容 Demo；不得以 benchmark 推論生產 SLA。 |

## 今日判讀與可執行方向

- **Deep research**：先為 OpenViking 與 Graphify 定義一個隔離的「資料來源 → provenance → 查詢 → 刪除」測試；OpenViking 的 AGPL-3.0 不可未審查即放入商業產品。
- **Demo content**：MoneyPrinterTurbo 適合把「一個提示如何變成短影音」做成公開 demo；diagram-design 可作為同支內容的架構圖產生方式。兩者都要先驗證輸出品質與授權。
- **Skill candidate**：從 mattpocock/skills 與 ai-memory 提取可驗收的單一流程，而不是安裝未知集合：例如「交接摘要必含證據、未驗證項目、下一個可執行命令」。
- **Watch**：munder-difflin、Orca 因早期風險／issue 負債而只追蹤；首見 `choiyounggi/dev-loop` 的成長尚未量得，明日再確認而非補寫 `+0`。
- **Reference only**：superpowers 是有價值的方法論參考，但與現行 RTK、明確 staging、人工核准邊界衝突的自動工作流不採用。

## 明日追蹤清單

1. 重新量測 `mattpocock/skills`、OpenViking、diagram-design、ai-memory 的 snapshot delta，確認不是單日噪音。
2. 檢查 OpenViking 的 AGPL 網路服務義務、部署邊界與近期 issues；未釐清前不進入商業 wiki。
3. 以一份不含客戶資料的文件集，比較 Graphify 和既有 LLM Wiki 的 evidence/provenance、更新成本、檢索命中。
4. 對 `dev-loop` 保留首見狀態，次輪才計算成長；檢查其 README、授權與 release。
5. 驗證 MoneyPrinterTurbo 的繁中腳本、素材來源、成本與人工審稿流程，才能放進可公開的 demo pipeline。
