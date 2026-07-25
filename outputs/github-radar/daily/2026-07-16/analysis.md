# GitHub AI Trend Radar — 2026-07-16

> 執行時間：2026-07-17 00:12 Asia/Taipei；目標日：2026-07-16。
>
> 來源：GitHub Trending `since=daily`（抓取時的 rolling 24h 動能）與入選 repo README / Releases 頁。`GITHUB_TOKEN` 不存在；collector 先以 `--limit 10` 執行，於第 19 個候選遭匿名 GitHub REST API 403 rate limit；已依規則再以 `--limit 5` 重試，仍在第一個查詢即 403。因此本次**沒有** `repos.json`、`report.md` 或 API snapshot，且 `star_delta` 無法計算。下列 `stars today` 是 Trending 當下的滾動日訊號，不是可回放的 2026-07-16 歷史快照。
>
> **2026-07-17 00:27 後續驗證**：本機 GitHub CLI 已登入 `AdamLien`。以 `GITHUB_TOKEN="$(gh auth token)"` 補跑十組查詢、每組最多 5 筆，已成功產生 44 個 repo 的 API `repos.json`、`report.md` 和 `snapshots/repos-2026-07-17.json`。此快照的實際抓取日是 2026-07-17，且前一日 API baseline 不存在，故 `star_delta` 仍為首次快照值，不能倒推成 2026-07-16 的歷史增量；下次排程應直接使用此 token 注入方式，便可累積可比較的 delta。

## 今日判讀

最明確的訊號不是單一模型或框架，而是「把 agent 行為做成可安裝、可組合、可檢查的 skills」，以及把 code / docs / schema 轉成可查詢 knowledge graph。前者適合課程與 AI 辦公室自動化的交付規範，後者值得拿 metabiz wiki 做受控 PoC。

排序以 `stars today`、`stars today / total stars`、文件清楚度及近期 release 為主；**不以總星數作排名**。

| 優先 | Repo | 分類 | stars today | 總 stars | 日動能 / 總星 | 判讀 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Skill candidate / Demo | 3,181 | 10.2k | 31.2% | Skills 類爆發，且直接覆蓋 Claude Code、Cursor、Codex |
| 2 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 1,138 | 88.5k | 1.3% | code + docs + schema 的知識圖譜，7/16 有新 release |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 2,073 | 173k | 1.2% | 工程流程 skills 的高品質、可組合參考 |
| 4 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Deep research / Demo | 647 | 26.7k | 2.4% | RAG、deep research、multi-agent 與個人化學習的完整產品化案例 |
| 5 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Reference only / Demo | 935 | 122k | 0.8% | 可執行 Agent 與 RAG 範例的選題池 |
| 6 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | Watch | 633 | 65.8k | 1.0% | 低成本模型 coding-agent harness 與 QA computer use |
| 7 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | Skill candidate / Demo | 141 | 3.9k | 3.6% | 設計工程 skills CLI，適合和 Hallmark 作對照內容 |
| 8 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | Reference only | 62 | 9.5k | 0.7% | 官方 Copilot Agent 嵌入 SDK，作平台能力追蹤 |

## 入選 repo 與建議

### 1. Hallmark — Skill candidate / Demo/content idea

- **用途**：Claude Code、Cursor、Codex 的 anti-AI-slop 網頁設計 skill；含 build、audit、redesign、study 四個操作，並提供安裝與跨工具位置說明。
- **為什麼紅**：3,181 stars today / 10.2k（31.2%）是本輪最異常的相對動能；README 把抽象的「避免 AI 味」具體成 57 個 gates 和可展示作品，極適合傳播。
- **維護訊號**：133 commits、7 issues、9 PR；MIT，但尚無 GitHub release。
- **風險**：設計審美規則不等於品牌策略；安裝第三方 skill 前要先審 SKILL.md、外部命令與授權素材，不能直接帶入客戶專案。
- **Adam 可用性**：做一支「同一 brief：裸 prompt vs Hallmark skill」短片；也可提煉其 audit/checklist 思路，形成 mIMS / metabiz 前端交付前的設計 QA skill。

### 2. Graphify — Deep research

- **用途**：把程式碼、SQL schema、文件、論文、圖片和影片轉成可查詢 knowledge graph；定位為 Claude Code、Codex、Cursor 等 coding agent 的 skill。
- **為什麼紅**：1,138 stars today / 88.5k；README 定位清楚，且 0.9.17 在 7/16 發布、已有 163 個 releases，維護活躍度是本輪最強之一。
- **風險**：對大型私有 repo / wiki 需要先驗證索引時間、增量更新、資料不外送、權限與刪除語意；高星數不表示適合直接存取機敏知識庫。
- **Adam 可用性**：最高優先 PoC。以可公開或已去識別的 metabiz wiki 子集合測試：檢索準確性、來源連結、過期頁辨識、刪文後圖譜清除；通過才考慮正式知識層。

### 3. mattpocock/skills — Skill candidate

- **用途**：工程工作流 skills，強調小、可調整、可組合；覆蓋規格、tickets、TDD、debug、research、code review、domain model 等。
- **為什麼紅**：2,073 stars today / 173k；不只收藏清單，README 把「user-invoked orchestration」與「model-invoked reusable discipline」分層，適合作為 agent coordination 的教材。
- **維護訊號**：v1.1.0 於 7/8 發布、4 個 releases、172 issues；MIT。
- **風險**：整包導入會與既有 Codex skills 和團隊流程重疊；應挑單一 workflow 比對後採用，勿把其 CLAUDE 導向設定直接覆蓋現有規範。
- **Adam 可用性**：課程可講「Skill 不是 prompt collection，而是可測試的工作流介面」；優先比較 `/grill-with-docs`、`/tdd`、`/diagnosing-bugs` 與既有 skills 的差異。

### 4. DeepTutor — Deep research / Demo

- **用途**：終身個人化 AI tutor，組合 RAG、deep research、multi-agent、知識庫與教學互動。
- **為什麼紅**：647 stars today / 26.7k；相對動能 2.4%，且 7/9 發布 v1.5.1、已有 55 releases。近期版本處理失敗文件的單筆刪除與多模態文件 ingestion，顯示真實 KB 維運取向。
- **風險**：教育產品的完整堆疊很重，不能把 demo 當成可直接部署的企業知識庫；先釐清模型成本、個資、內容正確性與評量偏誤。
- **Adam 可用性**：可做「RAG 不只是聊天：怎麼處理 ingestion、來源、失敗文件與個人化」課程案例；對 metabiz wiki 只取其知識庫治理觀念，不建議直接導入全產品。

### 5. awesome-llm-apps — Reference only / Demo pool

- **用途**：100+ 可 clone、客製、部署的 AI Agent 與 RAG app 範例。
- **為什麼紅**：935 stars today / 122k；README 清楚、Apache-2.0，適合快速掃描題材與 demo 組合。
- **風險**：聚合庫沒有 release，範例品質、維護狀態、依賴安全性不一；只能作 discovery pool，不能作採用背書。
- **Adam 可用性**：每週從中挑 1 個「可在 10 分鐘演示」的 app，搭配成本與安全限制，不要把列表本身當課程主體。

### 6. Open Interpreter — Watch

- **用途**：針對低成本模型的 coding agent；可切換多個 harness，並以 QA skill 驅動 browser / native app 測試。
- **為什麼紅**：633 stars today / 65.8k；README 對 harness emulation、computer use、跨平台 sandbox 的說明具體。
- **風險**：agent 能執行命令與操作 UI，權限隔離、金鑰與核准流程是首要問題；公開 repo 的活動數字也顯示需要先做版本與安全審核。
- **Adam 可用性**：追蹤其「低成本模型 + harness」方法，用作不同 coding agent 的成本/可靠度比較；不直接接入 production automation。

### 7. UI Skills — Skill candidate / Demo

- **用途**：設計工程師向的 skills CLI，可列出分類並讓 agent 選擇適用 UI skill。
- **為什麼紅**：141 stars today / 3.9k，雖絕對量較小，但相對動能 3.6%；README 與 CLI 命令非常清楚，MIT、已有 8 releases。
- **風險**：最新 release 為 6/22；UI patterns 需要與既有品牌系統及 accessibility 標準一起驗證。
- **Adam 可用性**：和 Hallmark 做二段式 demo：先用 UI Skills 選擇技術 pattern，再用品牌/設計 QA 收斂視覺；適合 AI 辦公室的前端交付流程。

### 8. GitHub Copilot SDK — Reference only

- **用途**：官方多平台 SDK，讓服務與 app 嵌入 GitHub Copilot Agent。
- **為什麼紅**：62 stars today / 9.5k，動能不高但屬平台訊號；103 releases、7/8 有 Java 版更新，文件與 release 活躍度佳。
- **風險**：綁定 Copilot 產品/授權與平台路線，與 Codex 主力流程不是可互換關係。
- **Adam 可用性**：作「agent 可嵌入產品」的 reference；若課程或客戶已有 Copilot 生態，再深入其 SDK，不列為當下建置優先。

## 對 Adam 的可執行結論

1. **課程主題**：用 Hallmark + mattpocock/skills 講「把 agent 從 prompt 使用者升級成有 guardrail 的工作流執行者」；以 DeepTutor 補 RAG/KB 維運現實。
2. **內容選題**：兩支短 demo 最值得拍：`Hallmark audit/redesign 前後`、`Graphify 對 code + SQL + docs 的單一問題溯源`。兩者都要清楚揭露是本機或測試資料。
3. **AI 辦公室自動化**：採用「router → reusable skills → verification」三層，不採全自動黑箱 agent。先把需求釐清、資料來源、權限確認、輸出驗證做成可見 checkpoints。
4. **metabiz wiki**：Graphify 是 research/Poc 候選；DeepTutor 的 ingestion / source / deletion semantics 是設計參考。任何正式接入前必做：資料分類、最小權限、可追溯引文、增量同步、刪除回收與離線/外送檢查。

## 明日持續追蹤

- `Graphify-Labs/graphify`：release 是否維持、私有資料處理與增量索引證據。
- `Nutlope/hallmark`：快速成長是否轉成 issue/PR 維護，及其 skill 安全邊界。
- `mattpocock/skills`：v1.1.0 後的 issues、Codex 相容性與可拆用 skill。
- `HKUDS/DeepTutor`：RAG ingestion/刪除與 release 品質；避免只看教育 demo。
- `openinterpreter/openinterpreter`：harness、sandbox、QA computer-use 的安全與模型成本。
- `github/copilot-sdk`：官方 SDK 新 release 與權限/API 變化。

## 產物狀態

- `analysis.md`：已產生（本檔）。
- `repos.json`、`report.md`、`snapshots/repos-2026-07-17.json`：已於後續 authenticated 補跑生成，涵蓋 44 個 repo；這是第一個 API baseline，`star_delta` 尚無歷史比較意義。
