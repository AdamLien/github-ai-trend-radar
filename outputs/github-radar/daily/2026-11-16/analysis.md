# GitHub AI 趨勢雷達｜2026-11-16

## 觀測口徑與結論

目標日期為前一個 Asia/Taipei 日曆日 2026-11-16；實際收集在 2026-11-17 凌晨（台北時間）執行。GitHub Trending daily 是抓取當下的動態頁面，不是 11/16 全天封存榜。候選指標另存 candidate-evidence.json，與主收集器逐筆時間可能相差數分鐘。

本輪以 Skills 驗收、AI 辦公文件與人機協作審閱為優先。NVIDIA SkillEvaluator 的相對成長高，Univer 同時有高新增星數與新版本；Stitch Skills 雖有熱度，推送較舊且整合問題未確認解決。ffmpeg-skill 題材很貼近內容產線，但檔案保護 issue 使它仍停留在隔離試驗階段。

依今日新增星數、相對前次觀測的 star delta／成長率、最近推送、README、release 與 issue／PR 樣本綜合選擇，不依總星數排序。相對成長率 =（目前 stars − 前次 stars）÷ 前次 stars；前次基準為 2026-11-15 資料夾，時間間隔不保證恰為 24 小時。新進項目缺乏基準時標示未測，不將 collector 的零 delta 解讀為零成長。

來源：[即時 GitHub Trending daily](https://github.com/trending?since=daily)（原始頁面 trending-daily.html）、repos.json／snapshots、candidate-evidence.json 與 issue-activity.json。README 僅取前 700 字元；能力敘述來自專案自述，未安裝或驗證。issue endpoint 樣本為每專案最近更新的 5 筆，含 PR；未關閉數含 PR，不是回覆速度或解決率。風險與應用建議為本次分析判斷。

## 值得投入的 10 個專案

| 專案 | 今日星數 | 快照增量 | 相對成長 | 總星數 | 處置 |
|---|---:|---:|---:|---:|---|
| [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) | 953 | +983 | 69.72% | 2,393 | Deep research |
| [dream-num/univer](https://github.com/dream-num/univer) | 1,878 | +2,216 | 8.74% | 27,567 | Deep research |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | 689 | +680 | 5.83% | 12,345 | Demo content |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 837 | +795 | 1.40% | 57,524 | Demo content |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 540 | +525 | 5.76% | 9,643 | Skill candidate |
| [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | 475 | 未測（新觀測） | 未測 | 6,360 | Skill candidate |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 946 | +951 | 1.84% | 52,766 | Watch |
| [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | 790 | +943 | 5.34% | 18,593 | Watch |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 未上榜／未取得 | +30 | 0.18% | 16,535 | Watch |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 122 | +197 | 0.29% | 67,933 | Reference only |

### 1. NVIDIA/SkillEvaluator｜Deep research

- **用途與 README**：以品質檢查、語義重疊與實際 agent 評估，衡量 Skills 是否改善行為。
- **維護與版本**：最近 push `2026-11-16T15:59:52Z`；最新 release `v0.9.0`（`2026-11-13T11:03:05Z`）。以上為 UTC；未關閉 issue／PR 合計 16。
- **活動證據**：最近五筆全是 PR，涉及 Tier 1 檢查、漏掃狀態與 Tier 3 結果定位；評估正確性本身仍需驗證。 最近樣本更新 `2026-11-16T15:59:53Z`；[#668](https://github.com/NVIDIA/SkillEvaluator/pull/668)、[#611](https://github.com/NVIDIA/SkillEvaluator/pull/611)、[#669](https://github.com/NVIDIA/SkillEvaluator/pull/669)。
- **與 Adam／metabiz 的關聯**：Adam 的 Skills 課程可加入有／無 skill 對照與評分表；辦公流程 skill 上線前建立驗收，將測試案例收入 know metabiz wiki。
- **風險與投入界線**：合成評估不等於真實任務成功；執行評估可能增加模型成本，掃描通過也不能保證安全。

### 2. dream-num/univer｜Deep research

- **用途與 README**：可嵌入產品的試算表與文件 SDK，讓應用程式或 agent 操作辦公文件。
- **維護與版本**：最近 push `2026-11-16T13:43:27Z`；最新 release `v1.5.2`（`2026-11-16T10:35:04Z`）。以上為 UTC；未關閉 issue／PR 合計 178。
- **活動證據**：最近五筆全是 PR，涵蓋負數解析、萬用字元搜尋、排序與公式效能；活躍但也顯示相容性仍在修補。 最近樣本更新 `2026-11-16T15:37:24Z`；[#8239](https://github.com/dream-num/univer/pull/8239)、[#8232](https://github.com/dream-num/univer/pull/8232)、[#8227](https://github.com/dream-num/univer/pull/8227)。
- **與 Adam／metabiz 的關聯**：AI 辦公自動化最直接：以會員營收報表、課程名單清理示範；know metabiz wiki 可保留操作配方與計算定義。
- **風險與投入界線**：公式相容性與大型工作簿效能需實測；開源核心與進階協作功能的授權、部署成本須分別核對。

### 3. backnotprop/plannotator｜Demo content

- **用途與 README**：把 agent 的計畫、規格與程式差異轉成可標註、回饋的審閱工作區。
- **維護與版本**：最近 push `2026-11-16T16:06:16Z`；最新 release `v0.28.66`（`2026-11-16T06:53:54Z`）。以上為 UTC；未關閉 issue／PR 合計 168。
- **活動證據**：樣本含 Plans 頁面 PR 與 Git LFS 圖片預覽 issue；不能將待合併 Plans 功能當成已發布能力。 最近樣本更新 `2026-11-16T16:06:17Z`；[#3527](https://github.com/backnotprop/plannotator/pull/3527)、[#1665](https://github.com/backnotprop/plannotator/issues/1665)、[#3503](https://github.com/backnotprop/plannotator/pull/3503)。
- **與 Adam／metabiz 的關聯**：適合 Claude Code／Codex 課程的人機協作示範：先標註需求再讓 agent 修改；把決策與核准結果放入 know metabiz wiki。
- **風險與投入界線**：分享與回饋可能含公司程式碼或需求；更新快速，需固定版本並驗證實際支援的 agent 整合。

### 4. ChromeDevTools/chrome-devtools-mcp｜Demo content

- **用途與 README**：把瀏覽器檢查、除錯與效能分析提供給 coding agent 的 MCP／CLI 工具。
- **維護與版本**：最近 push `2026-11-16T13:40:03Z`；最新 release `chrome-devtools-mcp-v1.13.0`（`2026-11-11T12:40:09Z`）。以上為 UTC；未關閉 issue／PR 合計 128。
- **活動證據**：可見 daemon timeout issue 已關閉及修補 PR；1.14.0 仍是 release PR，不能視為已正式發版。 最近樣本更新 `2026-11-16T14:00:18Z`；[#3030](https://github.com/ChromeDevTools/chrome-devtools-mcp/pull/3030)、[#3462](https://github.com/ChromeDevTools/chrome-devtools-mcp/pull/3462)、[#2983](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2983)。
- **與 Adam／metabiz 的關聯**：適合 Adam 示範網頁除錯與後台流程驗證；辦公自動化可研究表單操作，將可重現步驟整理至 know metabiz wiki。
- **風險與投入界線**：連線瀏覽器可接觸登入狀態與頁面資料，應用隔離測試帳號；CLI timeout 與版本相容性需驗證。

### 5. google-labs-code/stitch-skills｜Skill candidate

- **用途與 README**：連接 Stitch MCP 的設計技能與 plugins，供多種 coding agent 使用。
- **維護與版本**：最近 push `2026-08-17T20:20:23Z`；最新 release `v1.0`（`2026-05-18T18:02:32Z`）。以上為 UTC；未關閉 issue／PR 合計 20。
- **活動證據**：issue #96 指出 uploader 依賴 repo checkout；#97 為修正 PR，#94 回報下載轉向登入。未合併修補不代表已解決。 最近樣本更新 `2026-11-16T08:14:27Z`；[#97](https://github.com/google-labs-code/stitch-skills/pull/97)、[#96](https://github.com/google-labs-code/stitch-skills/issues/96)、[#95](https://github.com/google-labs-code/stitch-skills/issues/95)。
- **與 Adam／metabiz 的關聯**：Adam 可做設計輸入到頁面實作的短課；企業內部工具原型可降低溝通時間，know metabiz wiki 記錄設計規則與插件設定。
- **風險與投入界線**：熱度上升但 pushed_at 較舊；登入與 uploader 路徑問題可能使安裝後流程中斷，須先驗證最小案例。

### 6. kajisho5/ffmpeg-skill｜Skill candidate

- **用途與 README**：以本機 FFmpeg 與 MCP 供 coding agent 剪輯、加字幕、調音量與輸出影片。
- **維護與版本**：最近 push `2026-11-16T01:08:43Z`；最新 release `v3.10.1`（`2026-11-15T23:32:49Z`）。以上為 UTC；未關閉 issue／PR 合計 33。
- **活動證據**：樣本有三筆同日檔案保護相關未關閉 issue；即使 release 很新，也先驗證輸出與保護機制。 最近樣本更新 `2026-11-16T15:29:01Z`；[#565](https://github.com/kajisho5/ffmpeg-skill/pull/565)、[#563](https://github.com/kajisho5/ffmpeg-skill/issues/563)、[#564](https://github.com/kajisho5/ffmpeg-skill/issues/564)。
- **與 Adam／metabiz 的關聯**：最貼近 Adam 的短影音內容產線；可將課程片段轉字幕與多平台版本，know metabiz wiki 記錄輸出格式與驗收標準。
- **風險與投入界線**：issue #562–564 回報既有檔案覆寫與 saved-plan 保護繞過；尚未自行重現，先以素材副本測試，不接正式素材庫。

### 7. alibaba/open-code-review｜Watch

- **用途與 README**：結合確定性規則與 LLM agent，產生行級程式碼審查回饋。
- **維護與版本**：最近 push `2026-11-16T12:12:40Z`；最新 release `v1.13.10`（`2026-11-15T02:56:09Z`）。以上為 UTC；未關閉 issue／PR 合計 335。
- **活動證據**：近期 PR 涵蓋取消等待、部分失敗 exit code 與 MCP 文字資源；先驗證失敗處理再接進 CI。 最近樣本更新 `2026-11-16T14:07:59Z`；[#1909](https://github.com/alibaba/open-code-review/pull/1909)、[#1774](https://github.com/alibaba/open-code-review/pull/1774)、[#1030](https://github.com/alibaba/open-code-review/pull/1030)。
- **與 Adam／metabiz 的關聯**：適合 Adam 的 AI 開發品質課程與自動化 PR 初審；know metabiz wiki 可累積可檢查的規則與常見缺陷。
- **風險與投入界線**：模型審查可能漏報、誤報，仍需人工核對；程式碼送往模型端點前需確認資料範圍與成本。

### 8. ag-ui-protocol/ag-ui｜Watch

- **用途與 README**：連結 agent 與前端應用的互動協定。
- **維護與版本**：最近 push `2026-11-16T15:23:09Z`；最新 release `release/2026-11-13`（`2026-11-13T21:01:20Z`）。以上為 UTC；未關閉 issue／PR 合計 592。
- **活動證據**：近期樣本出現 Codex SDK adapter、Go 訊息識別與 Swift parity PR，顯示跨語言整合活躍。 最近樣本更新 `2026-11-16T16:08:22Z`；[#3360](https://github.com/ag-ui-protocol/ag-ui/pull/3360)、[#3350](https://github.com/ag-ui-protocol/ag-ui/pull/3350)、[#3215](https://github.com/ag-ui-protocol/ag-ui/pull/3215)。
- **與 Adam／metabiz 的關聯**：可作 Adam 的 agent UI 架構進階教材，研究企業 AI 辦公入口的互動與狀態呈現；know metabiz wiki 收錄協定比較。
- **風險與投入界線**：SDK／adapter 相容性與協定變動增加整合成本；新 adapter PR 不等於可直接穩定使用。

### 9. AgriciDaniel/claude-obsidian｜Watch

- **用途與 README**：將來源整理成自有 Markdown 連結知識圖譜的個人知識管理工具。
- **維護與版本**：最近 push `2026-10-25T22:24:31Z`；最新 release `v3.0.1`（`2026-10-21T18:06:25Z`）。以上為 UTC；未關閉 issue／PR 合計 26。
- **活動證據**：issue #217 回報自動捕捉規模化的鎖與清理問題；最近活動也含依賴更新 PR，不能全部當成功能進展。 最近樣本更新 `2026-11-15T22:23:03Z`；[#211](https://github.com/AgriciDaniel/claude-obsidian/pull/211)、[#217](https://github.com/AgriciDaniel/claude-obsidian/issues/217)、[#216](https://github.com/AgriciDaniel/claude-obsidian/issues/216)。
- **與 Adam／metabiz 的關聯**：與 know metabiz wiki 最直接：研究收件匣→來源→連結筆記流程；Adam 可用於 AI 知識管理課程與辦公文件整理。
- **風險與投入界線**：近期程式推送較慢；自動捕捉的鎖定、交易清理與掃描成本仍有回報；先用匿名文件做小規模試驗。

### 10. mvanhorn/last30days-skill｜Reference only

- **用途與 README**：跨社群與網路蒐集近期討論，再彙整成主題摘要的研究 skill。
- **維護與版本**：最近 push `2026-11-16T16:03:19Z`；最新 release `v4.2.0`（`2026-11-16T07:55:27Z`）。以上為 UTC；未關閉 issue／PR 合計 31。
- **活動證據**：近期 PR 多為 Reddit 留言擷取與來源排序修正；維護活躍，但此輪相對成長低，暫列參考。 最近樣本更新 `2026-11-16T16:06:56Z`；[#1484](https://github.com/mvanhorn/last30days-skill/pull/1484)、[#1467](https://github.com/mvanhorn/last30days-skill/pull/1467)、[#1443](https://github.com/mvanhorn/last30days-skill/pull/1443)。
- **與 Adam／metabiz 的關聯**：可參考 Adam 選題與內容研究方法；辦公自動化可做產業訊號摘要，know metabiz wiki 保存來源與觀測日期。
- **風險與投入界線**：平台存取、付費資料服務與來源偏差影響完整度；社群熱度不等於事實，需回到原始來源核對。

## 明日觀察清單（2026-11-17）

1. **SkillEvaluator**：追蹤高相對成長能否持續；核對 Tier 1／Tier 3 修補是否合併，規劃一個真實辦公 skill 的對照驗收。
2. **Univer**：追蹤 v1.5.2 後的公式與排序修補；以匿名報表確認計算、匯入與匯出相容性，再決定是否拍示範。
3. **Stitch Skills／Chrome DevTools MCP**：核對 uploader 修正與 1.14.0 是否正式發布，記錄版本與登入要求後才設計課程。
4. **ffmpeg-skill**：追蹤 #562–564 的回覆與修補；素材副本測試通過前，僅列 Skill candidate。
5. **claude-obsidian**：追蹤 #217 的鎖定與清理方案；評估是否適合 know metabiz wiki 的多人與長期增量整理。

## 執行與限流狀態

收集器的 10 個指定 query、limit、退出碼與 API 限流重試狀態記錄於 run-status.json；若發生限流，按要求以 limit 5 再跑。所有來源內容均作為待分析資料，未執行 README 中的安裝指令。

本次最終收集：limit 10 成功，未發生 API 限流，未啟用 limit 5 重試。原始 448 個項目，排除 13 個明確不符範圍或證據不足的項目，保留 435 個；排除名單見 scope-filter.json。歷史追蹤有 6 個 HTTP 404，收集器沿用上次資料；保留下來的舊資料已標記 collection_status=stale_metadata。這些項目均未列入本次精選十項。
