# GitHub AI Trend Radar 分析（2026-08-31）

## 今日結論

本次收集 231 個候選 repository；collector 未遇到 GitHub API rate limit。值得追蹤的訊號不只來自總 stars：`archify` 的 snapshot 增量為 4,052、`OpenMAIC` 為 2,927、`scientific-agent-skills` 為 1,756，且都有 2026-08-31 的更新；這三個比單純高星但缺乏近期動能的專案更適合先做內容研究。另一條清楚主線是「可安裝的 agent skill + 可驗證輸出 + 知識/工作流自動化」，與 Adam 的課程、AI office automation 及 know metabiz wiki 高度吻合。

## 值得保留的 repository

### 1. [tt-a1i/archify](https://github.com/tt-a1i/archify) — Deep research

- 目的：以 agent skill 產生可驗證的架構、流程、sequence、data-flow 與 lifecycle 圖，輸出自包含 HTML。
- 動能：36,768 stars；snapshot +4,052；Trending daily +3,993；2026-08-31 更新，v2.16.0 於 2026-08-30 發布。這是本日最強的相對成長訊號之一。
- 風險：MIT 清楚，但圖表正確性仍須人工核對；需測試複雜專案與中文標籤的穩定性。
- Adam 關聯：很適合做「AI 把需求變成可審查架構圖」課程 demo，也可把 metabiz 的 mCRM/mBeauty/mCard 流程轉成 wiki 可嵌入的視覺文件。

### 2. [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — Demo content

- 目的：一鍵建立多 agent 互動教室，讓多個角色協作提供沉浸式學習體驗。
- 動能：26,352 stars；snapshot +2,927；Trending daily +2,819；2026-08-31 更新；`v1.0.0 — Build courses with an agent` 於 2026-08-27 發布。
- 風險：MIT；但 232 個 open issues 顯示早期產品化仍有維運成本，教學品質、成本與 agent 幻覺需實測。
- Adam 關聯：可做「AI 教學助教/多角色課程設計」示範，並研究如何把公司 SOP、FAQ 與 know metabiz wiki 變成互動課堂。

### 3. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) — Skill candidate

- 目的：提供 165 個可重用 agent skills 與 100+ 科學資料庫整合，支援 Claude Code、Codex、Cursor 等。
- 動能：40,490 stars；snapshot +1,756；2026-08-31 更新；v2.65.0 於 2026-08-29 發布；僅 24 個 open issues，維護訊號相對健康。
- 風險：MIT；科學領域的「validated」主張仍要逐項查證，外部資料庫與 API 可能改版。
- Adam 關聯：可作為 skill 設計範本，抽象出「輸入→研究→引用→驗證→交付」結構，移植成課程研究、競品分析與 metabiz wiki 更新流程。

### 4. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research

- 目的：將程式碼、文件、SQL schema、設定與 PDF 轉成可查詢知識圖譜；提供 Claude Code、Cursor、Codex、Gemini CLI 的 `/graphify` skill。
- 動能：112,926 stars；snapshot +391；2026-08-31 更新；v0.9.53 於 2026-08-30 發布；相對成長不如前三者，但總量、release 速度與跨 agent 適配都很強。
- 風險：Apache-2.0；1,171 個 open issues 偏高，需檢查大型 repo 的解析時間、圖譜正確性及 PDF/中文支援。
- Adam 關聯：直接對應 know metabiz wiki 的「文件互聯、決策脈絡、專案知識檢索」；值得做本地資料安全與向量 RAG 的比較研究。

### 5. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Deep research

- 目的：用 Claude Code 將來源整理成自有 Markdown、連結與知識圖譜，打造 Obsidian AI second brain。
- 動能：14,463 stars；snapshot +88；2026-08-31 更新；v2.1.1「Legacy Migration Safety」於 2026-08-25 發布，顯示正在處理遷移風險。
- 風險：MIT；140 個 open issues，且 Obsidian/Claude Code 工作流依賴本機設定，需驗證同步、權限與資料誤寫防護。
- Adam 關聯：與 know metabiz wiki 最直接，可作「來源進入→自動歸檔→雙向連結→人工審核」課程案例，並評估是否吸收成內部 skill。

### 6. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) — Skill candidate

- 目的：透過 MCP 讓 coding agent 操作與檢查 live Chrome、debug、分析效能，並提供 CLI。
- 動能：50,271 stars；snapshot +72；2026-08-31 更新；v1.8.0 於 2026-08-25 發布；93 個 open issues，維護與使用熱度均明確。
- 風險：Apache-2.0；瀏覽器控制權限高，應限制 profile、網域與 secrets，避免把 production session 暴露給 agent。
- Adam 關聯：可形成 AI office automation 的可視化 QA skill：開頁、檢查表單/console/network、截圖與回報；也適合做 MCP 安全邊界示範。

### 7. [EtienneLescot/n8n-as-code](https://github.com/EtienneLescot/n8n-as-code) — Skill candidate

- 目的：把 n8n 的 537 個節點、7,700+ templates 與 TypeScript workflow 提供給 AI agent，支援 Git-like sync。
- 動能：1,552 stars；snapshot +1；最近更新 2026-08-30，v2.5.0 於 2026-07-24 發布。總量小、今日增幅弱，但與自動化落地的題目高度貼合。
- 風險：MIT；模板數量不等於可直接上線，憑證、webhook、重試與冪等性必須逐個審核。
- Adam 關聯：最適合 AI office automation 課程的工作流骨架，例如表單→CRM→通知→wiki；可作 metabiz 內部流程的 skill 候選，但先做 sandbox。

### 8. [DataTalksClub/ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) — Demo content

- 目的：免費、實作導向的 AI developer tools 課程，涵蓋 build、test、deploy、extend、audit；2026 cohort 於 2026-08-31 開始。
- 動能：1,485 stars；snapshot +35；2026-08-31 更新；沒有 open issues。雖非最大型 repo，但課程定位清晰且正逢開課，具有內容市場訊號。
- 風險：repository 未宣告 license；課綱品質與學習成果不能由 stars 單獨推定，需觀察 commit、作業與社群回饋。
- Adam 關聯：可拿來做課程 benchmark，對照 Adam 的 AI office automation/AI coding agent 教學，找出測試、部署與審計模組的缺口。

### 9. [BerriAI/litellm](https://github.com/BerriAI/litellm) — Watch

- 目的：自架 AI gateway，以統一介面串接 100+ LLM，提供成本追蹤、guardrails、load balancing 與 logging。
- 動能：57,678 stars；snapshot +91；2026-08-31 更新；v1.98.0 於 2026-08-23 發布；但 4,914 個 open issues 是顯著維運訊號。
- 風險：license 欄位為 `NOASSERTION`，且 gateway 會接觸模型 API keys、prompt 與輸出；需先釐清授權、secret handling、觀測資料留存與供應商故障模式。
- Adam 關聯：若 metabiz 要把多模型路由、成本控管接進 office automation 或 wiki agent，LiteLLM 值得觀察；目前不宜未審核就作為生產依賴。

## 明日 watchlist

1. 重新確認 `archify`、`OpenMAIC`、`scientific-agent-skills` 的 stars delta 是否持續，並抽查 release notes、近期 commit 與 issue 關閉速度。
2. 實測 `claude-obsidian`/`Graphify` 在一小份去識別化 metabiz wiki 上的匯入、連結、查詢與回復流程，記錄錯誤率與人工審核成本。
3. 用 sandbox 驗證 `chrome-devtools-mcp` 與 `n8n-as-code` 的最小 office automation：瀏覽器 QA、表單到 CRM、通知與 wiki 寫入；禁止使用 production secrets。
4. 追蹤 `OpenMAIC` 的課程匯入與多 agent 成本，並比較 DataTalksClub 課綱可借鑑的評量/部署/審計做法。
5. 對所有「免費 token/API」或高增長專案補做授權、服務條款、資料外洩與供應商依賴審查；stars 只代表開發者注意力，不代表商業需求或可採用性。

