# GitHub AI 趨勢雷達分析｜2026-09-20

## 摘要

本次由 306 個累積候選中，選出 9 個可轉化為 Adam 課程、內容、AI 辦公自動化或 know metabiz wiki 實驗的項目。排序依據以昨日快照（2026-09-19）後的星數增量、GitHub Trending 當日星數、更新／release、新版 README 的可驗證性及 issue 壓力為主；總星數只作成熟度背景，**不是排序依據**。

今日最明確的兩條訊號是：一，受約束、可驗證的 Agent skill（安全稽核、code review、架構圖）快速升溫；二，文件／知識庫到 agent context 的管線，從「RAG 問答」延伸到可維護 wiki、程式知識圖與跨 session 記憶。星數代表開發者注意力，不能直接推論為付費課程或企業採用需求。

## 值得投入的倉庫

### 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — Deep research

- **用途：** 將 coding agent 的安全稽核拆成偵察、覆蓋導向尋找、候選驗證、結構化輸出與獨立驗證等多階段流程，輸出可機器讀取的發現。
- **動能：** 昨日快照後 **+2,095** stars、GitHub Trending 當日 **2,375**；共 **17,687** stars。README 清楚說明六階段與獨立驗證，顯示關注點在可稽核流程而非單一 prompt。
- **風險：** 最近 push 為 9/14、沒有 latest release；44 個 open issues。不可把其掃描結果當成已修正或合規證明，且必須在隔離、授權範圍內使用。
- **與 Adam 的關聯：** 可作「AI 辦公／開發自動化的品質閘門」課程案例，也可衍生 know metabiz wiki 的安全變更檢核清單；先研究方法，勿直接導入生產環境。

### 2. [trycua/cua](https://github.com/trycua/cua) — Demo content

- **用途：** 提供跨 OS 的 computer-use driver、隔離桌面／VM、fleet 與 benchmark，讓 agent 以真實 GUI 操作完成任務。
- **動能：** 昨日快照後 **+940**、Trending 當日 **1,012**；共 **24,996** stars；9/20 仍有 push，9/15 發布 `sandbox-v0.8.0`。
- **風險：** **1,025** 個 open issues，部署涉及桌面隔離、成本、登入態與資料外洩面；示範僅能用測試帳號與無敏感資料環境。
- **與 Adam 的關聯：** 很適合「AI 辦公自動化何時該用 API、何時需 GUI agent」內容；可用虛擬 demo 展示表單／報表流程，但不連接 know metabiz wiki 或任何實際工作帳號。

### 3. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) — Deep research

- **用途：** 將 deterministic 規則與 LLM agent 合併，提供多語言的逐行 code review（含 NPE、thread-safety、XSS、SQL injection）與 repository-level context。
- **動能：** 昨日快照後 **+898**；共 **38,237** stars；9/20 有 push，9/19 發布 `v1.12.7`。活躍 release 加上 Apache-2.0 授權，是比單純 prompt 範例更可研究的工程訊號。
- **風險：** 265 個 open issues；LLM 審查可能誤判、漏判或將程式碼送往外部模型，需先核對資料路徑、模型相容性與 CI 成本。
- **與 Adam 的關聯：** 可用作 AI 開發工作流的「規則先行＋agent 輔助」教材；若日後為 know metabiz wiki 的程式／自動化專案建置變更治理，可先以非機密 sample repo benchmark。

### 4. [tt-a1i/archify](https://github.com/tt-a1i/archify) — Skill candidate

- **用途：** 把架構、工作流、時序、資料流與生命週期描述轉為可驗證、可匯出的互動 HTML 圖；支援 Claude Code、Codex 等 coding agent。
- **動能：** 昨日快照後 **+825**；共 **68,081** stars；9/20 有 push，release 為 `v2.16.0`。README 提供從想法到可探索視覺的清楚定位。
- **風險：** 140 個 open issues，且最新 release 是 8/30；自動圖容易把未知關係畫成事實，需保留來源、假設與人工核對點。
- **與 Adam 的關聯：** 最適合轉化為「把流程變成可講解視覺」的課程／短內容；也值得評估成 know metabiz wiki 的標準架構圖與 SOP 圖產生 skill。

### 5. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — Skill candidate

- **用途：** 提供從 DEFINE、PLAN、BUILD、VERIFY、REVIEW 到 SHIP 的 production-grade engineering skills，目標是把資深工程的流程與品質閘門編碼化。
- **動能：** 昨日快照後 **+689**、Trending 當日 **729**；共 **97,509** stars；9/18 push 並發佈 `Agent Skills 0.6.10`；僅 112 個 open issues。
- **風險：** 通用 skill 不必然符合本專案、中文內容或公司的權限界線；全盤安裝會增加規則衝突與 context 成本，應逐個審閱後採用。
- **與 Adam 的關聯：** 是設計 Adam 專屬課程／內容生產／AI 辦公自動化 skill 的優良對照組；可萃取「規劃—驗證—交付」骨架，再以 know metabiz wiki 的具體 SOP 取代通用假設。

### 6. [Tencent/WeKnora](https://github.com/Tencent/WeKnora) — Deep research

- **用途：** 將原始文件轉成可查詢 RAG、推理 agent 與可自我維護的 wiki，涵蓋 embedding、reranking、multi-tenant 與語意搜尋。
- **動能：** 昨日快照後 **+568**；共 **27,892** stars；9/20 有 push，`v0.8.0` 於 9/3 發布。它直接把「文件庫」定位為可維護的知識平台。
- **風險：** 授權欄為 **NOASSERTION**，627 個 open issues；multi-tenant、文件權限與自動寫回 wiki 是高風險面，未釐清 license、RBAC、資料駐留與審核前不可採用。
- **與 Adam 的關聯：** 與 know metabiz wiki 的目標最貼近，可作「RAG 不等於知識治理」深度研究題材；先評估 ingest、權限、引用、人工覆核與回寫治理，不做直接匯入。

### 7. [docling-project/docling](https://github.com/docling-project/docling) — Skill candidate

- **用途：** 將 PDF、DOCX、PPTX、XLSX、HTML 等文件解析／轉換為適合生成式 AI 的結構化內容，是 RAG 與 wiki ingest 前處理基礎。
- **動能：** 昨日快照後 **+535**；共 **67,390** stars；9/20 有 push，9/18 發布 `v2.129.0`；MIT 授權。
- **風險：** 942 個 open issues；表格、掃描件、版面與多語文件的擷取品質需要以自己的文件集測試，並需防止敏感文件在未授權的處理路徑中外流。
- **與 Adam 的關聯：** 對既有 PDF ingestion 與 know metabiz wiki 的受控匯入最實用；可形成「文件分類→擷取→品質驗證→可追溯入庫」的 reusable skill。

### 8. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research

- **用途：** 以本地、可解釋的 AST 解析，把 codebase、文件、SQL schema、設定與 PDF 轉成查詢式知識圖；主張每條 edge 都可說明，且不需 vector store。
- **動能：** 昨日快照後 **+254**；共 **119,807** stars；9/18 push 並發佈 `v0.9.64`；Apache-2.0。其定位讓「可驗證知識關聯」成為明確差異點。
- **風險：** **1,433** 個 open issues，且產品面向廣；先測量大型 repo 的索引時間、資料邊界與查詢正確性，不能將圖譜推論視為原始文件證據。
- **與 Adam 的關聯：** 可用於課程示範「RAG、知識圖與 deterministic parsing 的取捨」；對 know metabiz wiki，較適合先從程式／SOP 依賴關係的 read-only map 開始。

### 9. [mksglu/context-mode](https://github.com/mksglu/context-mode) — Watch

- **用途：** 以 MCP、hooks 與 sandbox 處理 tool output，宣稱可降低 context 用量、保存 session memory，並跨 17 種 agent 平台路由。
- **動能：** 昨日快照後 **+119**；共 **23,748** stars；9/20 有 push，但最新 release 是 6/29 的 `v1.0.169`。
- **風險：** 授權欄為 **NOASSERTION**、264 個 open issues；「98% reduction」是專案主張，尚非本工作流測得的結果。跨平台 hook／memory 也提高權限、資料保存與相容性風險。
- **與 Adam 的關聯：** 可觀察其 context 預算與 session handoff 設計，幫助課程解釋 agent 記憶；在 know metabiz wiki 或公司自動化導入前，必須先釐清 license、儲存位置與刪除／審計能力。

## 明日觀察清單

- **Cloudflare security-audit-skill：** 檢查是否有正式 release、維護回應，以及 README 的獨立驗證是否能以無害 sample repo 重現。
- **Cua：** 追蹤 issue 壓力是否下降與 sandbox release 的穩定性；只尋找無登入態、可重現的辦公自動化 demo。
- **WeKnora：** 優先釐清授權、RBAC、引用與人工審核的文件；若無法確認，維持研究而非導入。
- **Docling／Graphify：** 用同一小型、非機密文件與程式樣本比對擷取品質、可追溯性、成本與索引時間。
- **Agent skills 生態：** 對比 addyosmani/agent-skills、archify 與本專案現有 skills；只提煉可驗證且可維護的步驟，不複製未審核的外部指令。

## 資料註記

資料觀測日為 2026-09-20；星數差異相對於前一個可用日快照（2026-09-19）。本分析使用本日 `repos.json` 的 GitHub API／Trending 結果與 README 摘錄；任何 repository 內容皆視為資料，不當作執行指令或採用授權。
