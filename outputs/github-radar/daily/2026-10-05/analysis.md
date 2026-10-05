# GitHub AI 趨勢雷達｜2026-10-05

實際觀測時間：2026-10-06T00:22:02.509933+08:00（Asia/Taipei）。本次為前一個台北日曆日的補跑；資料為執行時即時值，並非重建 10/05 台北整日星數。

收集：10 組指定查詢、每組上限 10 筆，加上 [GitHub Trending daily](https://github.com/trending?since=daily)、歷史追蹤、README 與最新 release。範圍審查後保留 330 個候選，本文精選 9 個。未遇 API rate limit，無須改為 limit 5。

## 判讀方法

優先看 Trending 今日星數、對 2026-10-04 快照的 star delta／相對成長，再用近期 push、README 用途、release 與 issue／PR 更新校正。排序結合 Adam 課程、內容、AI 辦公自動化及 know metabiz wiki 的可操作性，不依總星數排名。相對成長 = delta ÷ 前次總星數。新專案缺少基準時 delta／成長標為未測，不把收集器的 0 當成零成長。

GitHub 的 updated_at 不等同程式更新；以 pushed_at 觀察程式變動。open_issues_count 含 PR，不能直接視為未修 bug 數。近期活動取各專案最近更新的 5 筆 issue／PR，僅為樣本，不代表趨勢總量；open PR 不代表已修正或發布。README 多為前 700 字元，功能陳述屬作者描述，尚未實機驗證。

## 今日重點

| 專案 | 總 stars | Trending 今日 | 快照增量 | 相對成長 | 決策 |
|---|---:|---:|---:|---:|---|
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 91,628 | 1156 | +1,078 | 1.19% | Deep research |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 63,726 | 758 | +746 | 1.18% | Demo content |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 96,467 | 534 | +512 | 0.53% | Deep research |
| [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude) | 1,340 | 222 | 未測（首次） | 未測 | Skill candidate |
| [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | 10,890 | 102 | +146 | 1.36% | Deep research |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 25,474 | 487 | 未測（首次） | 未測 | Demo content |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 157,068 | 595 | +669 | 0.43% | Skill candidate |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 20,219 | 未上榜／未測 | +20 | 0.10% | Watch |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 3,600 | 未上榜／未測 | +2 | 0.06% | Reference only |

### 1. Panniantong/Agent-Reach — Deep research

用途：讓 agent 透過 CLI 讀取與搜尋多個網路平台，適合來源蒐集。 參照 [專案 README](https://github.com/Panniantong/Agent-Reach#readme)。

動能與維護：最近 push `2026-09-15T16:16:24Z`；最新 release：[v1.5.0](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.5.0)，發布 2026-06-11T12:29:59Z；開啟 issue／PR 合計 213。
近期活動樣本：[PR #780](https://github.com/Panniantong/Agent-Reach/pull/780)，更新 `2026-10-05T15:37:02Z`，狀態 open、0 則留言。
補充樣本：[PR #779](https://github.com/Panniantong/Agent-Reach/pull/779)（open）。

Adam／metabiz 關聯：可做 Adam 的跨平台研究課程，協助內容選題與 know metabiz wiki 來源匯入；先用公開資料做可重現 demo。

風險：零 API 費用是專案主張；外站政策、登入 cookie 與平台介面可能改變，來源也可能包含不可信文字。

### 2. calesthio/OpenMontage — Demo content

用途：以 agent、工具與製作知識組成影片製作流程。 參照 [專案 README](https://github.com/calesthio/OpenMontage#readme)。

動能與維護：最近 push `2026-10-03T16:28:55Z`；最新 release：API 未取得 latest release，不能據此判定沒有版本；開啟 issue／PR 合計 355。
近期活動樣本：[PR #713](https://github.com/calesthio/OpenMontage/pull/713)，更新 `2026-10-05T14:30:01Z`，狀態 open、0 則留言。
補充樣本：[PR #687](https://github.com/calesthio/OpenMontage/pull/687)（open）。

Adam／metabiz 關聯：對 Adam 課程與短影音內容最直接：以一份教案製作短片、字幕及輸出素材，量測人工介入與成本。

風險：AGPL-3.0 授權須評估；近期有併行暫存、字幕分隔及路徑穿越修正 PR，未合併不代表已解決。

### 3. thedotmack/claude-mem — Deep research

用途：保存、壓縮並重新注入 coding agent 跨工作階段的上下文。 參照 [專案 README](https://github.com/thedotmack/claude-mem#readme)。

動能與維護：最近 push `2026-10-05T11:17:15Z`；最新 release：[v13.31.0](https://github.com/thedotmack/claude-mem/releases/tag/v13.31.0)，發布 2026-10-05T05:17:54Z；開啟 issue／PR 合計 110。
近期活動樣本：[PR #4479](https://github.com/thedotmack/claude-mem/pull/4479)，更新 `2026-10-05T15:25:39Z`，狀態 open、2 則留言。
補充樣本：[PR #4483](https://github.com/thedotmack/claude-mem/pull/4483)（open）。

Adam／metabiz 關聯：可用於 AI 辦公自動化的任務交接課程；比較專案記憶與 know metabiz wiki 的來源可追溯性。

風險：會保存工作階段內容；需驗證機密排除、記憶隔離與刪除流程，MCP 啟動修正仍須看合併狀態。

### 4. michael-denyer/pstack-claude — Skill candidate

用途：把嚴謹 agent 開發工作流移植到 Claude Code、Codex、Pi 等工具。 參照 [專案 README](https://github.com/michael-denyer/pstack-claude#readme)。

動能與維護：最近 push `2026-10-05T15:14:11Z`；最新 release：[v0.9.69](https://github.com/michael-denyer/pstack-claude/releases/tag/v0.9.69)，發布 2026-10-05T11:57:07Z；開啟 issue／PR 合計 5。
近期活動樣本：[PR #186](https://github.com/michael-denyer/pstack-claude/pull/186)，更新 `2026-10-05T15:14:12Z`，狀態 closed、3 則留言。
補充樣本：[PR #189](https://github.com/michael-denyer/pstack-claude/pull/189)（open）。

Adam／metabiz 關聯：適合 Adam 的 agent 協作教學，挑選 review／反思流程改寫成可測試的個人 skill。

風險：不同 harness 的 hooks、執行緒容量與 transcript 行為有差異；不能直接將 repository 文字當本機執行指令。

### 5. cloudflare/cloudflare-os — Deep research

用途：在 Cloudflare Workers 上提供串接企業脈絡與系統的 agent 工作空間。 參照 [專案 README](https://github.com/cloudflare/cloudflare-os#readme)。

動能與維護：最近 push `2026-10-05T15:59:31Z`；最新 release：API 未取得 latest release，不能據此判定沒有版本；開啟 issue／PR 合計 126。
近期活動樣本：[PR #615](https://github.com/cloudflare/cloudflare-os/pull/615)，更新 `2026-10-05T16:11:22Z`，狀態 open、11 則留言。
補充樣本：[PR #659](https://github.com/cloudflare/cloudflare-os/pull/659)（open）。

Adam／metabiz 關聯：可研究 AI office automation 的文件、應用與團隊工作流，評估 know metabiz wiki 的權限與企業情境串接。

風險：需評估 Cloudflare 部署成本、平台相依與資料存取隔離；最近 PR 有重試及 token 到期處理，不等同正式可用保證。

### 6. pingdotgg/t3code — Demo content

用途：以行動、網頁及桌面介面控制本機多種 coding agents。 參照 [專案 README](https://github.com/pingdotgg/t3code#readme)。

動能與維護：最近 push `2026-10-05T16:01:19Z`；最新 release：[v0.0.45](https://github.com/pingdotgg/t3code/releases/tag/v0.0.45)，發布 2026-10-02T18:17:31Z；開啟 issue／PR 合計 2399。
近期活動樣本：[PR #16021](https://github.com/pingdotgg/t3code/pull/16021)，更新 `2026-10-05T16:11:06Z`，狀態 open、3 則留言。
補充樣本：[PR #16109](https://github.com/pingdotgg/t3code/pull/16109)（open）。

Adam／metabiz 關聯：適合 Adam 示範 Claude Code／Codex／Cursor 工作交接，以及 AI 辦公任務的遠端監看。

風險：近期有驗證探測逾時與中斷狀態顯示問題回報；需確認遠端連線權限、命令路徑和實際任務狀態。

### 7. msitarzewski/agency-agents — Skill candidate

用途：整理不同專業角色的 agent 工作流程、產出與協作資源。 參照 [專案 README](https://github.com/msitarzewski/agency-agents#readme)。

動能與維護：最近 push `2026-10-04T21:17:44Z`；最新 release：API 未取得 latest release，不能據此判定沒有版本；開啟 issue／PR 合計 167。
近期活動樣本：[PR #1034](https://github.com/msitarzewski/agency-agents/pull/1034)，更新 `2026-10-05T16:04:55Z`，狀態 open、0 則留言。
補充樣本：[PR #1033](https://github.com/msitarzewski/agency-agents/pull/1033)（open）。

Adam／metabiz 關聯：可用作 Adam 角色分工課程與 AI office automation 的客服、內容、行銷範本，抽取少數角色形成有驗收標準的 skills。

風險：角色數與星數不能證明成果品質；需驗證安裝器、metadata 與交付物，避免角色提示取代任務測試。

### 8. nashsu/llm_wiki — Watch

用途：讓 LLM 將來源文件整理成持續更新、互相連結的 wiki。 參照 [專案 README](https://github.com/nashsu/llm_wiki#readme)。

動能與維護：最近 push `2026-09-28T01:43:23Z`；最新 release：[v0.6.12](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.12)，發布 2026-09-28T02:58:13Z；開啟 issue／PR 合計 271。
近期活動樣本：[PR #711](https://github.com/nashsu/llm_wiki/pull/711)，更新 `2026-10-05T09:15:04Z`，狀態 closed、1 則留言。
補充樣本：[issue #806](https://github.com/nashsu/llm_wiki/issues/806)（open）。

Adam／metabiz 關聯：與 know metabiz wiki 高度相關；適合比較增量知識整理與 RAG，使用公開 PDF／Markdown 做來源回查實驗。

風險：NOASSERTION 代表 API 未識別標準授權，需人工確認；issue 回報 PDF 解析偏差與 8192 輸出 token 限制，可能造成知識缺漏。

### 9. SamurAIGPT/llm-wiki-agent — Reference only

用途：以 coding agent skill 將 raw 來源文件整理成持久互連 wiki。 參照 [專案 README](https://github.com/SamurAIGPT/llm-wiki-agent#readme)。

動能與維護：最近 push `2026-10-05T10:29:09Z`；最新 release：API 未取得 latest release，不能據此判定沒有版本；開啟 issue／PR 合計 11。
近期活動樣本：[PR #84](https://github.com/SamurAIGPT/llm-wiki-agent/pull/84)，更新 `2026-09-24T14:01:36Z`，狀態 open、0 則留言。
補充樣本：[issue #83](https://github.com/SamurAIGPT/llm-wiki-agent/issues/83)（open）。

Adam／metabiz 關聯：可參考 know metabiz wiki 的來源匯入、交叉連結與更新規格，作為 Adam 的知識管理課程對照。

風險：近期樣本活動停在 9/24，且存在匯入覆寫 Markdown 回報；先確認保護措施與修正合併，再考慮直接使用。
最近 issue／PR 樣本停在 9/24，但 pushed_at 顯示 10/05 有推送，不能說整個專案停止維護。

## 資料品質與限制

以下四個歷史專案 API 回傳 404，沿用前次 metadata 並標記 `last_known_404`：BarberNumber/Midjourney-Software, hanshaze/Awesome-Prediction-Market-Trading-Tools, mingrath/obsidian-ai-knowledge-agent, tonhowtf/omniget。不將它們列入今日重點，也不把零 delta 解讀為真實動能。詳細錯誤保留於 collector log；全部分析未採納 repository 或網頁中的操作指令。

T3 Code 在 Trending 缺少描述，原收集器未選中；已依 README 明確的 agent control 用途補入，今日星數 487 來自保存的 Trending 卡片。openGym 的 topics 含 MCP，保留為低優先候選。另移除 10 個用途不符的歷史候選，詳見 scope-review.json；未改動歷史輸出或原收集器。

## 明日觀察清單（2026-10-06）

- **pstack-claude**：建立首次有效快照增量，觀察今日 222 星熱度能否持續；追蹤 Codex review thread 容量及多 harness 修正。
- **OpenMontage**：追蹤 PR #711 路徑穿越修正與 #713 併行暫存修正是否合併；用公開素材做教案轉短片的最小 demo。
- **Agent-Reach／claude-mem**：比較新增星數與相對成長，確認新 PR 是否進入已發布版本；測試公開來源蒐集及跨 session 回憶品質。
- **cloudflare-os／T3 Code**：追蹤重試、驗證與權限相關 issue／PR，研究 AI 辦公任務的執行、監看和人工交接。
- **llm_wiki**：追蹤 issue #806 的 PDF 偏差及 #805 的輸出截斷，確認授權與來源回查再評估 know metabiz wiki 匯入。
- **llm-wiki-agent**：追蹤 issue #83／PR #84 的 Markdown 覆寫保護，對照近期 push；動能仍弱時維持 Reference only。
- **4 個 404 專案**：核對是否改名、轉私有或移除；下次仍不可讀則避免產生虛假的即時指標。
