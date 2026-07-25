# GitHub AI Trend Radar — 2026-07-20（台灣）

> 收集時間：2026-07-21 00:16（Asia/Taipei）；目標日期為前一個台灣日期 2026-07-20。這是一份「現在可觀測」的 radar，而非 GitHub Trending 的歷史封存。

## 摘要

- 已用已登入 GitHub 帳號的 API token 跑完十組指定查詢，得到 **89 個去重 repo**、`repos.json`、`report.md` 與 2026-07-21 快照；沒有 rate limit，因此維持 `--limit 10`。
- folder 本身是第一個快照，內建 `stars_delta=0` 沒有資訊價值。為避免誤判，本報告另以 2026-07-19 資料夾中可重疊的 **88 個 repo** 重算約 24 小時 star delta。
- GitHub Trending daily 在本次讀取只回傳前端「Loading」殼，沒有可驗證的 repo 清單或 `stars today`；因此本日不宣稱任何 `stars today`，以可重算 delta、推送/發版活動、README 定位與風險排序。
- 本日主線不是再加一個 agent framework，而是三條可驗證的實作題：**可追溯 code/wiki context（Graphify）**、**token/context 成本控制（headroom）**、以及**把 agent workflow 變成可稽核的 loop/任務制度（loop-engineering、Multica）**。

## 今日最值得追的 repo

| Repo | 分類 | 約 24h 訊號 | 用途與為何值得看 | 對 Adam 的可用性 | 主要風險 |
| --- | --- | --- | --- | --- | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **Deep research** | **+643**；92,071 stars；7/20 推送與 v0.9.22 發版 | 將 code、文件、SQL schema、設定與 PDF 轉成可查詢知識圖；明確支援 Claude Code、Cursor、Codex、Gemini CLI，並主張本地 deterministic AST、每條邊可解釋。README 定位清楚且當日仍有發版。 | 最接近 `know metabiz wiki`／程式脈絡的「可溯源查詢」PoC；可拍「RAG 之外：為何程式知識需要結構化邊」課程段落。 | 即使 AST 在地，餵入私有 wiki/ERP schema 前仍要驗證資料外送、索引刪除、權限隔離與授權；先用去識別子集。 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | **Deep research** | **+579**；60,623 stars；7/20 推送；Apache-2.0；v0.32.0 | 壓縮 tool output、log、檔案和 RAG chunk，提供 library、proxy 與 MCP server；正中 coding agent 的 context 成本/噪音問題。 | 適合做「壓縮前後答案正確率、延遲、token」實驗，成為 AI 辦公室或 wiki agent 的可觀測成本閘門。 | 任何「same answers」效益都要用 Adam 的真實任務做 holdout 驗證；壓縮可能遺失稽核細節或安全關鍵欄位。 |
| [obra/superpowers](https://github.com/obra/superpowers) | **Reference only** | **+580**；258,043 stars；7/20 推送；MIT | Agentic skills framework + 軟體開發方法論；增量與總星數都極高，仍有推送。 | 可作為「skill 是可執行工作契約，而非 prompt 收藏」的對照教材，借鑑測試、計畫、驗證的規律。 | 生態熱度不等於直接採用；先抽取可對應現有 Codex skill 的規則，避免導入第二套權威或流程衝突。 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | **Watch** | **+607**；73,284 stars；7/20 推送；MIT；v0.80.10 | 統一 LLM API、agent loop、TUI 與 coding-agent CLI 的 toolkit；是本日增量第二高且 release 很新。 | 可做「同一任務換模型/agent loop 的成本與可重現性」技術 demo；適合作為 runtime 參考。 | 不是現有多代理工作板的直接替代品；須先確認模型供應商、權限、記錄與 Mac 開發環境整合。 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | **Skill candidate** | **+179**；8,785 stars；7/20 推送；MIT | 提供 loop-audit、loop-init、loop-cost 與 orchestration patterns，焦點是把 prompt/agent 設計成可迭代的工程 loop。 | 最值得萃取成 Adam 內部 skill 的是：任務循環診斷、成本預算、停止條件與可驗證 handoff；可連接課程的「agent 從 demo 到作業系統」。 | repo 相對小，star growth 可能受短期傳播影響；不要未評估就把其 CLI 或角色框架當標準。 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | **Watch** | **+141**；41,194 stars；7/20 推送與 v0.4.6 發版 | 管理型 agents 平台：派工、追蹤進度、累積 skills；與 Adam 已研究的 human+multi-agent workbench 問題高度相鄰。 | 可拿來對照 Mission Control/Plane 的責任邊界：誰派工、誰核准、誰保存 agent memory 與品質證據。 | `NOASSERTION` license、1,167 open issues；先做隔離 demo，勿接真實 backlog、憑證或內部知識。 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | **Skill candidate** | **+171**；79,437 stars；MIT；最近推送 7/18 | production-grade coding-agent skills；README 定位單一、可作為可重用工程技能的審查樣本。 | 適合精選幾個低風險、可測試的規範，與既有 Codex skills 比較，形成「可安裝 skill 的審核表」。 | 不要把熱門 skill collection 直接加入全域：檢查 shell 執行、資料讀取、網路行為、授權和與 RTK/既有 AGENTS 規則衝突。 |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | **Demo/content idea** | **+74**；9,690 stars；MIT；v1.9.2 | 以 Markdown 擁有權、來源丟入後自組織/連結為核心，且明確提及 Karpathy LLM Wiki pattern。 | 很適合做「Obsidian LLM Wiki：不可變 raw source → wiki synthesis → discovery surfaces」的課程/demo 對照。 | 最近推送/發版在 5 月，非本日活躍核心；自動分類/連結不等於事實正確或知識治理，保留人工審核與來源鏈。 |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | **Watch** | **+69**；14,963 stars；7/20 推送與 v0.6.5 發版 | 桌面端將文件變成持久、互連 wiki，主張不同於每次從頭 retrieve-and-answer 的傳統 RAG。 | 可作為 `know metabiz wiki` 的 UX 與「持續整理 vs. 查詢時 RAG」比較案例。 | `NOASSERTION` license；先核對文件上傳、向量/索引儲存、刪除與機密資料處理，不能把它視為現成企業知識庫。 |

## 可轉成內容、課程與辦公室自動化的行動

1. **Deep research：Graphify 去識別 PoC。** 固定一個小型 code + Markdown + schema 樣本，驗證來源連結、刪除後再索引、ACL、外送與查詢幻覺；產出一段「knowledge graph 何時勝過向量 RAG」的證據型內容。
2. **Demo/content：Headroom correctness × cost。** 用三個真實工作（長 log 排錯、wiki 問答、MCP tool 回傳）比較原文/壓縮後的答案、token、耗時與漏答，禁止只報節省率。
3. **Skill candidate：loop audit。** 把 loop-engineering 的問題化為現有 Codex workflow：目標、可觀測輸入、停損、審核人、證據、成本上限。這比直接安裝整套多 agent 框架更可控。
4. **AI 辦公室：先定權責、後選 runtime。** Multica、pi、superpowers 的共同啟示是能力已很多；Adam 的瓶頸仍是任務准入、人類核准、資料權限與可回溯 handoff，而不是少一個 agent loop。

## 風險與假陽性

- 本日是 API snapshot 的跨資料夾比較，不是 GitHub 官方歷史 Trending。Delta 約跨 2026-07-20 → 2026-07-21 的收集時間；避免用它聲稱「7/20 當天精準新增星數」。
- `stars / total` 只是一個注意力 proxy；本表刻意把總星高但不直接解決 Adam 近期問題的 repo 標為 Reference/Watch。
- license 為 `NOASSERTION` 的 Multica、LLM Wiki 不列入直接採用；先完成 license 與資料流審查。任何 MCP/agent 工具也不得未隔離就連 ERP、私有 wiki 或憑證。

## 明日繼續追蹤

- `Graphify-Labs/graphify`：release 後 issue 反應、私有資料邊界與本地解析證據。
- `headroomlabs-ai/headroom`：壓縮品質 benchmark、MCP proxy 的安全和可觀測性。
- `cobusgreyling/loop-engineering`：可獨立萃取的 loop-audit/cost pattern，以及是否能以測試驗證。
- `multica-ai/multica`：license 澄清、issue 回應、權限/審核模型；只做隔離評估。
- `earendil-works/pi`：新 release 穩定性、模型供應商與 coding-agent runtime 的差異。
- `AgriciDaniel/claude-obsidian`、`nashsu/llm_wiki`：Markdown ownership、raw-source provenance、刪除與 access-control 是否真正可實作。

## 產物

- API records：`repos.json`（89 repos）
- collector report：`report.md`
- snapshot：`snapshots/repos-2026-07-21.json`
- 本分析：`analysis.md`
