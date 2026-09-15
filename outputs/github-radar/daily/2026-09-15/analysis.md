# GitHub AI Trend Radar 分析（2026-09-15）

## 今日判讀

本次以 GitHub Trending daily 加上 10 組指定搜尋詞蒐集，共檢查 283 個 repo。判斷不以總星數單獨排序，而是綜合今日 Trending 星數、前一快照的 star delta、fork delta、最近 push/release、README 可操作性與 issue 活躍度。今日最強訊號是 `alibaba/open-code-review`（Trending 2,751、snapshot +2,744），其次是 `addyosmani/agent-skills`（Trending 354、+334）；高星但增長較慢的 repo 則保留為課程基準或參考。

## 值得投入的 repo

### 1. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

- **定位：Deep research**
- **用途：** Go 寫的混合式 code review 工具，以確定性規則管線搭配 LLM agent，提供逐行評論、多語言規則，以及 OpenAI/Anthropic 相容介面。
- **動能：** 27,748 stars；今日 Trending +2,751，snapshot delta +2,744、fork delta +173；2026-09-15 push 且同日發布 v1.12.2，動能與維護訊號都很強。
- **風險：** 162 個 open issues；企業級規則與 LLM review 的誤判、CI 整合成本仍需實測，不能只以熱門度判斷準確率。
- **對 Adam 的價值：** 很適合做「規則引擎 + agent review」課程案例，也可轉成 metabiz AI office automation 的 PR 品質閘門與 know metabiz wiki 的程式碼治理章節。

### 2. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

- **定位：Skill candidate**
- **用途：** 面向 AI coding agents 的 production-grade engineering skills，涵蓋 Claude Code、Codex、Cursor 等環境。
- **動能：** 94,595 stars；今日 Trending 354、snapshot delta +334、fork delta +25；2026-09-15 metadata 更新，最新 0.6.9 於 2026-09-05 發布。
- **風險：** 121 個 open issues；技能跨 agent runtime 的相容性、版本漂移與授權細節需逐檔確認。
- **對 Adam 的價值：** 可作為本 monorepo skill 設計的對照樣本，萃取可重複的研究、測試、文件與 code-review workflow，服務課程與 AI 辦公自動化。

### 3. [mattpocock/skills](https://github.com/mattpocock/skills)

- **定位：Demo content**
- **用途：** 從實際 `.agents` 目錄整理工程師技能，示範把日常工程流程包成 agent 可載入的 skill。
- **動能：** 262,673 stars；snapshot delta +784、fork delta +61；2026-09-15 更新，最新 v1.2.3 於 2026-08-06 發布。
- **風險：** 497 個 open issues，且缺少明確 topics；高星數可能包含社群擴散效應，需檢查各 skill 的測試與適用邊界。
- **對 Adam 的價值：** 適合做「把自己的工作流程變成 Skill」示範，直接連到課程作業、metabiz 內部 SOP 自動化與 wiki 知識沉澱。

### 4. [openai/codex](https://github.com/openai/codex)

- **定位：Reference only**
- **用途：** 在終端機執行的輕量 coding agent，是 Codex workflow 與 agent 能力邊界的基準實作。
- **動能：** 124,361 stars；snapshot delta +275、fork delta +78；2026-09-15 更新並持續 push，最新 0.154.0 於 2026-09-09 發布。
- **風險：** 17,266 個 open issues，規模大且變動快；使用方式、模型能力與安全限制可能快速改變，不能把 repo star 當成產品承諾。
- **對 Adam 的價值：** 用來校準 Codex 課程與本 monorepo 的 skill 介面、權限和 terminal workflow；作為參考基線，不直接採用未驗證做法。

### 5. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

- **定位：Demo content**
- **用途：** 以 MCP server 讓 Claude、Cursor、Copilot 等 coding agent 控制與檢查 live Chrome，支援 DevTools、除錯、效能分析與 CLI。
- **動能：** 52,045 stars；snapshot delta +121、fork delta +25；2026-09-15 更新，v1.9.0 於 2026-09-08 發布。
- **風險：** 102 個 open issues；瀏覽器自動化涉及權限、資料外洩與不穩定 UI 狀態，demo 必須使用隔離帳號與測試資料。
- **對 Adam 的價值：** 可做「agent 操作瀏覽器完成辦公流程」示範，連接表單、CRM、網站 QA 與 dashboard 驗證，是 AI office automation 的高可視化案例。

### 6. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)

- **定位：Deep research**
- **用途：** 以 Claude Code skill 將來源整理成擁有者可控的 Markdown knowledge graph，支援擷取、連結、檢索與 vault 維護。
- **動能：** 14,928 stars；snapshot delta +36、fork delta +2；2026-09-15 更新，v2.2.0 於 2026-09-10 發布。
- **風險：** 21 個 open issues 代表仍需看實際維護深度；自動整理可能造成錯誤連結、重複筆記或敏感內容落盤。
- **對 Adam 的價值：** 與 know metabiz wiki 最直接相關，可研究 Markdown ownership、來源到筆記的 provenance、知識圖譜與 agent skill 的組合，亦可轉成課程專題。

### 7. [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)

- **定位：Watch**
- **用途：** offline-first 知識與教育伺服器，整合 Wikipedia、書籍、課程、地圖及可選的 local AI，在自有硬體上運作。
- **動能：** 37,100 stars；snapshot delta +309、fork delta +20；2026-09-15 更新，最近 release v1.34.1 於 2026-09-02。
- **風險：** README 顯示範圍很廣但 topics 不明確；離線資料包、硬體需求、內容授權與 local AI 品質要先做小型 PoC。
- **對 Adam 的價值：** 可觀察「私有、可攜、離線知識庫」是否適合 metabiz wiki 或課程內容包；目前先看，不急著採用。

### 8. [BerriAI/litellm](https://github.com/BerriAI/litellm)

- **定位：Skill candidate**
- **用途：** 統一 100+ LLM provider 的 AI gateway，提供 OpenAI 格式、成本追蹤、guardrails、負載平衡與 logging。
- **動能：** 58,792 stars；snapshot delta +77、fork delta +33；2026-09-15 push 並發布 v1.101.0，更新頻率高。
- **風險：** 5,095 個 open issues 是本次候選中最高；`NOASSERTION` license、供應商差異、路由錯誤與成本/資料治理風險都需正式評估。
- **對 Adam 的價值：** 值得抽象成「多模型 gateway + 成本/安全觀測」的 office automation skill 或課程模組；先在低敏感資料與小流量環境驗證。

## 明日 watchlist

1. 追蹤 `alibaba/open-code-review` 的 Trending 星數是否仍維持，以及 v1.12.2 的 issue/PR 回應品質。
2. 追蹤 `addyosmani/agent-skills`、`mattpocock/skills` 是否新增跨 Codex/Claude/Cursor 的共通 skill 介面，並抽查測試與授權。
3. 對 `AgriciDaniel/claude-obsidian` 做最小 PoC：來源匯入、連結建立、引用回溯與敏感資料處理。
4. 比較 `ChromeDevTools/chrome-devtools-mcp` 與其他 browser MCP 的登入隔離、可重現性與失敗復原。
5. 觀察 `project-nomad` 的 release、安裝體驗及內容授權；若 delta 持續，安排離線 wiki 架構研究。
6. 檢查 `BerriAI/litellm` issue backlog 與 v1.101.0 release notes，再決定是否納入內部 gateway 試點。
7. 重新檢查今日兩個新 Trending 項目 `MG1937/ASC`、`linhay/harmony-next.skills` 的 README、license、維護者活動與下一日 star delta。

## 限定與判讀備註

GitHub stars 代表開發者注意力，不等同市場需求、穩定性或商業採用。今日 collector 未出現 API rate-limit 錯誤；個別 Trending repo 回傳 404 時保留了既有 metadata，故需在明日確認其可見性與資料是否恢復。
