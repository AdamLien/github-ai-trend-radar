# GitHub AI 趨勢雷達｜2026-11-04

目標日期：2026-11-04（Asia/Taipei 前一日）；實際開始觀測：2026-11-05T00:11:25.029010+08:00。

本輪收錄 411 個搜尋／Trending／歷史追蹤專案，精選 8 個。未偵測到 GitHub API rate-limit；使用 --limit 10，未降額重跑。 歷史 metadata 回退 4 筆。

## 判讀方式與資料限制

- 排序綜合 Trending stars today、相鄰快照增星、相對成長、最近 push、README、release 與近期 issue／PR，以及 Adam 的實際用途；不是總星數排行榜。
- Trending 是執行時取得的滾動 daily 頁面，不能宣稱為目標日的完整歷史排名。快照差值是兩次抓取間的淨差，不等同 stars today；相對成長＝差值／前次總星數。首次觀測不以 0% 解讀。
- README 是作者描述；未安裝、未跑效能測試。issue／PR 僅抽樣最近更新的 5 筆（包含 PR），不能當作完整 issue 處理率。開啟中的發布 PR 不等於已發布 release；查無 latest release 亦可能是 API 未取得。
- 搜尋每組以總星數取樣，有成熟專案偏差；精選用成長、實際用途與風險修正。未取得 Trending daily 的專案仍可因 wiki／課程關聯入選。
- 原始證據： [Trending daily](https://github.com/trending?since=daily)、本目錄 repos.json、snapshots/、editorial-evidence.json、trending-daily-source.json 與 collection-status.json。

## 精選總覽

| 專案 | stars today | 快照增星 | 相對成長 | 總星數 | 建議 |
|---|---:|---:|---:|---:|---|
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | 2,053 | 未量測 | 未量測 | 4,247 | Deep research |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 2,463 | +2,409 | +20.02% | 14,442 | Demo content |
| [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 524 | +532 | +5.14% | 10,874 | Skill candidate |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 1,376 | +1,619 | +0.52% | 312,688 | Skill candidate |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 1,165 | +1,055 | +0.95% | 112,581 | Watch |
| [scenario-labs/skills](https://github.com/scenario-labs/skills) | 224 | 未量測 | 未量測 | 2,219 | Demo content |
| [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | 121 | 未量測 | 未量測 | 12,372 | Watch |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未上榜／未取得 | +41 | +0.19% | 21,379 | Deep research |

## 1. NVIDIA/auto-ontology｜Deep research

- **用途與 README 判讀：** 把資料庫 metadata、業務名詞與可審核 SQL 編成 ontology，透過 MCP／REST 提供 agent 使用的語意層。 [README](https://github.com/NVIDIA/auto-ontology/blob/main/README.md)
- **動能與維護：** 總星數 4,247；Trending daily 2053；快照差值 首次／無前次值，未量測（比較日 無）。最近 push 2026-11-04T15:04:47Z；open_issues_count 42（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：未取得 latest release（不推定沒有版本）。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 可設計「企業 AI 為何需要共同名詞」課程；對 AI 辦公室報表、會員／訂單指標與 know metabiz wiki 的術語治理特別相關。先用匿名示例表格測試指標追溯，不把它視為文件 wiki 的直接替代品。
- **風險：** README 的準確度主張尚未由本輪獨立測試；部署、模型供應商與資料庫權限增加維運成本；ontology 的人工審核仍是關鍵。
- **近期活動證據：** [PR #412：Add an Elasticsearch vector store with an opt-in hybrid search mode](https://github.com/NVIDIA/auto-ontology/pull/412)；狀態 open，更新 2026-11-04T16:05:23Z。
- **近期活動證據：** [PR #413：Install the Ossie converter from apache/ossie-converters](https://github.com/NVIDIA/auto-ontology/pull/413)；狀態 open，更新 2026-11-04T15:09:14Z。
- **下一步：** 追蹤向量維度相容、Elasticsearch hybrid search 的 PR 是否合併，及是否新增可重現評測。

## 2. vercel-labs/agent-desktop｜Demo content

- **用途與 README 判讀：** 透過作業系統 accessibility tree 讓 agent 讀取與操作桌面程式，並提供 MCP 介面。 [README](https://github.com/vercel-labs/agent-desktop/blob/main/README.md)
- **動能與維護：** 總星數 14,442；Trending daily 2463；快照差值 2409（比較日 2026-11-03）。最近 push 2026-11-03T23:16:15Z；open_issues_count 160（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：[v1.1.0](https://github.com/vercel-labs/agent-desktop/releases/tag/v1.1.0)，發布 2026-11-03T04:13:45Z。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 適合錄製「從自然語言到桌面操作」課程示範；AI 辦公室可先試無敏感資料的表單搬運，執行紀錄可整理進 know metabiz wiki。
- **風險：** 本輪 issue 回報 macOS 過期程序會影響 inventory、Windows UWP app identity 不一致；桌面權限與誤操作需要實機驗證。
- **近期活動證據：** [PR #556：fix(macos): drop app records with no live process instead of failing inventory](https://github.com/vercel-labs/agent-desktop/pull/556)；狀態 open，更新 2026-11-04T14:53:41Z。
- **近期活動證據：** [Issue #355：macOS: one stale NSRunningApplication (process gone, terminated=false) fails every inventory command](https://github.com/vercel-labs/agent-desktop/issues/355)；狀態 open，更新 2026-11-04T14:25:50Z。
- **下一步：** 觀察 macOS inventory 修補是否合併，以及 Windows UWP 的 snapshot／screenshot 是否一致。

## 3. max-sixty/worktrunk｜Skill candidate

- **用途與 README 判讀：** 把 Git worktree 的建立、切換與平行 agent 開發流程包成 CLI。 [README](https://github.com/max-sixty/worktrunk/blob/main/README.md)
- **動能與維護：** 總星數 10,874；Trending daily 524；快照差值 532（比較日 2026-11-03）。最近 push 2026-11-04T14:07:58Z；open_issues_count 71（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：[v0.81.0](https://github.com/max-sixty/worktrunk/releases/tag/v0.81.0)，發布 2026-10-20T21:28:34Z。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 可整理成 Adam 的「多 agent 平行開發」操作 Skill 與課程，讓 AI 辦公室自動化腳本各自在獨立工作目錄開發；know metabiz wiki 可記錄分支與回收流程。
- **風險：** worktree、shell 整合與 hooks 仍會影響實際工作目錄；Windows Terminal 的 wt 名稱衝突已有近期問題，不能把一個已關閉 issue 當作所有版本都已修好。
- **近期活動證據：** [Issue #4696：`nightly` failing on `main` (push)](https://github.com/max-sixty/worktrunk/issues/4696)；狀態 closed，更新 2026-11-04T14:19:02Z。
- **近期活動證據：** [PR #4698：fix(plugins): skip Windows Terminal's wt in the pi, omp, and OpenCode plugins](https://github.com/max-sixty/worktrunk/pull/4698)；狀態 closed，更新 2026-11-04T14:07:58Z。
- **下一步：** 檢查 Windows alias 修補進入哪個 release，並觀察 nightly 失敗是否再出現。

## 4. mattpocock/skills｜Skill candidate

- **用途與 README 判讀：** 將需求澄清、工程設計、實作與審查方法整理成 coding agent 可重複使用的 Skills。 [README](https://github.com/mattpocock/skills/blob/main/README.md)
- **動能與維護：** 總星數 312,688；Trending daily 1376；快照差值 1619（比較日 2026-11-03）。最近 push 2026-11-04T11:45:30Z；open_issues_count 210（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：[v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2)，發布 2026-10-29T10:27:41Z。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 適合與 Adam 現有課程和 Skills 做差異比較；挑一個 code review／研究流程做示範，AI 辦公室 SOP 與 know metabiz wiki 可採用明確的輸入、產出與驗收條件。
- **風險：** 近期 issue 指出 implement 與 code-review 對未提交變更的處理不一致；大量安裝或自動更新可能改變既有工作方式。先逐項比對本地版本。
- **近期活動證據：** [Issue #511：(Bug) `implement` and `code-review` disagree on reviewing uncommitted changes](https://github.com/mattpocock/skills/issues/511)；狀態 open，更新 2026-11-04T15:12:23Z。
- **近期活動證據：** [PR #1368：feat: publish skills to npm as @mattpocock/skills](https://github.com/mattpocock/skills/pull/1368)；狀態 open，更新 2026-11-04T11:45:49Z。
- **下一步：** 追蹤 review 範圍不一致的 issue，以及 npm 發布 PR；不把尚未合併 PR 視為可用安裝管道。

## 5. thedotmack/claude-mem｜Watch

- **用途與 README 判讀：** 記錄 agent session、壓縮觀察並於後續工作檢索，提供跨 session 記憶與 MCP 搜尋。 [README](https://github.com/thedotmack/claude-mem/blob/main/README.md)
- **動能與維護：** 總星數 112,581；Trending daily 1165；快照差值 1055（比較日 2026-11-03）。最近 push 2026-11-04T08:19:38Z；open_issues_count 136（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：[v15.9.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.9.0)，發布 2026-11-02T18:03:43Z。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 適合「AI 記憶與知識庫有何差別」課程；AI 辦公室的任務交接可受益，但 know metabiz wiki 應保留可審查的正式知識，而不是直接匯入所有 session。
- **風險：** session 記錄可能包含公司資料；README 的 private 排除標籤仍需驗證。近期 issue 涉及 self-hosted 後端 queue wait 與 paid-send budget，成本和穩定性需先試跑。
- **近期活動證據：** [Issue #4737：90s idle timeout fires on queue wait with a self-hosted backend, and transient failures spend the paid-send budget and park batches permanently (13.35.0)](https://github.com/thedotmack/claude-mem/issues/4737)；狀態 open，更新 2026-11-04T15:51:09Z。
- **近期活動證據：** [PR #5369：fix(prompt-import): decode JSON tool strings while preserving raw input](https://github.com/thedotmack/claude-mem/pull/5369)；狀態 open，更新 2026-11-04T15:46:12Z。
- **下一步：** 追蹤 idle timeout／queue wait 問題、記錄匯入與 project identity 修補是否進入 release。

## 6. scenario-labs/skills｜Demo content

- **用途與 README 判讀：** 以 Skills 與 Scenario MCP 串接圖片、影片、音訊及 3D 素材生成，亦提供創作工具的專家流程。 [README](https://github.com/scenario-labs/skills/blob/main/README.md)
- **動能與維護：** 總星數 2,219；Trending daily 224；快照差值 首次／無前次值，未量測（比較日 無）。最近 push 2026-11-04T09:40:43Z；open_issues_count 36（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：[skills-v0.60.1](https://github.com/scenario-labs/skills/releases/tag/skills-v0.60.1)，發布 2026-10-29T15:25:46Z。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 可用於 Adam 的內容製作示範，尤其品牌一致性、素材生成前成本評估；AI 辦公室可先做單一匿名素材，know metabiz wiki 保存製作流程與模型選擇。
- **風險：** 依賴 Scenario 帳號、外部服務與用量費用；Skill 的 MIT 授權不代表生成素材、模型與商用服務條款完全相同。完整工具鏈還需相容版本與應用程式。
- **近期活動證據：** [PR #363：feat(scenario-game-ua-ads): add mobile game UA ad skill](https://github.com/scenario-labs/skills/pull/363)；狀態 open，更新 2026-11-04T12:13:07Z。
- **近期活動證據：** [PR #342：chore: release skills 0.61.0](https://github.com/scenario-labs/skills/pull/342)；狀態 open，更新 2026-11-03T18:15:01Z。
- **下一步：** 觀察 0.61.0 發布 PR 是否合併、Node／Windows symlink 文件是否落地，以及新廣告 Skill 的可重現性。

## 7. Thysrael/Horizon｜Watch

- **用途與 README 判讀：** 把 RSS、GitHub 等來源彙整為可設定 profile 的 AI 雙語新聞簡報，並提供 CLI 與 MCP。 [README](https://github.com/Thysrael/Horizon/blob/main/README.md)
- **動能與維護：** 總星數 12,372；Trending daily 121；快照差值 首次／無前次值，未量測（比較日 無）。最近 push 2026-11-03T17:20:32Z；open_issues_count 6（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：未取得 latest release（不推定沒有版本）。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 與 Adam 每日選題和 AI 辦公室情報整理高度接近；可做「同來源、不同受眾」內容示範，know metabiz wiki 可接收人工核對後的摘要與原始連結。
- **風險：** 摘要品質依賴來源、模型與抽取器；近期 JSON 解析修補 PR 仍開啟。公開輸出或推播前應檢查日期、引用與重複內容；本輪未啟用任何傳送功能。
- **近期活動證據：** [PR #198：fix(ai): find the JSON object past brace text and braces inside strings](https://github.com/Thysrael/Horizon/pull/198)；狀態 open，更新 2026-11-04T15:00:51Z。
- **近期活動證據：** [PR #197：feat(extractors): add Keenable content extractor](https://github.com/Thysrael/Horizon/pull/197)；狀態 open，更新 2026-11-04T12:30:58Z。
- **下一步：** 追蹤 JSON 解析修補與新抽取器 PR，確認失敗重跑是否會重複產出。

## 8. nashsu/llm_wiki｜Deep research

- **用途與 README 判讀：** 把原始文件增量整理為互連 wiki，提供來源追溯、快取、知識圖與桌面介面。 [README](https://github.com/nashsu/llm_wiki/blob/main/README.md)
- **動能與維護：** 總星數 21,379；Trending daily 未上榜／未取得；快照差值 41（比較日 2026-11-03）。最近 push 2026-10-21T11:17:29Z；open_issues_count 299（GitHub 此欄包含開啟 PR，不能解讀為待修 bug 數）。最新 release：[v0.6.13](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.13)，發布 2026-10-22T01:21:07Z。
- **Adam／內容／AI 辦公室／know metabiz wiki：** 對 know metabiz wiki 最直接：可比較 raw sources／wiki／schema 分層、來源異動與刪除的傳播；適合 Adam 的「RAG 與持續維護知識」課程，以及 AI 辦公室 SOP 文件整理。
- **風險：** 本輪沒有驗證引用正確率、企業權限或協作能力；Linux 啟動缺少 libayatana-appindicator3 的 issue 仍開啟，長文件分段生成 PR 尚待合併。
- **近期活動證據：** [Issue #847：Linux: startup panic in libappindicator-sys when libayatana-appindicator3 is not installed](https://github.com/nashsu/llm_wiki/issues/847)；狀態 open，更新 2026-11-04T13:09:04Z。
- **近期活動證據：** [PR #846：fix: generate long sources section by section](https://github.com/nashsu/llm_wiki/pull/846)；狀態 open，更新 2026-11-03T20:59:35Z。
- **下一步：** 追蹤 Linux 啟動依賴修補、長文件分段生成、刪除來源後索引一致性。

## 明日觀察清單

下次執行預計 2026-11-06；仍按執行時的台北前一日歸檔。

- **NVIDIA/auto-ontology：** 追蹤向量維度相容、Elasticsearch hybrid search 的 PR 是否合併，及是否新增可重現評測。
- **vercel-labs/agent-desktop：** 觀察 macOS inventory 修補是否合併，以及 Windows UWP 的 snapshot／screenshot 是否一致。
- **max-sixty/worktrunk：** 檢查 Windows alias 修補進入哪個 release，並觀察 nightly 失敗是否再出現。
- **mattpocock/skills：** 追蹤 review 範圍不一致的 issue，以及 npm 發布 PR；不把尚未合併 PR 視為可用安裝管道。
- **thedotmack/claude-mem：** 追蹤 idle timeout／queue wait 問題、記錄匯入與 project identity 修補是否進入 release。
- **scenario-labs/skills：** 觀察 0.61.0 發布 PR 是否合併、Node／Windows symlink 文件是否落地，以及新廣告 Skill 的可重現性。
- **Thysrael/Horizon：** 追蹤 JSON 解析修補與新抽取器 PR，確認失敗重跑是否會重複產出。
- **nashsu/llm_wiki：** 追蹤 Linux 啟動依賴修補、長文件分段生成、刪除來源後索引一致性。

優先做兩個可驗證的小實驗：以匿名資料測 auto-ontology 的業務名詞與 SQL 可追溯性；以相同文件測 LLM Wiki 的增量更新、來源刪除與引用正確性。內容示範優先選 agent-desktop；Skill 整理優先評估 worktrunk 與既有工程 Skills 的差異。
