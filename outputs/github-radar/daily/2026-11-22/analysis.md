# GitHub AI 趨勢雷達｜2026-11-22

> 本次執行於台北時間 2026-11-23，資料夾日期為前一日 2026-11-22。API 與 Trending 為執行時即時觀測，並非回溯重建 11 月 22 日整日行情。

## 判讀方法

先看 Trending 今日增星、相對成長，再看快照增量、推送時間、README、release 與近期 issue／PR，並依 Adam 課程、內容、AI 辦公自動化及 know metabiz wiki 的實際用途安排研究順序。下列順序為編輯優先級，沒有只依總星數排序。

- 今日增星來自 [GitHub Trending Daily](https://github.com/trending?since=daily) 的觀測時滑動視窗。
- 快照增量 = 本次總星數 − 2026-11-21 快照；相對成長 = 增量 ÷ 前次星數。兩個視窗不完全相同，不能把增量都稱為今日增星。
- 未上 Trending 用「—」，不代表增星為零；首次追蹤沒有有效基準時用「未測」。
- open_issues 是 GitHub 的 issue／PR 合計指標，不能直接當成未解決 bug 數；另抓取最近更新的 5 筆 issue／PR 判讀維護活動。
- README 僅為短摘錄，可能被徽章占滿；未進行安裝、效能測試或正式導入驗證。授權風險依 API 欄位提出待查項目。

## 本日值得投入的 10 個專案

| 優先 | 專案 | 總星數 | Trending 今日 | 快照增量 | 相對成長 | 建議 |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 11,801 | 516 | 516 | 4.57% | Skill candidate |
| 2 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | 14,270 | 395 | 414 | 2.99% | Deep research |
| 3 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 62,567 | 687 | 696 | 1.12% | Deep research |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 72,527 | 673 | 735 | 1.02% | Skill candidate |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 70,148 | 513 | 487 | 0.70% | Demo content |
| 6 | [cursor/plugins](https://github.com/cursor/plugins) | 18,333 | 301 | 314 | 1.74% | Skill candidate |
| 7 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 206,741 | 910 | 862 | 0.42% | Deep research |
| 8 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 76,640 | 537 | 531 | 0.70% | Watch |
| 9 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 21,820 | — | 19 | 0.09% | Deep research |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | 323,951 | 785 | 484 | 0.15% | Watch |

### 1. google-labs-code/stitch-skills｜Skill candidate

**用途：**把 Stitch MCP 的設計流程封裝為 Agent Skills；README 列出 Codex、Claude Code、Cursor 等相容工具。

**動能與維護：**小基數的今日成長值得優先驗證；最新 PR 涉及安裝驗證失敗處理，顯示跨環境可靠性仍在改善。 最近推送：2026-11-20；API 最新 release：v1.0（2026-05-18）；open_issues 合計 28。
最近更新樣本：[#111](https://github.com/google-labs-code/stitch-skills/pull/111)（2026-11-22T15:17:58Z，PR，open）。

**風險：**需驗證 MCP 連線、帳號依賴與安裝腳本；有 release 不代表近期主線修改已進入該版本。

**Adam／metabiz 關聯：**Adam 可示範設計稿到前端的跨 agent 課程，延伸 metabiz 官網及 AI 辦公介面原型。

來源：[專案與 README](https://github.com/google-labs-code/stitch-skills#readme)、[release](https://github.com/google-labs-code/stitch-skills/releases)、[近期 issue／PR](https://github.com/google-labs-code/stitch-skills/issues?q=sort%3Aupdated-desc)。

### 2. Tracer-Cloud/opensre｜Deep research

**用途：**自架 CI/CD 故障診斷 agent；README 描述讀取失敗 run、追查原因並產生可供審查的修正。

**動能與維護：**同日 release、推送及近期 PR 同時存在，較只有 star 熱度更值得研究。 最近推送：2026-11-22；API 最新 release：v0.1.2026.11.22（2026-11-22）；open_issues 合計 20。
最近更新樣本：[#7097](https://github.com/Tracer-Cloud/opensre/pull/7097)（2026-11-22T15:09:14Z，PR，closed）。

**風險：**模型誤診、CI 權限及修正品質需實測；PR 標題中的修復不能推定所有使用版本都已安全。

**Adam／metabiz 關聯：**可做 Adam 開發自動化課程案例，驗證 metabiz CI 失敗到人工審核修復的完整流程。

來源：[專案與 README](https://github.com/Tracer-Cloud/opensre#readme)、[release](https://github.com/Tracer-Cloud/opensre/releases)、[近期 issue／PR](https://github.com/Tracer-Cloud/opensre/issues?q=sort%3Aupdated-desc)。

### 3. HKUDS/CLI-Anything｜Deep research

**用途：**把既有軟體能力轉為 agent 可操作的 CLI 介面。

**動能與維護：**今日熱門且近期 PR 包含 LibreOffice Calc 公式命名空間修正；適合用真實辦公任務驗證，而非僅展示安裝。 最近推送：2026-11-20；API 最新 release：v0.4.0（2026-06-25）；open_issues 合計 285。
最近更新樣本：[#649](https://github.com/HKUDS/CLI-Anything/pull/649)（2026-11-22T11:33:19Z，PR，open）。

**風險：**軟體相依、版本差異及檔案寫入副作用；未合併的 Calc PR 尚不能視為可用修正。

**Adam／metabiz 關聯：**優先製作試算表與文件操作的 AI 辦公自動化課程，將可重現步驟整理成 metabiz 內部操作 wiki。

來源：[專案與 README](https://github.com/HKUDS/CLI-Anything#readme)、[release](https://github.com/HKUDS/CLI-Anything/releases)、[近期 issue／PR](https://github.com/HKUDS/CLI-Anything/issues?q=sort%3Aupdated-desc)。

### 4. mvanhorn/last30days-skill｜Skill candidate

**用途：**跨 Reddit、X、YouTube、HN 與網頁蒐集近期議題並彙整摘要的研究 skill。

**動能與維護：**本日有新版與推送；近期 PR 涉及搜尋運算子和 webhook 憑證遮罩，需一併看資料品質與操作可靠度。 最近推送：2026-11-22；API 最新 release：v4.6.0（2026-11-22）；open_issues 合計 17。
最近更新樣本：[#1560](https://github.com/mvanhorn/last30days-skill/pull/1560)（2026-11-22T15:20:22Z，PR，open）。

**風險：**平台 API 可用性、費用、取樣偏差及來源可信度；自動摘要需回查原始來源。

**Adam／metabiz 關聯：**Adam 可把 GitHub 雷達延伸為選題研究、短影音腳本和課程需求探索，將可引用摘要收進 know metabiz wiki。

來源：[專案與 README](https://github.com/mvanhorn/last30days-skill#readme)、[release](https://github.com/mvanhorn/last30days-skill/releases)、[近期 issue／PR](https://github.com/mvanhorn/last30days-skill/issues?q=sort%3Aupdated-desc)。

### 5. cathrynlavery/diagram-design｜Demo content

**用途：**輸出自含 HTML 與 SVG 圖解的 coding-agent skill，可用於流程圖及架構說明。

**動能與維護：**README 與 description 的圖型數量不同，應實測輸出而非轉述宣傳數字；近期 PR 持續修整文件與驗證工具。 最近推送：2026-11-22；API 最新 release：未取得；open_issues 合計 45。
最近更新樣本：[#539](https://github.com/cathrynlavery/diagram-design/pull/539)（2026-11-22T15:14:46Z，PR，open）。

**風險：**字型、繁中排版及 SVG 匯出品質需檢查；目前未取得 latest release，不代表沒有開發活動。

**Adam／metabiz 關聯：**直接用來製作 Adam 課程的 MCP／RAG 流程圖、AI 辦公 SOP 與 know metabiz wiki 架構圖。

來源：[專案與 README](https://github.com/cathrynlavery/diagram-design#readme)、[release](https://github.com/cathrynlavery/diagram-design/releases)、[近期 issue／PR](https://github.com/cathrynlavery/diagram-design/issues?q=sort%3Aupdated-desc)。

### 6. cursor/plugins｜Skill candidate

**用途：**Cursor 官方外掛與規格集合；README 顯示每個 plugin 有獨立 manifest，並含教學與持續學習案例。

**動能與維護：**今日熱門、近期有推送與外掛擴充 PR；相對成長比僅看累積規模更有辨識力。 最近推送：2026-11-22；API 最新 release：未取得；open_issues 合計 690。
最近更新樣本：[#547](https://github.com/cursor/plugins/pull/547)（2026-11-22T14:37:18Z，PR，open）。

**風險：**GitHub license 欄位未標明，複用前需逐插件確認；生態平台差異、外部 SaaS 權限及記憶寫入需審核。

**Adam／metabiz 關聯：**適合 Adam 比較 Cursor、Claude Code、Codex 的 plugin／skill 工作流，提取 AI 辦公學習回顧與知識維護的設計參考。

來源：[專案與 README](https://github.com/cursor/plugins#readme)、[release](https://github.com/cursor/plugins/releases)、[近期 issue／PR](https://github.com/cursor/plugins/issues?q=sort%3Aupdated-desc)。

### 7. firecrawl/firecrawl｜Deep research

**用途：**提供網頁搜尋、擷取與資料來源存取，作為 agent 與知識庫的資料匯入層。

**動能與維護：**今日 star 絕對增量高，但基數大，需與相對成長並看；近期 PR 涉及私有位址防護與 robots crawl-delay。 最近推送：2026-11-22；API 最新 release：v2.11.0（2026-06-19）；open_issues 合計 914。
最近更新樣本：[#5970](https://github.com/firecrawl/firecrawl/pull/5970)（2026-11-22T15:17:46Z，PR，open）。

**風險：**AGPL-3.0 的產品整合方式需另行核對；抓取合規、來源更新及內網存取控制需驗證，未合併 PR 不等於已修復。

**Adam／metabiz 關聯：**可用於 know metabiz wiki 的來源匯入實驗，也能示範網站轉結構化資料的辦公自動化內容。

來源：[專案與 README](https://github.com/firecrawl/firecrawl#readme)、[release](https://github.com/firecrawl/firecrawl/releases)、[近期 issue／PR](https://github.com/firecrawl/firecrawl/issues?q=sort%3Aupdated-desc)。

### 8. toeverything/AFFiNE｜Watch

**用途：**整合文件、白板與規劃的知識工作空間，README 主打 local-first 與隱私。

**動能與維護：**今日熱門且有近期推送與 PR；latest release 較舊，應分清主線維護與穩定版交付。 最近推送：2026-11-22；API 最新 release：v0.27.4（2026-08-18）；open_issues 合計 842。
最近更新樣本：[#15885](https://github.com/toeverything/AFFiNE/pull/15885)（2026-11-22T14:40:13Z，PR，closed）。

**風險：**license 為 NOASSERTION，需查實際授權；協作同步、備份、權限與既有 wiki 的搬遷成本仍需驗證。

**Adam／metabiz 關聯：**適合 Adam 的 AI 辦公工具比較；可評估作為 know metabiz wiki 的編輯與視覺規劃介面。

來源：[專案與 README](https://github.com/toeverything/AFFiNE#readme)、[release](https://github.com/toeverything/AFFiNE/releases)、[近期 issue／PR](https://github.com/toeverything/AFFiNE/issues?q=sort%3Aupdated-desc)。

### 9. nashsu/llm_wiki｜Deep research

**用途：**把文件增量整理為持久、互相連結的 wiki，與每次重新檢索回答的 RAG 流程形成比較案例。

**動能與維護：**非本次 Trending 候選，因與 know metabiz wiki 高度相關保留；近期有原始來源讀取 PR 活動，但推送與 release 較舊。 最近推送：2026-10-21；API 最新 release：v0.6.13（2026-10-22）；open_issues 合計 301。
最近更新樣本：[#759](https://github.com/nashsu/llm_wiki/pull/759)（2026-11-22T10:48:59Z，PR，closed）。

**風險：**license 為 NOASSERTION；生成知識可能失真、來源追溯與衝突更新需測；closed PR 也不等於已合併或已發布。

**Adam／metabiz 關聯：**優先用公開 SOP 測試增量更新與引用追溯，形成 Adam 的 RAG 對比持久 wiki 課程及 metabiz 導入研究。

來源：[專案與 README](https://github.com/nashsu/llm_wiki#readme)、[release](https://github.com/nashsu/llm_wiki/releases)、[近期 issue／PR](https://github.com/nashsu/llm_wiki/issues?q=sort%3Aupdated-desc)。

### 10. obra/superpowers｜Watch

**用途：**把 coding-agent 開發方法整理為可組合 skills 與工作流程。

**動能與維護：**今日仍熱門，但累積規模很大；近期 issue 提到 skill 是否實際被觸發，採用效果須看任務結果。 最近推送：2026-11-03；API 最新 release：v7.0.2（2026-11-03）；open_issues 合計 362。
最近更新樣本：[#2728](https://github.com/obra/superpowers/issues/2728)（2026-11-22T13:40:42Z，issue，open）。

**風險：**工作流可能增加上下文與時間成本；自動套用規範需符合現有專案，不能把文件中的指令直接當執行授權。

**Adam／metabiz 關聯：**Adam 可錄製同題任務的品質與成本比較，萃取適合公司 AI 開發 SOP 的方法，再納入 know metabiz wiki。

來源：[專案與 README](https://github.com/obra/superpowers#readme)、[release](https://github.com/obra/superpowers/releases)、[近期 issue／PR](https://github.com/obra/superpowers/issues?q=sort%3Aupdated-desc)。

## 明日觀察清單（2026-11-23）

1. **Stitch Skills、OpenSRE**：確認今日約 4.57%、2.99% 的相對成長是否延續，對照新 release 和安裝／CI 回報；優先排 30 分鐘公開範例實測。
2. **CLI-Anything**：追蹤 LibreOffice Calc PR 是否合併並進入可安裝版本；用公開試算表檢查公式保留與檔案可重開。
3. **last30days-skill**：確認新版來源可用率與引用品質，檢查 webhook 遮罩修正的實際交付狀態，評估接入 Adam 選題流程。
4. **llm_wiki、AFFiNE、Firecrawl**：以同一組公開文件比較匯入、更新、引用與備份；追蹤原始來源存取和抓取防護修正，不直接放入公司機密文件。
5. **diagram-design、cursor/plugins、superpowers**：觀察繁中示範成果、安裝相容性與技能觸發可靠度；用同題任務比較時間、成本與可重現性。
6. **elementalsouls/Claude-BugHunter**：今日 Trending +1,721，熱度高但用途偏資安研究，本日未列投入前十；僅追蹤維護、授權與可信案例，不執行安全測試工具。

## 收集狀態

已使用指定 10 組查詢、`--limit 10`、Trending Daily 與 README 收集完成。共取得 457 個專案，人工排除 18 個明顯離題或無法核實的歷史項目，保留 439 個；其中 14 個來自本次 Trending Daily。

未觀察到 GitHub API rate-limit 錯誤，未啟用 `--limit 5` 重跑。保留的 4 個失效歷史專案使用舊 metadata，已標記 `metadata_stale` 並清空快照增量，不列入 mover 表；本篇 10 個候選均非回退資料。

範圍排除理由見 `scope-review.json`，近期 issue／PR 見 `activity-evidence.json`，原始 Trending 卡片見 `trending-daily-source.json`，執行狀態見 `run-status.json`。
