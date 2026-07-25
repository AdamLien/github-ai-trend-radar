# GitHub AI Trend Radar — 2026-07-13（已核對 README 版）

> 修訂時間：2026-07-14（Asia/Taipei）。本版逐一閱讀五個入選 repo 的原始 README，並核對 LICENSE；不再把 Trending 的簡短描述延伸成未證實的產品能力或內容標題。
>
> 動量資料仍只來自 GitHub Trending daily：`stars today`、總 stars 與前者／後者比例。匿名 GitHub API 在 collector 過程中限流，因此本版**沒有**宣稱 API star delta、release 日期或 issue 活躍度。那些是下次有 `GITHUB_TOKEN` 後才要補的核對項目。

## 本日結論

這五個 repo 並不是同一類工具：

- **Graphify** 是只要在 Claude Code 執行 `/graphify` 的本地知識圖譜產生器；可輸出 HTML graph、Obsidian vault、Markdown wiki、JSON，並可啟動 MCP stdio server。
- **Hallmark** 是 UI 設計 skill，不是一般用途的 coding framework；其核心是依 brief 選擇版型與主題、做 anti-pattern 檢查，另有 audit / redesign / study 三個命令。
- **Spec Kit** 是規格驅動開發工具鏈：以 `specify` CLI 和 agent slash commands，把 constitution → spec → plan → tasks → implement 排成明確流程。
- **Awesome LLM Apps** 是作者自己維護、可 clone 執行的多類模板庫，不是框架或單一 RAG 產品。
- **Marketing Skills** 是依 Agent Skills spec 寫的行銷工作技能庫；所有其他 skill 會先讀 `product-marketing` 作共同 context。

## 已驗證入選清單

| Repo | 分類 | GitHub Trending 訊號 | README 已驗證的用途與操作 | LICENSE | 目前限制／風險 |
| --- | --- | --- | --- | --- | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 1,028 stars today / 84,157 total（1.22%） | 安裝 `pip install graphifyy && graphify install`（README 說 PyPI 名稱暫為 `graphifyy`）；在 Claude Code 執行 `/graphify <folder>`。它對程式碼做 tree-sitter／call graph，對文件與圖片使用 Claude 抽取關係；輸出 `graph.html`、`obsidian/`、`wiki/`、`graph.json`、報告與快取。支援 `--update`、`--watch`、`--wiki`、`--mcp`。 | MIT | **只明確支援 Claude Code**，不是已證實的 Codex skill；文件／圖片抽取會使用 Claude。README 的 71.5x token benchmark 是專案自述，尚未獨立重現。導入私有資料前需測資料流、成本與圖譜正確性。 |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Skill candidate | 802 / 4,875（16.45%） | 透過 `npx skills add nutlope/hallmark` 安裝；README 明列 Claude Code、Cursor、Codex 的放置路徑。預設用來生成新 UI；`hallmark audit <target>` 只評估既有 code 不修改，`redesign` 保留 copy／IA／brand 後重做，`study <screenshot\|URL>` 抽取設計 DNA，能輸出 `design.md` 交接。 | MIT | 它是設計規則集，不保證 UI 的商業成效或 accessibility。README 所稱的 57 個 slop-test gates 與自我批評機制需要用真實 brief 實測，不能只看示例頁。 |
| [github/spec-kit](https://github.com/github/spec-kit) | Deep research | 508 / 120,400（0.42%） | 需先有 `uv`，以 `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z` 安裝；`specify init` 可選 agent integration。README 描述的主流程是 `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`；Codex CLI skills mode 使用 `$speckit-*`。 | MIT | 這是開發流程改造，不是直接提升生成品質的套件。要先以一個小功能驗證，避免 constitution／spec／plan 變成沒有被採用的文件成本。 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Reference only | 1,006 / 119,348（0.84%） | README 定位為「可 clone、修改、交付」的自有範例模板庫，分成 agent skills、starter／advanced／always-on／multi-agent、MCP、RAG、memory、fine-tuning 等類別。最低範例是 clone repo、進入指定範例、安裝 requirements、執行 Streamlit；README 也聲稱每個模板有原始碼與教學。 | Apache-2.0 | 這不是已驗證品質一致的 production framework；每個子範例的 provider、API key、版本、評估與安全界線都不同。只能逐一挑案例評估，不能因主 repo 熱度整包採用。 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Skill candidate | 260 / 38,285（0.68%） | 面向 technical marketers／founders 的 Agent Skills spec 技能庫，涵蓋 CRO、copywriting、SEO、analytics、growth engineering；README 說可用於 Claude Code、Codex、Cursor、Windsurf。核心設計是 `product-marketing` 作共用 context，其他技能先讀它再執行；可用 `npx skills add ... --skill cro copywriting` 選裝。 | MIT | 行銷建議會受輸入的產品／受眾 context 影響；不應把 skill 產出視為市場證據。若要引入，先選一個技能和一個可量測 KPI 做對照。 |

## 對 Adam 的實際可用性（只根據已驗證功能）

### AI 辦公室與 metabiz wiki

- **Graphify 可做隔離 POC，不可直接導入**：最小測試是選一個無敏感資料的資料夾，確認 `/graphify` 產出的 `obsidian/` 和 `wiki/` 是否可讀、`graph.json` 的關係是否準確、以及文件抽取是否會送至 Claude。這是知識「轉換」工具，不是現成的 wiki 同步器。
- **Marketing Skills 可讀作模板結構**：其 `product-marketing` 共用 context + 專門職能 skill 的設計，可以作為 metabiz 未來技能包的參考；尚未驗證可直接套用到報價、CRM 或 wiki 寫入。

### 開發工作流

- **Spec Kit 最適合先做一個功能試跑**：用既有小需求走完整五步，驗證產出的 spec、plan、tasks 是否真的減少反覆溝通，再決定是否納入團隊標準。
- **Hallmark 應放在 UI 生成／檢查實驗**：其 `audit` 的「不修改」特性適合先對現有頁面得到 punch list；通過人工 design review 後才考慮 `redesign`。

### 課程／內容

本輪不再直接產出吸睛標題。可被 README 支持、值得進一步製作的 demo 只有三個：

1. Graphify：同一個公開小型 repo，展示 `/graphify` 產出的 graph、Obsidian vault、wiki 三種產物，並人工檢查一條關係是否正確。
2. Spec Kit：用一個小功能逐步展示 constitution、spec、plan、tasks 的交接，而不是聲稱它必然比 vibe coding 好。
3. Hallmark：對同一份現有 UI code 先跑 `audit`，再由人工決定是否跑 `redesign`；展示它實際提出的問題，而不是預先承諾美感結果。

## 明日要補的核對，不先下結論

1. 使用 `GITHUB_TOKEN` 重新跑 collector，補上完整快照與 true `stars_delta`。
2. 對 Graphify、Hallmark、Spec Kit 逐一查 latest release、最近 push、open issues／maintainer 回覆，再決定 Deep research 是否保留。
3. 真正執行三個最小 POC：Graphify 的公開資料夾、Hallmark audit、Spec Kit 小功能；把輸入、版本、輸出和失敗點寫入下一份報告。
4. Awesome LLM Apps 只從一個具名子範例開始，閱讀其 requirements、資料處理與 provider 依賴後，才可列為可用 demo。
