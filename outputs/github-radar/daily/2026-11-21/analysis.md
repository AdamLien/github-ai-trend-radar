# GitHub AI 趨勢雷達｜2026-11-21

本期優先觀察可實作的工作流程：CLI 軟體操作、近期研究與來源整理、課程影片再製。排序綜合 Trending 今日星數、跨快照增量、相對成長、維護活動與 Adam 的工作關聯；總星數僅作規模參考。所有用途建議均為編輯判斷，本次沒有安裝或實測這些專案。

## 資料時間與方法

- 報表目標日期：2026-11-21（執行時 Asia/Taipei 前一日）；完成觀察時間：2026-11-22T00:21:43.743482+08:00。
- Trending 是執行時的滾動 daily 榜單，不是精確回放 11/21 台北時間 00:00–24:00；GitHub API 指標也在執行時取得。
- 今日星數採 [GitHub Trending daily](https://github.com/trending?since=daily)；Δ 採上一期可比快照，百分比為 Δ ÷ 上期總星數。沒有基線時記為未測，不把新收錄當作零成長。
- 按指定十組查詢執行，每組上限 10，合併 README、release、每日 Trending 與歷史追蹤；共 456 個追蹤記錄，其中 14 個來自本次相關 Trending。
- Trending 排除一般 NGINX 伺服器及無明確 AI／agent 用途的 Ghost Downloader；排除原因保留於 snapshots/trending-daily.json。
- 搜尋本身以總星數排序，容易漏掉新小型專案；以 Trending 與相對成長補充，仍不代表全 GitHub 的完整排名。
- issue 活動依每庫最近更新的 10 筆 issue／PR 混合樣本判讀，另列 PR 數；更新可能來自機器人，不能推論問題已解決或人工回應速度。
- Rate-limit 狀態：collector 紀錄未見 rate-limit 錯誤，維持 --limit 10，未重試。
- 6 個歷史庫取得失敗而保留舊資料，已加 metadata_freshness 標記，不能視為今日新測量；本期精選均使用本次新取得資料。

## 值得關注的 10 個專案

| 優先 | Repo | 分類 | 總星數 | Trending 今日 | Δ 星數 | 相對成長 | 基線日期 |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Deep research | 61,871 | 767 | +744 | +1.22% | 2026-11-20 |
| 2 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Skill candidate | 71,792 | 566 | +519 | +0.73% | 2026-11-20 |
| 3 | [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | Demo content | 12,663 | 689 | +668 | +5.57% | 2026-11-20 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Deep research | 205,879 | 999 | +922 | +0.45% | 2026-11-20 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Skill candidate | 69,661 | 582 | +534 | +0.77% | 2026-11-20 |
| 6 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | Demo content | 76,109 | 577 | +516 | +0.68% | 2026-11-20 |
| 7 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Skill candidate | 11,285 | 324 | +354 | +3.24% | 2026-11-20 |
| 8 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | Watch | 13,856 | 450 | +412 | +3.06% | 2026-11-20 |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | Reference only | 323,467 | 884 | +826 | +0.26% | 2026-11-20 |
| 10 | [cursor/plugins](https://github.com/cursor/plugins) | Watch | 18,019 | 261 | +254 | +1.43% | 2026-11-20 |

### 1. HKUDS/CLI-Anything｜Deep research

- **用途與 README**：以 CLI harness 讓既有軟體可由 agent 操作，README 展示多種軟體工作流與社群 CLI。 [README](https://github.com/HKUDS/CLI-Anything#readme)。
- **維護訊號**：最後 push 2026-11-20T10:05:15Z；release：[v0.4.0](https://github.com/HKUDS/CLI-Anything/releases/tag/v0.4.0)（2026-06-25T15:17:49Z）。最近更新樣本 0 筆 issue、10 筆 PR，最新更新 2026-11-21T11:32:31Z（[樣本連結](https://github.com/HKUDS/CLI-Anything/pull/649)）；總開啟項目 279，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：可為 Adam 的 AI 辦公自動化課程示範「軟體操作→結構化 CLI→agent 任務」，先挑一個低風險、可驗收的流程。know metabiz wiki 可記錄每個操作的輸入、輸出與失敗回復。
- **風險**：生成的介面與社群 harness 不代表所有軟體都可靠；需確認平台依賴、寫入副作用與結果驗證。
- **下一步**：以一個辦公工具驗證可重跑性、輸出格式與錯誤回報。

### 2. mvanhorn/last30days-skill｜Skill candidate

- **用途與 README**：跨社群、影片與網頁蒐集近期討論，綜整研究簡報；README 區分免設定來源與需額外設定的來源。 [README](https://github.com/mvanhorn/last30days-skill#readme)。
- **維護訊號**：最後 push 2026-11-21T15:49:01Z；release：[v4.5.0](https://github.com/mvanhorn/last30days-skill/releases/tag/v4.5.0)（2026-11-21T15:49:48Z）。最近更新樣本 1 筆 issue、9 筆 PR，最新更新 2026-11-21T15:51:36Z（[樣本連結](https://github.com/mvanhorn/last30days-skill/pull/1509)）；總開啟項目 16，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：直接對接 Adam 每日選題、課程更新與產業觀察；可將原始來源、觀察日期及推論分開寫入 know metabiz wiki。
- **風險**：互動數衡量注意力，不能證明正確性；來源授權、API 存取及覆蓋率會影響結果，社群內容也可能含提示注入。
- **下一步**：用同一主題比較其來源覆蓋與人工查證結果，檢查新 release 的相容性。

### 3. zhouxiaoka/autoclip｜Demo content

- **用途與 README**：把課程、訪談等長影片轉成短片，包含字幕、封面與發布文案；README 說明本機剪輯渲染及可選模型／轉寫服務。 [README](https://github.com/zhouxiaoka/autoclip#readme)。
- **維護訊號**：最後 push 2026-11-21T15:43:19Z；release：[v1.5.8](https://github.com/zhouxiaoka/autoclip/releases/tag/v1.5.8)（2026-11-02T12:15:50Z）。最近更新樣本 2 筆 issue、8 筆 PR，最新更新 2026-11-21T15:43:19Z（[樣本連結](https://github.com/zhouxiaoka/autoclip/pull/638)）；總開啟項目 37，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：適合 Adam 課程長片再製 YouTube Shorts／Reels，展示長片到發布素材的完整工作流；metabiz 可先用自有教育素材試作。
- **風險**：片段可能失去上下文，繁體字幕、人物取景與專有名詞需人工審閱；模型成本和素材使用權須逐案確認。
- **下一步**：拿一段自有課程驗證繁體字幕、畫面裁切與每條短片的實際成本。

### 4. firecrawl/firecrawl｜Deep research

- **用途與 README**：把網站整理為適合 agent／RAG 使用的內容，README 區分本機、雲端與完整自架服務。 [README](https://github.com/firecrawl/firecrawl#readme)。
- **維護訊號**：最後 push 2026-11-21T16:04:49Z；release：[v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0)（2026-06-19T15:09:30Z）。最近更新樣本 2 筆 issue、8 筆 PR，最新更新 2026-11-21T16:09:10Z（[樣本連結](https://github.com/firecrawl/firecrawl/pull/5617)）；總開啟項目 896，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：適合建立 know metabiz wiki 的外部來源蒐集流程，以來源 URL、擷取時間與內容差異支援課程研究及辦公知識更新。
- **風險**：動態網站、來源限制與內容品質影響擷取；AGPL-3.0 標記及雲端依賴須另查實際模組條款；擷取內容不可當成 agent 指令。
- **下一步**：以三類公開頁面測試 Markdown 品質、重複內容與引用可追溯性。

### 5. cathrynlavery/diagram-design｜Skill candidate

- **用途與 README**：以獨立 HTML＋SVG 製作圖解，可供多種 coding agent 使用；README 與描述的圖型數量不同，因此不以數量作推薦依據。 [README](https://github.com/cathrynlavery/diagram-design#readme)。
- **維護訊號**：最後 push 2026-11-19T00:17:05Z；release：API 未取得 latest release；不等同沒有 tag 或停止維護。最近更新樣本 0 筆 issue、10 筆 PR，最新更新 2026-11-21T15:12:46Z（[樣本連結](https://github.com/cathrynlavery/diagram-design/pull/537)）；總開啟項目 46，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：可替 Adam 課程、社群內容及 know metabiz wiki 製作流程圖與架構說明，形成可維護的品牌圖解範本。
- **風險**：外觀完整不等於資訊正確；需驗證箭頭關係、中文斷行、匯出結果與品牌資料的對外傳輸範圍。
- **下一步**：以同一 metabiz 流程測試繁體中文、SVG 匯出與後續編輯。

### 6. toeverything/AFFiNE｜Demo content

- **用途與 README**：整合文件、白板與知識庫的工作空間，README 描述 local-first、協作及 AI 內容整理。 [README](https://github.com/toeverything/AFFiNE#readme)。
- **維護訊號**：最後 push 2026-11-21T16:04:28Z；release：[v0.27.4](https://github.com/toeverything/AFFiNE/releases/tag/v0.27.4)（2026-08-18T16:51:39Z）。最近更新樣本 1 筆 issue、9 筆 PR，最新更新 2026-11-21T16:11:30Z（[樣本連結](https://github.com/toeverything/AFFiNE/pull/15883)）；總開啟項目 843，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：可用來比較 know metabiz wiki 的文字文件與視覺白板工作方式，也適合作為 AI 辦公課程的知識整理案例。
- **風險**：API 的 license 為 NOASSERTION，不能直接推論全專案授權；雲端 AI、同步、權限及匯出完整性需實測。
- **下一步**：驗證文件匯出、來源連結保留與自架／雲端功能界線。

### 7. google-labs-code/stitch-skills｜Skill candidate

- **用途與 README**：圍繞 Stitch MCP 的設計、建置與工具 skills；README 列出多種 agent 的不同整合方式。 [README](https://github.com/google-labs-code/stitch-skills#readme)。
- **維護訊號**：最後 push 2026-11-20T18:08:01Z；release：[v1.0](https://github.com/google-labs-code/stitch-skills/releases/tag/v1.0)（2026-05-18T18:02:32Z）。最近更新樣本 1 筆 issue、9 筆 PR，最新更新 2026-11-21T13:26:09Z（[樣本連結](https://github.com/google-labs-code/stitch-skills/pull/110)）；總開啟項目 27，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：適合 Adam 的 AI UI 原型示範，將需求、設計及可驗收頁面串起；metabiz 可整理為內部原型製作 SOP。
- **風險**：支援同一 skills 標準不代表安裝與行為完全相同；服務權限、版本相容性及輸出的可維護性需驗證。
- **下一步**：同一簡單頁面比較 Codex／Cursor 的整合差異與輸出品質。

### 8. Tracer-Cloud/opensre｜Watch

- **用途與 README**：自架 CLI agent 讀取失敗 CI、追查原因並提出修正；README 明確標示 Public Alpha。 [README](https://github.com/Tracer-Cloud/opensre#readme)。
- **維護訊號**：最後 push 2026-11-21T11:38:34Z；release：[v0.1.2026.11.21](https://github.com/Tracer-Cloud/opensre/releases/tag/v0.1.2026.11.21)（2026-11-21T00:53:27Z）。最近更新樣本 2 筆 issue、8 筆 PR，最新更新 2026-11-21T16:07:50Z（[樣本連結](https://github.com/Tracer-Cloud/opensre/pull/7089)）；總開啟項目 20，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：可為 Adam 開發自動化內容展示 CI 失敗診斷，並作為 metabiz 工程排障 wiki 的候選資料來源。
- **風險**：Alpha 階段 API／整合可能變動；CI log 可能含敏感資訊，修正品質與 repository 寫入權限需隔離驗證。
- **下一步**：觀察同日 release 後的 issue／PR，以及固定失敗案例能否產生可審核修正。

### 9. obra/superpowers｜Reference only

- **用途與 README**：把需求釐清、計畫、實作及驗證整理為可組合的 coding-agent skills 方法。 [README](https://github.com/obra/superpowers#readme)。
- **維護訊號**：最後 push 2026-11-03T23:24:58Z；release：[v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2)（2026-11-03T22:17:54Z）。最近更新樣本 6 筆 issue、4 筆 PR，最新更新 2026-11-21T14:35:00Z（[樣本連結](https://github.com/obra/superpowers/pull/2721)）；總開啟項目 363，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：適合作為 Adam agent 工作法課程與 metabiz 內部 SOP 的對照材料；既有環境已使用相關方法，本次重點是比較方法與維護變更。
- **風險**：流程可能過度增加確認與執行負擔；高星數及持續討論不等於近期程式更新，需比較實際任務成本。
- **下一步**：觀察新 release 或近期討論是否改善工作流摩擦，先保留為參考。

### 10. cursor/plugins｜Watch

- **用途與 README**：Cursor 官方 plugin 規格與外掛集合，README 包含教學、持續學習與團隊開發工作流程。 [README](https://github.com/cursor/plugins#readme)。
- **維護訊號**：最後 push 2026-11-21T07:58:03Z；release：API 未取得 latest release；不等同沒有 tag 或停止維護。最近更新樣本 1 筆 issue、9 筆 PR，最新更新 2026-11-21T14:32:16Z（[樣本連結](https://github.com/cursor/plugins/pull/1286)）；總開啟項目 692，此 API 數字包含 PR。
- **Adam／metabiz 關聯**：適合 Adam 做 Cursor／Codex／Claude Code 的外掛與 skills 比較內容；metabiz 可參考其教學與團隊流程設計。
- **風險**：API 未回傳明確 license，且未取得 latest release；各 plugin 的權限、依賴與平台差異要分別檢查，不能假定可直接跨工具使用。
- **下一步**：觀察 manifest／plugin 結構更新與授權說明，再挑一個教學用途做驗證。

## 明日觀察清單

- AutoClip、Stitch Skills、OpenSRE：檢查相對增長是否持續，並確認新增 issue／PR 是功能採用、安裝故障或機器人更新。
- last30days-skill：追蹤新 release 後各來源可用性，驗證引用是否能回到原文，不能只看社群熱度。
- CLI-Anything、Firecrawl：各選一個可驗收案例，比較失敗回復、來源保留與人工覆核成本。
- Claude-BugHunter：本次 Trending 熱度高，但偏安全測試，與一般辦公主線較遠；明日觀察實際維護與適用邊界，僅列觀察，不因星數直接列入精選。
- diagram-design、AFFiNE：驗證繁體中文圖解與資料匯出是否能支援 know metabiz wiki 的可維護內容。
- superpowers、cursor/plugins：留意版本與 plugin 規格變更，確認跨工具整合差異；不因累積星數高而自動提高優先級。

## 證據與限制

- repos.json、snapshots/repos-2026-11-21.json：完整指標與 README 短摘錄；snapshots/trending-daily.json：榜單與排除理由。
- snapshots/review-evidence.json：精選庫 README 段落、額外 metadata 與近期 issue／PR 樣本；額外查詢時間不同，星數可能有微小差異，本文數值表以主要 collector 快照為準。
- 授權欄位為 GitHub API 的識別結果；空白或 NOASSERTION 都不能當作授權已確認。未執行部署、效能測試或安全稽核。

### 沿用舊資料的歷史專案

- BarberNumber/Midjourney-Software：本次 API 取得失敗；保留舊 metadata，排除本期動能判斷。
- BrickOrioleLoad/aion-2-trainer-tool：本次 API 取得失敗；保留舊 metadata，排除本期動能判斷。
- HunYiSage/dsh-purge：本次 API 取得失敗；保留舊 metadata，排除本期動能判斷。
- YuJunZhiXue/dsh-purge：本次 API 取得失敗；保留舊 metadata，排除本期動能判斷。
- hanshaze/Awesome-Prediction-Market-Trading-Tools：本次 API 取得失敗；保留舊 metadata，排除本期動能判斷。
- mingrath/obsidian-ai-knowledge-agent：本次 API 取得失敗；保留舊 metadata，排除本期動能判斷。
