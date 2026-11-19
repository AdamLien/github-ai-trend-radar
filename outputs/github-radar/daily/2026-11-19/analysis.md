# GitHub AI 趨勢雷達｜2026-11-19

## 觀測口徑與判讀

- 目標日期為 Asia/Taipei 昨日 2026-11-19；實際蒐集在 2026-11-20 執行。這是指定歸檔日的即時快照，不是重建昨日午夜的歷史榜單。
- 搜尋採指定十組關鍵字，初始每組 10 筆，合併即時 [GitHub Trending daily](https://github.com/trending?since=daily)、README 與歷史追蹤清單。篩選 AI、MCP、Skills、agent、LLM、RAG、知識庫與開發自動化；排除通用 NGINX 與下載器。
- 排序綜合 stars today、相較 2026-11-18 快照的 star delta／相對增幅、程式 push、README、release、議題／PR 活動及 Adam 使用情境；總星數僅代表既有規模。這份順序是編輯優先級，不是客觀綜合分數。
- stars today 為 Trending 的滾動顯示值，與快照差值的時間窗不同。相對增幅 =（本次星數 − 前次星數）／前次星數；前次未收錄標示無基準，不以零增長代替。
- 下列星數、README 摘錄及近期議題取自 review-evidence.json 的獨立補查；repos.json 為完整收集器較晚完成的快照，可能有少量即時星數差。近期活動只抽查最近更新的五個 issue／PR，不代表解決率或完整活動統計；open issues 計數亦包含 PR。
- API 限流狀態：未發生；--limit 10 成功，未啟用 --limit 5。詳見 collection-status.json。

## 今日精選（10 個）

### 1. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) — Deep research

- 用途：彙整多平台近期討論與來源，形成研究摘要。
- 動能：總星數 **70,612**；stars today **952**；快照差值 **+865**；相對增幅 **1.24%**。
- 維護證據：最近 push `2026-11-19T08:23:36Z`；最新 release `v4.3.2`（2026-11-17T15:56:44Z）；open issues／PR 23。 [最近活動](https://github.com/mvanhorn/last30days-skill/pull/1471)：fix(reddit): free Reddit floor, one hydrator and honest path health（2026-11-19T15:25:30Z）。
- 風險：平台存取、付費 API 與來源偏差會影響覆蓋；近期 Reddit 路徑與 X 搜尋有修正，摘要仍須逐項核對。
- Adam／metabiz 關聯：最適合把 Adam 每日選題與課程更新做成可查證的研究流程；辦公自動化可用於產業情報，know metabiz wiki 則保留原文連結與觀察日期。
- 建議下一步：先用同一題材比較公開原始來源與輸出，量測連結有效率。

### 2. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) — Skill candidate

- 用途：將 Stitch MCP 設計能力封裝成可複用的 agent skills 與 plugins。
- 動能：總星數 **10,621**；stars today **303**；快照差值 **+302**；相對增幅 **2.93%**。
- 維護證據：最近 push `2026-11-18T05:00:25Z`；最新 release `v1.0`（2026-05-18T18:02:32Z）；open issues／PR 21。 [最近活動](https://github.com/google-labs-code/stitch-skills/pull/100)：docs: add missing site-md skill to README（2026-11-18T08:55:29Z）。
- 風險：需確認外部設計服務與各 host 的安裝差異；近期 uploader 修復 PR 尚開啟，不能把宣稱相容視為已驗證。
- Adam／metabiz 關聯：適合 Adam 的設計到網站課程與 demo；可將 AI 辦公表單、metabiz 服務頁的設計迭代整理成 wiki 操作教材。
- 建議下一步：先以一個簡單管理頁測試設計交接與生成結果。

### 3. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — Demo content

- 用途：把既有軟體能力包裝為 agent 可使用的命令列介面。
- 動能：總星數 **60,337**；stars today **899**；快照差值 **+867**；相對增幅 **1.46%**。
- 維護證據：最近 push `2026-09-22T02:01:29Z`；最新 release `v0.4.0`（2026-06-25T15:17:49Z）；open issues／PR 265。 [最近活動](https://github.com/HKUDS/CLI-Anything/pull/671)：feat: add DaVinci Resolve CLI (standalone repo)（2026-11-19T16:08:11Z）。
- 風險：最新 push 早於近期議題活動；3MF 的 NaN／無窮值輸入與覆寫問題仍有開啟議題，應以可拋棄素材驗證。
- Adam／metabiz 關聯：適合 Adam 展示 AI 操作桌面軟體與辦公自動化；know metabiz wiki 可記錄輸入、輸出及人工複核步驟。
- 建議下一步：選擇單一匯出工作，測試格式正確性與失敗時的檔案完整性。

### 4. [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) — Demo content

- 用途：將課程、訪談與播客長片重製成短片、字幕、封面及發布文案。
- 動能：總星數 **11,039**；stars today **110**；快照差值 **+267**；相對增幅 **2.48%**。
- 維護證據：最近 push `2026-11-19T14:33:37Z`；最新 release `v1.5.8`（2026-11-02T12:15:50Z）；open issues／PR 45。 [最近活動](https://github.com/zhouxiaoka/autoclip/pull/620)：优化首次出片流程：新首屏、一键配模型和 2×2 默认模型布局（2026-11-19T14:33:38Z）。
- 風險：README 指出雲端模型按量計費；近期有模型連線、專案恢復與診斷修復，尚須驗證字幕品質與素材授權。
- Adam／metabiz 關聯：直接對應 Adam 課程內容再利用與 Shorts；辦公端可整理內訓重點，wiki 保存素材來源及剪輯決策。
- 建議下一步：用一段自有課程測試繁中字幕、片段邊界及實際費用。

### 5. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — Skill candidate

- 用途：以 HTML＋SVG 產出自含圖解，供多種 coding agent 使用。
- 動能：總星數 **68,463**；stars today **332**；快照差值 **+305**；相對增幅 **0.45%**。
- 維護證據：最近 push `2026-11-19T00:17:05Z`；最新 release `未取得`（無發布日期）；open issues／PR 38。 [最近活動](https://github.com/cathrynlavery/diagram-design/pull/190)：feat: host-aware install doctor for Playwright, Cowork, marketplace, and Pi（2026-11-19T06:06:43Z）。
- 風險：描述稱 45 類，README 稱 51 類，文件口徑尚需確認；近期安裝檢查與 selector 驗證仍有修正 PR。
- Adam／metabiz 關聯：可將 Adam 課程的 agent／RAG 流程視覺化，也適合 AI 辦公 SOP 與 know metabiz wiki 的架構圖。
- 建議下一步：用相同 SOP 生成一張圖，檢查繁中文字、排版與離線開啟。

### 6. [obra/superpowers](https://github.com/obra/superpowers) — Reference only

- 用途：以可組合 skills 形成 coding agent 的完整軟體開發方法。
- 動能：總星數 **321,823**；stars today **2029**；快照差值 **+1,999**；相對增幅 **0.63%**。
- 維護證據：最近 push `2026-11-03T23:24:58Z`；最新 release `v7.0.2`（2026-11-03T22:17:54Z）；open issues／PR 360。 [最近活動](https://github.com/obra/superpowers/issues/2716)：subagent-driven-development: the fix-loop model escalation (rounds 4-5) has no stated scope, so the escalated implementer carries on into later tasks（2026-11-19T02:11:42Z）。
- 風險：熱度最高不代表應整套導入；近期議題反映 skill 過度觸發及子 agent 任務範圍延伸，需避免不必要流程成本。
- Adam／metabiz 關聯：適合作為 Adam agent 開發課程的工作流對照；辦公自動化可借鏡驗證關卡，wiki 收錄可採用的流程原則。
- 建議下一步：比較小任務導入前後的耗時、步驟數與交付品質。

### 7. [cursor/plugins](https://github.com/cursor/plugins) — Watch

- 用途：提供 Cursor plugin 規格與官方整合範例。
- 動能：總星數 **17,475**；stars today **383**；快照差值 **+370**；相對增幅 **2.16%**。
- 維護證據：最近 push `2026-11-19T06:52:20Z`；最新 release `未取得`（無發布日期）；open issues／PR 686。 [最近活動](https://github.com/cursor/plugins/issues/1173)：pstack: poteto-mode can't start from a stored prompt (task cards, scheduled or headless sessions)（2026-11-19T15:25:07Z）。
- 風險：未取得明確 SPDX 授權與正式 release；近期議題包含 headless 啟動、模型識別及 Windows 換行相容問題。
- Adam／metabiz 關聯：可支援 Adam 跨 coding agent 的插件課程與 demo；辦公工具整合及 wiki 記憶更新可參考其結構。
- 建議下一步：追蹤 changelog 請求與自動執行相容性，再決定是否製作教學。

### 8. [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) — Deep research

- 用途：提供網頁搜尋、擷取與知識資料供應能力。
- 動能：總星數 **203,800**；stars today **795**；快照差值 **無基準**；相對增幅 **無基準**。
- 維護證據：最近 push `2026-11-19T15:42:50Z`；最新 release `v2.11.0`（2026-06-19T15:09:30Z）；open issues／PR 833。 [最近活動](https://github.com/firecrawl/firecrawl/pull/5839)：feat(api): purge a deleted team's change tracking rows from Bigtable（2026-11-19T15:45:16Z）。
- 風險：AGPL-3.0 與商用服務模式須依實際部署確認；最新正式 release 早於近期 push，瀏覽器相容性與資料刪除仍有 PR。
- Adam／metabiz 關聯：適合 Adam 教學展示來源到 RAG 的流程；AI 辦公情報與 know metabiz wiki 可增加更新來源及引用。
- 建議下一步：以少量公開網頁驗證擷取完整度、引用與變更追蹤。

### 9. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) — Deep research

- 用途：從文件持續建構互相連結的持久 wiki。
- 動能：總星數 **21,771**；stars today **未上榜／無值**；快照差值 **+25**；相對增幅 **0.11%**。
- 維護證據：最近 push `2026-10-21T11:17:29Z`；最新 release `v0.6.13`（2026-10-22T01:21:07Z）；open issues／PR 300。 [最近活動](https://github.com/nashsu/llm_wiki/pull/667)：fix: caption images in the configured output language（2026-11-16T23:20:13Z）。
- 風險：授權顯示 NOASSERTION，最新 push 與 release 較舊；仍有語言輸出及 Windows 外部解析服務連線議題，不能據此推定企業級協作可用。
- Adam／metabiz 關聯：與 know metabiz wiki 最直接相關，可作 Adam「RAG 與持久知識整理」課程對照；辦公端適合測試文件增量整理。
- 建議下一步：驗證增量更新、來源追溯、繁中輸出與刪除後的知識一致性。

### 10. [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) — Watch

- 用途：結合文件、白板與規劃的本機優先知識工作空間。
- 動能：總星數 **74,923**；stars today **170**；快照差值 **無基準**；相對增幅 **無基準**。
- 維護證據：最近 push `2026-11-18T09:58:41Z`；最新 release `v0.27.4`（2026-08-18T16:51:39Z）；open issues／PR 841。 [最近活動](https://github.com/toeverything/AFFiNE/issues/13903)：[Feature Request]: Use Kanban tile space better（2026-11-19T08:59:00Z）。
- 風險：NOASSERTION 需要閱讀實際授權；近期 CPU／GPU 負載及自帶模型連線問題仍開啟，不宜只憑總星數決定遷移。
- Adam／metabiz 關聯：可作 Adam AI 辦公課程的知識工作台比較，並評估 know metabiz wiki 的編輯體驗及匯入匯出。
- 建議下一步：以小型文件集測試資源消耗、匯出可攜性與 AI provider 連線。

## 明日觀察清單

- last30days-skill：確認跨平台來源可用性與修復落地，追蹤熱度能否延續。
- stitch-skills：觀察相對增長是否持續，以及 plugin uploader 與跨 host 安裝問題。
- AutoClip：追蹤新版本、模型設定及專案恢復問題，優先驗證繁中字幕實作。
- CLI-Anything：關注 3MF 數值輸入防護與原生匯出修正；議題活躍不等於已合併。
- diagram-design：追蹤圖型數量文件一致性與安裝診斷，確認適合課程素材輸出。
- llm_wiki／AFFiNE：評估增量知識、來源可追溯與搬移可攜性，維持小規模評估。
- elementalsouls/Claude-BugHunter：Trending 顯示 +1,353 stars today；屬資安技能包，本日未列入通用辦公優先十選。後續只評估授權測試場景的教學價值。

## 來源與限制

主要來源為各專案 GitHub metadata、README、latest release 與最近更新議題；可重查 review-evidence.json、trending-daily.json、repos.json 與 snapshots/。用途與價值判斷屬本報告分析，README 宣稱未視為已完成實測。沒有執行候選專案、安裝其套件或採納其文字為指令。


## 本次執行品質註記

- 初始候選 454；人工排除 8 個非主題項目，保留 446 個。
- --limit 10 完成，未發生 GitHub API 限流，未啟用 --limit 5。
- 6 個歷史項目回應 404，保留舊資料並標記 metadata_freshness=last_known_404；不應將其零差值視為實測無成長。名單見 scope-review.json。
- 實際蒐集時間 2026-11-20T00:23:37.443565+08:00，資料歸檔日為 2026-11-19。
