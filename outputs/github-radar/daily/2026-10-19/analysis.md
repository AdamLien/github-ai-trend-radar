# GitHub AI 趨勢雷達｜2026-10-19

## 本期判讀

優先探索 AI 求職流程、跨 agent 記憶與上下文壓縮；同時保留熱度較低但直接對應 know metabiz wiki 的知識整理工具。以下依實作與研究價值安排，不按總 stars 排名。用途與導入建議為本次分析判斷，尚未實際安裝或測試這些專案。

## 觀察範圍與方法

- 目標日期是台北前一個日曆日 2026-10-19；收集始於 2026-10-20 00:10（Asia/Taipei）。數字為執行時觀察，不是回溯重建昨天 00:00–24:00 的日結。
- 使用指定十組查詢、每組 `--limit 10`、每日 Trending 與 README 摘錄；保留歷史追蹤，範圍複核及同名去重後共 349 個專案。
- Trending 來源：[GitHub Trending daily](https://github.com/trending?since=daily)。`stars today` 是該頁當下的滾動觀察；Δ stars 為本次與 2026-10-18 相鄰快照的差，兩者時間窗不同。相對成長＝Δ／前期 stars。未上日榜記為「未觀察到」，不能當成零成長。
- 檢視描述、README 摘錄、`pushed_at`、最新 release 及最近更新的十筆 issues／PR 活動。README 開頭可能只是徽章，不能據此認定完整功能；push 日期也不是品質保證。
- `open_issues` 可能包含 PR，不能當成未修復缺陷數；最近十筆樣本不是完整 issue 吞吐或維護者回應時間。詳見 `issue-evidence.json`。
- 未偵測 API 限流，無須降為 limit 5。四個既有專案遇到 HTTP 404，已在 JSON 標示 `historical_fallback`；其沿用數字不能視為新觀察的零成長，也未納入下列精選。
- 範圍排除、Trending 補入與原始日榜卡片分別見 `scope-review.json`、`trending-evidence.json`；收藏多不等於適合導入。

## 十個值得追蹤的專案

| 專案 | 分類 | 總 stars | stars today | Δ stars | 相對成長 |
|---|---|---:|---:|---:|---:|
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Demo content | 56,105 | 3860 | +4,060 | 7.80% |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Deep research | 11,047 | 666 | +744 | 7.22% |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Deep research | 76,092 | 317 | +318 | 0.42% |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Skill candidate | 55,037 | 607 | +612 | 1.12% |
| [stablyai/orca](https://github.com/stablyai/orca) | Demo content | 97,863 | 1591 | +1,634 | 1.70% |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Reference only | 217,442 | 1310 | +1,263 | 0.58% |
| [morluto/rea](https://github.com/morluto/rea) | Watch | 333,354 | 未觀察到 | +15,126 | 4.75% |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Watch | 76,980 | 564 | +612 | 0.80% |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | Skill candidate | 3,637 | 未觀察到 | +4 | 0.11% |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Watch | 20,786 | 未觀察到 | +39 | 0.19% |

### 1. MadsLorentzen/ai-job-search — Demo content

- **用途：**以 Claude Code 串接職缺評估、履歷調整、求職信與面試準備。
- **動能判讀：**今日熱度及相對成長同時突出，適合用具體任務展示 agent 工作流，優先於只展示工具清單。
- **維護證據：**最近 push `2026-10-19T15:34:30Z`；[最新 release](https://github.com/MadsLorentzen/ai-job-search/releases)：v1.7.2（2026-09-29T18:32:55Z）。開放 issues／PR 欄位 54；[最近活動](https://github.com/MadsLorentzen/ai-job-search/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 2 筆、PR 8 筆，最近 issue 更新 `2026-10-19T13:50:42Z`。
- **風險與限制：**履歷含個資，產生的經歷與職缺對應需要人工查核；實際使用前需確認資料流與寄送動作。
- **與 Adam／metabiz 的關聯：**Adam 可製作「個人 AI 助理處理一段完整工作」課程與短影音；將同樣的來源整理、文件草稿與人工確認流程延伸至 AI 辦公。know metabiz wiki 可收錄流程設計與驗收條件。
- **來源：**[專案與 README](https://github.com/MadsLorentzen/ai-job-search)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 2. akitaonrails/ai-memory — Deep research

- **用途：**替 coding CLI 保存長期記憶，支援不同 agent 工具之間交接上下文。
- **動能判讀：**相對成長高，總 stars 遠低於大型平台仍有強烈動能；值得以交接成功率與記憶正確性做研究。
- **維護證據：**最近 push `2026-10-19T15:46:18Z`；[最新 release](https://github.com/akitaonrails/ai-memory/releases)：v3.1.1（2026-10-17T18:09:02Z）。開放 issues／PR 欄位 27；[最近活動](https://github.com/akitaonrails/ai-memory/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 0 筆、PR 10 筆，最近 issue 更新 `未在樣本觀察到`。
- **風險與限制：**持久記憶可能留下過期結論或敏感資料；目前最近十筆活動樣本均為 PR，不能據此推斷沒有 issue 或問題已解決。
- **與 Adam／metabiz 的關聯：**Adam 可示範跨 coding agent 接手任務；AI 辦公可研究會議到待辦的交接，know metabiz wiki 則需要記憶來源、有效日期與修訂紀錄。
- **來源：**[專案與 README](https://github.com/akitaonrails/ai-memory)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 3. headroomlabs-ai/headroom — Deep research

- **用途：**在工具輸出、日誌、檔案及 RAG 片段進入 LLM 前做上下文壓縮，提供程式庫、proxy 與 MCP 整合。
- **動能判讀：**同時有 Trending 與正向快照增量；題材的價值在可量測的成本及答案品質，不以 stars 規模決定優先度。
- **維護證據：**最近 push `2026-10-17T18:29:50Z`；[最新 release](https://github.com/headroomlabs-ai/headroom/releases)：v0.41.0（2026-10-14T22:46:09Z）。開放 issues／PR 欄位 483；[最近活動](https://github.com/headroomlabs-ai/headroom/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 2 筆、PR 8 筆，最近 issue 更新 `2026-10-19T15:32:28Z`。
- **風險與限制：**README 摘錄開頭以圖片與徽章為主；壓縮比例與品質維持屬專案宣稱，本次未重現。壓縮可能移除關鍵例外與引用依據。
- **與 Adam／metabiz 的關聯：**Adam 可做相同辦公任務的 token／成本／正確率對照內容；know metabiz wiki 可用有標準答案的文件測試檢索壓縮後的引用完整度。
- **來源：**[專案與 README](https://github.com/headroomlabs-ai/headroom)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 4. HKUDS/CLI-Anything — Skill candidate

- **用途：**將軟體操作能力包裝成可供 agent 呼叫的 CLI 介面。
- **動能判讀：**Trending 動能仍強，但最近 push 與 release 早於本次觀察數週至數月，需將關注熱度與維護速度分開看。
- **維護證據：**最近 push `2026-09-22T02:01:29Z`；[最新 release](https://github.com/HKUDS/CLI-Anything/releases)：v0.4.0（2026-06-25T15:17:49Z）。開放 issues／PR 欄位 200；[最近活動](https://github.com/HKUDS/CLI-Anything/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 4 筆、PR 6 筆，最近 issue 更新 `2026-10-19T03:31:56Z`。
- **風險與限制：**不同軟體的覆蓋與命令可靠度需要逐項驗證；具副作用的工具必須定義失敗處理與復原步驟。
- **與 Adam／metabiz 的關聯：**Adam 可挑一項熟悉的辦公軟體做實作課；先把單一任務轉為有輸入、輸出與驗收條件的 Skill，know metabiz wiki 保存支援版本及操作證據。
- **來源：**[專案與 README](https://github.com/HKUDS/CLI-Anything)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 5. stablyai/orca — Demo content

- **用途：**以桌面、行動及遠端介面管理多個 coding agent。
- **動能判讀：**Trending、快照增量及當期 release 都有訊號，適合展示工作分派與結果檢查，而非僅比較總 stars。
- **維護證據：**最近 push `2026-10-19T16:16:18Z`；[最新 release](https://github.com/stablyai/orca/releases)：v1.4.230（2026-10-19T06:30:00Z）。開放 issues／PR 欄位 8,600；[最近活動](https://github.com/stablyai/orca/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 3 筆、PR 7 筆，最近 issue 更新 `2026-10-19T16:20:15Z`。
- **風險與限制：**open_issues 數量高且包含 PR，不能直接當成缺陷數；多 agent 同時操作專案可能出現衝突、成本失控及遠端權限問題。
- **與 Adam／metabiz 的關聯：**Adam 可錄製兩個 agent 分工再人工整合的內容；AI 辦公可評估任務看板與覆核節點，know metabiz wiki 可保存各任務決策與責任邊界。
- **來源：**[專案與 README](https://github.com/stablyai/orca)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 6. anomalyco/opencode — Reference only

- **用途：**開源 coding agent，作為開發工作流與 CLI 體驗的比較基準。
- **動能判讀：**絕對增量與 Trending 仍強，但相對成長低於本期的小型記憶工具；保留為基準，避免每期都由大型工具佔據研究資源。
- **維護證據：**最近 push `2026-10-19T16:08:16Z`；[最新 release](https://github.com/anomalyco/opencode/releases)：v1.19.3（2026-10-16T12:31:52Z）。開放 issues／PR 欄位 4,635；[最近活動](https://github.com/anomalyco/opencode/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 9 筆、PR 1 筆，最近 issue 更新 `2026-10-19T16:17:31Z`。
- **風險與限制：**模型供應商設定、工具執行權限與版本相容性都會影響體驗；本次未實測其任務成功率。
- **與 Adam／metabiz 的關聯：**Adam 課程可比較讀碼、修改及驗證的基本流程；AI 辦公自動化只借鏡任務分解與覆核方法，know metabiz wiki 記錄可重現環境與工具差異。
- **來源：**[專案與 README](https://github.com/anomalyco/opencode)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 7. morluto/rea — Watch

- **用途：**以 agent 協助逆向分析應用行為及原生二進位檔。
- **動能判讀：**本期快照增量最大且相對成長顯著，但未在當次 Trending 日榜觀察到；需要續查增量的持續性及對應功能變化。
- **維護證據：**最近 push `2026-10-19T16:16:43Z`；[最新 release](https://github.com/morluto/rea/releases)：rea-agents-6.7.0（2026-10-18T07:45:18Z）。開放 issues／PR 欄位 1,252；[最近活動](https://github.com/morluto/rea/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 5 筆、PR 5 筆，最近 issue 更新 `2026-10-19T16:19:57Z`。
- **風險與限制：**高增量可能受宣傳或資料時間差影響，不能據此推論真實採用。逆向分析有較高技術門檻，需使用有權分析的樣本並驗證結果。
- **與 Adam／metabiz 的關聯：**對 Adam 進階工程課有研究價值；與一般 AI 辦公及 know metabiz wiki 的直接關聯較低，可先收錄 agent 工具鏈與證據保存方式，不列為導入優先項。
- **來源：**[專案與 README](https://github.com/morluto/rea)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 8. ruvnet/ruflo — Watch

- **用途：**組合多 agent 協作、記憶、RAG 與 coding 工具的 orchestration harness。
- **動能判讀：**Trending 與快照成長方向一致，也有近期 push／release；先驗證一個小流程再決定是否深入多 agent 架構。
- **維護證據：**最近 push `2026-10-19T16:08:32Z`；[最新 release](https://github.com/ruvnet/ruflo/releases)：v3.57.0（2026-10-17T22:38:55Z）。開放 issues／PR 欄位 1,063；[最近活動](https://github.com/ruvnet/ruflo/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 5 筆、PR 5 筆，最近 issue 更新 `2026-10-19T15:55:43Z`。
- **風險與限制：**整合面廣會增加安裝、狀態同步與除錯成本；README 摘錄不足以證明協作可靠性或節省成本。
- **與 Adam／metabiz 的關聯：**Adam 可做單 agent 與多 agent 同任務對照；AI 辦公可挑資料整理加報告草稿，know metabiz wiki 必須保存各步輸入來源與失敗案例。
- **來源：**[專案與 README](https://github.com/ruvnet/ruflo)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 9. SamurAIGPT/llm-wiki-agent — Skill candidate

- **用途：**將來源文件持續整理為互相連結的 Markdown wiki，提供 coding agent 可使用的知識整理流程。
- **動能判讀：**星數增量小，但 README 直接描述 Skill 與 raw／wiki 工作法，和 know metabiz wiki 的需求最接近，因此保留高相關低熱度題材。
- **維護證據：**最近 push `2026-10-19T08:55:19Z`；[最新 release](https://github.com/SamurAIGPT/llm-wiki-agent/releases)：本次 API 未取得最新 release，不能據此判定從未發布。開放 issues／PR 欄位 12；[最近活動](https://github.com/SamurAIGPT/llm-wiki-agent/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 5 筆、PR 5 筆，最近 issue 更新 `2026-09-24T13:43:30Z`。
- **風險與限制：**本次 API 未取得最新 release；自動整理可能誤引來源、覆寫既有結論或漏掉矛盾，需要來源鏈、差異審查與人工確認。
- **與 Adam／metabiz 的關聯：**Adam 可示範從原始資料到 wiki 頁面的完整課程；AI 辦公可處理會議／SOP，know metabiz wiki 可先試一組公開文件並檢查引用與重複匯入。
- **來源：**[專案與 README](https://github.com/SamurAIGPT/llm-wiki-agent)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

### 10. nashsu/llm_wiki — Watch

- **用途：**跨平台桌面應用，將文件增量組織成可持續維護、互相連結的 wiki。
- **動能判讀：**增量溫和且近期 push／release 較早；以桌面操作的教學便利性與知識維護需求補足熱榜視野。
- **維護證據：**最近 push `2026-09-28T01:43:23Z`；[最新 release](https://github.com/nashsu/llm_wiki/releases)：v0.6.12（2026-09-28T02:58:13Z）。開放 issues／PR 欄位 286；[最近活動](https://github.com/nashsu/llm_wiki/issues?q=sort%3Aupdated-desc)十筆樣本含 issue 8 筆、PR 2 筆，最近 issue 更新 `2026-10-19T04:47:58Z`。
- **風險與限制：**API 授權欄位為 NOASSERTION，導入前需要閱讀完整授權條文；另需確認文件儲存、同步、備份與來源引用品質。
- **與 Adam／metabiz 的關聯：**Adam 可用圖形介面展示知識庫持續更新；AI 辦公適合評估非工程使用者的文件整理體驗，know metabiz wiki 可與 CLI Skill 比較人工維護負擔。
- **來源：**[專案與 README](https://github.com/nashsu/llm_wiki)；完整量測欄位見 `repos.json`，issue 時間證據見 `issue-evidence.json`。

## 明日觀察清單

1. **ai-job-search、ai-memory：**比較相同口徑的 Δ 與相對成長，觀察熱度是否持續；以一份公開履歷樣本、一次跨 agent 任務交接規劃可重現測試。
2. **headroom：**建立包含關鍵例外、引用及長 JSON 的固定測試集，同時量測 token 與答案正確率，不直接採信宣傳比例。
3. **CLI-Anything：**確認近期 issue／PR 是否對應新版本或支援修正，挑一個可復原的辦公操作評估 Skill 化。
4. **Orca、OpenCode、Ruflo：**對照 release 變更與最近 issue，觀察多 agent 任務衝突、復原與成本，先做小型隔離示範。
5. **rea：**再次核對異常大的快照增量與實際功能改變，若只有熱度上升則維持 Watch。
6. **llm-wiki-agent、llm_wiki：**比較同一批公開來源的引用保留、矛盾標示、重複匯入、刪除來源與授權；以 know metabiz wiki 的維護成本決定下一步。
7. **四個 404 追蹤項：**確認是否改名、轉私有或移除；持續失聯時停止拿沿用的 stars 作新成長比較。

## 執行紀錄

- Collector：limit 10 成功；API rate limit 未偵測到；limit 5 未執行。
- 四個 HTTP 404：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。
- 本文來源均作為觀察資料處理；本次只收集與分析，未執行來源專案提供的安裝或操作內容。
