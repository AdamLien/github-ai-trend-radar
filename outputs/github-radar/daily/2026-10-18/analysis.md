# GitHub AI 趨勢雷達｜2026-10-18

目標日期為 Asia/Taipei 昨日；本次於 2026-10-19 補跑。資料代表補跑時的即時觀測，不是 10/18 台灣零時至午夜的完整封存統計。

## 今日判斷

優先做 AI 辦公流程與跨工具記憶的可驗證示範；知識管理研究保留 llm_wiki；多 agent 編排先檢查協調與專案隔離。以下為行動優先序，非總星數排行榜。

## 方法與資料品質

- 依指定十個 query，以 `--limit 10 --include-trending-daily --include-readme` 成功執行；未觀察到 API 限流，未觸發 limit=5。搜尋按總星數取樣有偏差，以 Trending、相對成長、近期 push、README、release 及 issue／PR 抽樣補充判讀。
- stars today 來自 [GitHub Trending daily](https://github.com/trending?since=daily)，是 GitHub 頁面統計視窗；快照增量比較 2026-10-17 的本地快照，兩者不可互換或相加。相對成長＝增量÷前次星數；無基準時不得推定零成長。
- 語意確認 VoiceStudio 與 ComfyUI 為 AI 專案，補上關鍵字篩選漏掉的 Trending 訊號；未確認為範圍內的影片修復工具不納入推薦。以 canonical full_name 合併重複項後共 358 個專案。
- README 僅讀取摘要，功能敘述不代表實測。每個入選專案另取最近更新的 5 筆 issue／PR；GitHub issues endpoint 包含 PR，open_issues 也不應解讀為純 bug 數。所有日期／時間原始欄位為 UTC。
- 4 個歷史專案回傳 404，沿用舊資料並標註 `metadata_status=stale_404`，未納入下列推薦；其零差值不能解讀為當日沒有成長。詳見 run-status.json。
- 原始依據：repos.json、snapshots/repos-2026-10-18.json、trending-evidence.json、issue-activity.json、collector-limit-10.log。

## 值得追蹤的 10 個專案

| 專案 | Stars today | 快照增量 | 相對成長 | 總星數 | 分類 |
|---|---:|---:|---:|---:|---|
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | 2,213 | +2,367 | 4.76% | 52,045 | Demo content |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | 513 | +520 | 5.32% | 10,303 | Deep research |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 1,187 | +1,064 | 2.57% | 42,424 | Skill candidate |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 2,098 | +1,956 | 2.69% | 74,598 | Demo content |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 582 | +546 | 1.01% | 54,425 | Demo content |
| [cursor/plugins](https://github.com/cursor/plugins) | 351 | +397 | 3.25% | 12,608 | Skill candidate |
| [stablyai/orca](https://github.com/stablyai/orca) | 1,146 | +1,164 | 1.22% | 96,229 | Watch |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 1,417 | +1,357 | 0.63% | 216,179 | Watch |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未上榜 | +25 | 0.12% | 20,747 | Deep research |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 502 | +462 | 0.61% | 76,368 | Reference only |

### 1. MadsLorentzen/ai-job-search — Demo content

- 用途：以 Claude Code 串起職缺評估、履歷調整、求職信及面試準備。
- 動能判斷：短期增長強，且流程容易拆成可教、可驗證的辦公任務。
- 維護訊號：最近 push `2026-10-18T06:16:56Z`；updated `2026-10-18T16:11:18Z`；未結 issue／PR 合計 27；latest release：[v1.7.2](https://github.com/MadsLorentzen/ai-job-search/releases/tag/v1.7.2)（2026-09-29T18:32:55Z）。
- 近期議題：抽樣 5 筆均為 PR，包含非 ASCII、資料型別及評分錯誤處理；顯示修補活動，未證明已合併。 [issue／PR 來源](https://api.github.com/repos/MadsLorentzen/ai-job-search/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的 AI 辦公室課程與履歷內容示範；可借用「來源→評分→文件產出」流程設計 metabiz 提案助手。
- 風險與限制：履歷個資、職缺來源條款與生成內容正確性需逐項檢查；不能把產出當成事實。
- 證據：[README](https://github.com/MadsLorentzen/ai-job-search/blob/HEAD/README.md)、[儲存庫](https://github.com/MadsLorentzen/ai-job-search)；摘要及計數保存於 repos.json。

### 2. akitaonrails/ai-memory — Deep research

- 用途：為 coding CLI 提供長期記憶，協助不同 agent 工具接續工作。
- 動能判斷：相對成長高於多數大型專案，且近日有正式 release，值得優先研究。
- 維護訊號：最近 push `2026-10-17T19:53:00Z`；updated `2026-10-18T16:11:35Z`；未結 issue／PR 合計 35；latest release：[v3.1.1](https://github.com/akitaonrails/ai-memory/releases/tag/v3.1.1)（2026-10-17T18:09:02Z）。
- 近期議題：5 筆為 PR，涉及過期頁面的健康統計、跨專案度數與寫入權限；不能推定修正已發布。 [issue／PR 來源](https://api.github.com/repos/akitaonrails/ai-memory/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的 Claude Code／Codex 交接教學；可研究 know metabiz wiki 的記憶索引、來源與過期機制。
- 風險與限制：跨專案記憶可能誤帶客戶資訊；需驗證隔離、TTL、刪除及還原行為，尚未實測。
- 證據：[README](https://github.com/akitaonrails/ai-memory/blob/HEAD/README.md)、[儲存庫](https://github.com/akitaonrails/ai-memory)；摘要及計數保存於 repos.json。

### 3. anthropics/claude-plugins-official — Skill candidate

- 用途：提供 Anthropic 維護的 Claude Code plugin 目錄，包含內部與外部 plugins。
- 動能判斷：Trending 熱度與近期 push 同時成立，可挑單一工作流研究封裝方式。
- 維護訊號：最近 push `2026-10-18T16:06:52Z`；updated `2026-10-18T16:10:16Z`；未結 issue／PR 合計 1,189；latest release：API 未取得 latest release；不代表從未發布。
- 近期議題：抽樣含 1 筆數學驗證 PR 與 4 筆重複安裝宣傳 issue，活動品質參差。 [issue／PR 來源](https://api.github.com/repos/anthropics/claude-plugins-official/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的 skills／plugins 課程素材；可參考將 metabiz wiki 查詢與辦公流程封裝成有範圍限制的 skill。
- 風險與限制：官方目錄含第三方元件；README 提醒需自行信任各 plugin。抽樣重複安裝宣傳 issue，數量不可直接當成採用成長。
- 證據：[README](https://github.com/anthropics/claude-plugins-official/blob/HEAD/README.md)、[儲存庫](https://github.com/anthropics/claude-plugins-official)；摘要及計數保存於 repos.json。

### 4. debpalash/VoiceStudio — Demo content

- 用途：本地語音複製、配音、轉錄與有聲內容製作工具。
- 動能判斷：Trending 與快照增量均高；直接對應內容生產需求。
- 維護訊號：最近 push `2026-10-18T13:51:44Z`；updated `2026-10-18T16:14:31Z`；未結 issue／PR 合計 226；latest release：[v0.5.6](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)（2026-09-23T08:53:32Z）。
- 近期議題：抽樣出現 Windows Python 環境缺失、後端啟動逾時及配音時間欄位 PR；先做最小可重現 demo。 [issue／PR 來源](https://api.github.com/repos/debpalash/VoiceStudio/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的課程配音、短影音及字幕工作流內容；可示範 AI 辦公室會議轉錄後整理進 know metabiz wiki。
- 風險與限制：AGPL-3.0 與模型個別條款需在商用整合前確認；另有 Python 環境、後端啟動及 GPU 部署風險，聲音素材須有授權。
- 證據：[README](https://github.com/debpalash/VoiceStudio/blob/HEAD/README.md)、[儲存庫](https://github.com/debpalash/VoiceStudio)；摘要及計數保存於 repos.json。

### 5. HKUDS/CLI-Anything — Demo content

- 用途：把軟體能力轉為 agent 可操作的 CLI 介面。
- 動能判斷：仍有 Trending 動能，但最後 push 與 release 較早，不能以當日熱度推定維護交付速度。
- 維護訊號：最近 push `2026-09-22T02:01:29Z`；updated `2026-10-18T16:09:57Z`；未結 issue／PR 合計 192；latest release：[v0.4.0](https://github.com/HKUDS/CLI-Anything/releases/tag/v0.4.0)（2026-06-25T15:17:49Z）。
- 近期議題：抽樣 QGIS 3.34 錯誤與 FreeCAD／3MF 修補 PR；近期討論活躍不等於主線已修復。 [issue／PR 來源](https://api.github.com/repos/HKUDS/CLI-Anything/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 教授「既有軟體→CLI→agent」的 AI 辦公室自動化；可將文件處理結果寫成 metabiz wiki SOP。
- 風險與限制：不同軟體及版本的命令相容性差異大，需驗證輸出與錯誤處理。
- 證據：[README](https://github.com/HKUDS/CLI-Anything/blob/HEAD/README.md)、[儲存庫](https://github.com/HKUDS/CLI-Anything)；摘要及計數保存於 repos.json。

### 6. cursor/plugins — Skill candidate

- 用途：Cursor plugin 規格與官方 plugins；README 列出教學與持續學習等範例。
- 動能判斷：中型專案有可見相對成長，適合作為 Claude Code plugins 的對照教材。
- 維護訊號：最近 push `2026-10-18T07:31:08Z`；updated `2026-10-18T16:12:45Z`；未結 issue／PR 合計 277；latest release：API 未取得 latest release；不代表從未發布。
- 近期議題：抽樣含新增 plugin、版本調整及 formal verification skill 的 PR；closed 不等同已合併或已發布。 [issue／PR 來源](https://api.github.com/repos/cursor/plugins/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的跨工具 skills 封裝課程；可比較知識交接、教學回顧與 metabiz wiki 的資料格式。
- 風險與限制：API 未提供可識別的整庫 SPDX 授權，且無 latest release；逐項查授權與相容版本後才重用。
- 證據：[README](https://github.com/cursor/plugins/blob/HEAD/README.md)、[儲存庫](https://github.com/cursor/plugins)；摘要及計數保存於 repos.json。

### 7. stablyai/orca — Watch

- 用途：多 coding agent 工作台，支援桌面、行動及遠端 runtime。
- 動能判斷：Trending 超過千星且近期有 release；先關注協調可靠性，再決定深入導入。
- 維護訊號：最近 push `2026-10-18T16:14:07Z`；updated `2026-10-18T16:17:37Z`；未結 issue／PR 合計 8,456；latest release：[v1.4.229](https://github.com/stablyai/orca/releases/tag/v1.4.229)（2026-10-17T06:54:05Z）。
- 近期議題：抽樣含 runtime 重構、worktree hooks PR 與 inbox 範圍錯誤 issue，後者仍 open。 [issue／PR 來源](https://api.github.com/repos/stablyai/orca/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的多 agent 協作課程；可模擬研究、寫稿、驗證分工，評估 metabiz wiki 維護任務的交接。
- 風險與限制：大量未結 issue／PR 只是負載訊號；抽樣回報協調收件匣空結果與範圍判定問題，需測試任務不遺失及權限隔離。
- 證據：[README](https://github.com/stablyai/orca/blob/HEAD/README.md)、[儲存庫](https://github.com/stablyai/orca)；摘要及計數保存於 repos.json。

### 8. anomalyco/opencode — Watch

- 用途：開源 AI coding agent。
- 動能判斷：絕對增長與 Trending 都強，但相對成長低於 ai-memory；保留作工具比較而非因總星數排第一。
- 維護訊號：最近 push `2026-10-18T15:03:39Z`；updated `2026-10-18T16:13:09Z`；未結 issue／PR 合計 4,674；latest release：[v1.19.3](https://github.com/anomalyco/opencode/releases/tag/v1.19.3)（2026-10-16T12:31:52Z）。
- 近期議題：5 筆皆為 issue，包含 provider baseURL、MCP 結構及 plugin API；至少一筆 MCP 問題已 closed，但未確認修復版本。 [issue／PR 來源](https://api.github.com/repos/anomalyco/opencode/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的 coding agent 比較內容，評估 AI 辦公室腳本與 wiki 維護流程能否跨工具搬移。
- 風險與限制：provider 與 MCP 設定可能靜默忽略，需固定版本驗證；issue 提及的 v2 行為不能等同 API latest release 的 v1 行為。
- 證據：[README](https://github.com/anomalyco/opencode/blob/HEAD/README.md)、[儲存庫](https://github.com/anomalyco/opencode)；摘要及計數保存於 repos.json。

### 9. nashsu/llm_wiki — Deep research

- 用途：以來源文件增量建立、更新並互連持久 wiki 的跨平台應用。
- 動能判斷：未上本次 Trending，增長較小；因與 know metabiz wiki 的需求高度一致，保留研究優先度。
- 維護訊號：最近 push `2026-09-28T01:43:23Z`；updated `2026-10-18T15:15:34Z`；未結 issue／PR 合計 285；latest release：[v0.6.12](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.12)（2026-09-28T02:58:13Z）。
- 近期議題：5 筆為 Pi adapter、read-only WikiToolServer 與 release 準備議題，最後活動在 10/17；屬待辦，不是已交付功能。 [issue／PR 來源](https://api.github.com/repos/nashsu/llm_wiki/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：可供 Adam 講解「檢索問答」與「持續整理知識」的工作流；優先研究 know metabiz wiki 的來源溯源、衝突修訂與匯出。
- 風險與限制：授權欄位為 NOASSERTION，需直接核對 LICENSE；來源幻覺、誤覆寫與存取控制尚待驗證，不能依個人桌面工具推定企業能力。
- 證據：[README](https://github.com/nashsu/llm_wiki/blob/HEAD/README.md)、[儲存庫](https://github.com/nashsu/llm_wiki)；摘要及計數保存於 repos.json。

### 10. ruvnet/ruflo — Reference only

- 用途：整合多 agent 編排、記憶與向量 RAG 的 meta-harness。
- 動能判斷：有熱度及近期 release，但目前的隔離風險使其只適合研究架構與反例。
- 維護訊號：最近 push `2026-10-18T11:13:04Z`；updated `2026-10-18T16:16:37Z`；未結 issue／PR 合計 1,053；latest release：[v3.57.0](https://github.com/ruvnet/ruflo/releases/tag/v3.57.0)（2026-10-17T22:38:55Z）。
- 近期議題：抽樣含 #4254 與對應 open PR #4276，以及 Windows 相容、文件命令修補；PR 存在不代表 release 已涵蓋。 [issue／PR 來源](https://api.github.com/repos/ruvnet/ruflo/issues?state=all&sort=updated&direction=desc&per_page=5)
- Adam／metabiz 關聯：適合 Adam 的 agent orchestration 架構內容；可作 metabiz 多客戶知識分區的設計檢查參考。
- 風險與限制：open issue #4254 回報任務狀態跨專案混入；在證實修復與隔離前不作客戶環境導入候選。
- 證據：[README](https://github.com/ruvnet/ruflo/blob/HEAD/README.md)、[儲存庫](https://github.com/ruvnet/ruflo)；摘要及計數保存於 repos.json。

## 明日觀察清單

1. **ai-job-search、VoiceStudio**：stars today 與相對成長是否延續；選一份匿名文件或已授權音檔做端到端 demo，記錄人工修訂時間。
2. **ai-memory**：追蹤 TTL、跨專案統計與寫入權限 PR 是否合併且進 release，再設計隔離測試。
3. **Claude plugins／Cursor plugins**：挑一個最小 plugin 比較 manifest、依賴、權限與授權；辨識重複宣傳 issue，避免把雜訊當需求。
4. **llm_wiki**：關注 Pi read-only adapter 與 WikiToolServer 進度；先用非敏感文件評估來源回鏈、衝突及匯出，再談 know metabiz wiki 整合。
5. **Orca／Ruflo／OpenCode**：追蹤 inbox 範圍、跨專案狀態與 MCP 設定問題的實際修復版本；未證實前維持 Watch／Reference only。
6. **CLI-Anything／ComfyUI**：觀察熱度是否伴隨主線更新；分別挑固定版本的軟體操作與內容生產任務，評估可重現性。
7. **資料衛生**：重查 4 個 404 專案是否改名或移除；保持歷史紀錄，不把沿用資料列入成長排名。
