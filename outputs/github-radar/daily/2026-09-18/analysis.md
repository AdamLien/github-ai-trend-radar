# GitHub AI 趨勢雷達分析（2026-09-18）

## 結論

本次收集 297 個候選庫；GitHub Trending 當日新增／在榜訊號比歷史總星數更值得重視。由於可用的上一份完整日快照是 2026-09-16，且本輪累積候選的 `stars_delta` 均為 0，不能把它解讀為「沒有成長」；今天以 Trending 的當日星數、相對規模、最近 push／release、README 是否可操作，以及 issue 壓力來判斷。優先採取兩條路線：一是把可驗證的 agent skills 轉成課程與內部工作法，二是以受控帳號／最小權限方式測試瀏覽器與知識工作自動化。

| Repository | 動能與依據 | 總星數 | 分類 |
| --- | --- | ---: | --- |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Trending 當日 **3,019** 星（本輪最高）；README 清楚說明六階段、隔離 agent 與獨立驗證的稽核流程。 | 12,630 | Skill candidate |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Trending 當日 **2,724** 星；9/18 有 push 與 v1.12.6 release，且把規則式檢查和 LLM agent 結合。 | 36,376 | Deep research |
| [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) | 新進雷達，Trending 當日 **1,319** 星；9/18 push、9/17 CLI release；README 明確支援 Codex、Claude Code、Cursor 等既有登入瀏覽器。 | 5,064 | Demo content |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Trending 當日 **965** 星；9/17 push，README 將 skills、memory、安全與 research-first 開發整合成 agent harness。 | 261,722 | Deep research |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Trending 當日 **677** 星；9/18 push 並發布 0.6.10，README 有從 plan 到 ship 的可重複工程品質閘門。 | 96,222 | Skill candidate |
| [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | 新進雷達，Trending 當日 **571** 星；9/18 push、9/14 v1.0.0；定位自架、多使用者、多 agent。 | 3,854 | Watch |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Trending 當日 **300** 星；9/18 更新。README 將 skills、connectors、slash commands 與 sub-agents 打包為職能插件。 | 24,774 | Demo content |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 新進雷達，Trending 當日 **298** 星；9/17 push 並發布 v1.13.1，主題是 AI coding assistant 的 spec-driven development。 | 69,185 | Deep research |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | 新進雷達，Trending 當日 **140** 星；9/18 push，提供可本機執行的 memory／context engine 與自架路徑。 | 30,127 | Watch |

## 值得採取的行動與風險

### cloudflare/security-audit-skill

- **用途：** 讓 coding agent 依偵察、覆蓋率導向搜尋、候選驗證、結構化輸出與獨立覆核執行安全稽核。
- **對 Adam／Metabiz 的關聯：** 很適合萃取成「AI 協作程式碼審查與交付前檢核」課程單元，也可成為 Metabiz 專案維護、客製開發與 wiki 變更的安全驗證範本。
- **風險：** 安全掃描與 agent 的工具權限不可直接對客戶或 production 執行；先用刻意脆弱的測試庫、只讀權限與人工複核。雖 README 清晰，但本日沒有 release，需自行釘選版本／commit。

### alibaba/open-code-review

- **用途：** 對 PR 或程式變更做行級評論，結合 deterministic pipeline、多語言安全規則與 OpenAI／Anthropic 相容的 LLM agent。
- **對 Adam／Metabiz 的關聯：** 可做「AI code review 何時要規則、何時要 LLM」的高意圖內容；亦值得研究能否轉化為 Metabiz 客製案的 CI 品質關卡與 wiki 中的交付準則。
- **風險：** 230 個 open issues 代表整合和邊界情境仍有壓力；先以一個非關鍵 repository 比對現有 CI 的誤報率，且勿把敏感程式碼自動送往未核准模型端點。

### Tencent/BrowserSkill

- **用途：** 以 CLI + 瀏覽器 extension 把使用者已登入的瀏覽器分頁，明確借給 shell 型 AI agent 操作。
- **對 Adam／Metabiz 的關聯：** 是很直觀的 AI 辦公自動化 demo：彙整公開研究、檢查 CMS／後台資料、從表單到 wiki 草稿；可比較「read-only research」與「會寫入帳號」的治理差別。
- **風險：** 這是登入態瀏覽器自動化，可能觸及 cookie、個資與誤操作。只用獨立測試 profile、限定可借用分頁與無權限帳號；50 個 open issues 下，不應先用於付款、CRM 寫入或客戶帳號。

### affaan-m/ECC

- **用途：** 為 Claude Code、Codex、OpenCode、Cursor 等建立有 skills、memory、安全與研究優先流程的 agent harness。
- **對 Adam／Metabiz 的關聯：** 適合做「不是更多 prompts，而是可量測的 agent operating system」內容，並把研究、計畫、驗證、wiki handoff 分段納入 Metabiz 團隊工作流。
- **風險：** 261,722 星與 39,167 forks 容易造成成熟錯覺；228 個 open issues、範圍很大，應先取一段 workflow（例如 research-first + verify）做小型試點，避免一次導入整套 framework。

### addyosmani/agent-skills

- **用途：** 把資深工程師的規劃、建置、驗證、review、交付流程封裝為可重用的 agent skills。
- **對 Adam／Metabiz 的關聯：** 可作為 Codex skill 設計教材與內部 skill QA 標竿；特別適合把報價前需求澄清、文件 QA、程式改動驗證等重複步驟逐步固化。
- **風險：** 通用 engineering skills 不等於 Metabiz 業務規則；需把客戶資料、報價核准、Odoo 寫入等高風險操作拆出人工 approval，並在 fork／引用前審閱每個 skill 的 shell 與外部工具行為。

### TencentCloud/Octop

- **用途：** 面向團隊的自架、多使用者、多 agent AI assistant。
- **對 Adam／Metabiz 的關聯：** 可作為「公司內部 AI cowork／知識協作」的架構研究，與 know Metabiz wiki 的長期維護、角色分工與審計需求相符。
- **風險：** 專案很新（2026-07 建立），但已有 235 個 open issues；先做架構、身分、資料保留和多租戶隔離 review，不把它視為可立即承載內部知識的正式平台。

### anthropics/knowledge-work-plugins

- **用途：** 為職能與團隊打包 skills、connectors、slash commands、sub-agents，主要供 Claude Cowork，也宣稱相容 Claude Code。
- **對 Adam／Metabiz 的關聯：** 是把「Metabiz wiki 維護／課程內容研究／例行辦公」從 prompt 集升級為職能包的最佳 demo 參考；可先拆解其插件資訊架構，而非綁定特定產品。
- **風險：** 沒有版本化 release 資訊，且平台相容性、connector 的資料邊界須逐一驗證；採用其模式時應保持 provider-neutral 的 skill 文件與本地可測試性。

### Fission-AI/OpenSpec

- **用途：** 用明確 specification 驅動 AI coding assistant 的計畫、變更與驗收。
- **對 Adam／Metabiz 的關聯：** 可融入客製開發課程的「先規格、再 agent」章節，也可讓需求、驗收條件、變更紀錄回寫 know Metabiz wiki，降低長任務遺失上下文。
- **風險：** 232 個 open issues；規格流程有額外前置成本。先選需求常變但可量化驗收的內部小功能，評估是否真的降低返工，而非把模板本身變成負擔。

### supermemoryai/supermemory

- **用途：** 提供可本地執行的 agent memory／context engine、API 與 self-host 路徑。
- **對 Adam／Metabiz 的關聯：** 值得研究為 wiki／文件助理提供「工作記憶」而不等同於全量 RAG 的可能性；可延伸成 AI 辦公自動化中脈絡壓縮與知識更新的內容題材。
- **風險：** 107 個 open issues，最近 server release 為 2026-08；先以去識別化 wiki 副本測試召回、刪除權與資料保留，勿把 memory 與真實的知識正確性混為一談。

## 明日 watchlist

1. 再跑同一組 queries，比較 BrowserSkill、Octop、OpenSpec、supermemory 是否仍留在 Trending，以及第一次可用的日差星數／相對成長。
2. 追蹤 `open-code-review` 的 v1.12.6 後續 issue／release；若誤報與規則可調，再排一個隔離 CI demo。
3. 用最小、可撤銷的測試環境演示 BrowserSkill：只讀公開網站、單一借用分頁、全程錄製並驗證 agent 是否確實歸還控制權。
4. 將 `security-audit-skill`、`agent-skills`、`knowledge-work-plugins` 的共同結構整理成 Metabiz skill checklist：輸入範圍、工具權限、品質閘門、人工核准、證據與 wiki handoff。
5. 對 Octop 與 supermemory 做資料治理 desk review：SSO／角色、secret handling、刪除與保留、self-host 成本、多租戶隔離；未通過前只列為研究，不導入客戶資料。

## 方法註記

分類每案僅採用一個限定標籤：`Deep research`、`Demo content`、`Skill candidate`、`Watch` 或 `Reference`。本分析將當日 Trending 視為短期注意力訊號，不等同採用建議或商業需求；所有寫入型自動化均應先經權限、資料與人工覆核設計。
