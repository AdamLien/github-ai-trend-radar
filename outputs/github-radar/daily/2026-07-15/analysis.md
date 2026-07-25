# GitHub AI Trend Radar — 2026-07-15（台灣）

> 產生時間：2026-07-16 00:12–00:16（Asia/Taipei）。GitHub Trending 的 `daily` 是執行當下的 rolling 24 小時榜；本次在跨日後取得，作為 7/15 收尾的近似動能快照，而非可回溯的歷史頁面。
>
> `GITHUB_TOKEN` 未設定。collector 先以 `--limit 10`、再依規則降為 `--limit 5` 嘗試，皆被 GitHub REST API 403 rate limit 擋下；因此**沒有 `repos.json`、snapshot 或可比較的 `star_delta`**。以下 `stars today` 僅來自 Trending HTML，總 stars 與用途則逐一核對 repo 首頁/README。

## 結論

今天的信號不是新的 MCP server，而是「把 agent 行為產品化」：可移植的 Skills（`mattpocock/skills`、`hallmark`、`marketingskills`）、安全護欄（`destructive_command_guard`），以及可被拿去教學/示範的 Agent/RAG 範本。最值得優先實作驗證的是 Hallmark、dcg 與 Matt Pocock 的 skills；OpenCut 是內容製作自動化的高動能觀察項目，但它的 MCP/自動化能力仍在重寫路線圖中，不能當成現成方案。

## 今日最值得追的 repo

| Repo | 分類 | 用途（README/首頁核對） | 動能 | 為何值得看 | 主要風險 |
|---|---|---|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | Deep research；Skill candidate | 從作者 `.claude` 目錄整理出的工程 Skills，含 `skills/`、`.claude-plugin`、`.agents` 與安裝/發布結構。MIT。 | **2,160 today**；171,849 總星；約 **1.26%** | 今天絕對新增最高；有 2026-07-08 release，結構可直接用來比對我們的 skill packaging。 | 高星集合不等於每個 skill 都適合本機流程；需逐項檢查權限、依賴與輸出品質。 |
| [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | Demo/content idea；Watch | 開源 CapCut 替代品；README 說明現正以 Rust core 重寫，規劃 plugin-first、MCP server、headless batch rendering 與 editor scripting。MIT。 | **1,505 today**；70,759 總星；約 **2.13%** | 創作者工作流與 AI 辦公室內容很貼近，且「剪輯器為何要有 MCP/headless」是好題目。 | 新版尚在重寫，README 指出目前應用 classic；尚未開放外部貢獻，不能把規劃中的 MCP 當可用功能。 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Demo/content idea；Reference only | 100+ 可 clone、customize、ship 的 AI Agent/RAG 範例，目錄包含 agent skills、MCP agents、always-on agents。Apache-2.0。 | **1,278 today**；121,687 總星；約 **1.05%** | 適合把單一範例拆成 Adam 的課程 demo／短影音實作起點。 | 範例庫不是架構背書；每個範例的維護度、模型費用與 secrets 管理要個別查。 |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | **Skill candidate；Deep research** | Claude Code、Cursor、Codex 的 anti-AI-slop 設計 skill；提供 build、audit、redesign、study 四種操作，並有明確安裝方式。MIT。 | **1,119 today**；7,480 總星；約 **14.96%** | 今日相對動能最高的一群；可直接改善 AI 產生頁面的設計審稿與 handoff。 | 它是設計品質規則集，不是可量化的商業成效保證；先以 mIMS/metabiz 實例做 A/B review。 |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Watch | 個人交易 agent；repo 明示 MCP、multi-agent、LLM、backtesting 與 wiki。MIT。 | **924 today**；23,497 總星；約 **3.93%** | 可研究多 agent、tool/wikilayer 如何包成可展示產品。 | 金融/交易領域不應作為投資建議或直接導入；需獨立驗證資料來源、回測與權限邊界。 |
| [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | Reference only；Demo/content idea | AI/ML research engineer 的數學、CS、ML、computational linguistics 自學教材集合。 | **729 today**；5,740 總星；約 **12.70%** | 高相對動能，適合「AI 工具使用者下一步該補什麼基礎」的內容選題。 | 是學習資源而非可整合的 automation/agent 元件；不可取代正式課綱或教材審核。 |
| [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | Deep research；Reference only | 低成本模型 coding agent；README 有多種 harness（含 `claude-code`、`qwen-code`、`swe-agent` 等）切換說明。 | **607 today**；65,264 總星；約 **0.93%** | 對「agent harness vs model」的課程比較很有用，且可作為 Codex 外的對照組。 | 會執行程式/系統操作的 agent 需沙箱與 approval；不要以「低成本」推論品質或安全性。 |
| [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | **Deep research；Skill candidate** | `dcg` 阻擋 agent 執行危險 git/shell 指令，提供 allowlist 驗證與過期規則 dry-run。 | **497 today**；4,642 總星；約 **10.71%** | 是 coding agent 上線時最具體的安全護欄候選；README 的 allowlist 操作路徑清楚。 | 規則過嚴會阻礙正常自動化，過寬又失去保護；先在非 production repo 測 false positive。 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Skill candidate；Demo/content idea | 給 Claude Code 與 AI agents 的 CRO、文案、SEO、分析與 growth engineering skills；有 validation script 與 plugin 結構。 | **390 today**；39,524 總星；約 **0.99%** | 可以萃取「內容企劃 → landing page → 成效檢核」的技能介面設計，不必整包採用。 | 行銷輸出仍要符合 metabiz 品牌、事實與法規；不能自動發布或把轉換率主張當保證。 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Watch；Deep research | 終身個人化教學系統；repo 含 CLI/web/tests，README 列出 LlamaIndex、LightRAG、agent engine 與 Codex-inspired CLI 等依賴/靈感。 | **128 today**；26,120 總星；約 **0.49%** | 對「文件/RAG 不只回答，還要記住學習歷程」及課程產品化有研究價值。 | 今日動能較低；需先評估資料持久化、學員隱私與繁體中文品質，不能直接接 know metabiz wiki。 |

> 比率 = `stars today / 當下總 stars`，只用來看短期注意力密度，不代表品質、營收或真實採用。`star_delta` 因本次 API 快照失敗而不提供。

## 對 Adam 的可用行動

- **課程**：做一個「Skill 不是 prompt：如何有 install、驗證、權限與版本」單元，以 `mattpocock/skills`、Hallmark、dcg 為三個層次範例。
- **內容選題**：
  1. 「爆紅 1,119 星/日的 Hallmark：AI 網頁不再長得像同一個模板，但它不能替你做品牌決策。」
  2. 「Agent 最大風險不是模型笨，是它真的能下 `git reset --hard`：dcg 的 guardrail 設計。」
  3. 「OpenCut 的 MCP/headless 路線，揭示內容剪輯下一步是可被 agent 編排；但今天還不能直接上 production。」
- **AI 辦公室自動化**：先研究 dcg 的規則/allowlist 模型，將 destructive action 與一般寫檔操作分級；OpenCut 只列入未來影片批次化 watchlist。
- **know metabiz wiki**：DeepTutor 的 RAG/學習歷程是研究參考，不能直接接 wiki。先維持既有 wiki intake，若要試驗，另建去識別化的副本與 retrieval 評測集。

## 明日追蹤清單

1. `Nutlope/hallmark`：是否持續高相對動能；讀 ROADMAP 與 issue/PR，挑一個真實頁面做 audit。
2. `Dicklesworthstone/destructive_command_guard`：安裝前先審查預設規則與 macOS/Codex 相容性；只在 disposable repo 做 dry-run。
3. `mattpocock/skills`：比較其 skill metadata、版本與驗證腳本，挑 1–2 個低權限 skill 深讀。
4. `OpenCut-app/OpenCut`：追蹤 MCP/headless 是否真的落地到 release；在此之前不排入工具鏈。
5. `HKUDS/Vibe-Trading`、`HKUDS/DeepTutor`：僅追 agent orchestration/RAG 設計，不碰交易決策；確認是否有可重現 demo 與近期 issue 回應。

## 執行產物與限制

- Trending daily HTML：成功擷取並以 AI/agent/skills/RAG 範圍過濾。
- GitHub collector：已按指定十組 query 跑過 `--limit 10`；rate limited 後再以 `--limit 5` 跑過，均為匿名 REST 403。
- 本次未產生：`repos.json`、`report.md`、`snapshots/`（collector 在第一個搜尋 API 請求即失敗）。下次需提供可用 `GITHUB_TOKEN` 才能恢復跨日 `star_delta` 比較。
