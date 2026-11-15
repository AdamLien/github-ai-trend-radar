# GitHub AI 趨勢雷達｜2026-11-15

本期 target_date：2026-11-15。實際收集：2026-11-16T00:11:32.030341+08:00 至 2026-11-16T00:23:49.527846+08:00（Asia/Taipei）。

## 判讀方法與資料限制

- 執行指定十組搜尋，`--limit 10 --include-trending-daily --include-readme`；合併歷史追蹤並依 GitHub 回傳 full_name 去重後共 432 個 repo（原收集 445 筆，14 筆重複身分，另補入 ggml 1 筆）。GitHub Trending daily 共保留 12 個 AI／agent／Skills 相關項目，原始頁與篩選審核見 `snapshots/trending-daily.html`、`snapshots/trending-cards.json`、`scope-review.json`。ggml 因原關鍵字漏判 machine learning，另行補抓。
- 「今日星數」是 GitHub Trending 頁面的即時 stars today；「快照差」是本次與 2026-11-14 快照的總星數差，兩者時間窗不同，不能相加，也不是嚴格的台北昨日全天統計。相對增長＝快照差／前期總星數。首次觀測沒有可比較基準，表中以 — 表示，資料欄的 0 不解讀成零成長。
- 排序依實作價值、今日星數、快照差、相對增長、近期 push／release、README 及 issue／PR 活動綜合判斷，不按總星數排序。SkillEvaluator 總星較少，因能驗證 Skills 成效列為首要研究；Wiki 候選雖增長較慢，因 know metabiz 的直接需求保留。
- 每個精選另取 README 全文及最近更新的 5 筆 issue／PR；這是活動樣本，不是完整 issue 趨勢或品質評分。GitHub open_issues_count 包含 PR，不視為缺陷數。未合併 PR 僅為追蹤訊號。所有用途與採用優先序皆為編輯評估，未安裝、未做產品效能驗證。
- Rate-limit：未觀測到 API rate-limit 錯誤；limit 10 成功，無須改用 limit 5。另有 6 個歷史 repo 回傳 404，保留舊值並標記 last_known，均未列入精選。詳見 `collection-status.json` 與 `report.md`。

## 今日值得投入的 10 個 repo

| 優先 | Repo | 總星數 | 今日星數 | 快照差 | 相對增長 | 判定 |
|---|---|---:|---:|---:|---:|---|
| 1 | [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) | 1,410 | 133 | —（首次） | — | Deep research |
| 2 | [dream-num/univer](https://github.com/dream-num/univer) | 25,351 | 1,041 | +1,040 | 4.28% | Demo content |
| 3 | [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | 6,845 | 1,220 | +1,268 | 22.74% | Skill candidate |
| 4 | [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | 11,665 | 860 | +837 | 7.73% | Demo content |
| 5 | [Tencent/LoopForge](https://github.com/Tencent/LoopForge) | 1,283 | 484 | +513 | 66.62% | Deep research |
| 6 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 56,729 | 718 | +636 | 1.13% | Demo content |
| 7 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 51,815 | 688 | +614 | 1.20% | Deep research |
| 8 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 9,118 | 248 | —（首次） | — | Skill candidate |
| 9 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 21,676 | — | +17 | 0.08% | Deep research |
| 10 | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 3,700 | — | +4 | 0.11% | Watch |

### 1. NVIDIA/SkillEvaluator｜Deep research

**用途與關聯：** 分層檢查 agent skills，結合品質、語意重複與實際任務對照評測。把 Skills 教學從安裝數量推進到有效性驗證；可替 Adam 課程與辦公自動化 SOP 建立有／無 Skill 的對照實驗。

**動能與維護：** 總星數 1,410；Trending 今日 133；首次入庫，快照增長未知。最近 push：2026-11-15T12:03:33Z；latest release：[v0.9.0](https://github.com/NVIDIA/SkillEvaluator/releases/tag/v0.9.0)，2026-11-13T11:03:05Z。最近更新 5 筆 issue／PR 樣本中，5 筆在觀測近 24 小時內更新；未結 issue／PR 總數 25。

活動證據：[PR #560](https://github.com/NVIDIA/SkillEvaluator/pull/560)，open，最近更新 2026-11-15T12:03:44Z；僅作維護訊號，未推論已發版。

**風險：** 靜態分數不等於任務效益；live evaluation 需要 agent、模型與 sandbox，可能產生費用。

**建議動作：** 驗證一個 wiki 匯入 Skill 是否提高來源引用正確率，先用匿名資料比較任務成功率與成本。

來源：[NVIDIA/SkillEvaluator README](https://github.com/NVIDIA/SkillEvaluator#readme)；本地證據：`snapshots/NVIDIA__SkillEvaluator-activity.json`、`repos.json`。

### 2. dream-num/univer｜Demo content

**用途與關聯：** 可嵌入產品的試算表與文件 SDK，提供公式、編輯、外掛及程式介面。適合 Adam 示範「AI 產生資料→人員在表格覆核→系統回寫」；對 metabiz 報價、營運報表與辦公流程有直接價值。

**動能與維護：** 總星數 25,351；Trending 今日 1041；相較 2026-11-14 快照 +1,040（4.28%）。最近 push：2026-11-15T03:11:29Z；latest release：[v1.5.0](https://github.com/dream-num/univer/releases/tag/v1.5.0)，2026-11-14T10:33:37Z。最近更新 5 筆 issue／PR 樣本中，5 筆在觀測近 24 小時內更新；未結 issue／PR 總數 168。

活動證據：[PR #8209](https://github.com/dream-num/univer/pull/8209)，open，最近更新 2026-11-15T16:11:10Z；僅作維護訊號，未推論已發版。

**風險：** 開源核心與商業 Web／Server／AI SDK 授權不同；Excel 相容性與複雜公式仍須實測。

**建議動作：** 以匿名營運資料製作可編輯週報 demo，再查核匯入匯出與所需商業功能。

來源：[dream-num/univer README](https://github.com/dream-num/univer#readme)；本地證據：`snapshots/dream-num__univer-activity.json`、`repos.json`。

### 3. GoogleChrome/modern-web-guidance-src｜Skill candidate

**用途與關聯：** 維護供 coding agents 使用的現代 Web 平台知識、相容性資料與評測來源。可作 Adam 的 agent 前端課程內容與 Skill 品質案例；改善 metabiz wiki／管理介面的前端產出。

**動能與維護：** 總星數 6,845；Trending 今日 1220；相較 2026-11-14 快照 +1,268（22.74%）。最近 push：2026-11-15T12:09:36Z；latest release：API 未取得 latest release（不等於沒有 tags 或套件版本）。最近更新 5 筆 issue／PR 樣本中，5 筆在觀測近 24 小時內更新；未結 issue／PR 總數 396。

活動證據：[PR #3605](https://github.com/GoogleChrome/modern-web-guidance-src/pull/3605)，open，最近更新 2026-11-15T14:22:31Z；僅作維護訊號，未推論已發版。

**風險：** 此庫是編寫與評測來源，實際安裝入口另有發佈庫；近期修正不代表每個建議均已發佈。

**建議動作：** 取一個舊式前端範例，比較套用 guidance 前後的相容性與可維護性。

來源：[GoogleChrome/modern-web-guidance-src README](https://github.com/GoogleChrome/modern-web-guidance-src#readme)；本地證據：`snapshots/GoogleChrome__modern-web-guidance-src-activity.json`、`repos.json`。

### 4. backnotprop/plannotator｜Demo content

**用途與關聯：** 讓人員標註計畫、文件、HTML、程式差異並將回饋送回 coding agent。適合 Adam 示範需求澄清、審稿與人員覆核；know metabiz wiki 可借用內容審閱回饋模式。

**動能與維護：** 總星數 11,665；Trending 今日 860；相較 2026-11-14 快照 +837（7.73%）。最近 push：2026-11-15T16:14:11Z；latest release：[v0.28.65](https://github.com/backnotprop/plannotator/releases/tag/v0.28.65)，2026-11-15T00:07:22Z。最近更新 5 筆 issue／PR 樣本中，5 筆在觀測近 24 小時內更新；未結 issue／PR 總數 229。

活動證據：[PR #3409](https://github.com/backnotprop/plannotator/pull/3409)，open，最近更新 2026-11-15T16:11:47Z；僅作維護訊號，未推論已發版。

**風險：** 近期開發密集；新 PR 不能當成已發佈能力，分享計畫或差異時也要檢查敏感內容。

**建議動作：** 測試一輪「計畫→標註→agent 修改→覆核」，另追蹤排程 routines PR 是否合併與發版。

來源：[backnotprop/plannotator README](https://github.com/backnotprop/plannotator#readme)；本地證據：`snapshots/backnotprop__plannotator-activity.json`、`repos.json`。

### 5. Tencent/LoopForge｜Deep research

**用途與關聯：** 自架 coding-agent 工作台，結合角色、Docker workspace、SOP、腳本與人工關卡。適合 Adam 的多 agent 課程與 metabiz 內部交付 SOP；可示範研究、實作、覆核與交付責任鏈。

**動能與維護：** 總星數 1,283；Trending 今日 484；相較 2026-11-14 快照 +513（66.62%）。最近 push：2026-11-15T11:05:37Z；latest release：[v0.3.8](https://github.com/Tencent/LoopForge/releases/tag/v0.3.8)，2026-11-12T13:05:58Z。最近更新 5 筆 issue／PR 樣本中，5 筆在觀測近 24 小時內更新；未結 issue／PR 總數 77。

活動證據：[PR #891](https://github.com/Tencent/LoopForge/pull/891)，open，最近更新 2026-11-15T15:51:45Z；僅作維護訊號，未推論已發版。

**風險：** README 說明預設 Docker socket 可控制主機 daemon，不適合作為不可信多租戶隔離；還有維運與模型成本。 GitHub API 授權欄為 NOASSERTION，商用前需查核實際 LICENSE 與依賴條款。

**建議動作：** 先用內建 script／approval 示範驗證關卡、退回與紀錄，再評估接入真實專案。

來源：[Tencent/LoopForge README](https://github.com/Tencent/LoopForge#readme)；本地證據：`snapshots/Tencent__LoopForge-activity.json`、`repos.json`。

### 6. ChromeDevTools/chrome-devtools-mcp｜Demo content

**用途與關聯：** 以 MCP 與 CLI 讓 coding agent 檢視 Chrome、網路請求、console 與效能 trace。適合 Adam 錄製瀏覽器除錯案例；可用於 metabiz wiki、CRM 與辦公表單的前端驗收。

**動能與維護：** 總星數 56,729；Trending 今日 718；相較 2026-11-14 快照 +636（1.13%）。最近 push：2026-11-15T03:06:25Z；latest release：[chrome-devtools-mcp-v1.13.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0)，2026-11-11T12:40:09Z。最近更新 5 筆 issue／PR 樣本中，5 筆在觀測近 24 小時內更新；未結 issue／PR 總數 131。

活動證據：[PR #3497](https://github.com/ChromeDevTools/chrome-devtools-mcp/pull/3497)，open，最近更新 2026-11-15T09:20:09Z；僅作維護訊號，未推論已發版。

**風險：** 連線的瀏覽器內容可被 client 讀取或修改；cookie 匯入等尚未合併 PR 不應視為穩定功能。

**建議動作：** 使用乾淨測試 profile 重現一個效能或表單問題，比較 agent 診斷品質。

來源：[ChromeDevTools/chrome-devtools-mcp README](https://github.com/ChromeDevTools/chrome-devtools-mcp#readme)；本地證據：`snapshots/ChromeDevTools__chrome-devtools-mcp-activity.json`、`repos.json`。

### 7. alibaba/open-code-review｜Deep research

**用途與關聯：** 以確定性分析管線結合 LLM agent 的程式碼審查工具。適合 Adam 示範「規則＋AI」審查方法；可評估 metabiz 自動化腳本與 wiki 工具的 PR 初審。

**動能與維護：** 總星數 51,815；Trending 今日 688；相較 2026-11-14 快照 +614（1.20%）。最近 push：2026-11-15T02:41:14Z；latest release：[v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10)，2026-11-15T02:56:09Z。最近更新 5 筆 issue／PR 樣本中，5 筆在觀測近 24 小時內更新；未結 issue／PR 總數 345。

活動證據：[PR #1943](https://github.com/alibaba/open-code-review/pull/1943)，open，最近更新 2026-11-15T15:33:46Z；僅作維護訊號，未推論已發版。

**風險：** 模型可能誤報、漏報；程式碼傳輸邊界與不同平台取消行為需驗證，不能替代人工審核。

**建議動作：** 用已知缺陷的測試 PR 衡量誤報與漏報，再比較規則及 LLM 各自的貢獻。

來源：[alibaba/open-code-review README](https://github.com/alibaba/open-code-review#readme)；本地證據：`snapshots/alibaba__open-code-review-activity.json`、`repos.json`。

### 8. google-labs-code/stitch-skills｜Skill candidate

**用途與關聯：** 為 Stitch 設計流程提供跨 coding agent 的 skills 與 plugins。適合 Adam 示範設計稿到元件的工作流，並作 metabiz wiki／內部工具介面提案。

**動能與維護：** 總星數 9,118；Trending 今日 248；首次入庫，快照增長未知。最近 push：2026-08-17T20:20:23Z；latest release：[v1.0](https://github.com/google-labs-code/stitch-skills/releases/tag/v1.0)，2026-05-18T18:02:32Z。最近更新 5 筆 issue／PR 樣本中，0 筆在觀測近 24 小時內更新；未結 issue／PR 總數 19。

活動證據：[issue #96](https://github.com/google-labs-code/stitch-skills/issues/96)，open，最近更新 2026-11-06T12:07:03Z；僅作維護訊號，未推論已發版。

**風險：** README 說明並非正式支援的 Google 產品；現有 issue 提及資源下載轉登入頁與 uploader 路徑，須確認目前可重現性。 最近 push 在 2026-08，熱度上升與維護新鮮度需分開判讀。

**建議動作：** 驗證設計資源取得與安裝流程，成功後再選一個 Skill 改編成可教學範例。

來源：[google-labs-code/stitch-skills README](https://github.com/google-labs-code/stitch-skills#readme)；本地證據：`snapshots/google-labs-code__stitch-skills-activity.json`、`repos.json`。

### 9. nashsu/llm_wiki｜Deep research

**用途與關聯：** 將多格式來源增量整理成持續維護的 wiki，包含來源追溯與檢索。直接對應 know metabiz wiki；可作 Adam「文件堆變成可維護知識庫」課程與 AI 辦公教材。

**動能與維護：** 總星數 21,676；Trending 今日 未上榜／未提供；相較 2026-11-14 快照 +17（0.08%）。最近 push：2026-10-21T11:17:29Z；latest release：[v0.6.13](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.13)，2026-10-22T01:21:07Z。最近更新 5 筆 issue／PR 樣本中，0 筆在觀測近 24 小時內更新；未結 issue／PR 總數 302。

活動證據：[issue #155](https://github.com/nashsu/llm_wiki/issues/155)，open，最近更新 2026-11-13T13:22:51Z；僅作維護訊號，未推論已發版。

**風險：** 多格式解析、模型與雲端服務帶來成本及資料邊界；目前有 schema 顯示與 MinerU 連線相關問題。 GitHub API 授權欄為 NOASSERTION，商用前需查核實際 LICENSE 與依賴條款。 最近 push 在 2026-10-21；近期 issue 活動未必表示程式已修復。

**建議動作：** 用少量匿名會議紀錄測試來源追溯、重複匯入、矛盾更新與刪除後的一致性。

來源：[nashsu/llm_wiki README](https://github.com/nashsu/llm_wiki#readme)；本地證據：`snapshots/nashsu__llm_wiki-activity.json`、`repos.json`。

### 10. SamurAIGPT/llm-wiki-agent｜Watch

**用途與關聯：** 以 coding agent skill 將 raw 文件整理成來源頁、實體、概念、綜整與操作紀錄。最貼近 Adam 現有 Skills 與 know metabiz wiki 的 Markdown 流程，可作最小可行的內容整理原型。

**動能與維護：** 總星數 3,700；Trending 今日 未上榜／未提供；相較 2026-11-14 快照 +4（0.11%）。最近 push：2026-11-09T11:35:34Z；latest release：API 未取得 latest release（不等於沒有 tags 或套件版本）。最近更新 5 筆 issue／PR 樣本中，0 筆在觀測近 24 小時內更新；未結 issue／PR 總數 13。

活動證據：[PR #86](https://github.com/SamurAIGPT/llm-wiki-agent/pull/86)，open，最近更新 2026-10-20T12:40:51Z；僅作維護訊號，未推論已發版。

**風險：** 近期活動較慢；尚有避免覆寫既有 Markdown 的未合併 PR，匯入前須驗證可回復性。

**建議動作：** 只在複本測試重複匯入與既有頁保留，觀察維護者是否處理資料覆寫問題。

來源：[SamurAIGPT/llm-wiki-agent README](https://github.com/SamurAIGPT/llm-wiki-agent#readme)；本地證據：`snapshots/SamurAIGPT__llm-wiki-agent-activity.json`、`repos.json`。

## 明日觀察清單（下一期 target_date：2026-11-16）

1. **LoopForge、modern-web-guidance-src、Plannotator**：檢查快照相對增長是否延續，而非只看單日上榜；LoopForge 本期小基期增長特別強，需觀察後續採用與維護。
2. **SkillEvaluator**：建立第二個快照取得真實增長基準；挑一個 Adam 既有 Skill，設計有／無 Skill 的對照任務，記錄正確率、成本與安全檢查差異。
3. **Univer**：確認本期 v1.5.0 的試算表匯出、公式與授權邊界；下一步是小型辦公報表示範，而非直接承諾完整 Office 替代。
4. **Chrome DevTools MCP、OpenCodeReview**：追蹤 cookie/profile 與 Windows 取消行為等 PR 的合併及 release 狀態；以測試環境驗證後才安排教學。
5. **Stitch Skills**：追蹤 [#94](https://github.com/google-labs-code/stitch-skills/issues/94) 的下載轉登入頁問題與 [#96](https://github.com/google-labs-code/stitch-skills/issues/96) 的 uploader 路徑問題；若基本流程仍失敗，暫緩 demo。
6. **know metabiz wiki**：比較 nashsu/llm_wiki 與 llm-wiki-agent 的來源追溯、重複匯入、刪除與矛盾更新；追蹤 [llm-wiki-agent #84](https://github.com/SamurAIGPT/llm-wiki-agent/pull/84) 對既有 Markdown 覆寫的處理。
7. **補充觀察**：[ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) 今日 +393，可觀察 agent 與辦公前端的串接；[ggml-org/ggml](https://github.com/ggml-org/ggml) 今日 +154，暫作本地 AI 基礎設施參考，優先度低於直接可做課程與業務流程的項目。

## 本期執行證據

- 指定十組查詢與執行結果：`collection-status.json`、`collector-limit-10.log`。
- GitHub Trending daily：[原始來源](https://github.com/trending?since=daily)，已保存 HTML 與解析卡片；本期判讀使用直接抓取的快照。
- 6 個 HTTP 404 歷史項目只保留最後已知資料，無法視為本次仍公開可用；不列入推薦，不以其零增長推論市場冷卻。
- 本文分類是編輯決策；`repos.json` 的精選分類已同步，其他歷史項目仍保留自動分類。
