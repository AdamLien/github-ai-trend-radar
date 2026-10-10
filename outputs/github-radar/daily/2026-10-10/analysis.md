# GitHub AI 趨勢雷達｜2026-10-10

目標日期為 Asia/Taipei 的前一個日曆日；實際收集時間（UTC）：2026-10-10T16:19:38.778942+00:00。本報使用執行當下的 GitHub API 與 Trending，並非回溯還原 2026-10-10 收盤資料。

## 判讀方式與資料品質

- 依「今日星數＋快照增量／相對成長＋近期提交／release＋README 可落地性＋Issue／PR 活動」綜合挑選，排序是編輯優先度，不按總星數。高熱度的 rea 仍列 Watch；辦公與 wiki 相關項目即使增量較小也入選。
- 快照差值對照 2026-10-09；相對成長＝差值 ÷ 前次星數。Trending stars today 是 GitHub 滾動榜單訊號，與兩次快照差值的時間窗不同，不能相加。缺少 Trending 數值表示未取得，並非零。
- 查詢按 GitHub stars 排序且每組上限 10，會偏向成熟專案；以 Trending 與歷史追蹤補充，仍不是全 GitHub 的完整排名。
- 十組指定查詢使用 --limit 10、--include-trending-daily、--include-readme、--snapshot-date 2026-10-10；未觀察到 API rate-limit 錯誤，未啟用 --limit 5 重試。
- Trending 原始卡片與觀測時間保存在 [trending-observation.json](trending-observation.json)。人工保留 11 個 AI／agent／skills／模型框架項目，排除 AnyPS5、Flutter；補正關鍵字篩選漏項與每日星數。最終按 GitHub canonical full_name 去除重複。
- 四個歷史 repo 回傳 404 並保留舊資料：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。本次不推薦；舊資料不代表今天仍可取得。
- Issue／PR 抽樣每個候選最近更新的 5 筆，state=all，包含 PR，不能推算完整 issue 解決率；open_issues API 計數也包含 PR。證據見 [issue-activity.json](issue-activity.json)。未安裝或執行候選專案；用途與風險是依公開資訊的分析判斷。

## 十個值得關注的 repo

| Repo | 今日星數 | 快照增量 | 相對成長 | 總星數 | 建議 |
|---|---:|---:|---:|---:|---|
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 1,189 | +1,069 | 2.25% | 48,633 | Skill candidate |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 515 | +510 | 0.87% | 59,169 | Demo content |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 626 | +575 | 2.05% | 28,652 | Deep research |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 1,737 | +1,709 | 0.61% | 283,968 | Skill candidate |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 178 | +226 | 0.87% | 26,132 | Deep research |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未取得 | +75 | 0.37% | 20,427 | Watch |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 未取得 | +70 | 0.15% | 46,284 | Deep research |
| [storytold/artcraft](https://github.com/storytold/artcraft) | 3,217 | +3,011 | 28.78% | 13,473 | Demo content |
| [morluto/rea](https://github.com/morluto/rea) | 25,784 | +26,396 | 67.77% | 65,347 | Watch |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 279 | +318 | 0.15% | 217,996 | Reference only |

### 1. cathrynlavery/diagram-design — Skill candidate

- **用途與 README 訊號：**將架構、流程與概念產出為單一 HTML＋SVG 圖解；README 明確提供自然語言範例與跨 coding agent 使用方式。
- **維護動能：**最近提交 2026-10-10T04:32:06Z；最新 release API 未取得最新 release。目前 open_issues（含 PR）82；最近 5 筆更新中 0 筆 Issue、5 筆 PR，最新更新 2026-10-10T14:14:06Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**適合 Adam 課程架構圖、短影音概念圖、AI 辦公流程圖，以及 know metabiz wiki 的系統關係圖。先用一份既有文件比較人工修改成本。
- **風險與下一步：**近期 PR 仍在修正匯入標籤解析；44 種圖表是專案宣稱，繁中排版、編輯與輸出穩定性尚未實測。 參考 [Issue／PR #284](https://github.com/cathrynlavery/diagram-design/pull/284)。

### 2. hugohe3/ppt-master — Demo content

- **用途與 README 訊號：**把文件／主題轉成原生 PowerPoint，專案宣稱支援圖表、動畫、旁白與既有簡報範本；近期 release 是較強的交付訊號。
- **維護動能：**最近提交 2026-10-08T07:45:46Z；最新 release v6.7.0（2026-10-08T02:01:38Z）。目前 open_issues（含 PR）6；最近 5 筆更新中 4 筆 Issue、1 筆 PR，最新更新 2026-10-10T05:56:50Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**可做 Adam「wiki 文件變課程簡報」示範，連接內容製作與 AI 辦公自動化；know metabiz wiki 可作來源資料。
- **風險與下一步：**Windows 的 attribution_guard.py 有無診斷訊息即退出的回報；還需驗證中文字體、版面、可編輯性與媒體依賴。 參考 [Issue／PR #311](https://github.com/hugohe3/ppt-master/issues/311)。

### 3. anthropics/knowledge-work-plugins — Deep research

- **用途與 README 訊號：**以職能插件封裝 skills、connectors、slash commands 與 subagents；README 指向 Cowork 並說明 Claude Code 相容。
- **維護動能：**最近提交 2026-10-10T07:38:13Z；最新 release API 未取得最新 release。目前 open_issues（含 PR）140；最近 5 筆更新中 1 筆 Issue、4 筆 PR，最新更新 2026-10-10T07:38:15Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**最貼近 Adam AI 辦公課程；可把 CRM、研究與文件整理流程映射到 metabiz 場景，並將範例與輸入／輸出規格記錄到 know metabiz wiki。
- **風險與下一步：**近期抽樣主要是 connector 自動更新 PR，不能把更新數量等同成熟度；實際可用性仍取決於連接器權限、資料來源與環境。 參考 [Issue／PR #1301](https://github.com/anthropics/knowledge-work-plugins/pull/1301)。

### 4. mattpocock/skills — Skill candidate

- **用途與 README 訊號：**彙整日常工程 skills 與工作方法；README 是實務導向技能集合，而非單一模型或平台。
- **維護動能：**最近提交 2026-10-09T10:57:08Z；最新 release v1.3.1（2026-10-04T12:48:18Z）。目前 open_issues（含 PR）164；最近 5 筆更新中 4 筆 Issue、1 筆 PR，最新更新 2026-10-10T16:10:34Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**適合 Adam 的 coding agent 課程與技能設計內容；AI 辦公可借用需求釐清流程，know metabiz wiki 可保存團隊流程與驗收規則。
- **風險與下一步：**Issue 回報 grilling 把問題寫成陳述句；高星數不保證互動效果，應挑單一 skill 驗證並避免與既有規則重複。 參考 [Issue／PR #1249](https://github.com/mattpocock/skills/issues/1249)。

### 5. mksglu/context-mode — Deep research

- **用途與 README 訊號：**以 MCP＋hooks 隔離工具輸出、保留 session 記憶並管理 context；README 與描述把焦點放在 context 使用效率。
- **維護動能：**最近提交 2026-10-10T12:06:33Z；最新 release v1.0.169（2026-06-29T18:18:53Z）。目前 open_issues（含 PR）339；最近 5 筆更新中 2 筆 Issue、3 筆 PR，最新更新 2026-10-10T12:59:39Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**可做 Adam「長任務 context 成本」研究內容；對 AI 辦公多步驟任務與 know metabiz wiki 大量來源檢索有間接價值。
- **風險與下一步：**描述中的 98% 減量屬作者宣稱；Issue 指出每分鐘重新開啟 session DB 帶來磁碟寫入，且授權 API 回傳 NOASSERTION，需閱讀實際授權。 參考 [Issue／PR #1248](https://github.com/mksglu/context-mode/issues/1248)。

### 6. nashsu/llm_wiki — Watch

- **用途與 README 訊號：**跨平台桌面知識庫，從來源增量建立互連 wiki；README 強調自動建立並保持更新的知識庫。
- **維護動能：**最近提交 2026-09-28T01:43:23Z；最新 release v0.6.12（2026-09-28T02:58:13Z）。目前 open_issues（含 PR）274；最近 5 筆更新中 2 筆 Issue、3 筆 PR，最新更新 2026-10-10T09:39:52Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**與 know metabiz wiki 最直接相關，可研究來源追溯、增量更新與矛盾處理；適合 Adam 的 RAG 與持久 wiki 比較課程及辦公文件整理示範。
- **風險與下一步：**Windows 0.6.12 回報背景全量掃描／hash 放大造成 CPU 負載；近期效能 PR 尚不能證明問題解決，另需查明 NOASSERTION 授權與多人協作能力。 參考 [Issue／PR #812](https://github.com/nashsu/llm_wiki/issues/812)。

### 7. DeusData/codebase-memory-mcp — Deep research

- **用途與 README 訊號：**以 MCP 把程式庫轉成持久知識圖譜，供 coding agent 查詢結構與呼叫關係；README 展示版本、測試與語言覆蓋資訊。
- **維護動能：**最近提交 2026-10-10T11:31:48Z；最新 release v0.11.0（2026-09-15T23:40:39Z）。目前 open_issues（含 PR）625；最近 5 筆更新中 1 筆 Issue、4 筆 PR，最新更新 2026-10-10T16:11:15Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**適合 Adam 的 MCP 與 coding agent 課程；可串接 metabiz 技術 wiki 的程式碼證據，辦公用途以技術文件與開發交接為主。
- **風險與下一步：**查詢速度與 token 節省仍屬作者宣稱；JSX／Swift 等解析修正持續進行，圖譜覆蓋不全時需回讀來源，不能把沒有查到當成不存在。 參考 [Issue／PR #2579](https://github.com/DeusData/codebase-memory-mcp/pull/2579)。

### 8. storytold/artcraft — Demo content

- **用途與 README 訊號：**面向藝術家、設計師與影片創作者的 AI 創作工作台；README 提供影片示範，topics 涵蓋 AI 影片與圖像生成。
- **維護動能：**最近提交 2026-10-10T08:18:00Z；最新 release artcraft-v0.41.0（2026-09-26T11:14:22Z）。目前 open_issues（含 PR）121；最近 5 筆更新中 4 筆 Issue、1 筆 PR，最新更新 2026-10-10T16:01:09Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**適合 Adam 的 AI 內容製作示範與課程素材；辦公端可探索行銷素材流程，know metabiz wiki 保存素材來源與操作記錄。
- **風險與下一步：**Linux 支援仍有討論，另有繪圖板壓感與 launcher 問題；目前主要適合小型示範，外部模型服務成本與素材可追溯性需另驗證。 參考 [Issue／PR #2002](https://github.com/storytold/artcraft/issues/2002)。

### 9. morluto/rea — Watch

- **用途與 README 訊號：**以 agents／MCP 研究應用程式行為與原生二進位；README 描述跨二進位、應用與執行期行為的工具入口。
- **維護動能：**最近提交 2026-10-10T16:10:30Z；最新 release rea-agents-6.3.0（2026-10-09T23:56:42Z）。目前 open_issues（含 PR）136；最近 5 筆更新中 2 筆 Issue、3 筆 PR，最新更新 2026-10-10T16:12:14Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**可做 Adam 的 agent 工具編排與開發者自動化進階內容；AI 辦公關聯較低，know metabiz wiki 可保存自有系統的調查方法與證據。
- **風險與下一步：**今日增長異常強，但不等於能力已驗證；近期仍修正 binary plist 與 browser frame 行為。僅在授權樣本上評估，暫不作入門課程主線。 參考 [Issue／PR #1594](https://github.com/morluto/rea/issues/1594)。

### 10. multica-ai/andrej-karpathy-skills — Reference only

- **用途與 README 訊號：**用單一 CLAUDE.md 整理 coding agent 的假設、範圍控制與驗證原則；README 說明靈感來源，屬社群整理。
- **維護動能：**最近提交 2026-04-20T10:05:04Z；最新 release API 未取得最新 release。目前 open_issues（含 PR）132；最近 5 筆更新中 0 筆 Issue、5 筆 PR，最新更新 2026-10-09T18:19:30Z。時間皆為 UTC。
- **與 Adam／metabiz 的關聯：**可作 Adam 課程的工程行為對照；辦公自動化也可借用明確驗收原則，know metabiz wiki 可整理實際團隊經驗。
- **風險與下一步：**最近 pushed_at 停在四月，當前抽樣多是文件 PR；API 未識別授權且未取得 release。與既有規範可能重複，先引用方法，不直接匯入整套指令。 參考 [Issue／PR #208](https://github.com/multica-ai/andrej-karpathy-skills/pull/208)。

## 明日觀察清單

- **diagram-design／ppt-master：**以同一份繁中 wiki 文件各做一個圖解與五頁可編輯簡報，量測修改時間、版面與來源追溯；追蹤 diagram 匯入修正及 Windows 問題。
- **knowledge-work-plugins：**挑一個 CRM 或文件職能，畫出 connector 所需權限與輸入／輸出；分辨自動 dependency bump 與實際功能改進。
- **context-mode／llm_wiki：**追蹤 #1248 與 #812／#813 是否合併、發布及提供效能證據，再安排長任務或大量文件示範。
- **mattpocock/skills／codebase-memory-mcp：**挑一個已有流程比較 skill 的實際改善；觀察 grilling 互動修正與 JSX 解析覆蓋。
- **rea／artcraft：**先看是否連續兩日有高增量與 fork 成長，再確認核心問題處理與平台支援；不把一次爆量當成長期需求。
- **補充候選：**alibaba/open-code-review、addyosmani/agent-skills、stablyai/orca 的快照增量值得續追；明日補查 README、release 與 Issue 後再決定是否替換精選。
- **資料品質：**維持相同十組查詢與時間窗；對 404 歷史項目另標記不可用，持續檢查 canonical name、缺少授權／README 與首次入榜的未量測成長。

## 原始來源

- [GitHub Trending daily](https://github.com/trending?since=daily)
- [完整 repo 指標](repos.json)、[收集器報告](report.md)、[日期快照](snapshots/repos-2026-10-10.json)
