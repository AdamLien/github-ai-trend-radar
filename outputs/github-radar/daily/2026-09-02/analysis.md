# GitHub AI Trend Radar 分析

日期：2026-09-02（Asia/Taipei）  
資料來源：GitHub Trending daily 與十組指定 GitHub repository search；本日共收集 242 筆，以下挑選 8 個值得追蹤的專案。判斷以今日星數、快照星數增量、相對成長、最近更新／版本、README 清晰度與 issue 訊號綜合評估，不以總星數單獨排序。

## 值得追蹤的 repositories

### 1. [tt-a1i/archify](https://github.com/tt-a1i/archify) — Skill candidate

- **用途：** 將程式碼庫或系統描述轉成可驗證、可匯出的架構、流程、sequence 與 data-flow 互動圖；支援 Codex、Claude Code、Cursor 與 OpenCode。
- **動能：** 43,449 stars；本快照 +2,079，今日更新，v2.16.0 於 2026-08-30 發布；90 個 open issues。星增量是本批最強之一，README 有預覽圖與清楚的安裝／產品定位。
- **風險：** MIT 但仍需實測輸出正確性、Node.js 相依性與大型 codebase 的穩定度；issue 數量值得持續觀察。
- **Adam／Metabiz 關聯：** 可包成「AI 辦公室自動產生系統圖」課程示範，也適合把 know metabiz wiki 的服務、流程與 agent 邊界視覺化；可評估做成可重用 Skill。

### 2. [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — Demo content

- **用途：** 一鍵建立多 Agent 互動式課堂，將教學內容轉為沉浸式、可互動的學習體驗。
- **動能：** 30,386 stars；本快照 +1,221，2026-09-02 有更新，v1.0.0（Build courses with an agent）於 2026-08-27 發布；229 個 open issues。課程定位、Banner、使用指南與版本訊息完整。
- **風險：** MIT；但 229 個 issues 反映早期快速成長的維運負擔，部署與多 Agent 成本尚待驗證。
- **Adam／Metabiz 關聯：** 非常適合做「Agent 如何生成課程」與互動教學 Demo；可研究其課程資料模型，回饋 Adam 的 AI 課程設計與 Metabiz 內訓自動化。

### 3. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — Deep research

- **用途：** 為 Claude Code 提供 research → write → review → revise → finalize 的學術研究工作流與 Skills。
- **動能：** 45,447 stars；本快照 +733，2026-09-02 更新；v3.21.1 於 2026-08-24 發布；18 個 open issues。README 提供繁中版本、版本標記、DOI 與清楚的端到端流程。
- **風險：** API 顯示 NOASSERTION，README 標示 CC BY-NC 4.0；商業課程、客戶交付或 Skill 改作前需確認授權範圍，且研究結論仍需人工查證。
- **Adam／Metabiz 關聯：** 可作為深度研究、課程備課、競品分析與 know metabiz wiki 寫作的參考基準；優先研究其可拆分的研究閘門與審稿流程。

### 4. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research

- **用途：** 把程式碼、文件、SQL schema、設定檔與 PDF 轉成可查詢的 knowledge graph，提供 Claude Code、Cursor、Codex、Gemini CLI 的 `/graphify` Skill；主打 deterministic AST 與不依賴 vector store。
- **動能：** 113,872 stars；本快照 +616，2026-09-02 更新，v0.9.53 於 2026-08-30 發布；11,080 forks、1,217 open issues。README 有多語言入口、產品預覽與清楚的技術差異化。
- **風險：** Apache-2.0；open issues 很高，且需驗證索引耗時、圖譜品質與跨語言支援，不能直接假設其結果適合正式知識庫。
- **Adam／Metabiz 關聯：** 與 know metabiz wiki 的結構化檢索、程式庫交接與 agent onboarding 高度相關；可做「Graph RAG vs vector RAG」內容與實驗。

### 5. [volcengine/OpenViking](https://github.com/volcengine/OpenViking) — Watch

- **用途：** 面向 AI Agent 的 Context Database，統一 Agent memory、knowledge RAG 與 Skills，提供中文文件與線上 Demo。
- **動能：** 35,139 stars；本快照 +235，2026-09-02 更新；v0.4.17.1 於 2026-08-31 發布；2,694 forks、600 open issues。定位直接對準長期記憶、上下文與 Skill 整合這個快速升溫的層。
- **風險：** AGPL-3.0 對 SaaS／商業整合有合規與散布義務風險；600 個 issues 及 self-evolving 宣稱需要實作級驗證，先不要直接採用。
- **Adam／Metabiz 關聯：** 可作為 know metabiz wiki 的記憶層與 RAG 架構研究對象，也能轉成「Agent memory、知識庫、Skills 如何合一」課程題材。

### 6. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) — Skill candidate

- **用途：** 以 MCP server 讓 coding agent 操控並檢查 live Chrome，支援可靠瀏覽器自動化、除錯、效能分析，另有 CLI。
- **動能：** 50,544 stars；本快照 +158，2026-09-02 更新；v1.8.0 於 2026-08-25 發布；3,552 forks、85 open issues。Apache-2.0，README 有 npm、工具參考、變更記錄與 troubleshooting 入口。
- **風險：** 需要瀏覽器控制權與本機執行環境；權限隔離、敏感頁面、登入狀態與自動化誤操作需在辦公室流程中設防。
- **Adam／Metabiz 關聯：** 可示範「Agent 讀取儀表板、測試網站、擷取流程證據」，並評估納入 AI office automation 的瀏覽器 QA／報表 Skill。

### 7. [EtienneLescot/n8n-as-code](https://github.com/EtienneLescot/n8n-as-code) — Skill candidate

- **用途：** 將 n8n 變成 agent 可操作的 workflow toolkit，涵蓋 537 個 nodes、7,700+ templates、Git-like sync 與 TypeScript workflows。
- **動能：** 1,552 stars；本快照 +2，2026-09-02 更新；v2.5.0 於 2026-07-24 發布；182 forks、19 open issues。MIT，README 有 CI、文件與 VS Code Marketplace 入口，技術路徑清楚但今日星增量不高。
- **風險：** n8n workflow 的 secrets、權限、外部副作用與 schema 漂移是主要風險；模板數量多不等於每個模板可安全投入生產。
- **Adam／Metabiz 關聯：** 直接連結 AI office automation：CRM、報價、內容發布與 wiki 同步都可作 n8n + Agent 教學；值得先做一個最小可回滾流程。

### 8. [DataTalksClub/ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) — Reference only

- **用途：** 免費、實作導向的 AI developer tools 課程，涵蓋建置、測試、部署、延伸與稽核，2026 cohort 已於 8 月 31 日開始。
- **動能：** 1,527 stars；本快照 +12，2026-09-02 更新；無 release、242 forks、0 open issues。README 有課程封面、註冊入口與 AI-native software engineering 的明確主張。
- **風險：** API 未辨識授權（README 也未見明確 license badge）；內容與 cohort 時程可能快速變動，商業引用前需確認授權與課程差異化。
- **Adam／Metabiz 關聯：** 是競品／同類課程的定位參考，可比較其 hands-on、工程紀律與 agent 工具編排方式，作為 Adam 課程產品設計的 benchmark，不直接複製教材。

## 綜合判讀

今日訊號集中在三條線：一是把 Agent 能力封裝成可重用 Skills（archify、academic-research-skills）；二是把知識、記憶與 codebase 結構化（Graphify、OpenViking）；三是讓 Agent 直接操作瀏覽器與業務流程（chrome-devtools-mcp、n8n-as-code）。OpenMAIC 則顯示「Agent 生成課程」正在從概念走向可展示產品。

相對成長最值得注意的是 archify、OpenMAIC 與 academic-research-skills；它們同時具備近期更新或 release 訊號與清楚 README。OpenViking 的星數與 issue 活躍度都高，但 AGPL 與成熟度使它適合 Watch。DataTalksClub 課程雖然動能小，卻是 Adam 內容策略不可忽略的參照組。星數高但授權不清、文件不足或安全邊界不明的專案，暫不列入採用建議。

## 明日 watchlist

1. **archify：** 確認星增量是否延續，實測同一個 Metabiz 流程的圖表可驗證性與匯出品質。
2. **OpenMAIC：** 追 v1.0.0 後的 issue／release，確認課程生成是否能重現且部署成本可接受。
3. **academic-research-skills：** 核對授權、繁中流程與研究引用防幻覺機制，評估拆成內部研究 Skill。
4. **Graphify／OpenViking：** 比較 graph-based code knowledge 與 context database 的索引、更新、權限與資料留存模型。
5. **chrome-devtools-mcp／n8n-as-code：** 做最小權限的瀏覽器 QA 與可回滾辦公流程 Demo，記錄 secrets、登入狀態與副作用控制。
6. **新進 Trending：** pacifio/atlas、blader/humanizer、google-research/timesfm、sngyai/Sequoia-X、vercel-labs/portless、superlinked/sie；下一輪補齊基線後再判斷相對成長。
