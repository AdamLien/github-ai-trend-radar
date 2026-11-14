# GitHub AI 趨勢雷達｜2026-11-14

## 日期、範圍與方法

目標日期是 Asia/Taipei 的前一曆日 2026-11-14，實際執行日為 2026-11-15；執行時間見 collection-status.json。GitHub Trending daily 和 API 數字都是本次抓取時的觀測，不是 11/14 台北零時至午夜的歷史重建。

執行指定十組搜尋、合併 [GitHub Trending daily](https://github.com/trending?since=daily)、README 與歷史追蹤後，本日保留 416 個範圍內專案，其中 12 個由當次 Trending 帶入。搜尋以總 stars 排序只是候選入口；以下九項依 stars today、快照增量、相對成長、近期 push、README、release 與 issue／PR 證據，以及 Adam 的實際用途選出，沒有依總 stars 排名。

快照增量比較 2026-11-13 的觀測；相對成長＝本次 stars 增量 ÷ 前次 stars。觀測間隔未必正好 24 小時，首次觀測記為未知；未上 Trending 的「—」不等於零成長。stars today、快照增量和相對成長是不同指標，不可互相替代。

人工複核排除 13 個明顯不符範圍的工具或通用資料庫，詳見 scope-exclusions.json；Trending 原始頁面與卡片資料保存在 snapshots/。另有改名或轉址造成的 14 筆重複紀錄，已依 canonical full_name 合併來源並保留較高的星數觀測，詳見 canonical-deduplication.json。歷史追蹤專案不代表今日 Trending 入榜。

未偵測到 GitHub API 限流；指定十組查詢均以 --limit 10 執行，未觸發降至 5 的重試。

主收集器對 6 個歷史專案沿用上次已知資料，其中 1 個因 README 與 AI 描述不符而排除，本日保留 5 個沿用項目。清單見 collection-status.json；不可把沿用資料視為最新實測。

近期活動另以更新時間抽樣每庫十筆 issue／PR，保存在 snapshots/selected-repo-evidence.json，內含完整 README。open_issues_count 可能包含 PR，並非缺陷數；十筆樣本也不是全天活動量、解決率或維護者回應速度。本次未安裝、執行或重現各專案的功能與效能宣稱。

## 今日精選

| 專案 | 總 stars | Trending stars today | 快照增量 | 相對成長 | 判定 |
| --- | ---: | ---: | ---: | ---: | --- |
| [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | 5,577 | 1,225 | +1,146 | 25.86% | Skill candidate |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 51,201 | 897 | +865 | 1.72% | Demo content |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 56,093 | 673 | +790 | 1.43% | Skill candidate |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | 10,828 | 412 | +495 | 4.79% | Demo content |
| [dream-num/univer](https://github.com/dream-num/univer) | 24,311 | 495 | +578 | 2.44% | Deep research |
| [Tencent/LoopForge](https://github.com/Tencent/LoopForge) | 770 | 101 | 未知（首次觀測） | 未知 | Deep research |
| [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 30,204 | 462 | +102 | 0.34% | Watch |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 119,879 | 227 | +245 | 0.20% | Reference only |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 21,659 | — | +18 | 0.08% | Watch |

### 1. GoogleChrome/modern-web-guidance-src｜Skill candidate

**用途：**將現代網頁平台、瀏覽器相容性與最佳實務整理成 coding agent 可用的 Skills；此處是內容撰寫、校準和評估的來源庫。

**動能：**總 stars 5,577；相較 2026-11-13 增加 +1,146 stars，相對成長 25.86%；Trending stars today 為 1,225。

**維護證據：**最近 push：2026-11-14T14:28:09Z；最新 release：API 未取得最新正式 release；不能據此斷言未發版。API 開啟項目數 390（可能包含 PR）。近期十筆抽樣為 3 筆 issue、7 筆 PR；例：[#3505](https://github.com/GoogleChrome/modern-web-guidance-src/pull/3505)（open，2026-11-14T14:30:58Z）；[#3232](https://github.com/GoogleChrome/modern-web-guidance-src/pull/3232)（open，2026-11-14T14:30:07Z）。

**Adam／metabiz 關聯：**Adam 可用同一個前端任務比較加入指引前後的品質，製作 Skills 評估課程；metabiz 辦公介面可採用經驗證的規範，know metabiz wiki 保存來源、版本與驗收案例。

**風險：**來源庫與發佈庫不同；README 指向 GoogleChrome/modern-web-guidance，不能把本庫直接等同可安裝套件。近期 #3505 正在釐清 Built-in AI 的瀏覽器專屬細節，跨瀏覽器能力仍需驗證。

證據：[README](https://github.com/GoogleChrome/modern-web-guidance-src#readme)、[releases](https://github.com/GoogleChrome/modern-web-guidance-src/releases)、[issues](https://github.com/GoogleChrome/modern-web-guidance-src/issues)。

### 2. alibaba/open-code-review｜Demo content

**用途：**以確定性規則和 LLM agent 共同審查程式碼，產生行級回饋與多語言檢查結果。

**動能：**總 stars 51,201；相較 2026-11-13 增加 +865 stars，相對成長 1.72%；Trending stars today 為 897。

**維護證據：**最近 push：2026-11-14T12:41:52Z；最新 release：v1.13.9（2026-11-13T09:47:57Z）。API 開啟項目數 336（可能包含 PR）。近期十筆抽樣為 3 筆 issue、7 筆 PR；例：[#1935](https://github.com/alibaba/open-code-review/issues/1935)（open，2026-11-14T16:00:06Z）；[#1934](https://github.com/alibaba/open-code-review/issues/1934)（open，2026-11-14T13:54:41Z）。

**Adam／metabiz 關聯：**Adam 可製作規則與模型審查互補的實驗內容，以刻意植入的錯誤檢驗漏報和誤報；metabiz 可評估 PR 檢查流程，wiki 保存測試案例與判斷依據。

**風險：**README 的規模與精準度宣稱未經本次獨立重現。近期 #1925 處理 workspace review 的 resume 支援，顯示中斷恢復也應納入測試；審查成功執行不等於所有問題皆被找到。

證據：[README](https://github.com/alibaba/open-code-review#readme)、[releases](https://github.com/alibaba/open-code-review/releases)、[issues](https://github.com/alibaba/open-code-review/issues)。

### 3. ChromeDevTools/chrome-devtools-mcp｜Skill candidate

**用途：**透過 MCP server 或 CLI 讓 coding agent 操作真實 Chrome、讀取網路與 console、擷取畫面並分析效能。

**動能：**總 stars 56,093；相較 2026-11-13 增加 +790 stars，相對成長 1.43%；Trending stars today 為 673。

**維護證據：**最近 push：2026-11-13T17:28:37Z；最新 release：chrome-devtools-mcp-v1.13.0（2026-11-11T12:40:09Z）。API 開啟項目數 122（可能包含 PR）。近期十筆抽樣為 0 筆 issue、10 筆 PR；例：[#3488](https://github.com/ChromeDevTools/chrome-devtools-mcp/pull/3488)（open，2026-11-14T14:14:58Z）；[#3487](https://github.com/ChromeDevTools/chrome-devtools-mcp/pull/3487)（open，2026-11-14T10:59:24Z）。

**Adam／metabiz 關聯：**適合 Adam 的瀏覽器驗收課程與可重用 Skill：檢查 AI 生成表單、辦公流程與網頁效能；know metabiz wiki 可保存重現步驟、畫面和驗收證據。

**風險：**README 表明 MCP client 能讀取與修改瀏覽器資料，且部分效能工具可能將 trace URL 送往 CrUX；示範應使用隔離測試帳號。近期 #3487 涉及 autoConnect 權限錯誤，環境相容性需實測；本次近期樣本全為 PR，不能推論 issue 回應品質。

證據：[README](https://github.com/ChromeDevTools/chrome-devtools-mcp#readme)、[releases](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases)、[issues](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues)。

### 4. backnotprop/plannotator｜Demo content

**用途：**提供本機瀏覽器審閱介面，讓使用者標註計畫、規格、HTML 和程式碼差異，再把回饋交回 agent。

**動能：**總 stars 10,828；相較 2026-11-13 增加 +495 stars，相對成長 4.79%；Trending stars today 為 412。

**維護證據：**最近 push：2026-11-14T16:08:49Z；最新 release：v0.28.64（2026-11-13T17:24:36Z）。API 開啟項目數 226（可能包含 PR）。近期十筆抽樣為 1 筆 issue、9 筆 PR；例：[#3357](https://github.com/backnotprop/plannotator/pull/3357)（open，2026-11-14T16:08:50Z）；[#3347](https://github.com/backnotprop/plannotator/pull/3347)（open，2026-11-14T16:07:34Z）。

**Adam／metabiz 關聯：**Adam 可示範先審計畫與產物再批准執行，將人機協作延伸到報價草稿、網頁與辦公文件；metabiz wiki 保存審閱理由與核准版本。

**風險：**近期 #3331、#3347 仍在調整語意差異與審閱版面，需驗證呈現是否遺漏重要修改；支援多個 agent 不代表每種整合都已在本次測試。

證據：[README](https://github.com/backnotprop/plannotator#readme)、[releases](https://github.com/backnotprop/plannotator/releases)、[issues](https://github.com/backnotprop/plannotator/issues)。

### 5. dream-num/univer｜Deep research

**用途：**以可擴充的試算表、文件、公式、渲染和命令系統建立可編輯的辦公介面，並讓應用程式或 agent 操作內容。

**動能：**總 stars 24,311；相較 2026-11-13 增加 +578 stars，相對成長 2.44%；Trending stars today 為 495。

**維護證據：**最近 push：2026-11-14T12:44:53Z；最新 release：v1.5.0（2026-11-14T10:33:37Z）。API 開啟項目數 165（可能包含 PR）。近期十筆抽樣為 0 筆 issue、10 筆 PR；例：[#8168](https://github.com/dream-num/univer/pull/8168)（open，2026-11-14T14:04:47Z）；[#8206](https://github.com/dream-num/univer/pull/8206)（open，2026-11-14T12:51:03Z）。

**Adam／metabiz 關聯：**與 Adam 的 AI 辦公自動化主題直接相關，可研究報表整理、資料校對與操作後人工覆核；metabiz 可探索內部文件介面，wiki 保存開源與商業功能對照。

**風險：**Apache-2.0 僅涵蓋本庫開源核心；README 說明商業插件、Server SDK 與部分 AI SDK 另行分發授權。展示能力不等於預設開源能力；需測試大型工作簿、公式與檔案往返相容性。

證據：[README](https://github.com/dream-num/univer#readme)、[releases](https://github.com/dream-num/univer/releases)、[issues](https://github.com/dream-num/univer/issues)。

### 6. Tencent/LoopForge｜Deep research

**用途：**自架 coding agent 協作工作區，以角色、Docker sandbox、可重複 SOP 和人工審批串起軟體交付，也提供本機工作流。

**動能：**總 stars 770；沒有前次可比較基線，快照增量與相對成長未知；Trending stars today 為 101。

**維護證據：**最近 push：2026-11-14T16:12:59Z；最新 release：v0.3.8（2026-11-12T13:05:58Z）。API 開啟項目數 249（可能包含 PR）。近期十筆抽樣為 6 筆 issue、4 筆 PR；例：[#832](https://github.com/Tencent/LoopForge/pull/832)（open，2026-11-14T16:09:11Z）；[#831](https://github.com/Tencent/LoopForge/issues/831)（open，2026-11-14T16:06:54Z）。

**Adam／metabiz 關聯：**Adam 可研究如何把一次性的 agent 提示變成可驗收 SOP；metabiz 可借鏡任務分派、執行證據與人工關卡，know metabiz wiki 保存 SOP 與執行紀錄的連結。

**風險：**這是偏軟體交付的編排平台，轉用一般辦公需額外整合。自架仍須處理 sandbox、工具權限和執行憑證；#810 的慢 heartbeat 問題及 #829 的 runner 修正，提醒需測試長任務與失敗恢復。

證據：[README](https://github.com/Tencent/LoopForge#readme)、[releases](https://github.com/Tencent/LoopForge/releases)、[issues](https://github.com/Tencent/LoopForge/issues)。

### 7. QwenLM/qwen-code｜Watch

**用途：**開源 coding agent，README 涵蓋終端機、編輯器、桌面、瀏覽器和聊天入口，並提供 SDK 與整合能力。

**動能：**總 stars 30,204；相較 2026-11-13 增加 +102 stars，相對成長 0.34%；Trending stars today 為 462。

**維護證據：**最近 push：2026-11-14T16:13:15Z；最新 release：sdk-typescript-v0.1.33（2026-11-13T01:14:28Z）。API 開啟項目數 2275（可能包含 PR）。近期十筆抽樣為 3 筆 issue、7 筆 PR；例：[#17250](https://github.com/QwenLM/qwen-code/pull/17250)（open，2026-11-14T16:11:18Z）；[#17266](https://github.com/QwenLM/qwen-code/issues/17266)（open，2026-11-14T16:10:15Z）。

**Adam／metabiz 關聯：**Adam 可用固定測試題比較不同 coding agent 的任務完成率與操作成本；metabiz 可評估開發流程與聊天入口，wiki 保存安裝條件、版本及評測紀錄。

**風險：**近期 #17266 回報 Windows Web Shell 產生大量 cmd 視窗與重疊 Git 輪詢，跨平台穩定性值得觀察。API latest release 可能是 SDK 元件版本，不能直接當主 CLI 版本；不同入口的權限也需分別驗證。

證據：[README](https://github.com/QwenLM/qwen-code#readme)、[releases](https://github.com/QwenLM/qwen-code/releases)、[issues](https://github.com/QwenLM/qwen-code/issues)。

### 8. JuliusBrussee/caveman｜Reference only

**用途：**透過精簡 agent 輸出、工具結果與上下文等方式減少 token 使用，提供 Skills、CLI 與中介整合。

**動能：**總 stars 119,879；相較 2026-11-13 增加 +245 stars，相對成長 0.20%；Trending stars today 為 227。

**維護證據：**最近 push：2026-11-14T07:52:12Z；最新 release：v4.1.0（2026-11-08T04:17:28Z）。API 開啟項目數 88（可能包含 PR）。近期十筆抽樣為 7 筆 issue、3 筆 PR；例：[#1530](https://github.com/JuliusBrussee/caveman/pull/1530)（open，2026-11-14T08:29:26Z）；[#1529](https://github.com/JuliusBrussee/caveman/pull/1529)（open，2026-11-14T08:09:20Z）。

**Adam／metabiz 關聯：**可作為 Adam 的 token 成本實驗素材，以相同任務比較費用、正確率與回覆可讀性；metabiz 辦公 SOP 可借鏡降低噪音，但 wiki 應保留完整原始依據。

**風險：**README 的節省數字來自專案自身測試，不能當普遍效益；壓縮可能損失限制條件。README 說明 CLI 預設有使用統計，壓縮檔案也可能送往設定的模型供應商；近期另有 CLI panic 與設定讀寫問題整理。

證據：[README](https://github.com/JuliusBrussee/caveman#readme)、[releases](https://github.com/JuliusBrussee/caveman/releases)、[issues](https://github.com/JuliusBrussee/caveman/issues)。

### 9. nashsu/llm_wiki｜Watch

**用途：**將文件逐步整理為持久、互相連結的 wiki，README 提供來源追溯、增量匯入、原始來源查詢與選用向量搜尋。

**動能：**總 stars 21,659；相較 2026-11-13 增加 +18 stars，相對成長 0.08%；本次未見 Trending stars today。

**維護證據：**最近 push：2026-10-21T11:17:29Z；最新 release：v0.6.13（2026-10-22T01:21:07Z）。API 開啟項目數 302（可能包含 PR）。近期十筆抽樣為 6 筆 issue、4 筆 PR；例：[#155](https://github.com/nashsu/llm_wiki/issues/155)（open，2026-11-13T13:22:51Z）；[#850](https://github.com/nashsu/llm_wiki/pull/850)（open，2026-11-13T08:51:12Z）。

**Adam／metabiz 關聯：**直接對應 know metabiz wiki 的知識整理情境；Adam 可比較持久 wiki 與即時 RAG 在更新、追溯和回答品質上的差異，作為 AI 知識管理課程內容。

**風險：**本次只驗證文件與活動資料，尚未重現引用正確率與增量更新品質。#849 回報 Windows 的 MinerU 雲端連線 403，#155 回報新增欄位顯示異常；license 的 NOASSERTION 代表 API 無法辨識，採用前需人工核對。

證據：[README](https://github.com/nashsu/llm_wiki#readme)、[releases](https://github.com/nashsu/llm_wiki/releases)、[issues](https://github.com/nashsu/llm_wiki/issues)。

## 下一輪追蹤（目標日期 2026-11-15）

- **GoogleChrome/modern-web-guidance-src：**檢查 #3505 與 WebGPU 指引進展，觀察新增 stars 是否延續；準備一個跨瀏覽器前端測試題。
- **alibaba/open-code-review：**追蹤 #1925 後續發版，以及 #1934 多規則檔組合；用同一個 PR 比較規則與 LLM 結果。
- **ChromeDevTools/chrome-devtools-mcp：**觀察 #3487 的權限錯誤說明是否合併，並測試獨立 Chrome 設定檔下的穩定連線。
- **backnotprop/plannotator：**追蹤語意差異審閱與新版面，確認標註回傳到正確的 agent 與檔案版本。
- **dream-num/univer：**檢查 #8168 大型工作簿公式效能與 #8139 文件參照支援，先界定純開源可完成的最小辦公案例。
- **Tencent/LoopForge：**建立後續快照基線，追蹤 #810、#829 與正式 release；挑一個有人工核准關卡的低權限 SOP 做評估。
- **QwenLM/qwen-code：**追蹤 #17266 與 SDK／主 CLI 版本對應，先確認環境穩定後再安排課程示範。
- **JuliusBrussee/caveman：**以含數字、例外條件和來源的辦公文件做 A/B 測試，同時量測 token 與資訊保留率，再決定是否升級為 Skill 候選。
- **nashsu/llm_wiki：**追蹤 #849、#155 與下一次程式更新；以一批非機密文件測試引用、重複匯入、更新及刪除後的一致性。

## 行動建議

優先將 Chrome MCP 與 Plannotator 設計成可重現的課程示範；Modern Web Guidance 列為 Skill 評估候選。Univer 與 LoopForge 先研究功能、授權和驗收邊界。LLM Wiki 維持對 know metabiz wiki 的直接觀察，但先以非機密文件驗證來源追溯及更新一致性。以上皆為本次證據支持的選題與研究判斷，尚不是部署或採用決策。
