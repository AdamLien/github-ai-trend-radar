# GitHub AI 趨勢雷達｜2026-11-02

## 日期與判讀方法

- 歸檔目標為前一個 Asia/Taipei 日曆日 **2026-11-02**；實際執行開始：2026-11-03T00:11:27.913107+08:00。
- [GitHub Trending daily](https://github.com/trending?since=daily) 觀測時間：2026-11-03T00:11:58.737713+08:00。這是執行當下的 rolling daily 榜單，並非可回溯的昨日整日統計。
- 本次保留 381 個主題相關 repo；Trending 15 張卡片保留 14 張，排除 Hyprland compositor。以 README／metadata 補上空簡介與關鍵字漏項；詳見 trending-scope-review.json、scope-review.json。
- API rate-limit：未偵測到錯誤；以 --limit 10 完成，無需降為 5。
- 指定十組搜尋依總星數發現候選，分析另綜合 stars today、相鄰快照差值／相對成長、最近 push、README、release、近期 Issue／PR 與 Adam 工作關聯決定投入順序。
- 快照差值以 2026-11-01 為基準；相對成長＝差值／前次總星數。觀測間隔不是嚴格 24 小時，差值不能稱為日增；首次觀測標為未量測，stars today 缺值不等於零。
- open_issues_count 可能包含 PR；活動只抽樣最近更新的 5 筆，不能推論整體處理速度。release 缺值表示未取得。README 宣稱及下述風險屬文件觀察／編輯判斷，本次未安裝或執行外部專案。

- **舊資料警示**：4 個歷史 repo 更新失敗，保留舊 metadata 並標記 fallback／Reference only，詳見 metadata-fallbacks.json；不屬於本篇 10 個精選，不將其星數視為新觀測。

## 值得投入的 10 個 repo

順序代表編輯投入優先度，並非總星數排名；Wiki 類候選因工作用途保留席位。

| Repo | stars today | 總 stars | 快照差值 | 相對成長 | 建議 |
|---|---:|---:|---:|---:|---|
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 3216 | 40,742 | +3,680 | +9.93% | Deep research |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 2243 | 8,613 | 未量測 | 未量測 | Demo content |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 1799 | 110,411 | +1,636 | +1.50% | Deep research |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 1380 | 33,188 | +1,306 | +4.10% | Skill candidate |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 970 | 309,936 | +920 | +0.30% | Skill candidate |
| [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 136 | 9,901 | +147 | +1.51% | Demo content |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 451 | 110,208 | +435 | +0.40% | Watch |
| [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | 654 | 15,868 | +670 | +4.41% | Watch |
| [JustVugg/colibri](https://github.com/JustVugg/colibri) | 655 | 46,306 | 未量測 | 未量測 | Reference only |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 未入榜／未量測 | 3,673 | +4 | +0.11% | Skill candidate |

### 1. pingdotgg/t3code — Deep research

- **用途**：以手機、網頁與桌面控制本機 coding agents；README 列出 Claude Code、Codex、Cursor 等整合。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T16:18:45Z；release：v0.1.6（2026-10-31T10:52:24Z）；open issues/PR：4212。
- **Adam／辦公／Wiki 關聯**：Adam 可製作「手機接手多 agent 開發」課程與內容；辦公可研究任務交接，know metabiz wiki 可作操作文件來源。
- **風險與驗證重點**：遠端操作與 session 權限需驗證；近期登入錯誤訊息修補仍是提案，不能把大量 PR 當作穩定性證明。
- **來源**：[README](https://github.com/pingdotgg/t3code#readme)、[Releases](https://github.com/pingdotgg/t3code/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T16:12:08Z，目前 open（[Issue／PR](https://github.com/pingdotgg/t3code/pull/29411)）；未合併提案不可當作已發布功能。

### 2. vercel-labs/agent-desktop — Demo content

- **用途**：以作業系統 accessibility tree 讀取並操作桌面 UI，README 主張比像素猜測更可靠。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T09:39:59Z；release：v1.0.2（2026-10-30T21:17:30Z）；open issues/PR：120。
- **Adam／辦公／Wiki 關聯**：適合 Adam 示範桌面 AI 辦公自動化；可將公開文件匯入 know metabiz wiki 的流程做成可重播教材。
- **風險與驗證重點**：首次觀測沒有增長基準；近期 Voice Memos 的目標歧義回報顯示相容性限制，權限政策 PR 尚待驗證。
- **來源**：[README](https://github.com/vercel-labs/agent-desktop#readme)、[Releases](https://github.com/vercel-labs/agent-desktop/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T15:21:40Z，目前 open（[Issue／PR](https://github.com/vercel-labs/agent-desktop/pull/490)）；未合併提案不可當作已發布功能。

### 3. thedotmack/claude-mem — Deep research

- **用途**：記錄並壓縮 agent session，將相關上下文帶到後續工作階段。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T16:11:18Z；release：v15.8.3（2026-11-02T06:26:25Z）；open issues/PR：125。
- **Adam／辦公／Wiki 關聯**：Adam 可做跨 session 記憶課程；辦公研究交接摘要，know metabiz wiki 應保留原始來源與引用供記憶校驗。
- **風險與驗證重點**：記憶可能保存敏感或過時資訊；近期大型 review 復原與 snapshot 效能變更需要實測。
- **來源**：[README](https://github.com/thedotmack/claude-mem#readme)、[Releases](https://github.com/thedotmack/claude-mem/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T16:12:19Z，目前 open（[Issue／PR](https://github.com/thedotmack/claude-mem/pull/5284)）；未合併提案不可當作已發布功能。

### 4. Donchitos/Claude-Code-Game-Studios — Skill candidate

- **用途**：把 Claude Code 組成角色分工、workflow skills 與協調系統的遊戲工作室。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-10-19T02:43:42Z；release：v1.2.0（2026-10-19T02:44:23Z）；open issues/PR：80。
- **Adam／辦公／Wiki 關聯**：Adam 可拆出角色責任與交付檢查課程；可借鏡辦公內容團隊及 know metabiz wiki 的編修分工。
- **風險與驗證重點**：簡介寫 72 skills、README 寫 74，應鎖定版本；熱度上升但最近 push 較早，多角色可能增加成本與協作衝突。
- **來源**：[README](https://github.com/Donchitos/Claude-Code-Game-Studios#readme)、[Releases](https://github.com/Donchitos/Claude-Code-Game-Studios/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T14:21:17Z，目前 open（[Issue／PR](https://github.com/Donchitos/Claude-Code-Game-Studios/pull/160)）；未合併提案不可當作已發布功能。

### 5. mattpocock/skills — Skill candidate

- **用途**：收集工程師使用的 coding agent skills 與可重用工作方法。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-01T11:42:33Z；release：v1.3.2（2026-10-29T10:27:41Z）；open issues/PR：203。
- **Adam／辦公／Wiki 關聯**：Adam 可挑單一規格、審查或 chief-of-staff 流程做課程；後者也與辦公及 know metabiz wiki 的維護責任有關。
- **風險與驗證重點**：近期回報含 YAML 解析及 Wiki Lint 缺少確定性步驟；高總星數不代表每個 skill 都可靠，需逐項驗證。
- **來源**：[README](https://github.com/mattpocock/skills#readme)、[Releases](https://github.com/mattpocock/skills/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T16:01:59Z，目前 open（[Issue／PR](https://github.com/mattpocock/skills/issues/1373)）；未合併提案不可當作已發布功能。

### 6. max-sixty/worktrunk — Demo content

- **用途**：以 CLI 管理 Git worktrees，服務平行 AI agent 工作流。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T10:03:56Z；release：v0.81.0（2026-10-20T21:28:34Z）；open issues/PR：60。
- **Adam／辦公／Wiki 關聯**：Adam 可示範多 agent 隔離工作區與合併；辦公腳本、know metabiz wiki 編修也可用分支留存修改脈絡。
- **風險與驗證重點**：刪除 worktree、hook 執行與推送目標可能影響工作區；近期 remote 解析修補仍需查明合併狀態。
- **來源**：[README](https://github.com/max-sixty/worktrunk#readme)、[Releases](https://github.com/max-sixty/worktrunk/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T16:05:55Z，目前 open（[Issue／PR](https://github.com/max-sixty/worktrunk/pull/4666)）；未合併提案不可當作已發布功能。

### 7. paperclipai/paperclip — Watch

- **用途**：提供管理工作中多個 agents 的開源應用。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T16:19:27Z；release：v2026.1023.0（2026-10-24T00:03:59Z）；open issues/PR：6637。
- **Adam／辦公／Wiki 關聯**：Adam 可研究 AI 辦公團隊的任務分派與責任追蹤，並以 know metabiz wiki 作有來源的任務知識層。
- **風險與驗證重點**：近期無目標執行與任務結案修補提示狀態一致性風險；大量 open issues/PR 不能直接解讀為解題效率。
- **來源**：[README](https://github.com/paperclipai/paperclip#readme)、[Releases](https://github.com/paperclipai/paperclip/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T16:09:41Z，目前 open（[Issue／PR](https://github.com/paperclipai/paperclip/pull/18616)）；未合併提案不可當作已發布功能。

### 8. FlashML-org/FreeToken — Watch

- **用途**：把大型模型 serving 帶到桌面；性能與硬體可行性屬專案宣稱。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T00:36:31Z；release：v0.2.1（2026-10-26T03:24:21Z）；open issues/PR：473。
- **Adam／辦公／Wiki 關聯**：Adam 可規劃本機 LLM 成本與部署課程；辦公、know metabiz wiki 可研究本機推論，但需先量測硬體及文件品質。
- **風險與驗證重點**：近期 Windows supervisor 路徑錯誤尚有回報；不能將桌面運行宣稱視為所有硬體都能達成的速度或成本。
- **來源**：[README](https://github.com/FlashML-org/FreeToken#readme)、[Releases](https://github.com/FlashML-org/FreeToken/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T14:02:56Z，目前 open（[Issue／PR](https://github.com/FlashML-org/FreeToken/issues/542)）；未合併提案不可當作已發布功能。

### 9. JustVugg/colibri — Reference only

- **用途**：以 C 與磁碟串流 experts 執行大型 MoE 模型的推論引擎。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T16:11:31Z；release：v2.1.0（2026-10-31T12:50:50Z）；open issues/PR：147。
- **Adam／辦公／Wiki 關聯**：可作 Adam 本機模型架構內容的參考；辦公與 know metabiz wiki 的關聯在推論底層，優先度低於可直接試用的應用。
- **風險與驗證重點**：首次觀測無可比增量；近期有舊 CPU 效能回報，模型格式、磁碟與記憶體瓶頸需獨立測試。
- **來源**：[README](https://github.com/JustVugg/colibri#readme)、[Releases](https://github.com/JustVugg/colibri/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-11-02T16:11:32Z，目前 closed（[Issue／PR](https://github.com/JustVugg/colibri/pull/2545)）；未合併提案不可當作已發布功能。

### 10. SamurAIGPT/llm-wiki-agent — Skill candidate

- **用途**：將來源文件增量整理為持久互連 wiki，README 定位為 coding agent skill。
- **動能與維護**：星數與相對成長見上表；最近 push：2026-11-02T11:11:47Z；release：未提供／未取得；open issues/PR：13。
- **Adam／辦公／Wiki 關聯**：與 know metabiz wiki 最直接相關；Adam 可做「來源→知識頁→引用與矛盾檢查」課程，辦公先用合成制度文件驗證。
- **風險與驗證重點**：需防止覆寫與來源提示注入，保留引用及回復能力；最新活動抽樣較舊，recent push 不足以證明維護問題已處理。
- **來源**：[README](https://github.com/SamurAIGPT/llm-wiki-agent#readme)、[Releases](https://github.com/SamurAIGPT/llm-wiki-agent/releases)；數據見 repos.json 與 editorial-evidence.json。
- **活動抽樣**：最近更新 2026-10-20T12:40:51Z，目前 open（[Issue／PR](https://github.com/SamurAIGPT/llm-wiki-agent/pull/86)）；未合併提案不可當作已發布功能。

## 明日觀察清單（2026-11-03）

1. **T3 Code／Agent Desktop**：確認當日熱度是否延續；為首次觀測建立第二個快照，追蹤桌面目標歧義、登入與權限政策提案的合併及發布。
2. **Claude-Mem**：追蹤 v15.8.3 後的 review 復原與效能變更；規劃記憶查核、刪除與來源引用的示範題。
3. **Game Studios／mattpocock skills**：檢查 skills 數量與版本差異、YAML 解析及 Wiki Lint；選單一最小流程做課程候選。
4. **Worktrunk／Paperclip**：追蹤 push remote 解析與任務結案狀態問題；以平行任務隔離、可回復性與人工交接評估辦公價值。
5. **FreeToken／Colibri**：確認硬體需求、Windows 可用性與實際吞吐；未實測前不引用速度或省成本結論。
6. **LLM Wiki Agent**：關注連結健康檢查與資料保全；設計 know metabiz wiki 的矛盾來源、引用追溯、增量編修與回復驗證。

## 可重現性

- collection-status.json 與 collector-limit-10.log（必要時另有 limit-5）：查詢、執行時間與 API rate-limit 狀態。
- trending-observation.json、trending-scope-review.json、scope-review.json：卡片資料、主題保留與排除、漏項補正。
- editorial-evidence.json、readme-evidence.json：README、release、metadata 與近期 Issue／PR 抽樣；取樣時間可能與完整 collector 不同，表格以最終 repos.json 為準。
- repos.json、report.md、snapshots/repos-2026-11-02.json：結構化資料、報告及快照。
