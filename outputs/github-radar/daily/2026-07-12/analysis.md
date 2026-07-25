# GitHub AI Trend Radar — 2026-07-12（台灣）

## 執行摘要

本次以台灣時間 2026-07-13 00:12 執行，目標日期定為前一天 **2026-07-12**。GitHub Trending daily 頁面在執行當下提供的「stars today」是本報告的主要動能訊號；它是 GitHub 的滾動日榜，不是可回溯到 7/12 00:00–23:59 的歷史快照。

最明顯的訊號不是又一個通用 agent framework，而是三個可立即落地的層次：

1. **Agent safety / guardrails**：`destructive_command_guard` 的 444 stars today 對 2.5k 總 stars，短期增速最突出。
2. **可示範的 agent 工具權限**：`DesktopCommanderMCP` 讓 Claude/MCP 取得終端與檔案操作能力，適合作為「能力很強但必須治理」的課程 demo。
3. **把 skills、template、RAG 與 automation 包成可教學的工作流**：`claude-code-templates`、`awesome-llm-apps`、`claude-cookbooks` 有清楚 README 與大量可拆解素材。

### 資料品質與限制

- `GITHUB_TOKEN` 不存在。collector 先以 `--limit 10` 執行，在第 31 個 repo 的 GitHub REST core API 呼叫收到 403 rate limit；依規則改以 `--limit 5` 重跑，第一個 repo 即被同一額度阻擋。
- API core 額度當時為 `0/60`，GitHub 回傳的重置時間為台灣時間約 **01:03**。因此本次沒有完整 `repos.json` / snapshot，也沒有可比較的 API `star delta`。
- 下列「總 stars」與「stars today」均取自本次抓到的 GitHub Trending daily 頁面；「stars today / total」是用該頁數值計算。這是首日基線，不應與跨日 API delta 混為一談。

## 今日最值得追的 repo

| Repo | 分類 | 動能 | 用途與為什麼紅 | 風險 |
| --- | --- | --- | --- | --- |
| [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Deep research | 444 today / 2,543 total（17.46%） | 阻擋 agent 執行危險 git 與 shell 命令。高日增比直接反映 coding agent 進入真實機器後的安全焦慮；README 定位清楚、問題具體。 | 需驗證規則誤擋率、bypass 途徑與是否可納入現有 Codex/Claude 工作流；不能把 guardrail 當成完整 sandbox。 |
| [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | Demo/content idea | 207 today / 7,904 total（2.62%） | 給 Claude 的 MCP server，提供 terminal、檔案搜尋、diff/edit。MCP「從聊天走進本機工作」的演示極直觀。 | 權限面很大；示範需用隔離目錄、最小權限與不含 secrets 的測試資料。 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Skill candidate | 274 today / 29,170 total（0.94%） | Claude Code 的 components、agents、commands、MCP、hooks 與管理 CLI；有文件、安裝路徑與 plugin dashboard。 | 模板集合不等於經過安全與品質驗證；與官方 skills/插件的版本相容性需逐項檢查。 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Demo/content idea | 549 today / 118,344 total（0.46%） | 100+ 可 clone 的 AI agent、MCP、RAG、multi-agent、voice 範例；README 明確主打可執行、provider-agnostic 與教學路徑。 | 範例廣但不代表 production-ready；依賴、API 成本與版本漂移需要在教學前重跑。 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Reference only | 464 today / 48,223 total（0.96%） | 官方 notebooks/recipes，適合作為 Claude 能力與 prompt/tool patterns 的一手參考。 | cookbook 的 notebook 成功不保證可直接投入長流程自動化；需確認目前 API/SDK 版本。 |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | Watch | 79 today / 13,670 total（0.58%） | 在 coding-agent 範圍內進入日榜，值得觀察其開發體驗與 agent loop 的差異化。 | Trending 頁未提供清楚描述；本次 API 受限，尚未完成 README、release、issue 健康度核查，暫不建議導入。 |

## 分類與 Adam 的可用性

### Deep research

- **`destructive_command_guard`**：可做一個「AI coding agent 上 production 前，最低限度要有哪三層保護」的課程小節。對 AI 辦公室自動化尤其重要：先界定可讀、可提案、可執行與需人工核准的動作。
- **`DesktopCommanderMCP`**：深入評估 MCP 權限模型、audit log 與人機核准點後，可轉為 metabiz 內部 agent 的受控桌面操作範例，而非直接給全權 shell。

### Demo/content idea

- **`awesome-llm-apps`**：內容主題可用「把一個 RAG 範例改成公司 wiki 問答，哪些資料治理仍不能省？」；採一個狹窄範例完成從資料夾、檢索到回答引用的端到端 demo。
- **`DesktopCommanderMCP`**：可做正反兩段 demo：先展示檔案搜尋與 diff，再展示為何 destructive command 需要攔截。這比單獨介紹 MCP 更能建立實務判斷力。

### Skill candidate

- **`claude-code-templates`**：不直接複製大包模板；先萃取 1–2 個有重複價值的模式（例如 repo onboarding、變更前安全檢查），轉為符合 Codex 本機規則與 metabiz 工作流的小型 skill。

### Watch

- **`t3code`**：明天先補 README、最近 release、未解 issue、授權與安裝成本。若仍有成長，再和 Codex / Claude Code / Cursor 的 task delegation 差異做比較。

### Reference only

- **`claude-cookbooks`**：拿來確認官方 capability 與範例寫法，不作為內部 workflow 的直接依賴。

## 對課程、內容、AI 辦公室與 metabiz wiki 的建議

1. **課程模組**：安排「Agent 能做什麼」後立刻接「Agent 不該直接做什麼」。以 `DesktopCommanderMCP` + `destructive_command_guard` 建立權限、核准、回滾三個概念。
2. **本週內容選題**：`MCP 不只是接工具：當 AI 會動你的檔案與終端，安全邊界怎麼畫？` 內容可用兩個上述 repo 的 daily momentum 作開場，但不要把 stars 當市場需求證明。
3. **AI 辦公室自動化**：以 `claude-code-templates` 的「模板化」訊號為靈感，優先把現有重複流程（資訊蒐集、草稿、核對、人工核准）拆成小 skills；寫入或發送類行為必須留可檢視的 approval gate。
4. **know metabiz wiki**：`awesome-llm-apps` 的 RAG 範例可用於探索資料夾級 ingestion、回答附來源與更新頻率，但 wiki 的權限、敏感資料分類、引用可追溯性與人工修正流程仍是主體，不應由模板取代。

## 明日續追清單

1. `Dicklesworthstone/destructive_command_guard`：核對日增是否延續、release/issue 活躍度與允許/拒絕策略。
2. `wonderwhy-er/DesktopCommanderMCP`：核對權限限制、維護狀態與是否有可審計的操作紀錄。
3. `davila7/claude-code-templates`：挑兩個 template 實測安裝、卸載、版本衝突與安全邊界。
4. `Shubhamsaboo/awesome-llm-apps`：挑一個 RAG 或 always-on agent 做 30 分鐘內可重現的 demo 篩選。
5. `pingdotgg/t3code`：補 API metadata、README/release/issues 後再決定是否升級為 deep research。
6. `anthropics/claude-cookbooks`：只追官方新增 recipe；把可重用片段與非正式 demo 區隔。

## 下一次執行

- 在 automation 環境提供 `GITHUB_TOKEN`，以避免匿名 REST core `60/hour` 限制；同一輸出目錄的 collector 完整成功後，才會建立跨日 `stars_delta` 基線。
- 保持 `--limit 5` 作為無 token 的保守回退，但在 core quota 未重置前仍無法完成 repo metadata 快照。
- 下一次先讀取本目錄的 snapshot；將 API delta、最近 push/release、issue 健康度和 README 清楚度一起排序，而非按總 stars。
