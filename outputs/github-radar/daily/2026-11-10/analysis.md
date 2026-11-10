# GitHub AI 趨勢雷達｜2026-11-10

## 判讀與資料口徑

本日優先研究 agent 可用的設計系統與 Skills 工作流；辦公自動化適合先做瀏覽器與 MCP 示範，know metabiz wiki 則採公開文件小樣本比較兩種 Wiki 方案。以下順序綜合 Trending 今日星數、快照星差、相對成長、README、程式推送、release 與 issue／PR 證據，並非總星數排名。

- 目標日期：Asia/Taipei 前一日 **2026-11-10**。實際完成觀測時間：2026-11-10T16:24:49.715286+00:00；抓取期間各庫時間不同。
- 執行時抓取 [GitHub Trending daily](https://github.com/trending?since=daily)，12 個卡片經語意篩選保留 8 個；4 個不相干項目排除。關鍵字漏掉 billion-context，已依上下文壓縮用途補回。
- 10 個指定查詢均使用 `--limit 10 --include-trending-daily --include-readme`；收集器成功，未回報 API 限流，因此沒有 limit 5 重試。
- 原始候選 425 個，語意審查後保留 412 個；13 個與主題無直接關係或描述不符的項目已排除。詳見 `scope-review.json`。
- Trending「stars today」是 GitHub 頁面視窗；快照 Δ 是本次總星數減前次 2026-11-09 快照；相對增長 = Δ ÷ 前次總星數。兩者觀測時間不同，不能相加或稱為相同的單日增長。新項目缺少基準時應標示未知，不把零當成停滯。
- `updated_at` 可被非程式活動影響，近期開發以 `pushed_at` 配合 release／PR 判讀。open issues 是存量且可能含 PR，並非當日新增量；近期活動僅抽樣最近更新的 5 筆 issue／PR。沒有 release 資料只代表未取得 latest release，不能推論停止維護。
- 7 個歷史庫的 metadata 讀取失敗並沿用舊值，其中 1 個已排除，保留的 6 個已標記 `metadata_stale`；不列入下列推薦與即時成長判斷。README 的效果敘述均視為作者主張，未安裝、執行或採信其中指令。

## 值得追蹤的 10 個專案

| 專案 | 判定 | stars today | 快照 Δ | 相對增長 | 總 stars |
| --- | --- | ---: | ---: | ---: | ---: |
| [meta/astryx](https://github.com/meta/astryx) | Deep research | 3111 | +3,054 | 16.07% | 22,063 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skill candidate | 1676 | +1,482 | 0.78% | 191,958 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 1223 | +1,178 | 0.37% | 320,555 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Demo content | 775 | +762 | 1.58% | 49,016 |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | Demo content | 792 | +746 | 13.10% | 6,440 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Skill candidate | 465 | +512 | 0.45% | 114,922 |
| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | Watch | 374 | +435 | 7.68% | 6,096 |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Deep research | 未上榜／無值 | +22 | 0.10% | 21,550 |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | Watch | 未上榜／無值 | +0 | 0.00% | 3,686 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Reference only | 530 | +499 | 2.52% | 20,337 |

### 1. meta/astryx — Deep research

**用途與 README 判讀：** 可供 coding agent 使用的 React／StyleX 設計系統，適合研究一致的元件與介面生成。 [專案與 README](https://github.com/meta/astryx#readme)。

**動能與維護：** stars today：3111；總 stars：22,063；快照 Δ：+3,054（前次 2026-11-09）。最後程式推送：2026-11-10T16:18:52Z；metadata 更新：2026-11-10T16:19:06Z。[Release](https://github.com/meta/astryx/releases)：v0.7.12；2026-11-10T11:16:31Z。open issues／PR 存量：683。

**對 Adam／metabiz 的價值（分析建議）：** Adam 可製作同一規格跨 agent 生成 UI 的課程；metabiz 後台先做隔離原型，不直接替換既有元件。

**風險：** README 標示 Beta；React 19+／StyleX 導入成本與行動裝置輸入體驗仍需驗證。近期 PR 不代表已發布修正。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [PR #9650](https://github.com/meta/astryx/pull/9650)：feat(core): PowerSearch suggests per-field values for free text via valueMatchBehavior；open；更新 2026-11-10T16:11:37Z。
- [PR #8125](https://github.com/meta/astryx/pull/8125)：feat(ContextMenu): open from a held finger on iOS 26's timeline；open；更新 2026-11-10T16:11:12Z。
- [PR #9777](https://github.com/meta/astryx/pull/9777)：feat(TextInput, TextArea, NumberInput): fields stay above the keyboard；open；更新 2026-11-10T16:11:02Z。

### 2. anthropics/skills — Skill candidate

**用途與 README 判讀：** 將任務指令、腳本與資源封裝成可重複執行的 Agent Skills，涵蓋文件與專業流程。 [專案與 README](https://github.com/anthropics/skills#readme)。

**動能與維護：** stars today：1676；總 stars：191,958；快照 Δ：+1,482（前次 2026-11-09）。最後程式推送：2026-11-06T22:32:32Z；metadata 更新：2026-11-10T16:14:25Z。[Release](https://github.com/anthropics/skills/releases)：未取得 latest release；無發布時間。open issues／PR 存量：1,511。

**對 Adam／metabiz 的價值（分析建議）：** 優先整理 Adam 的課程實作與 AI 辦公文件範例，為 metabiz 的報價、知識整理挑選可測量的單一 skill。

**風險：** API 未提供統一 SPDX 授權，須逐目錄核對；文件 diff 編碼與 GIF 寫入修正顯示仍需輸出檢查。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [PR #2179](https://github.com/anthropics/skills/pull/2179)：Fix GIFBuilder.save() overwriting the builder's frames and size；open；更新 2026-11-10T16:00:15Z。
- [PR #1765](https://github.com/anthropics/skills/pull/1765)：fix(office): decode redlining diffs as UTF-8；closed；更新 2026-11-10T14:44:56Z。
- [PR #1768](https://github.com/anthropics/skills/pull/1768)：fix(skill-creator): continue when report browser is unavailable；closed；更新 2026-11-10T14:44:43Z。

### 3. mattpocock/skills — Skill candidate

**用途與 README 判讀：** 日常軟體工程的研究、規劃、審查與實作 skills 集合。 [專案與 README](https://github.com/mattpocock/skills#readme)。

**動能與維護：** stars today：1223；總 stars：320,555；快照 Δ：+1,178（前次 2026-11-09）。最後程式推送：2026-11-09T14:03:07Z；metadata 更新：2026-11-10T16:18:39Z。[Release](https://github.com/mattpocock/skills/releases)：v1.3.2；2026-10-29T10:27:41Z。open issues／PR 存量：232。

**對 Adam／metabiz 的價值（分析建議）：** 可轉成 Adam 的 AI 工程工作流課程；先比對現有 skills，採用一個可驗證的研究或審查流程，降低重複規範。

**風險：** 近期 issue 回報研究後殘留 app／server／branch／暫存目錄，以及 review 只讀 committed changes；需驗證清理與未提交差異的處理。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [Issue #1412](https://github.com/mattpocock/skills/issues/1412)：research: no teardown step, so research runs leave apps, servers, branches and scratch dirs behind；open；更新 2026-11-10T12:31:03Z。
- [Issue #1411](https://github.com/mattpocock/skills/issues/1411)：grilling: end each round with a blank answer sheet；open；更新 2026-11-10T11:06:00Z。
- [Issue #1408](https://github.com/mattpocock/skills/issues/1408)：`implement` reviews before committing, but `code-review` only sees committed changes；open；更新 2026-11-10T08:33:22Z。

### 4. vercel-labs/agent-browser — Demo content

**用途與 README 判讀：** 以命令列與可存取性樹讓 agent 讀取並操作瀏覽器。 [專案與 README](https://github.com/vercel-labs/agent-browser#readme)。

**動能與維護：** stars today：775；總 stars：49,016；快照 Δ：+762（前次 2026-11-09）。最後程式推送：2026-11-10T16:04:30Z；metadata 更新：2026-11-10T16:19:39Z。[Release](https://github.com/vercel-labs/agent-browser/releases)：v0.42.0；2026-11-10T00:37:19Z。open issues／PR 存量：557。

**對 Adam／metabiz 的價值（分析建議）：** 適合 Adam 示範資料擷取到表格的 AI 辦公流程；metabiz 可先用測試帳號驗證後台資料整理。

**風險：** 近期 issue 回報 0.42.0 daemon 指令卡住；token budget 與 HTML 解析修正仍在 PR，需以固定版本測試逾時、登入狀態與結果。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [PR #2491](https://github.com/vercel-labs/agent-browser/pull/2491)：Make snapshot -c fit a token budget；open；更新 2026-11-10T16:05:42Z。
- [PR #2539](https://github.com/vercel-labs/agent-browser/pull/2539)：fix(read): respect quoted attributes and HTML comments；open；更新 2026-11-10T16:00:03Z。
- [Issue #2540](https://github.com/vercel-labs/agent-browser/issues/2540)：Daemon hangs indefinitely on all commands after start, even when Chrome is alive (0.42.0)；open；更新 2026-11-10T15:34:37Z。

### 5. homeassistant-ai/ha-mcp — Demo content

**用途與 README 判讀：** 透過 MCP 將 Claude 等助理接到 Home Assistant 的設定與自動化能力。 [專案與 README](https://github.com/homeassistant-ai/ha-mcp#readme)。

**動能與維護：** stars today：792；總 stars：6,440；快照 Δ：+746（前次 2026-11-09）。最後程式推送：2026-11-10T13:48:35Z；metadata 更新：2026-11-10T16:13:24Z。[Release](https://github.com/homeassistant-ai/ha-mcp/releases)：v9.1.2；2026-11-08T15:45:35Z。open issues／PR 存量：16。

**對 Adam／metabiz 的價值（分析建議）：** 適合 Adam 的 MCP 辦公空間自動化示範，將會議室設備狀態和規則串接；對 know metabiz wiki 可記錄設備與流程。

**風險：** README 提到 YAML 設定工具移至 beta；native Core API／trace 工具仍有變動。寫入設備前需測試狀態讀取、權限與回復流程。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [PR #3003](https://github.com/homeassistant-ai/ha-mcp/pull/3003)：feat(traces): move ha_get_automation_traces onto Core's trace data (#2632)；open；更新 2026-11-10T16:04:49Z。
- [PR #3044](https://github.com/homeassistant-ai/ha-mcp/pull/3044)：test: use real Core in webhook proxy liveness checks；open；更新 2026-11-10T15:58:54Z。
- [Issue #2632](https://github.com/homeassistant-ai/ha-mcp/issues/2632)：[FEATURE] Use native HA Core APIs, schemas, and flows for read and write tools；open；更新 2026-11-10T14:56:16Z。

### 6. addyosmani/agent-skills — Skill candidate

**用途與 README 判讀：** 將定義、規劃、建置、驗證、審查與交付串成工程 skills。 [專案與 README](https://github.com/addyosmani/agent-skills#readme)。

**動能與維護：** stars today：465；總 stars：114,922；快照 Δ：+512（前次 2026-11-09）。最後程式推送：2026-11-01T19:24:49Z；metadata 更新：2026-11-10T16:14:27Z。[Release](https://github.com/addyosmani/agent-skills/releases)：0.6.15；2026-10-31T06:40:31Z。open issues／PR 存量：133。

**對 Adam／metabiz 的價值（分析建議）：** Adam 可與 mattpocock 的工作流做對照課程；metabiz 可挑選架構教學或驗證步驟改善團隊知識交接。

**風險：** 近期 issue 指向自動模式未觸發；架構教學只是未合併 PR，不能當成可用正式功能；避免同時安裝互相重疊的技能。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [Issue #781](https://github.com/addyosmani/agent-skills/issues/781)：hey 我来自中国 最近在研究您的这份coding agent workflow 但和matt skills对比下来 我有一个疑惑；open；更新 2026-11-10T01:07:25Z。
- [PR #775](https://github.com/addyosmani/agent-skills/pull/775)：Add architecture-coaching skill (teach a human the architecture, verifiably)；open；更新 2026-11-08T06:51:50Z。
- [Issue #776](https://github.com/addyosmani/agent-skills/issues/776)：[skill-gap]: /build auto doesnt fire in auto mode；open；更新 2026-11-07T12:33:34Z。

### 7. ranxianglei/billion-context — Watch

**用途與 README 判讀：** 為長時間 coding agent 工作階段壓縮上下文與儲存記憶的插件。 [專案與 README](https://github.com/ranxianglei/billion-context#readme)。

**動能與維護：** stars today：374；總 stars：6,096；快照 Δ：+435（前次 2026-11-09）。最後程式推送：2026-11-10T16:18:14Z；metadata 更新：2026-11-10T16:21:14Z。[Release](https://github.com/ranxianglei/billion-context/releases)：v0.1.213；2026-11-07T23:25:08Z。open issues／PR 存量：956。

**對 Adam／metabiz 的價值（分析建議）：** 可設計 Adam 的成本與記憶品質實驗；know metabiz wiki 可研究長任務摘要，但應保留原始來源作為事實依據。

**風險：** README 的五倍 token 節省與月級工作階段是作者主張，尚未自行重現；壓縮會遺失細節。授權辨識為 NOASSERTION，資料表與 handoff 行為亦需追蹤。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [Issue #6121](https://github.com/ranxianglei/billion-context/issues/6121)：DSH: select models for native compaction with safe same-session handoff；open；更新 2026-11-10T16:07:53Z。
- [PR #5901](https://github.com/ranxianglei/billion-context/pull/5901)：[PR] storage: snapshot table compression foundation P0+P1 (schema v12 4-table + shadow write, all off by default, zero behavi ／ storage: 快照表压缩底座 P0+P1（schema v12 四表 + 影子写；open；更新 2026-11-10T16:12:15Z。
- [Issue #6072](https://github.com/ranxianglei/billion-context/issues/6072)：All repository documentation is available in Japanese. ／ 仓库所有文档都提供日文版本；open；更新 2026-11-10T16:03:07Z。

### 8. nashsu/llm_wiki — Deep research

**用途與 README 判讀：** 將來源文件整理為持續更新、互相連結的個人 Wiki 桌面應用。 [專案與 README](https://github.com/nashsu/llm_wiki#readme)。

**動能與維護：** stars today：未取得（不視為零）；總 stars：21,550；快照 Δ：+22（前次 2026-11-09）。最後程式推送：2026-10-21T11:17:29Z；metadata 更新：2026-11-10T15:58:59Z。[Release](https://github.com/nashsu/llm_wiki/releases)：v0.6.13；2026-10-22T01:21:07Z。open issues／PR 存量：300。

**對 Adam／metabiz 的價值（分析建議）：** 與 know metabiz wiki 最直接相關；Adam 可比較 RAG 查詢與預先整理 Wiki，先用公開文件測試中文、引文與增量更新。

**風險：** 近期 issue 回報 PDF 解析嚴重偏差，以及建立頁面／修正按鈕未實際套用。NOASSERTION 不是可直接判定的商用授權，須閱讀授權條款。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [PR #845](https://github.com/nashsu/llm_wiki/pull/845)：feat(search): add Keenable web search provider (key-free by default)；open；更新 2026-11-10T09:19:49Z。
- [Issue #806](https://github.com/nashsu/llm_wiki/issues/806)：上传的PDF内容解析出的结果出现了严重的偏差；open；更新 2026-11-09T04:35:19Z。
- [Issue #848](https://github.com/nashsu/llm_wiki/issues/848)：Bug: Review "Create Page" and Lint "Fix" buttons don't actually apply changes to the target file；open；更新 2026-11-09T04:20:05Z。

### 9. SamurAIGPT/llm-wiki-agent — Watch

**用途與 README 判讀：** 以 coding agent skill 將 raw 來源轉為持久互連的 Markdown Wiki。 [專案與 README](https://github.com/SamurAIGPT/llm-wiki-agent#readme)。

**動能與維護：** stars today：未取得（不視為零）；總 stars：3,686；快照 Δ：+0（前次 2026-11-09）。最後程式推送：2026-11-09T11:35:34Z；metadata 更新：2026-11-09T11:35:40Z。[Release](https://github.com/SamurAIGPT/llm-wiki-agent/releases)：未取得 latest release；無發布時間。open issues／PR 存量：13。

**對 Adam／metabiz 的價值（分析建議）：** 適合 know metabiz wiki 的小範圍原型；Adam 可用相同公開資料與桌面 Wiki 對照，測試來源追溯、矛盾處理與覆寫控制。

**風險：** 近期活動較慢；歷史 PR 涉及避免覆寫 Markdown 與索引連結解碼。README 對自動綜整的描述不等於準確度驗證。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [PR #86](https://github.com/SamurAIGPT/llm-wiki-agent/pull/86)：fix(health): decode percent-encoded index links；open；更新 2026-10-20T12:40:51Z。
- [PR #85](https://github.com/SamurAIGPT/llm-wiki-agent/pull/85)：fix(pdf2md): keep help output compatible with cp1252 terminals；open；更新 2026-10-08T14:04:06Z。
- [PR #84](https://github.com/SamurAIGPT/llm-wiki-agent/pull/84)：Prevent ingestion from overwriting existing Markdown files；open；更新 2026-09-24T14:01:36Z。

### 10. anthropics/claude-quickstarts — Reference only

**用途與 README 判讀：** 提供 Claude API 應用的起始範例，含客服與電腦操作場景。 [專案與 README](https://github.com/anthropics/claude-quickstarts#readme)。

**動能與維護：** stars today：530；總 stars：20,337；快照 Δ：+499（前次 2026-11-09）。最後程式推送：2026-11-06T19:37:57Z；metadata 更新：2026-11-10T16:14:34Z。[Release](https://github.com/anthropics/claude-quickstarts/releases)：未取得 latest release；無發布時間。open issues／PR 存量：240。

**對 Adam／metabiz 的價值（分析建議）：** 可作為 Adam 客服／AI 辦公課程的教學底稿，metabiz 以合成客服問題比較流程，不直接視作正式系統。

**風險：** 需要自行處理 API 成本、個資與失敗復原；近期修正目錄名稱處理及同秒軌跡衝突，範例仍需工程化。 採用判定是本次編輯評估，尚未完成部署或效能驗證。

**近期活動證據（抽樣，未合併 PR 不視為已完成）：**
- [PR #550](https://github.com/anthropics/claude-quickstarts/pull/550)：fix(agents): treat file-list directory names literally；open；更新 2026-11-10T15:53:32Z。
- [Issue #549](https://github.com/anthropics/claude-quickstarts/issues/549)：cinematic-ai-film-studio；open；更新 2026-11-10T15:19:03Z。
- [PR #472](https://github.com/anthropics/claude-quickstarts/pull/472)：fix(computer-use): keep same-second trajectories in separate directories；closed；更新 2026-11-10T14:45:17Z。

## 明日觀察清單（2026-11-11）

1. **Astryx**：今日 3,111 stars、快照相對成長超過 16%；核對 v0.7.12 後續修正與行動輸入問題，使用同一 UI 規格做小型原型比較。
2. **HA-MCP／billion-context**：相對成長明顯高於大型 Skills 庫；觀察熱度能否延續，核對 native Core 工具與壓縮／handoff 變動。壓縮工具先建立成本、事實保留率與回復品質基準。
3. **anthropics／mattpocock／addyosmani Skills**：只挑一個文件或研究流程，以固定輸入與驗收標準比較；追蹤編碼、清理與未提交變更審查問題是否真正修復。
4. **agent-browser**：優先追蹤 #2540 daemon 卡住與相關修正發布；固定版本重現後再錄製 AI 辦公示範。
5. **nashsu/llm_wiki**：追蹤 #806 PDF 解析與 #848 寫入未套用；用公開中文 PDF 記錄來源到 Wiki 的錯誤率與引用完整性，未通過前不導入內部文件。
6. **llm-wiki-agent**：確認覆寫防護 PR 是否合併，與桌面方案使用同一份資料做增量／衝突測試。星數持平，依用途保留觀察，不宣稱是今日爆紅。
7. **資料品質**：下次檢查 7 個沿用舊值的歷史庫是否恢復可讀，重新評估排除項目；以相同日期口徑比較快照，確認新發現庫的相對增長有足夠基準。

## 可追溯檔案

`repos.json` 與 `snapshots/repos-2026-11-10.json` 為審查後候選與數值；`trending-daily.json` 保存頁面卡片及語意篩選；`activity-evidence.json` 保存近期 issue／PR 抽樣；`editorial-selection.json` 保存採用評估；`collection-status.json` 保存查詢與重試／限流狀態；`report.md` 提供完整候選摘要。
