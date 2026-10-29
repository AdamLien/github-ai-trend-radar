# GitHub AI 趨勢雷達｜2026-10-29

目標日期：2026-10-29（Asia/Taipei 前一日）；實際收集時間：2026-10-30T00:20:54.242869+08:00。本次為執行當下的公開資料快照，不是回溯重建目標日結束時的數據。

依指定 10 組查詢、每組上限 10，合併 Trending daily 與既有追蹤後，共取得 382 個 repository。以下精選 9 個；順序綜合今日加星、快照增量、相對成長、近期 push、README、release 與近期 issue／PR 訊號，沒有按總星數排序。

API 限流：未偵測到；維持 --limit 10。collector exit code：0。補充 README／issue 請求的狀態另列於 review-evidence.json。

## 方法與證據限制

- 今日加星來自 [GitHub Trending daily](https://github.com/trending?since=daily)，與 collector 的快照星數差是不同時間窗，不能相加。保留的原始卡片見 trending-evidence.json。
- 星數差與相對成長依前次可用快照計算；相對成長＝差值／前次總星數。新收錄項目沒有基準時標示未知，不能把 collector 的預設 0 當作零成長。
- push 是提交活躍訊號，不保證功能完成；release 顯示最新發佈記錄，不代表已驗證穩定。最近 10 筆更新的 issue／PR 只是小樣本，不是每日總量，closed PR 也不代表已合併。
- README 的能力敘述是作者宣稱，本次只做文件與公開活動研究，沒有安裝或執行外部專案。open_issues 是 GitHub 的未結項目計數，可能包含 PR，不能單獨判斷健康度。

## 精選比較

| Repo | 今日加星 | 快照星數差 | 相對成長 | 總星數 | 判斷 |
|---|---:|---:|---:|---:|---|
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 2881 | +2,727（自 2026-10-28） | +2.96% | 94,726 | Demo content |
| [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) | 1116 | +1,062（自 2026-10-28） | +22.39% | 5,805 | Deep research |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未上榜／無資料 | +50（自 2026-10-28） | +0.24% | 21,141 | Deep research |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 459 | +482（自 2026-10-28） | +0.46% | 104,414 | Watch |
| [obra/superpowers](https://github.com/obra/superpowers) | 1037 | +998（自 2026-10-28） | +0.32% | 308,161 | Skill candidate |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 1926 | +1,889（自 2026-10-28） | +3.97% | 49,472 | Demo content |
| [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | 1178 | +1,064（自 2026-10-28） | +9.84% | 11,876 | Skill candidate |
| [nightly-labs/openbot](https://github.com/nightly-labs/openbot) | 705 | +660（自 2026-10-28） | +21.74% | 3,696 | Watch |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 240 | 未知（無前次基準） | 未知 | 7,898 | Watch |

## 1. pbakaus/impeccable — Demo content

用途：把視覺設計的引導、批評與稽核整理成 coding agent 可使用的技能與詞彙。README 提供同一需求的前後案例，可作教學對照。

動能與成熟度：今日加星 2881；總星數 94,726。最近 push：2026-10-29T16:08:13Z；未結項目 49；授權 Apache-2.0。最新 release：[cli-v4.8.0](https://github.com/pbakaus/impeccable/releases/tag/cli-v4.8.0)，發佈 2026-10-26T23:41:55Z。最近更新樣本含 3 筆 issue、7 筆 PR。
- [Issue #1220](https://github.com/pbakaus/impeccable/issues/1220)：[Bug] Directory scans skip .mjs and .cjs sources supported by explicit file scans（open，更新 2026-10-29T16:11:32Z）。
- [PR #1225](https://github.com/pbakaus/impeccable/pull/1225)：Fix: walk .mjs and .cjs sources in directory scans (#1220)（open，更新 2026-10-29T16:09:02Z）。

風險：設計評分與宣傳案例不等於使用者測試；近期 issue 涉及目錄掃描漏掉 .mjs/.cjs，需確認對實際專案的涵蓋。

對 Adam／metabiz 的關聯與下一步：Adam 可製作同一簡報／活動頁需求在有無設計技能時的比較內容，量測完成時間、可讀性與無障礙；metabiz 可先以非正式網站頁面試作。

來源：[repository／README](https://github.com/pbakaus/impeccable#readme)、[近期議題](https://github.com/pbakaus/impeccable/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 2. JetBrains/thinkrail — Deep research

用途：以 pi agent 為核心，結合 IDE、git worktree 隔離、living specs 與可重用 skills。

動能與成熟度：今日加星 1116；總星數 5,805。最近 push：2026-10-29T16:07:37Z；未結項目 271；授權 Apache-2.0。最新 release：[v0.2.0](https://github.com/JetBrains/thinkrail/releases/tag/v0.2.0)，發佈 2026-10-18T20:52:19Z。最近更新樣本含 0 筆 issue、10 筆 PR。
- [PR #1015](https://github.com/JetBrains/thinkrail/pull/1015)：fix(server): bound every sync git call and move hot reads off the loop（open，更新 2026-10-29T16:13:55Z）。
- [PR #987](https://github.com/JetBrains/thinkrail/pull/987)：fix(resources): recover from a refused Resources read and make replay overflow observable（open，更新 2026-10-29T16:13:09Z）。

風險：近期 PR 正處理同步 git 呼叫阻塞及檔案樹更新；功能快速演進，需實測效能、分支隔離與復原。

對 Adam／metabiz 的關聯與下一步：適合 Adam 的多 agent 開發課程，示範任務拆分到 worktree、審查再合併；對辦公自動化的直接價值較低，可借鏡規格持久化。

來源：[repository／README](https://github.com/JetBrains/thinkrail#readme)、[近期議題](https://github.com/JetBrains/thinkrail/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 3. nashsu/llm_wiki — Deep research

用途：將文件建立成可持續更新的結構化 wiki；README 列出來源追溯、增量快取、多格式匯入、來源限定查詢與檔案監看。

動能與成熟度：今日加星 未上榜／無資料；總星數 21,141。最近 push：2026-10-21T11:17:29Z；未結項目 286；授權 NOASSERTION。最新 release：[v0.6.13](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.13)，發佈 2026-10-22T01:21:07Z。最近更新樣本含 4 筆 issue、6 筆 PR。
- [Issue #832](https://github.com/nashsu/llm_wiki/issues/832)：Feature: configurable prompt section caps and Deep Research result count, a shared output style for ingest and chat, and output hooks（open，更新 2026-10-29T08:11:44Z）。
- [PR #704](https://github.com/nashsu/llm_wiki/pull/704)：[feature]自定义背景图、资源管理器打开、以及摄入队列清理（open，更新 2026-10-29T02:43:03Z）。

風險：近期 PR 涉及 watcher 自觸發重掃描；來源有連結不代表內容無幻覺。還需驗證刪除同步、機密資料處理、版本衝突與大型文件成本。

對 Adam／metabiz 的關聯與下一步：與 know metabiz wiki 最直接相關：用匿名 SOP／課程資料做小型基準，測試增量更新、來源定位、衝突與刪除後查詢；可產出 RAG 與持久 wiki 的教學比較。

來源：[repository／README](https://github.com/nashsu/llm_wiki#readme)、[近期議題](https://github.com/nashsu/llm_wiki/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 4. thedotmack/claude-mem — Watch

用途：擷取 agent session 的工作脈絡，壓縮後於後續 session 提供相關記憶；主打跨工具延續上下文。

動能與成熟度：今日加星 459；總星數 104,414。最近 push：2026-10-29T00:48:27Z；未結項目 146；授權 Apache-2.0。最新 release：[v15.5.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.5.0)，發佈 2026-10-29T00:48:22Z。最近更新樣本含 7 筆 issue、3 筆 PR。
- [Issue #3603](https://github.com/thedotmack/claude-mem/issues/3603)：[plan-15] Worker Port & Liveness Authority — one verified answer to "is a worker serving this port?"（open，更新 2026-10-29T15:58:51Z）。
- [Issue #5185](https://github.com/thedotmack/claude-mem/issues/5185)：Observer (openai-compatible): an error envelope inside a 2xx/SSE reply whose code is not numeric is classified unrecoverable even when the message says (HTTP 503): no retry, no quota fallback, pending observations discarded（open，更新 2026-10-29T15:08:28Z）。

風險：近期議題包含 worker 存活判定、觀察資料遺失與 Chroma sidecar 一致性；先驗證可重啟性、資料保留與敏感資料排除。

對 Adam／metabiz 的關聯與下一步：Adam 可示範跨天任務接續；AI 辦公室可評估週期性報表任務，但 know metabiz wiki 仍需獨立維護可引用的原始來源。

來源：[repository／README](https://github.com/thedotmack/claude-mem#readme)、[近期議題](https://github.com/thedotmack/claude-mem/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 5. obra/superpowers — Skill candidate

用途：把軟體開發方法整理成可組合的 skills 與工作流程。README 強調從需求到規劃、執行與驗證的完整方法。

動能與成熟度：今日加星 1037；總星數 308,161。最近 push：2026-10-23T03:48:57Z；未結項目 369；授權 MIT。最新 release：[v7.0.1](https://github.com/obra/superpowers/releases/tag/v7.0.1)，發佈 2026-10-21T21:05:11Z。最近更新樣本含 4 筆 issue、6 筆 PR。
- [PR #2641](https://github.com/obra/superpowers/pull/2641)：Feature/trajectory hierarchy（closed，更新 2026-10-29T03:27:45Z）。
- [PR #2640](https://github.com/obra/superpowers/pull/2640)：Removes AGENTS.md and adds note to README.md（closed，更新 2026-10-28T21:34:13Z）。

風險：框架會影響 agent 行為與流程成本；需逐項審閱技能、檢查是否與既有規範衝突，並實測簡單任務是否過度流程化。

對 Adam／metabiz 的關聯與下一步：適合 Adam 的 agent 工程課程及可重用工作法內容；metabiz 可挑需求澄清、驗證與任務交接片段作內部 skill 候選，本次沒有安裝或執行外部技能。

來源：[repository／README](https://github.com/obra/superpowers#readme)、[近期議題](https://github.com/obra/superpowers/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 6. HKUDS/DeepTutor — Demo content

用途：以長期個人化學習為目標的 AI tutor；README 的 v1.7.0 說明涵蓋模組化安裝、學習工作區、筆記及嵌入斷點續作。

動能與成熟度：今日加星 1926；總星數 49,472。最近 push：2026-10-29T10:14:05Z；未結項目 229；授權 Apache-2.0。最新 release：[v1.7.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.7.0)，發佈 2026-10-28T14:13:12Z。最近更新樣本含 2 筆 issue、8 筆 PR。
- [Issue #2166](https://github.com/HKUDS/DeepTutor/issues/2166)：Legacy TutorBot migration keeps non-ASCII directory names as partner_id → partner page always shows "Partner not found"（open，更新 2026-10-29T15:48:35Z）。
- [PR #2050](https://github.com/HKUDS/DeepTutor/pull/2050)：feat: manage generated output files（closed，更新 2026-10-29T15:32:40Z）。

風險：近期議題包含非 ASCII 目錄遷移造成頁面不可用；中文資料、答案正確性、模型費用與學習成效須獨立驗證。

對 Adam／metabiz 的關聯與下一步：Adam 可將自有課程資料做小型互動助教展示，測試引用、練習回饋與中文檔名；metabiz 可研究新人 SOP 學習，不宜將熱度當教學成效證據。

來源：[repository／README](https://github.com/HKUDS/DeepTutor#readme)、[近期議題](https://github.com/HKUDS/DeepTutor/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 7. elayadesign/ai-design-skills — Skill candidate

用途：小型設計技能集合；目前 README 主要列出 landing-page-design，涵蓋需求訪談、頁面結構、轉換文案與視覺系統。

動能與成熟度：今日加星 1178；總星數 11,876。最近 push：2026-10-27T16:02:10Z；未結項目 7；授權 MIT。最新 release：未取得正式 release（不代表沒有版本或套件發佈）。最近更新樣本含 2 筆 issue、5 筆 PR。
- [PR #8](https://github.com/elayadesign/ai-design-skills/pull/8)：Update SKILL.md（open，更新 2026-10-29T03:47:21Z）。
- [PR #6](https://github.com/elayadesign/ai-design-skills/pull/6)：Add CI check that validates SKILL.md frontmatter（open，更新 2026-10-28T21:14:01Z）。

風險：技能集合仍小；議題提出動畫規則與 hover 色彩變化衝突，另有 frontmatter 驗證 PR。須審閱規則一致性及平台安裝方式。

對 Adam／metabiz 的關聯與下一步：可與 impeccable 做同題比較，供 Adam 設計技能教學與活動頁內容；metabiz 可評估把需求訪談步驟整理為本地技能，先保留人工品牌審查。

來源：[repository／README](https://github.com/elayadesign/ai-design-skills#readme)、[近期議題](https://github.com/elayadesign/ai-design-skills/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 8. nightly-labs/openbot — Watch

用途：本機優先的持續 AI 工作夥伴桌面工作區，提供獨立對話、任務佇列、檔案交換、內嵌瀏覽器與 agent 間訊息。

動能與成熟度：今日加星 705；總星數 3,696。最近 push：2026-10-29T16:16:10Z；未結項目 336；授權 NOASSERTION。最新 release：[v0.54.0](https://github.com/nightly-labs/openbot/releases/tag/v0.54.0)，發佈 2026-10-29T14:47:49Z。最近更新樣本含 3 筆 issue、7 筆 PR。
- [Issue #3897](https://github.com/nightly-labs/openbot/issues/3897)：[Feature]: Native Gemini Live voice conversations with the existing OpenBot agent（open，更新 2026-10-29T16:09:14Z）。
- [PR #3580](https://github.com/nightly-labs/openbot/pull/3580)：Let agents create workflows from chat（open，更新 2026-10-29T15:59:34Z）。

風險：README 明示開發預覽，agent 預設 danger-full-access 且不逐項確認；近期仍討論不可逆動作前的協定檢查。只能先用隔離的測試資料與帳戶評估。

對 Adam／metabiz 的關聯與下一步：與 Adam AI 辦公室任務佇列、多角色交接內容高度相關；可先錄製匿名資料的多步工作展示，正式辦公流程仍須界定權限、紀錄與停止條件。

來源：[repository／README](https://github.com/nightly-labs/openbot#readme)、[近期議題](https://github.com/nightly-labs/openbot/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 9. CopilotKit/OpenBot — Watch

用途：以 AG-UI 串接不同 agent stack 的自架 AI coworker 模板，每個 coworker 擁有瀏覽器、檔案與工具並保留動作紀錄。

動能與成熟度：今日加星 240；總星數 7,898。最近 push：2026-10-29T15:58:44Z；未結項目 55；授權 MIT。最新 release：[v0.2.0](https://github.com/CopilotKit/OpenBot/releases/tag/v0.2.0)，發佈 2026-10-12T15:19:49Z。最近更新樣本含 8 筆 issue、2 筆 PR。
- [PR #879](https://github.com/CopilotKit/OpenBot/pull/879)：Close a computer's browsers before its memory runs out, and a Bot's idle tabs（open，更新 2026-10-29T16:10:17Z）。
- [PR #882](https://github.com/CopilotKit/OpenBot/pull/882)：Open a conversation at the bottom, keep it still while a Bot writes, and add a rail of turns（open，更新 2026-10-29T15:58:55Z）。

風險：README 明示 beta 與模板性質，預設 single-user 模式以管理者接納請求；近期有瀏覽器記憶體回收與 Responses API 工具相容性問題。

對 Adam／metabiz 的關聯與下一步：適合 Adam 製作自架 AI coworker 架構解說；metabiz 若研究辦公自動化，先驗證登入隔離、工具授權、稽核與部署成本，不能把模板等同維運完成的服務。

來源：[repository／README](https://github.com/CopilotKit/OpenBot#readme)、[近期議題](https://github.com/CopilotKit/OpenBot/issues)。擷取內容及活動時間保留於 review-evidence.json；數值以 repos.json 為準。

## 明日觀察清單

1. **impeccable、ai-design-skills**：比對今日加星與相對成長是否延續，追蹤掃描漏檔及動畫規則問題；固定同一頁面需求錄製有無技能的比較。
2. **thinkrail、兩個 OpenBot**：追蹤阻塞、瀏覽器記憶體與執行權限相關修正；兩個 OpenBot 是不同組織的獨立專案，避免混用成熟度判斷。
3. **llm_wiki、claude-mem**：觀察檔案監看、記憶持久性與復原議題，準備匿名 SOP 的新增／改版／刪除測試及來源引用評分。
4. **DeepTutor**：檢查新版本後的中文檔名與教材匯入情況，挑一堂自有課程定義可量測的助教示範。
5. **superpowers 與 MCP**：追蹤工作法變動；補看 [官方 MCP servers](https://github.com/modelcontextprotocol/servers) 是否有與辦公資料源相關的新內容。有明確 release 或議題證據再提高優先度，不因總星數大就列為熱點。

本次優先投入：設計 skills 的短內容比較，以及 llm_wiki 的 know metabiz wiki 小型評估；IDE 與 AI coworker 保持研究／觀察，待效能、權限與恢復能力可驗證後再考慮導入。


## 資料品質補記

Trending 原始卡片共 11 筆，人工按用途確認皆屬 AI／agent／skills／coding 或模型行為研究範圍；DeepTutor 與 OpenMausBot 原先因關鍵字篩選漏收，已依卡片補回今日加星與來源標記，並新增 OpenMausBot 的 API metadata。沒有修改收集器原始碼。

下列 4 個歷史追蹤專案回傳 HTTP 404，collector 沿用舊 metadata，這些不是本次的新鮮觀察，不用其增量推論動能：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。repos.json 及 snapshot 已標記 metadata_fresh=false；完整稽核資訊見 run-status.json。

API 回傳的 canonical full_name 有 8 筆重複（搜尋／歷史別名彙整），已按 canonical 名稱去重：collector 原始 389 筆，去重 381 個，加回漏收的 OpenMausBot 後最終 382 個。
