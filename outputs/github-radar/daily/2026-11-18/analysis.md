# GitHub AI 趨勢雷達｜2026-11-18

本期優先研究 SkillEvaluator 的 Skills 評估，以及 paper-orchestra 的高相對成長；last30days-skill 適合內容研究流程，llm_wiki 雖低成長仍直接對應 know metabiz wiki。以下順序綜合實作價值、動能與風險，並非總星數排名。

## 觀測時間、來源與判讀方式

- 目標日期：2026-11-18（Asia/Taipei 昨日）。實際執行與即時抓取在台北 2026-11-19；資料不代表昨日午夜的歷史狀態。
- 主來源：[GitHub Trending daily](https://github.com/trending?since=daily)、GitHub repositories／README／latest release API；10 個入選項目另查最近 5 筆 issue／PR，證據見 `activity-evidence.json`。
- 使用指定 10 組查詢、`--limit 10 --include-trending-daily --include-readme`；成功，未偵測 rate-limit，未觸發 `--limit 5` 重跑。
- 原始 450 筆記錄，合併更名／別名重複 14 筆，排除不符範圍 14 個，留下 422 個唯一候選。範圍審查見 `scope-review.json`；歷史名單的存在不等於推薦。
- 有 6 個歷史 repo 回傳 404；保留的舊資料有明確 stale 標記且不列入本期推薦，`delta_unmeasured` 的 0 是相容性占位值，不是無成長的證據。
- 「今日新增」是 Trending 滾動窗口；「快照增量」是與 2026-11-17 快照比較；相對成長＝增量÷前期總星數。不同窗口不可相加；沒有 Trending 值不等於今日零新增。
- 維護判讀看 pushed_at、release 與近期 issue／PR；updated_at 可能只是星數等互動，不視為程式更新。README 僅收前 700 字元摘要，包含徽章時證據有限；以下用途及效果未做本機安裝驗證。

## 十個值得追蹤的項目

| 優先 | Repo | 分類 | 總星數 | 今日新增 | 快照增量 | 相對成長 |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) | Deep research | 3,557 | 323 | +318 | 9.82% |
| 2 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Skill candidate | 69,747 | 1,062 | +1,002 | 1.46% |
| 3 | [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) | Demo content | 3,953 | 1,529 | +1,409 | 55.39% |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Deep research | 306,240 | 1,109 | +1,071 | 0.35% |
| 5 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Deep research | 21,746 | 未上榜／未知 | +20 | 0.09% |
| 6 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Demo content | 10,319 | 369 | +337 | 3.38% |
| 7 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Skill candidate | 59,470 | 384 | +455 | 0.77% |
| 8 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | Demo content | 210,906 | 315 | +13 | 0.01% |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | Watch | 319,824 | 823 | +734 | 0.23% |
| 10 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Watch | 10,833 | 2,322 | +2,261 | 26.38% |

### 1. NVIDIA/SkillEvaluator — Deep research

- **用途與 README**：評估 agent skills／plugins 的品質、安全性、語意重疊與實際行為效果。
- **動能判讀**：今日 +323、快照增量接近一成；小型基數且當日有 v1.0.1 release，研究優先度高於單看總星數的大型清單。
- **維護與 release**：最近 push `2026-11-18T09:12:59Z`；最新 release：[v1.0.1](https://github.com/NVIDIA/SkillEvaluator/releases/tag/v1.0.1)（2026-11-18T00:10:18Z）；GitHub open_issues_count 56（含 PR，並非回覆速度或已確認 bug 數）。
  - [PR #727：fix(tier3): preserve exit status for quoted script paths](https://github.com/NVIDIA/SkillEvaluator/pull/727)；open，更新 `2026-11-18T12:33:02Z`。
  - [Issue #784：（BUG）: Tier 1 security check fails as INCOMPLETE on a skill whose only gaps are two ES-module helpers (static_parse_limit)](https://github.com/NVIDIA/SkillEvaluator/issues/784)；open，更新 `2026-11-18T10:47:51Z`。
- **風險**：以自訂繁中任務集檢驗偵測結果；近期已有 Tier 1 安全檢查誤判為 INCOMPLETE 的回報，不能把評分當完整安全認證。
- **與 Adam 的關聯／可做內容**：Adam 課程可加入「如何驗證一個 Skill 有用」；挑 3 個現有辦公 Skills 做前後測，將評估報告與失敗案例寫入 know metabiz wiki。
- **下一步**：檢查 Tier 1 誤判與含空白路徑 exit status 修正是否合併；測量評估成本與誤報率。

### 2. mvanhorn/last30days-skill — Skill candidate

- **用途與 README**：跨社群與網路收集近期討論，整理有來源的主題研究摘要。
- **動能判讀**：今日 +1,062，快照 +1,002；有持續版本與 issue 活動，與每天產出課程題材的需求高度重合。
- **維護與 release**：最近 push `2026-11-17T22:37:11Z`；最新 release：[v4.3.2](https://github.com/mvanhorn/last30days-skill/releases/tag/v4.3.2)（2026-11-17T15:56:44Z）；GitHub open_issues_count 22（含 PR，並非回覆速度或已確認 bug 數）。
  - [PR #1486：chore(release): bump version to 4.2.1](https://github.com/mvanhorn/last30days-skill/pull/1486)；closed，更新 `2026-11-18T15:00:11Z`。
  - [Issue #1534：https://last30days.app/ is yours?](https://github.com/mvanhorn/last30days-skill/issues/1534)；closed，更新 `2026-11-18T14:51:31Z`。
- **風險**：社群資料的存取方式、配額與雜訊會影響結果；README 摘要多為徽章，需實測來源涵蓋與引用正確性。issue 中較舊版本 bump 標題不等於最新 release。
- **與 Adam 的關聯／可做內容**：製作「AI 辦公自動化最近 30 天」週報 Skill；輸入 Adam 的課程題目，產出可追溯的內容提案，再人工確認後存入 wiki。
- **下一步**：用同一繁中題目重跑，核對至少 5 個引用的日期、原文與摘要；觀察最新 release 的相容性。

### 3. google-research/paper-orchestra — Demo content

- **用途與 README**：用多 agent 把研究想法與實驗紀錄整理成含文獻與圖表的 LaTeX 稿件。
- **動能判讀**：今日 +1,529；快照 +1,409、相對成長超過五成，是本次高動能且適合展示編排分工的案例。
- **維護與 release**：最近 push `2026-11-15T18:08:08Z`；最新 release：未取得 latest release（不等於沒有維護）；GitHub open_issues_count 37（含 PR，並非回覆速度或已確認 bug 數）。
  - [Issue #49：Feature request: ACP (Agent Client Protocol) backend support](https://github.com/google-research/paper-orchestra/issues/49)；open，更新 `2026-11-17T19:15:09Z`。
  - [PR #47：Add Claude Code and Codex CLI backends, usage-limit handling and --resume](https://github.com/google-research/paper-orchestra/pull/47)；closed，更新 `2026-11-17T17:08:19Z`。
- **風險**：未取得 latest release；不可把 README 的完整論文產出主張當作已驗證品質，需逐一核對引用、圖表與原始實驗結果。
- **與 Adam 的關聯／可做內容**：課程示範「研究紀錄到文章初稿」；轉用為課程研究筆記及內部技術報告草稿，而非直接發布自動產生的結論。
- **下一步**：觀察 Claude Code／Codex CLI backend 與 resume 的合併變更、ACP backend 討論；測一份有固定事實來源的報告。

### 4. affaan-m/ECC — Deep research

- **用途與 README**：整合 coding agent 的 skills、記憶、安全與研究流程設定。
- **動能判讀**：今日 +1,109、快照約 +1,071；絕對增量高但相對成長低於小型候選，因此採選段研究，不因總星數高就全面導入。
- **維護與 release**：最近 push `2026-11-17T06:41:46Z`；最新 release：[v2.2.3](https://github.com/affaan-m/ECC/releases/tag/v2.2.3)（2026-10-01T23:00:36Z）；GitHub open_issues_count 164（含 PR，並非回覆速度或已確認 bug 數）。
  - [PR #3961：fix(project-detect): preserve extras in Python dependency arrays](https://github.com/affaan-m/ECC/pull/3961)；open，更新 `2026-11-18T15:20:14Z`。
  - [PR #3923：fix(ck): keep saved sessions when a registered project is initialized again](https://github.com/affaan-m/ECC/pull/3923)；closed，更新 `2026-11-18T15:18:19Z`。
- **風險**：框架設定面廣，可能與現有 Skills、hooks 或記憶機制重疊；近期仍在修 project detection 與 session 保留，需避免一次套入整套設定。
- **與 Adam 的關聯／可做內容**：Adam 進階課程可拆解 research-first 與記憶設計；選一個可回退的辦公工作流比較結果，將選用理由記入 wiki。
- **下一步**：追蹤 Python dependency extras 與 session 保留修正；確認挑選的元件對既有工作流沒有副作用。

### 5. nashsu/llm_wiki — Deep research

- **用途與 README**：把文件增量整理成持久、互相連結的 wiki，而非每次重新檢索後回答。
- **動能判讀**：未出現在本次 Trending；快照僅 +20。因 know metabiz wiki 的直接需求保留研究席位，並非熱度推薦。
- **維護與 release**：最近 push `2026-10-21T11:17:29Z`；最新 release：[v0.6.13](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.13)（2026-10-22T01:21:07Z）；GitHub open_issues_count 302（含 PR，並非回覆速度或已確認 bug 數）。
  - [PR #667：fix: caption images in the configured output language](https://github.com/nashsu/llm_wiki/pull/667)；closed，更新 `2026-11-16T23:20:13Z`。
  - [PR #845：feat(search): add Keenable web search provider (key-free by default)](https://github.com/nashsu/llm_wiki/pull/845)；open，更新 `2026-11-16T08:58:30Z`。
- **風險**：最新 push 與 release 在 10 月；GitHub license 為 NOASSERTION，需閱讀實際授權檔。來源覆寫、刪除同步、權限與錯誤知識累積都需實測。
- **與 Adam 的關聯／可做內容**：以公開或去識別文件比較「傳統 RAG vs 持久 wiki」；測試 know metabiz wiki 的來源追溯、雙向連結與更新流程，可直接成為課程案例。
- **下一步**：核對繁中圖片說明的修正與搜尋 provider PR；用同一份文件改版測試 wiki 是否保留來源及修正舊知識。

### 6. google-labs-code/stitch-skills — Demo content

- **用途與 README**：提供串接 Stitch MCP 的設計 Skills，README 列出跨 coding agent 相容方式。
- **動能判讀**：今日 +369、快照 +337，約 3.38% 成長；當日有程式推送及 README 補漏，適合短期 Demo。
- **維護與 release**：最近 push `2026-11-18T05:00:25Z`；最新 release：[v1.0](https://github.com/google-labs-code/stitch-skills/releases/tag/v1.0)（2026-05-18T18:02:32Z）；GitHub open_issues_count 21（含 PR，並非回覆速度或已確認 bug 數）。
  - [PR #100：docs: add missing site-md skill to README](https://github.com/google-labs-code/stitch-skills/pull/100)；closed，更新 `2026-11-18T08:55:29Z`。
  - [Issue #101：---](https://github.com/google-labs-code/stitch-skills/issues/101)；open，更新 `2026-11-18T08:52:24Z`。
- **風險**：跨 agent 相容是專案宣稱，尚未本機驗證；依賴 MCP 連線與服務條件，既有 release 日期較舊，應固定版本重現。
- **與 Adam 的關聯／可做內容**：課程示範從活動頁或課程頁需求到介面草案；把設計產出、人工修改與成功條件記入 AI 辦公 SOP。
- **下一步**：檢查 site-md 文件補漏後的完整流程，實測從需求到可修改介面的成功率與成本。

### 7. HKUDS/CLI-Anything — Skill candidate

- **用途與 README**：把軟體操作包裝為可供 agent 使用的 CLI 能力。
- **動能判讀**：今日 +384、快照 +455；仍有需求與 registry 活動，但最新 push 在 9 月，熱度與核心維護節奏需分開看。
- **維護與 release**：最近 push `2026-09-22T02:01:29Z`；最新 release：[v0.4.0](https://github.com/HKUDS/CLI-Anything/releases/tag/v0.4.0)（2026-06-25T15:17:49Z）；GitHub open_issues_count 242（含 PR，並非回覆速度或已確認 bug 數）。
  - [Issue #641：（Feature）: API-backed targets (closed-source / SaaS software with a public REST API)](https://github.com/HKUDS/CLI-Anything/issues/641)；open，更新 `2026-11-18T11:23:50Z`。
  - [PR #648：Add WireCat CLIs to the public registry](https://github.com/HKUDS/CLI-Anything/pull/648)；open，更新 `2026-11-17T22:50:45Z`。
- **風險**：不同目標軟體的覆蓋度及 CLI 穩定性有差異；近期 API-backed SaaS target 仍是功能需求，不能假設任何辦公軟體都支援。
- **與 Adam 的關聯／可做內容**：挑一個確定支援的工具包裝為可重跑 Skill；用於報表或素材處理課程，保留輸入、結果驗證與失敗回復步驟。
- **下一步**：查看 SaaS/API target 討論與 registry PR；先驗證單一目標，不先擴成通用自動化平台。

### 8. n8n-io/n8n — Demo content

- **用途與 README**：以視覺化流程、程式碼與 AI／MCP 元件串接資料及多步工作。
- **動能判讀**：今日 +315，但快照僅 +13、fork delta 為 -42；窗口或計數差異明顯，不把今日星數當成與昨日快照完全一致的成長證據。當日有 release 與密集 PR。
- **維護與 release**：最近 push `2026-11-18T16:19:42Z`；最新 release：[n8n@2.48.5](https://github.com/n8n-io/n8n/releases/tag/n8n@2.48.5)（2026-11-18T08:50:51Z）；GitHub open_issues_count 1238（含 PR，並非回覆速度或已確認 bug 數）。
  - [PR #44402：fix(MCP): exclude parent item fields from tool arguments](https://github.com/n8n-io/n8n/pull/44402)；open，更新 `2026-11-18T16:12:00Z`。
  - [PR #44246：feat(editor): Show agent triggers first and restyle trigger section](https://github.com/n8n-io/n8n/pull/44246)；open，更新 `2026-11-18T16:10:56Z`。
- **風險**：GitHub license 為 NOASSERTION、README 標示 fair-code，導入前須查實際條款；流程處理客戶資料與工具參數時需檢驗權限、重試及重複執行。
- **與 Adam 的關聯／可做內容**：最貼近 AI 辦公課程：表單輸入→摘要→人工核對→wiki 草稿或報表。此處僅提出 Demo 設計，未連接或寫入外部服務。
- **下一步**：追蹤 MCP tool arguments 排除 parent item fields 的修正；以固定輸入測試重試是否重複建立資料。

### 9. obra/superpowers — Watch

- **用途與 README**：以可組合 Skills 組織 coding agent 的軟體開發方法。
- **動能判讀**：今日 +823、快照 +734，但相對成長約 0.23%，最新 push 在 11 月初；適合作為方法論參照，不因總星數第一就優先安裝。
- **維護與 release**：最近 push `2026-11-03T23:24:58Z`；最新 release：[v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2)（2026-11-03T22:17:54Z）；GitHub open_issues_count 359（含 PR，並非回覆速度或已確認 bug 數）。
  - [Issue #2699：using-superpowers: pressure wording over-triggers skills on current Claude models](https://github.com/obra/superpowers/issues/2699)；open，更新 `2026-11-18T14:04:28Z`。
  - [Issue #2715：Drop compact from the SessionStart skill-reminder matcher](https://github.com/obra/superpowers/issues/2715)；open，更新 `2026-11-18T10:29:57Z`。
- **風險**：近期 issue 反映 skill 提示措辭過強造成過度觸發，以及 SessionStart matcher 問題；需觀察不同任務是否增加不必要步驟。
- **與 Adam 的關聯／可做內容**：作為 Adam agent 工作法課程對照組；比較簡單任務與複雜任務的完成時間、修改品質及提示成本，再寫成 wiki 選用準則。
- **下一步**：追蹤過度觸發與 compact matcher 討論，測試簡單任務是否能維持精簡流程。

### 10. elementalsouls/Claude-BugHunter — Watch

- **用途與 README**：彙整 Claude Code 的漏洞檢查與紅隊研究 Skills、模式及報告工作流。
- **動能判讀**：今日 +2,322、快照 +2,261，相對成長約 26%；熱度很強，但與一般辦公需求距離較遠，因此列觀察而非直接導入。
- **維護與 release**：最近 push `2026-11-18T13:09:42Z`；最新 release：[v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1)（2026-06-05T16:15:13Z）；GitHub open_issues_count 12（含 PR，並非回覆速度或已確認 bug 數）。
  - [PR #158：fix(skills): move oversized skill bodies into references (#82)](https://github.com/elementalsouls/Claude-BugHunter/pull/158)；closed，更新 `2026-11-18T11:32:14Z`。
  - [PR #173：fix(skills): split report-writing body into references (#82)](https://github.com/elementalsouls/Claude-BugHunter/pull/173)；open，更新 `2026-11-18T10:42:34Z`。
- **風險**：description 寫 82 skills、README 寫 83，顯示清單同步需核對；近期正把過大的 skill 內容移入 references。只在自有或已授權測試環境評估相關能力。
- **與 Adam 的關聯／可做內容**：課程可擷取「Skills 結構、引用與報告品質」案例；AI 辦公與 know metabiz wiki 的直接價值有限，保留為安全查核教材參考。
- **下一步**：追蹤 oversized skills 分拆是否完成，核對 skill 數量、引用可追溯性及固定版本的文件一致性。

## 明日觀察清單（2026-11-19 目標日）

1. **SkillEvaluator**：追蹤 v1.0.1 後續安全檢查修正；用自訂辦公 Skills 做誤報率與任務成效對照。
2. **paper-orchestra／Claude-BugHunter**：看高相對成長能否延續，並分別檢查引用品質及 Skills 分拆進度，避免把短期爆量當成熟度。
3. **last30days-skill**：對相同繁中題目核對來源完整性與 release 相容性，評估能否作為課程週報研究 Skill。
4. **nashsu/llm_wiki**：關注來源改版同步、繁中圖片說明與搜尋 provider 的變化；優先補查實際授權及來源追溯。
5. **n8n／Stitch／CLI-Anything**：各固定一個辦公或內容 Demo，記錄成功率、成本、權限與重試結果；本次沒有安裝或執行這些工具。
6. **資料品質**：再次比較 n8n 今日新增與跨快照差距；確認 404 舊資料是否移轉，持續排除 stale 記錄對動能排名的影響。

## 可核對的輸出

- `repos.json` 與 `snapshots/repos-2026-11-18.json`：本期範圍審查後的候選及動能資料。
- `report.md`：收集器摘要；本文為人工需求導向的繁體中文判讀。
- `trending-daily.html`：原始頁面留存（含網站上的非候選項目）；`trending-daily.json` 僅保留本次範圍內卡片。
- `activity-evidence.json`、`scope-review.json`、`run-status.json`、`collector-limit-10.log`：近期活動、排除、執行與錯誤證據。
