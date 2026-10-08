# GitHub AI 趨勢雷達｜2026-10-08

目標日期：台北前一曆日 2026-10-08。實際開始收集：2026-10-09T00:10:49.806123+08:00。共收集 339 個候選／累積追蹤專案，其中 5 個來自本次範圍內的 [GitHub Trending daily](https://github.com/trending?since=daily)。

本次最值得先研究 rea 的相對成長；最容易轉成課程內容的是 diagram-design；企業辦公與 know metabiz wiki 則優先研究 knowledge-work-plugins 的職能流程，並持續追蹤 llm_wiki 的匯入完整性。

## 判讀方法與資料品質

- 優先綜合 stars today、前次快照星數差、相對成長、最近 push、README、release 與 issue／PR 活動；以下順序同時考量 Adam 的應用價值，並非總星數榜。
- 星數差比較 2026-10-07 與本次快照；相對成長＝星數差 ÷ 前次總星數。Trending stars today 是即時滾動值，與快照差的時間窗口不同。未上本次榜單以「—」表示未知，不當作零。
- 這是延後執行的 2026-10-08 日報，資料在 2026-10-09 台北時間取得，不宣稱還原目標日零時至午夜的歷史榜單。
- 每個精選專案補查最近五筆 issue endpoint 活動與最近三筆 releases；issue endpoint 包含 PR，以下分開說明。open_issues 是 GitHub 的 issue／PR 混合計數，不當作 bug 數量。
- GitHub API 未偵測到 rate-limit，使用 --limit 10，無須 --limit 5 重試。四個歷史專案 API 404，沿用舊資料且已標示 metadata_fresh=false；不納入本次精選與新動能判斷：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。
- 收集器以總星數排序的搜尋會偏向成熟專案；本次以 Trending 補足當日熱度，並以應用相關性補入 wiki／自動化項目。README 的功能描述屬專案自述，尚未實際跑 demo。

## 精選比較

| 專案 | stars today | 快照星數差 | 相對成長 | 總星數 | 建議 |
|---|---:|---:|---:|---:|---|
| [morluto/rea](https://github.com/morluto/rea) | 7744 | +7,740 | 59.66% | 20,713 | Deep research |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 766 | +301 | 1.11% | 27,349 | Skill candidate |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 1163 | +1,206 | 2.70% | 45,872 | Demo content |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 1770 | +1,703 | 0.61% | 280,856 | Skill candidate |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 662 | +688 | 0.71% | 98,211 | Watch |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | — | +20 | 0.08% | 24,951 | Demo content |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | — | +37 | 0.18% | 20,309 | Watch |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | — | +55 | 0.07% | 83,522 | Deep research |

## 1. morluto/rea｜Deep research

**用途：** 以單一 MCP 串接應用行為、二進位與執行期逆向分析。README 有工具契約與入門路徑。

**動能與維護：** 最近 push：2026-10-08T16:16:16Z（UTC）；GitHub 開放 issue／PR 合計 82。最新 rea-agents-6.0.0 於 10/08（UTC）發布；最近五筆活動均為 PR，含 Windows artifact、MCP provider 與分析目標識別修正，顯示熱度伴隨工程工作。

**風險：** 重大版本連日變更，跨平台與原生工具相依性仍需驗證；示範限定自有或可合法分析的樣本。

**Adam／metabiz 關聯：** 適合 Adam 的 MCP 進階課、程式理解與逆向工具內容；對 know metabiz wiki 可借鏡「分析結果帶來源」模式，辦公自動化直接性較低。

來源：[README](https://github.com/morluto/rea#readme)、[releases](https://github.com/morluto/rea/releases)、[issue／PR 活動](https://github.com/morluto/rea/issues?q=sort%3Aupdated-desc)。

## 2. anthropics/knowledge-work-plugins｜Skill candidate

**用途：** 把 skills、connectors、commands 與 subagents 組成職能插件；README 列出業務、客服、生產力等場景。

**動能與維護：** 最近 push：2026-10-08T15:35:19Z（UTC）；GitHub 開放 issue／PR 合計 134。未取得 GitHub release；近期五筆活動均為 PR，多為 connector 更新，不能把自動更新量當成新增能力驗證。

**風險：** 涉及企業連接器權限與資料邊界；README 的相容性宣稱仍需逐工具驗證，不能假設所有插件可直接移植到 Codex。

**Adam／metabiz 關聯：** 最貼近 Adam 的 AI 辦公課與 metabiz SOP：可研究「客服處理→知識文章」及業務備訪流程，再轉成自家可審核 skill。

來源：[README](https://github.com/anthropics/knowledge-work-plugins#readme)、[releases](https://github.com/anthropics/knowledge-work-plugins/releases)、[issue／PR 活動](https://github.com/anthropics/knowledge-work-plugins/issues?q=sort%3Aupdated-desc)。

## 3. cathrynlavery/diagram-design｜Demo content

**用途：** 用 Agent Skills 產生獨立 HTML＋SVG 圖解；README 提供語意模式、版型、靜態輸出與既有圖形重繪說明。

**動能與維護：** 最近 push：2026-10-08T01:34:39Z（UTC）；GitHub 開放 issue／PR 合計 48。未取得 GitHub release；近期五筆 PR 涉及 PNG 匯出、RTL、無障礙與安全文件，README 版本字樣不等於正式 release。

**風險：** 繁體中文字型、文字溢出、SVG 無障礙與輸出尺寸需實測；未合併的 PNG 匯出 PR 不應當作現成功能。

**Adam／metabiz 關聯：** 非常適合 Adam 的課程架構圖、短片圖解與 AI 辦公流程；也可替 know metabiz wiki 製作帶來源的系統與 SOP 圖。

來源：[README](https://github.com/cathrynlavery/diagram-design#readme)、[releases](https://github.com/cathrynlavery/diagram-design/releases)、[issue／PR 活動](https://github.com/cathrynlavery/diagram-design/issues?q=sort%3Aupdated-desc)。

## 4. mattpocock/skills｜Skill candidate

**用途：** 提供可組合的小型工程 skills，README 強調可編輯、適配與不同 agent 的安裝方式。

**動能與維護：** 最近 push：2026-10-08T08:49:07Z（UTC）；GitHub 開放 issue／PR 合計 163。最新 v1.3.1 於 10/04（UTC）發布；近期樣本為四個 issue、一個 PR，涉及提問依賴順序、詞彙文件定位與決策重複浮現。

**風險：** 技能流程會影響 agent 行為；更新需比較差異，避免安裝重複與覆蓋本地客製規則。近期 issue 也顯示流程本身需要驗證。

**Adam／metabiz 關聯：** 適合 Adam 的工程型 AI 課程、需求訪談與技能設計內容；可研究詞彙與決策記錄如何支持 know metabiz wiki，企業辦公場景需再客製。

來源：[README](https://github.com/mattpocock/skills#readme)、[releases](https://github.com/mattpocock/skills/releases)、[issue／PR 活動](https://github.com/mattpocock/skills/issues?q=sort%3Aupdated-desc)。

## 5. thedotmack/claude-mem｜Watch

**用途：** 記錄並壓縮 agent 工作過程，在後續工作階段注入相關記憶；README 描述 lifecycle hooks、搜尋與隱私排除機制。

**動能與維護：** 最近 push：2026-10-07T00:57:45Z（UTC）；GitHub 開放 issue／PR 合計 122。最新 v13.34.2 於 10/06（UTC）發布；近期樣本一個 issue、四個 PR。[#4593](https://github.com/thedotmack/claude-mem/issues/4593) 回報 Pydantic／MCP 相依性導致 Chroma 搜尋失敗。

**風險：** 持久記憶可能保存敏感工作內容、注入錯誤或過時上下文；相依性故障是使用者回報，尚不能視為已修復。

**Adam／metabiz 關聯：** 適合 Adam 講解「跨工作階段記憶」與「可追溯 wiki」差別；可用匿名資料測試辦公助理，但先不要讓它成為 know metabiz wiki 的唯一事實來源。

來源：[README](https://github.com/thedotmack/claude-mem#readme)、[releases](https://github.com/thedotmack/claude-mem/releases)、[issue／PR 活動](https://github.com/thedotmack/claude-mem/issues?q=sort%3Aupdated-desc)。

## 6. activepieces/activepieces｜Demo content

**用途：** 提供 AI 工作流與可擴充 TypeScript pieces；README 表示 pieces 可暴露為 MCP servers。

**動能與維護：** 最近 push：2026-10-08T16:11:12Z（UTC）；GitHub 開放 issue／PR 合計 670。最新 0.92.2 於 10/07（UTC）發布；最近五筆均為 PR，含聊天、Square／Softr 連接器與開發依賴更新，活動不只來自星數。

**風險：** API license 欄位為 NOASSERTION；README 區分社群 MIT 與企業商業授權。外部 API 權限、重試與重複寫入需在示範中明確處理。

**Adam／metabiz 關聯：** 適合 Adam 的 AI 辦公自動化實作課：表單→分類→草稿→審核→知識庫；可用於 know metabiz wiki 的資料匯入與待審流程。

來源：[README](https://github.com/activepieces/activepieces#readme)、[releases](https://github.com/activepieces/activepieces/releases)、[issue／PR 活動](https://github.com/activepieces/activepieces/issues?q=sort%3Aupdated-desc)。

## 7. nashsu/llm_wiki｜Watch

**用途：** 桌面知識管理工具，從文件增量建立互連 wiki；README 包含來源追溯、文件匯入與原始來源問答模式。

**動能與維護：** 最近 push：2026-09-28T01:43:23Z（UTC）；GitHub 開放 issue／PR 合計 274。最新 v0.6.12 於 09/28（UTC）發布；push 也停在 09/28。最近樣本三個 issue、兩個 PR；[#809](https://github.com/nashsu/llm_wiki/issues/809) 回報匯入時來源摘要遭覆寫，另有 PDF 解析偏差回報。

**風險：** 匯入完整性、摘要覆寫與 PDF 事實偏差直接影響可信度；API license 為 NOASSERTION，移植前需另查完整 LICENSE。

**Adam／metabiz 關聯：** 與 know metabiz wiki 最直接相關，也適合 Adam 比較 RAG 與持久 wiki 的內容；優先以匿名 SOP 做可追溯性測試，等完整性問題處理後再擴大示範。

來源：[README](https://github.com/nashsu/llm_wiki#readme)、[releases](https://github.com/nashsu/llm_wiki/releases)、[issue／PR 活動](https://github.com/nashsu/llm_wiki/issues?q=sort%3Aupdated-desc)。

## 8. bytedance/deer-flow｜Deep research

**用途：** 用 subagents、memory、sandbox 與 skills 執行較長的研究、程式與內容任務；README 區分 2.0 harness 與舊 1.x 架構。

**動能與維護：** 最近 push：2026-10-08T15:34:33Z（UTC）；GitHub 開放 issue／PR 合計 894。最新 v2.1.0 於 09/24（UTC）發布；最近五筆均為 PR，包含排程修正、工具執行審核及 delegated fetch 的 SSRF 修正。工具審核 PR 仍 open。

**風險：** 長任務成本、沙箱權限與外部抓取邊界需驗證；已關閉 PR 不代表現有 release 已包含修正，未合併的審核功能不可當成已可用。

**Adam／metabiz 關聯：** 適合 Adam 的 agent 編排進階課與研究→草稿→知識庫 demo；know metabiz wiki 可借鏡分工與產物管理，導入前先量測成本與失敗恢復。

來源：[README](https://github.com/bytedance/deer-flow#readme)、[releases](https://github.com/bytedance/deer-flow/releases)、[issue／PR 活動](https://github.com/bytedance/deer-flow/issues?q=sort%3Aupdated-desc)。

## 明日觀察清單（下一期目標日 2026-10-09）

- **rea：** 觀察高相對增長是否延續、6.0.0 後是否有相容性修補；先做單一自有樣本的 MCP 工具成功率測試。
- **diagram-design：** 用繁體中文 SOP 製作一張圖，檢查溢出、可讀性與匯出；追蹤 PNG renderer PR #354。
- **knowledge-work-plugins／mattpocock skills：** 比較更新差異，挑一個客服知識文章流程與一個需求提問流程做技能候選，記錄工具權限與驗收標準。
- **claude-mem：** 追蹤 #4593 是否修復、是否發布相容版本；以匿名資料檢查記憶排除與跨工作階段注入。
- **llm_wiki：** 優先追蹤 #809 摘要覆寫與 PDF 解析問題；比較來源、生成頁與引用是否一致，未修復前維持 Watch。
- **activepieces：** 以唯讀資料或可撤銷測試資料做表單→審核→wiki 的小 demo，檢查重試與企業功能授權範圍。
- **deer-flow：** 查排程／SSRF 修正是否進入 release，追蹤工具審核 PR #5827；量測一次長任務的成本、時間與失敗恢復。

## 本次證據

- repos.json 與 snapshots/repos-2026-10-08.json：星數、增量、來源、README 摘要、更新與 release metadata。
- trending-daily-evidence.json：即時榜單的範圍內專案與 stars today。
- activity-evidence.json／readme-evidence.json：精選八個專案的補查來源。
- run-status.json／collector-limit-10.log：實際執行時間、limit、API 錯誤與 fallback 記錄。
