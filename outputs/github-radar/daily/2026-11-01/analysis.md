# GitHub AI 趨勢雷達｜2026-11-01

## 日期、資料與判讀方式

- 歸檔目標：前一個 Asia/Taipei 日曆日 **2026-11-01**。實際收集開始時間（UTC）：2026-11-01T16:11:22.416406+00:00。
- Trending 觀測時間（UTC）：2026-11-01T16:12:06.637408+00:00；來源：[GitHub Trending daily](https://github.com/trending?since=daily)。這是執行當下的 rolling daily 榜單，不能回推成 11 月 1 日整日統計。
- 本次保留 389 個 repo，Trending 卡片經人工主題校正保留 14 個。排除一般 API 清單、紫微排盤及 compositor；LLM jailbreak 清單僅作主題資料保留，不執行其內容。
- 未偵測到 GitHub API rate-limit 錯誤；使用 --limit 10，無需降為 5。
- 搜尋本身依 GitHub stars 排序，存在大型專案偏差；本篇選題另綜合 stars today、相鄰快照星數差／相對成長、最近 push、README、release 及近期 Issue／PR 抽樣，並以 Adam 的課程與工作用途決定優先度。
- 快照差值以 2026-10-31 的相同 repo 為基準；相對成長＝差值／前次星數。非同一時間點或非完整 24 小時，不能稱為嚴格日增。首次觀測沒有可比基準時標為未量測；stars today 缺值不等於零。
- open_issues 是 GitHub open_issues_count，可能包含 PR；近期活動僅取最多 5 筆最近更新的 Issue／PR，不能據此推論整體解題速度。README 宣稱及風險為文件觀察與編輯判斷，本次未安裝、執行或實測外部專案。

## 今日值得投入的 10 個 repo

下列順序是編輯投入優先度；Wiki 小型專案因工作關聯仍保留席位，並非按總星數排序。

| Repo | stars today | 總 stars | 快照差值 | 相對成長 | 建議 |
|---|---:|---:|---:|---:|---|
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 3100 | 37,062 | +2,716 | +7.91% | Deep research |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 1527 | 108,775 | +1,449 | +1.35% | Deep research |
| [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | 827 | 39,821 | +876 | +2.25% | Demo content |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 919 | 10,300 | +967 | +10.36% | Watch |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 970 | 31,882 | +997 | +3.23% | Skill candidate |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 178 | 9,330 | +241 | +2.65% | Demo content |
| [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | 436 | 5,980 | 未量測 | 未量測 | Reference only |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 573 | 39,970 | 未量測 | 未量測 | Reference only |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 未入本次榜／未量測 | 309,016 | +950 | +0.31% | Skill candidate |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 未入本次榜／未量測 | 3,669 | +2 | +0.05% | Skill candidate |

### 1. pingdotgg/t3code — Deep research

- **用途**：在手機、網頁與桌面統一控制本機 coding agents，README 明列 Claude Code、Codex、Cursor 等整合。
- **動能與維護**：數值見上表；最近 push：2026-11-01T16:09:32Z；最新 release：v0.1.6（2026-10-31T10:52:24Z）；open issues/PR：3,889。活動抽樣最新更新：2026-11-01T16:12:16Z。
- **對 Adam 的關聯**：可做 Adam「一人多 agent 工作台」課程與手機接手開發內容；AI 辦公可研究任務交接，know metabiz wiki 僅適合作為操作入口。
- **風險／驗證重點**：遠端控制與工作階段權限是主要風險；近期 PR 涉及首次啟動辨識及權限載入，不應假設跨裝置體驗已穩定。
- **來源**：[README](https://github.com/pingdotgg/t3code#readme)、[Releases](https://github.com/pingdotgg/t3code/releases)、[Issues](https://github.com/pingdotgg/t3code/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 2. thedotmack/claude-mem — Deep research

- **用途**：保存、壓縮並在後續 agent 工作階段注入上下文，定位是跨 session 記憶。
- **動能與維護**：數值見上表；最近 push：2026-11-01T05:21:17Z；最新 release：v15.8.0（2026-11-01T04:02:00Z）；open issues/PR：166。活動抽樣最新更新：2026-11-01T16:02:40Z。
- **對 Adam 的關聯**：適合 Adam 示範「上下文不失憶」；辦公流程可研究交接摘要，know metabiz wiki 則應保留可引用原始文件，避免以 agent 記憶取代知識來源。
- **風險／驗證重點**：記憶可能夾帶敏感內容、過時決策或提示注入；近期 launcher 與 Windows 啟動修補顯示需跨平台驗證。
- **來源**：[README](https://github.com/thedotmack/claude-mem#readme)、[Releases](https://github.com/thedotmack/claude-mem/releases)、[Issues](https://github.com/thedotmack/claude-mem/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 3. lightpanda-io/browser — Demo content

- **用途**：為 AI 與自動化設計的 headless browser，可研究瀏覽器工具鏈的資源成本。
- **動能與維護**：數值見上表；最近 push：2026-11-01T09:35:11Z；最新 release：1.0.2（2026-10-23T09:01:02Z）；open issues/PR：101。活動抽樣最新更新：2026-11-01T14:37:38Z。
- **對 Adam 的關聯**：適合 Adam 製作與既有 Chromium 流程的實測內容；辦公可試公開網站資料彙整，wiki 可用於匯入公開來源。
- **風險／驗證重點**：AGPL-3.0 授權需依整合方式評估；README 效能宣稱未在本次實測，近期 DOM token mutation 問題也提醒不能預設相容所有網站。
- **來源**：[README](https://github.com/lightpanda-io/browser#readme)、[Releases](https://github.com/lightpanda-io/browser/releases)、[Issues](https://github.com/lightpanda-io/browser/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 4. milind-soni/OpenMausBot — Watch

- **用途**：把多個 AI bots 放入聊天介面並提供可操作的虛擬機，屬於工作代理協作入口。
- **動能與維護**：數值見上表；最近 push：2026-11-01T12:20:36Z；最新 release：v0.1.137（2026-11-01T06:20:03Z）；open issues/PR：619。活動抽樣最新更新：2026-11-01T16:11:38Z。
- **對 Adam 的關聯**：與 Adam AI 辦公自動化及多助理展示直接相關；可先用測試資料做分工任務，wiki 只接公開或合成文件。
- **風險／驗證重點**：虛擬機、模型金鑰與外部動作帶來權限面；近期繁簡中文補全與 provider 支援是提案活動，仍須實際驗證可用性。
- **來源**：[README](https://github.com/milind-soni/OpenMausBot#readme)、[Releases](https://github.com/milind-soni/OpenMausBot/releases)、[Issues](https://github.com/milind-soni/OpenMausBot/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 5. Donchitos/Claude-Code-Game-Studios — Skill candidate

- **用途**：以多角色 agent、workflow skills 與 hooks 模擬遊戲工作室的分工及協調。
- **動能與維護**：數值見上表；最近 push：2026-10-19T02:43:42Z；最新 release：v1.2.0（2026-10-19T02:44:23Z）；open issues/PR：73。活動抽樣最新更新：2026-11-01T09:44:20Z。
- **對 Adam 的關聯**：Adam 可拆成角色責任、階段交付與協作課程；可借鏡到辦公內容團隊及 wiki 編修分工，不必沿用整套遊戲設定。
- **風險／驗證重點**：README 與簡介的 skills 數量不一致，應鎖定版本；多角色可能增加成本及衝突，近期 stage 寫入失敗修補值得追蹤。
- **來源**：[README](https://github.com/Donchitos/Claude-Code-Game-Studios#readme)、[Releases](https://github.com/Donchitos/Claude-Code-Game-Studios/releases)、[Issues](https://github.com/Donchitos/Claude-Code-Game-Studios/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 6. CopilotKit/OpenBot — Demo content

- **用途**：為 AI coworkers 提供獨立電腦、瀏覽器、檔案與工具，強調動作前決策及事後記錄。
- **動能與維護**：數值見上表；最近 push：2026-10-31T23:52:00Z；最新 release：v0.2.0（2026-10-12T15:19:49Z）；open issues/PR：85。活動抽樣最新更新：2026-11-01T11:01:05Z。
- **對 Adam 的關聯**：適合 Adam 製作「可追查的辦公 agent」示範；可研究 wiki 來源蒐集與人工覆核節點。
- **風險／驗證重點**：目前仍有 OAuth callback、SSH key 保管及群組分享相關議題；可追查不等於權限已安全，展示先用隔離環境。
- **來源**：[README](https://github.com/CopilotKit/OpenBot#readme)、[Releases](https://github.com/CopilotKit/OpenBot/releases)、[Issues](https://github.com/CopilotKit/OpenBot/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 7. beenuar/AiSOC — Reference only

- **用途**：將警示整合、LLM agent 分析與可重播決策帳本結合，並提供 MCP server。
- **動能與維護**：數值見上表；最近 push：2026-11-01T15:59:05Z；最新 release：v21.0.0（2026-11-01T05:05:15Z）；open issues/PR：16。活動抽樣最新更新：2026-11-01T15:59:07Z。
- **對 Adam 的關聯**：Adam 可取決策稽核與證據鏈設計作教材；know metabiz wiki 可借鏡可追溯引用，與日常辦公的直接適配度較低。
- **風險／驗證重點**：資安情境專業門檻高，README 的無金鑰與自架宣稱不等於偵測成效；連接組織身分與告警資料前需專門驗證。
- **來源**：[README](https://github.com/beenuar/AiSOC#readme)、[Releases](https://github.com/beenuar/AiSOC/releases)、[Issues](https://github.com/beenuar/AiSOC/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 8. patchy631/ai-engineering-hub — Reference only

- **用途**：集中 LLM、RAG 與真實 agent 應用的教學範例。
- **動能與維護**：數值見上表；最近 push：2026-11-01T04:39:16Z；最新 release：未提供／未取得（無可驗證發布時間）；open issues/PR：133。活動抽樣最新更新：2026-11-01T04:53:05Z。
- **對 Adam 的關聯**：可補 Adam 課程選題與實作素材；辦公與 know metabiz wiki 可挑 RAG／MCP 範例重做帶引用的文件問答。
- **風險／驗證重點**：近期 Issue／PR 指向 Pixeltable MCP 範例的 eval/exec 安全修補及依賴版本更新；教材需鎖版本與驗證，不能直接視為 production 配方。
- **來源**：[README](https://github.com/patchy631/ai-engineering-hub#readme)、[Releases](https://github.com/patchy631/ai-engineering-hub/releases)、[Issues](https://github.com/patchy631/ai-engineering-hub/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 9. mattpocock/skills — Skill candidate

- **用途**：工程師日常使用的 agent skills 集合，適合從任務設計與交付流程拆解。
- **動能與維護**：數值見上表；最近 push：2026-11-01T11:42:33Z；最新 release：v1.3.2（2026-10-29T10:27:41Z）；open issues/PR：199。活動抽樣最新更新：2026-11-01T13:37:49Z。
- **對 Adam 的關聯**：直接相關 Adam Skills 課程；可選規格拆解、審查與 chief-of-staff 類流程試作辦公技能，wiki 維護可借鏡審查責任。
- **風險／驗證重點**：總星數很高仍需逐項檢視；近期 grill 跳過規格／tickets 的回報顯示指令遵循可能受模型影響，本次不安裝或執行任何外部 skill。
- **來源**：[README](https://github.com/mattpocock/skills#readme)、[Releases](https://github.com/mattpocock/skills/releases)、[Issues](https://github.com/mattpocock/skills/issues)；本地數據見 repos.json 與 activity-evidence.json。

### 10. SamurAIGPT/llm-wiki-agent — Skill candidate

- **用途**：讓 coding agent 讀取來源並維護持久互連 wiki，與逐次檢索式 RAG 的維護方式不同。
- **動能與維護**：數值見上表；最近 push：2026-10-26T08:57:58Z；最新 release：未提供／未取得（無可驗證發布時間）；open issues/PR：13。活動抽樣最新更新：2026-10-20T12:40:51Z。
- **對 Adam 的關聯**：本日對 know metabiz wiki 最直接的候選；Adam 可做「原始來源→知識頁→引用／矛盾檢查」課程，辦公可用非敏感制度文件做小規模驗證。
- **風險／驗證重點**：來源內容不能當作 agent 指令；需保留來源、增量差異及回復能力。近期避免覆寫既有 Markdown 的提案尚不可視為已解決。
- **來源**：[README](https://github.com/SamurAIGPT/llm-wiki-agent#readme)、[Releases](https://github.com/SamurAIGPT/llm-wiki-agent/releases)、[Issues](https://github.com/SamurAIGPT/llm-wiki-agent/issues)；本地數據見 repos.json 與 activity-evidence.json。

## 明日觀察清單（2026-11-02）

1. **T3 Code**：stars today 是否延續高於快照相對成長的訊號；追蹤權限載入與首次啟動 provider PR 的實際合併及 release。
2. **Claude-Mem／OpenMausBot**：比較連續快照成長與 release 頻率；以非敏感範例設計記憶清除、跨 session 與繁中工作流驗證題。
3. **Lightpanda**：追蹤 DOM 相容性問題修正；下次再規劃固定網站集的資源／結果一致性比較，先不引用 README 效能倍數。
4. **Game Studios／mattpocock skills**：追蹤 stage 寫入與流程跳步回報，選一個最小 skill 做 Adam 課程候選，不整包安裝。
5. **LLM Wiki Agent**：優先查明防覆寫提案狀態；為 know metabiz wiki 設計兩份矛盾來源的增量編修與引用評分，勿用低星數排除。
6. **OpenBot／AiSOC／AI Engineering Hub**：分別觀察權限／金鑰保管、決策可重播，以及 MCP 範例安全修補是否進入可重現版本。

## 可重現性與附件

- `collection-status.json`／`collector-limit-10.log`：收集開始時間、指定查詢執行與 rate-limit 狀態；必要時另有 limit-5 log。
- `trending-observation.json`／`trending-scope-evidence.json`／`scope-review.json`：原始卡片、補充 metadata、主題篩選與漏項校正。
- `editorial-evidence.json`／`activity-evidence.json`：候選 repo 的 metadata／README 及最近 Issue／PR 抽樣；取樣時間可能早於完整 collector 結束，分析表格以最終 repos.json 為準。
- `repos.json`、`snapshots/repos-2026-11-01.json`、`report.md`：本次完整結構化資料、快照及收集報告。
