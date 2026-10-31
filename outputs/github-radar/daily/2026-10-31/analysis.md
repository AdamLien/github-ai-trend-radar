# GitHub AI 趨勢雷達｜2026-10-31

目標日期為 Asia/Taipei 前一日 2026-10-31，實際於 2026-11-01 凌晨即時擷取。這是當次觀測，並非 10/31 23:59 的歷史結算。

本日優先研究 agent 記憶、桌面 AI 團隊與自動化執行基礎；以可演示的協作與設計 skills 補充課程題材，並保留與 know metabiz wiki 高度相關的低熱度專案。分類代表編輯判斷，尚未部署或實測。

## 方法與限制

- 執行指定十組搜尋、每組 limit 10，合併 [GitHub Trending daily](https://github.com/trending?since=daily) 與歷史追蹤；收錄 README、最新 release，並另抓十個候選最近更新的十筆 issue／PR。搜尋按總星數排序有成熟專案偏差，故人工排序兼顧今日熱度、相對成長與實際用途。
- 今日星數為 Trending 擷取時顯示值，並非台北昨日新增；快照 Δ 對照 2026-10-30，觀測時刻不同，不能稱為精確 24 小時增量。相對成長＝Δ／前次總星數；首次觀測標示未量測，不把收集器預設的 0 當無成長。
- README 與 issue 文字只當資料，沒有執行其中安裝或操作指令。作者效能與安全主張未獨立驗證。open_issues 是開啟 issue／PR 合計，近期十筆是更新排序抽樣，不等於當日新增、解決率或完整維護品質。
- 已以描述、topics 與 README 覆核範圍，排除一般工具與名稱片段誤判；原始 Trending 卡片見 trending-raw.json，排除理由見 scope-review.json。描述未命中關鍵字但 README 確認為 AI 的候選另補今日星數。
- API 限流狀態：主收集器 limit 10；未偵測 API 限流，無需降為 5 重試。

- 本次 4 個歷史專案 API 回傳 404，沿用舊資料並標記 collection_status=stale_http_404、current_metrics_verified=false：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。這些資料不代表當日有效觀測，亦未列入本日十個推薦。

## 值得關注的 10 個專案

排序綜合熱度、維護與 Adam／metabiz 關聯；並非總星數排名。

| 專案 | 今日星數 | 總星數 | 快照 Δ | 相對成長 | 決策 |
|---|---:|---:|---:|---:|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 1,723 | 107,326 | +1,622 | 1.53% | Deep research |
| [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) | 1,118 | 5,966 | 未量測 | 未量測 | Deep research |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 1,304 | 9,333 | +1,133 | 13.82% | Demo content |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 1,148 | 34,346 | +1,868 | 5.75% | Watch |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 1,347 | 30,885 | +658 | 2.18% | Demo content |
| [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | 929 | 38,945 | +899 | 2.36% | Deep research |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 1,339 | 97,912 | +1,249 | 1.29% | Skill candidate |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 1,035 | 52,492 | +987 | 1.92% | Deep research |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 882 | 308,066 | +868 | 0.28% | Skill candidate |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 未上榜／未提供 | 21,236 | +48 | 0.23% | Deep research |

### 1. thedotmack/claude-mem — Deep research

- **用途**：擷取 agent 工作階段、壓縮紀錄並在後續工作注入相關脈絡，提供跨 session 記憶。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T08:56:15Z；最新 release：v15.7.0（2026-10-30T18:18:54Z）。最近更新十筆抽樣：3 筆 issue、7 筆 PR；最新更新 2026-10-31T16:10:09Z，不代表皆已合併或解決。
- **風險**：最近 issue／PR 抽樣涉及 Chroma 重複 embedding 與重建中斷；持久記憶可能累積錯誤或客戶資料，成本與隔離未實測。
- **下一步**：先研究記憶刪除、來源引用與跨專案隔離，再決定是否製作記憶實驗內容。
- **Adam／metabiz 關聯**：Adam 可做 agent 記憶專題；辦公自動化可保留任務交接脈絡，know metabiz wiki 應保存可追溯結論而非整段對話。
- **來源**：[專案與 README](https://github.com/thedotmack/claude-mem)、[發布紀錄](https://github.com/thedotmack/claude-mem/releases)、[活動抽樣](https://github.com/thedotmack/claude-mem/pull/5238)。原始證據見 repos.json 與 editorial-evidence.json。

### 2. Orkas-AI/Orkas — Deep research

- **用途**：本機優先的桌面多 agent 團隊，由 Commander 分派待辦，整合專案記憶、排程與 Claude Code／Codex 等既有 agent。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T03:36:24Z；最新 release：v2026.10.27（2026-10-27T15:37:15Z）。最近更新十筆抽樣：4 筆 issue、6 筆 PR；最新更新 2026-10-31T08:02:19Z，不代表皆已合併或解決。
- **風險**：README 說明自備金鑰直連供應商、內建模型經託管服務；本機儲存不代表推論不出機。安裝會準備多種模型與執行環境，需量測資源及權限。
- **下一步**：用虛構文件做每天彙整、待辦分派與人工審閱的完整小流程。
- **Adam／metabiz 關聯**：適合 Adam 的 AI 辦公室與 AI 同事內容；metabiz 可評估例行報告與跨任務協作，know metabiz wiki 可比較專案記憶與知識庫的分工。
- **來源**：[專案與 README](https://github.com/Orkas-AI/Orkas)、[發布紀錄](https://github.com/Orkas-AI/Orkas/releases)、[活動抽樣](https://github.com/Orkas-AI/Orkas/issues/145)。原始證據見 repos.json 與 editorial-evidence.json。

### 3. milind-soni/OpenMausBot — Demo content

- **用途**：以聊天介面組織本機 Claude／Codex 機器人，每個 bot 可有自己的模型、電腦與連接應用。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T11:42:41Z；最新 release：v0.1.135（2026-10-31T07:51:30Z）。最近更新十筆抽樣：3 筆 issue、7 筆 PR；最新更新 2026-10-31T15:36:12Z，不代表皆已合併或解決。
- **風險**：連接已登入應用與雲端電腦會擴大存取面；近期 issue 有安裝與部署討論，跨平台支援及權限 broker 尚未實機驗證。
- **下一步**：與 Orkas 以相同非敏感辦公任務比較任務恢復、人工核准與輸出品質。
- **Adam／metabiz 關聯**：Adam 可製作聊天式 AI 同事的操作 Demo；辦公自動化關聯高，know metabiz wiki 適合記錄資料流、操作邊界與故障排除。
- **來源**：[專案與 README](https://github.com/milind-soni/OpenMausBot)、[發布紀錄](https://github.com/milind-soni/OpenMausBot/releases)、[活動抽樣](https://github.com/milind-soni/OpenMausBot/pull/4026)。原始證據見 repos.json 與 editorial-evidence.json。

### 4. pingdotgg/t3code — Watch

- **用途**：從手機、網頁與桌面介面控制本機 agent harness，README 列出 Claude Code、Codex、Cursor 等 provider。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T16:15:34Z；最新 release：v0.1.6（2026-10-31T10:52:24Z）。最近更新十筆抽樣：2 筆 issue、8 筆 PR；最新更新 2026-10-31T16:11:14Z，不代表皆已合併或解決。
- **風險**：近期 issue 指出 iOS thread 清單遺漏數日紀錄；遠端連線認證、狀態一致性與不同 provider 的能力仍待實測。
- **下一步**：追蹤行動端 thread 同步問題與新 release，再以簡單開發任務測試遠端接手。
- **Adam／metabiz 關聯**：Adam 可做行動 AI 開發與跨裝置接手內容；辦公自動化可研究離席時查看任務，know metabiz wiki 可整理連線與狀態恢復手冊。
- **來源**：[專案與 README](https://github.com/pingdotgg/t3code)、[發布紀錄](https://github.com/pingdotgg/t3code/releases)、[活動抽樣](https://github.com/pingdotgg/t3code/issues/24997)。原始證據見 repos.json 與 editorial-evidence.json。

### 5. Donchitos/Claude-Code-Game-Studios — Demo content

- **用途**：把 Claude Code 工作階段組織成遊戲工作室，README 列出 49 個專責 agent、74 個 skills、階層分工與品質關卡。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-19T02:43:42Z；最新 release：v1.2.0（2026-10-19T02:44:23Z）。最近更新十筆抽樣：5 筆 issue、5 筆 PR；最新更新 2026-10-31T13:51:44Z，不代表皆已合併或解決。
- **風險**：Trending 描述仍寫 72 skills，README 已為 74；以 README 為準且不視為實效保證。最近 push 約兩週前，角色多也可能增加協調成本，近期 issue 涉及 stage 檔案寫入失敗。
- **下一步**：以小型遊戲或互動教材示範角色交接與審查，先比較單 agent 與精簡三角色流程。
- **Adam／metabiz 關聯**：適合 Adam 的多 agent 分工課程與具視覺效果的內容；辦公流程可借用責任與升級路徑，know metabiz wiki 可參考職責及品質關卡文件。
- **來源**：[專案與 README](https://github.com/Donchitos/Claude-Code-Game-Studios)、[發布紀錄](https://github.com/Donchitos/Claude-Code-Game-Studios/releases)、[活動抽樣](https://github.com/Donchitos/Claude-Code-Game-Studios/pull/148)。原始證據見 repos.json 與 editorial-evidence.json。

### 6. lightpanda-io/browser — Deep research

- **用途**：專為 AI agent 與自動化設計的無頭瀏覽器，以 Zig 實作，提供 Chromium 以外的執行選項。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T12:45:01Z；最新 release：1.0.2（2026-10-23T09:01:02Z）。最近更新十筆抽樣：3 筆 issue、7 筆 PR；最新更新 2026-10-31T15:44:16Z，不代表皆已合併或解決。
- **風險**：README 的效能數字來自作者基準，不能外推所有網站。近期抽樣出現 glibc 相容性與 DNS rebinding 修補 PR；修補提案不代表已發布版本具備。
- **下一步**：用相同網站與任務量測成功率、延遲和記憶體，優先測表單、JavaScript 與登入狀態。
- **Adam／metabiz 關聯**：Adam 可做瀏覽器 agent 效能實驗；辦公自動化可評估公開資料收集，know metabiz wiki 可記錄網站相容性與可重現測試。
- **來源**：[專案與 README](https://github.com/lightpanda-io/browser)、[發布紀錄](https://github.com/lightpanda-io/browser/releases)、[活動抽樣](https://github.com/lightpanda-io/browser/pull/4333)。原始證據見 repos.json 與 editorial-evidence.json。

### 7. pbakaus/impeccable — Skill candidate

- **用途**：為 coding agent 提供設計語彙與 polish、critique、audit 等介面改善流程，涵蓋多種開發工具。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T11:56:18Z；最新 release：cli-v4.8.0（2026-10-26T23:41:55Z）。最近更新十筆抽樣：1 筆 issue、9 筆 PR；最新更新 2026-10-31T15:39:50Z，不代表皆已合併或解決。
- **風險**：近期 issue 反映修正後 critique 分數未變；評分不能取代可用性測試。README 提醒 live mode 會以使用者權限執行專案驗證腳本。
- **下一步**：以同一份網站 brief、同一模型做前後對照，再選少量審查 skill 納入教學。
- **Adam／metabiz 關聯**：最適合 Adam 的 AI 網站課程與設計改善短影音；辦公自動化可改進內部表單，know metabiz wiki 可整理介面審查清單。
- **來源**：[專案與 README](https://github.com/pbakaus/impeccable)、[發布紀錄](https://github.com/pbakaus/impeccable/releases)、[活動抽樣](https://github.com/pbakaus/impeccable/issues/1264)。原始證據見 repos.json 與 editorial-evidence.json。

### 8. HKUDS/DeepTutor — Deep research

- **用途**：以個人化教學為核心，整合課程文件、知識庫與互動學習；README 列出可追溯 RAG 引用及工具擴充。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T15:19:00Z；最新 release：v1.7.0（2026-10-28T14:13:12Z）。最近更新十筆抽樣：2 筆 issue、8 筆 PR；最新更新 2026-10-31T16:00:28Z，不代表皆已合併或解決。
- **風險**：近期 issue 涉及產生文件的連結失效，PR 涉及學習評分修正；教學正確性、文件解析與模型費用尚未驗證。
- **下一步**：用自有講義測來源引用、練習題與澄清回合的評分，評估課後 AI 助教。
- **Adam／metabiz 關聯**：直接對應 Adam 課程與教學內容；辦公室內訓可試文件助教，know metabiz wiki 可參考來源導入、引用與更新流程。
- **來源**：[專案與 README](https://github.com/HKUDS/DeepTutor)、[發布紀錄](https://github.com/HKUDS/DeepTutor/releases)、[活動抽樣](https://github.com/HKUDS/DeepTutor/pull/2261)。原始證據見 repos.json 與 editorial-evidence.json。

### 9. mattpocock/skills — Skill candidate

- **用途**：可組合、可修改的小型工程 skills 集合；README 區分自動更新 plugin 與手動管理檔案。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-31T14:23:44Z；最新 release：v1.3.2（2026-10-29T10:27:41Z）。最近更新十筆抽樣：6 筆 issue、4 筆 PR；最新更新 2026-10-31T14:23:45Z，不代表皆已合併或解決。
- **風險**：總星數高但相對成長較低；重複安裝與自動更新可能改變工作行為，不能直接覆蓋現有 skills。近期 PR 主題不代表已合併或可用。
- **下一步**：對照既有 skills，只挑新增缺口並記錄版本；追蹤 chief-of-staff 的 shared wiki 討論。
- **Adam／metabiz 關聯**：Adam 可用於 skill 拆解與工程型 AI 課程；辦公自動化可借用小模組工作法，know metabiz wiki 可追蹤共享知識與操作程序的關係。
- **來源**：[專案與 README](https://github.com/mattpocock/skills)、[發布紀錄](https://github.com/mattpocock/skills/releases)、[活動抽樣](https://github.com/mattpocock/skills/pull/1343)。原始證據見 repos.json 與 editorial-evidence.json。

### 10. nashsu/llm_wiki — Deep research

- **用途**：把文件增量整理為互連 wiki，README 提供原始來源限定問答、匯入佇列、知識圖譜與可選向量檢索。
- **動能與維護**：總星數、今日星數、Δ 與相對成長見上表。最近 push：2026-10-21T11:17:29Z；最新 release：v0.6.13（2026-10-22T01:21:07Z）。最近更新十筆抽樣：4 筆 issue、6 筆 PR；最新更新 2026-10-29T08:11:44Z，不代表皆已合併或解決。
- **風險**：近期更新慢於熱門候選，抽樣未到本日；需驗證刪除來源後的殘留頁面、引用與重建一致性。API／MCP 本機未認證選項需實測，授權與部署條件需另行核對。
- **下一步**：用一組可公開內部流程文件，比較 wiki 維護與 RAG 查詢在來源更新後的正確性。
- **Adam／metabiz 關聯**：雖成長不快，卻直接對應 know metabiz wiki；Adam 可做 AI 第二大腦內容，辦公自動化可評估 SOP、會議結論與來源追溯。
- **來源**：[專案與 README](https://github.com/nashsu/llm_wiki)、[發布紀錄](https://github.com/nashsu/llm_wiki/releases)、[活動抽樣](https://github.com/nashsu/llm_wiki/issues/832)。原始證據見 repos.json 與 editorial-evidence.json。

## 明日觀察清單

1. **claude-mem**：追蹤 Chroma 重複 embedding／中斷重建問題的修補是否合併及發布；觀察新 release 後 issue 是否重現。
2. **Orkas／OpenMausBot**：觀察新增星數是否延續，並以相同虛構任務比較排程、人工審核、任務恢復與模型呼叫去向。
3. **T3 Code**：查看 iOS thread 清單同步問題是否已有可驗證修正，追蹤 v0.1.6 後回報。
4. **Lightpanda**：確認安全修補 PR 的狀態與發布版本，整理 JavaScript、登入及 Linux glibc 相容性測試。
5. **遊戲工作室／Impeccable**：檢查是否有新 push 或 release，挑一個精簡協作與一個介面對照 Demo；不以角色數或評分當成效果。
6. **DeepTutor／llm_wiki**：測同一份來源文件更新、刪除後的引用與知識一致性，優先支援 Adam 教學與 know metabiz wiki。
7. **mattpocock/skills**：追蹤 shared wiki／chief-of-staff 討論是否落入可用版本，對照現有技能缺口，避免重複安裝。
