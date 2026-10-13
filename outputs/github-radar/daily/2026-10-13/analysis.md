# GitHub AI 趨勢雷達｜2026-10-13

目標日期依 Asia/Taipei 前一日計算；補跑實際採集時間：2026-10-13T16:12:47.297806+00:00（UTC）。這是當下 API 與 Trending 的觀察，不是昨日收盤或歷史 Trending 重建。

## 取樣與判讀

- 以十組指定查詢各取最多 10 個結果，合併 [GitHub Trending daily](https://github.com/trending?since=daily) 與歷史追蹤名單；實際採集與降量重試狀態見 collection-status.json。
- 今日星數為 Trending 頁面欄位；快照增量比較 2026-10-12 的已存總星數，相對成長＝增量／前次總星數。兩者觀察窗口不同，不能互相替代，也不是精確 24 小時成長。沒有前值時標示未量測，不把新收錄當成零成長。
- 優先順序綜合今日星數、快照增量、相對成長、最近程式推送、README、release 與近期 issue／PR；總星數只提供規模背景。AI 辦公與 know metabiz wiki 的實際關聯可讓較低增長專案取得研究優先權。
- updated_at 可能只反映互動，因此以 pushed_at 評估程式更新。open_issues 包含 PR，不能當成純 bug 數；近期五筆 issue／PR 是活動樣本，沒有用數量推定品質或解決率。
- VoiceStudio 與 ArtCraft 的 AI topics 補足簡介關鍵字漏判。gods-eye-view 與 xtool 的此次卡片／簡介不足以確認 AI／agent／開發自動化核心用途，因此不列入今日推薦。
- 未執行、安裝或採納任何候選 repo 的指令；功能與效能宣稱僅是研究線索。

## 十個值得關注的專案

| 優先序／專案 | 行動分類 | 今日星數 | 快照增量 | 相對成長 | 總星數 |
| --- | --- | ---: | ---: | ---: | ---: |
| 1. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Skill candidate | 1,813 | +1,602 | 3.08% | 53,696 |
| 2. [mksglu/context-mode](https://github.com/mksglu/context-mode) | Deep research | 978 | +959 | 3.55% | 27,953 |
| 3. [storytold/artcraft](https://github.com/storytold/artcraft) | Demo content | 4,078 | +4,023 | 19.46% | 24,694 |
| 4. [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Demo content | 1,691 | +2,199 | 3.67% | 62,141 |
| 5. [vercel-labs/skills](https://github.com/vercel-labs/skills) | Skill candidate | 187 | +302 | 0.89% | 34,275 |
| 6. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Deep research | 未上榜 | +71 | 0.35% | 20,621 |
| 7. [activepieces/activepieces](https://github.com/activepieces/activepieces) | Deep research | 未上榜 | +8 | 0.03% | 25,031 |
| 8. [lyogavin/airllm](https://github.com/lyogavin/airllm) | Watch | 1,004 | +884 | 2.37% | 38,114 |
| 9. [morluto/rea](https://github.com/morluto/rea) | Watch | 54,706 | +54,234 | 38.13% | 196,463 |
| 10. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference only | 未上榜 | +41 | 0.04% | 91,210 |

### 1. cathrynlavery/diagram-design — Skill candidate

**用途：** 以單一 HTML＋SVG 製作品牌化圖解，README 與簡介的圖種數分別為 45 與 44，顯示文件版本仍需核對。
**動能與維護：** 最近程式推送 `2026-10-13T14:57:55Z`；API 更新 `2026-10-13T16:12:38Z`；最新 release：API 未取得最新 release，不能據此斷言沒有版本。開啟 issue／PR 合計 37。近期已關閉外層 Markdown fence 誤判 Mermaid 範例的問題；仍有樣式匯出修正 PR。
**對 Adam／metabiz 的價值：** 適合 Adam 的 AI 課程講義、短影音架構圖與 know metabiz wiki 的流程說明；先用一張會員服務流程圖做內容範例。
**風險與限制：** Mermaid 匯入與匯出樣式仍在修正；採用時需驗證分支語意、SVG 可讀性與輸出授權，不能只看圖片好看。
**查核來源：** [README 與專案](https://github.com/cathrynlavery/diagram-design)、[release](https://github.com/cathrynlavery/diagram-design/releases)、[近期活動證據](https://github.com/cathrynlavery/diagram-design/issues/419)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 2. mksglu/context-mode — Deep research

**用途：** 透過 MCP、hooks 與工具輸出隔離降低 coding agent 的上下文占用，並保留工作階段記憶；98% 壓縮是專案宣稱，尚未實測。
**動能與維護：** 最近程式推送 `2026-10-12T18:05:18Z`；API 更新 `2026-10-13T16:12:37Z`；最新 release：v1.0.169（2026-06-29T18:18:53Z）。開啟 issue／PR 合計 354。近期 Windows 安裝 SQLite 依賴會觸發 npm 錯誤，相關 macOS 安裝路徑也有回報；MCP handshake 修正尚在 PR。
**對 Adam／metabiz 的價值：** 對 Adam 的 coding agent 課程與 AI 辦公長任務有直接價值；以讀取大型報表、文件與工具 log 比較 token、正確率與恢復能力。
**風險與限制：** 安裝涉及原生 SQLite 依賴，且跨平台 routing／hook 相容性仍有修正；API 授權欄位未提供可確定的 SPDX，需另讀 LICENSE。
**查核來源：** [README 與專案](https://github.com/mksglu/context-mode)、[release](https://github.com/mksglu/context-mode/releases)、[近期活動證據](https://github.com/mksglu/context-mode/issues/1139)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 3. storytold/artcraft — Demo content

**用途：** 結合 AI 影像／影片與創作介面的藝術工作台，適合探索內容製作流程，而非視為已驗證的成品產線。
**動能與維護：** 最近程式推送 `2026-10-11T13:47:59Z`；API 更新 `2026-10-13T16:12:40Z`；最新 release：artcraft-v0.41.0（2026-09-26T11:14:22Z）。開啟 issue／PR 合計 312。近期有啟動器故障回報，另有介面翻譯與外部模型整合討論。
**對 Adam／metabiz 的價值：** 可做 Adam 的 AI 創作工具示範與課程素材前製；與辦公自動化關聯較低，know metabiz wiki 可記錄素材來源與操作經驗。
**風險與限制：** 高相對成長仍須連續觀察；近期 launcher 故障回報未關閉，第三方模型成本、輸出權利與可重現性需實測。
**查核來源：** [README 與專案](https://github.com/storytold/artcraft)、[release](https://github.com/storytold/artcraft/releases)、[近期活動證據](https://github.com/storytold/artcraft/issues/2276)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 4. debpalash/VoiceStudio — Demo content

**用途：** 本地語音複製、配音、轉錄與有聲內容工具，topics 明確標示 AI；646 語言等涵蓋範圍屬專案宣稱。
**動能與維護：** 最近程式推送 `2026-10-13T15:04:49Z`；API 更新 `2026-10-13T16:12:37Z`；最新 release：v0.5.6（2026-09-23T08:53:32Z）。開啟 issue／PR 合計 125。近期 API URL 驗證與音訊處理修正仍在 PR，活躍開發不代表所有修正已發行。
**對 Adam／metabiz 的價值：** 適合 Adam 的繁中課程配音、短影音與會議逐字稿示範；可把逐字稿納入 know metabiz wiki 的來源層。
**風險與限制：** AGPL-3.0 對服務整合有授權影響，模型另有條款；繁中音質、硬體需求與語音使用權必須依素材確認。
**查核來源：** [README 與專案](https://github.com/debpalash/VoiceStudio)、[release](https://github.com/debpalash/VoiceStudio/releases)、[近期活動證據](https://github.com/debpalash/VoiceStudio/pull/2704)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 5. vercel-labs/skills — Skill candidate

**用途：** 跨 coding agent 的 Skill 管理 CLI；README 列出 Claude Code、Codex、Cursor 等工具支援。
**動能與維護：** 最近程式推送 `2026-10-09T17:54:47Z`；API 更新 `2026-10-13T16:12:37Z`；最新 release：v1.7.2（2026-10-09T16:46:55Z）。開啟 issue／PR 合計 1,107。近期全域更新的目錄副作用回報與修正 PR 仍開啟，另有移除及 lock 清理修正。
**對 Adam／metabiz 的價值：** 適合 Adam 的 Skills 課程與團隊技能分發；可研究如何讓辦公文件整理 Skill 在多工具間維持版本一致，wiki 記錄採用清單。
**風險與限制：** 近期全域更新會建立未安裝 agent 目錄的問題未結案；第三方 Skill 可執行任意指令，應逐一檢視內容與權限。
**查核來源：** [README 與專案](https://github.com/vercel-labs/skills)、[release](https://github.com/vercel-labs/skills/releases)、[近期活動證據](https://github.com/vercel-labs/skills/issues/2331)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 6. nashsu/llm_wiki — Deep research

**用途：** 把文件增量整理成持久、互連的 wiki，適合比較來源整理與每次 RAG 檢索的差異。
**動能與維護：** 最近程式推送 `2026-09-28T01:43:23Z`；API 更新 `2026-10-13T16:06:50Z`；最新 release：v0.6.12（2026-09-28T02:58:13Z）。開啟 issue／PR 合計 275。Windows 週期性掃描／雜湊負載問題仍開啟，改善 rescan 與內容 hash 的 PR 待驗證。
**對 Adam／metabiz 的價值：** 與 know metabiz wiki 最直接相關；以少量公開文件評估來源引用、去重、增量更新與錯誤更正，也可轉成 Adam 的知識管理課程。
**風險與限制：** 主分支推送與 release 已隔一段時間；桌面背景掃描耗 CPU 的回報仍開啟，個人桌面設計不等於企業權限治理，授權 API 為 NOASSERTION。
**查核來源：** [README 與專案](https://github.com/nashsu/llm_wiki)、[release](https://github.com/nashsu/llm_wiki/releases)、[近期活動證據](https://github.com/nashsu/llm_wiki/issues/812)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 7. activepieces/activepieces — Deep research

**用途：** 以 AI agents、MCP 與視覺化工作流程串接辦公服務，提供企業流程自動化研究入口。
**動能與維護：** 最近程式推送 `2026-10-13T16:01:16Z`；API 更新 `2026-10-13T15:37:15Z`；最新 release：0.92.3（2026-10-12T18:43:34Z）。開啟 issue／PR 合計 704。近期修正資料未改變時仍觸發流程的問題，PR 尚未合併，適合當作冪等性教材。
**對 Adam／metabiz 的價值：** 適合 Adam 的 AI 辦公自動化課程及 metabiz 報表、會員服務流程；知識文件輸入 wiki 前可加審核節點。
**風險與限制：** 總星數成長較慢但 release 與程式推送新；連接器權限、重試、冪等性與授權範圍仍需逐項確認，未實作 mCRM 整合。
**查核來源：** [README 與專案](https://github.com/activepieces/activepieces)、[release](https://github.com/activepieces/activepieces/releases)、[近期活動證據](https://github.com/activepieces/activepieces/pull/16468)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 8. lyogavin/airllm — Watch

**用途：** 透過記憶體管理探索大模型在低 VRAM 環境的執行；README 的大型模型與低顯存數字是作者宣稱。
**動能與維護：** 最近程式推送 `2026-10-13T06:24:34Z`；API 更新 `2026-10-13T16:12:37Z`；最新 release：v4.0.0（2026-09-05T15:43:11Z）。開啟 issue／PR 合計 164。近期仍有每次查詢耗時極長的回報，另有訓練與非 CUDA quickstart 修正 PR。
**對 Adam／metabiz 的價值：** 可做 Adam 的本地 LLM 成本與效能課程研究；若要支援辦公問答或 wiki，需要先驗證延遲、磁碟與模型授權。
**風險與限制：** 低 VRAM 不等於低總成本或可互動速度；已有極慢推論 issue，不能據此向企業承諾效能。
**查核來源：** [README 與專案](https://github.com/lyogavin/airllm)、[release](https://github.com/lyogavin/airllm/releases)、[近期活動證據](https://github.com/lyogavin/airllm/issues/374)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 9. morluto/rea — Watch

**用途：** 以 agents 執行應用與原生 binary 的逆向工程，含 MCP 與多 coding agent 生態整合。
**動能與維護：** 最近程式推送 `2026-10-13T16:11:23Z`；API 更新 `2026-10-13T16:12:39Z`；最新 release：rea-agents-6.4.0（2026-10-11T03:58:03Z）。開啟 issue／PR 合計 528。近期 MCP schema、artifact 與 source map 修正 PR 活躍，不能把開啟中的 PR 當成已發行功能。
**對 Adam／metabiz 的價值：** 適合 Adam 的進階 agent 工具鏈內容，但與日常 AI 辦公、know metabiz wiki 的直接關聯較低；限於自有或獲授權的教材樣本評估。
**風險與限制：** 今日星數與快照增幅異常突出，尚未驗證成長來源與使用品質；逆向工程範圍、執行隔離與依賴成本需確認，熱度不等於推薦安裝。
**查核來源：** [README 與專案](https://github.com/morluto/rea)、[release](https://github.com/morluto/rea/releases)、[近期活動證據](https://github.com/morluto/rea/pull/2877)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

### 10. modelcontextprotocol/servers — Reference only

**用途：** MCP 的參考 server 實作；README 明確把它定位為示範 SDK／協定能力的參考集合。
**動能與維護：** 最近程式推送 `2026-10-13T05:54:47Z`；API 更新 `2026-10-13T16:08:03Z`；最新 release：v1.0.0（2026-10-11T02:40:29Z）。開啟 issue／PR 合計 480。近期自動 version PR 未執行 CI 的問題已關閉並有修正 PR，顯示釋出流程仍值得追蹤。
**對 Adam／metabiz 的價值：** 可作 Adam 的 MCP 課程、安全連接器設計與辦公工具串接教材；know metabiz wiki 可建立工具介面與權限規範的參考頁。
**風險與限制：** 參考 server 應用前仍需補正式環境的驗證、權限與營運機制；高總星數與 issue 數不能視為部署成熟度，授權需核實。
**查核來源：** [README 與專案](https://github.com/modelcontextprotocol/servers)、[release](https://github.com/modelcontextprotocol/servers/releases)、[近期活動證據](https://github.com/modelcontextprotocol/servers/issues/5110)。README 摘要與五筆近期 issue／PR 存於 editorial-evidence.json；數據以 repos.json 與 snapshots/ 為準。

## 明日觀察清單｜2026-10-14

1. **diagram-design：** 用公開的會員流程測試中文標籤、分支語意、Mermaid 匯入與 SVG 匯出，確認今天修正是否進入主分支。
2. **context-mode：** 追蹤 #1139／#1174 安裝問題與 MCP handshake PR；記錄可重現版本後，才設計 token 節省實驗。
3. **ArtCraft／VoiceStudio：** 追蹤今天的高相對成長是否持續；用非敏感素材驗證啟動、繁中配音、成品品質與模型成本。
4. **vercel-labs/skills：** 觀察 #2331 全域更新問題與未安裝 agent 目錄修正，評估技能鎖定版本與跨工具移除行為。
5. **llm_wiki：** 追蹤 #812 背景 CPU／掃描問題，設計 know metabiz wiki 的來源引用、增量同步與修訂驗證資料集。
6. **Activepieces：** 追蹤無實際變更仍觸發流程的修正與 0.92.3 後續版本，整理 AI 辦公自動化的重試／冪等性教材。
7. **AirLLM／rea：** 前者先測量可用延遲，後者先核對異常星數動能是否續增；暫維持 Watch，避免把宣稱與熱度直接轉成產品推薦。
8. **MCP servers：** 追蹤 version PR 的 CI 與 release 差異，作為參考實作教學素材。

## 採集狀態與資料限制

採集完成：十組查詢使用 --limit 10，合併 354 個追蹤專案，其中 7 個為此次範圍內的 Trending；未遇 API rate-limit，無需 --limit 5 重試。補查十個候選的 README、release 與五筆近期 issue／PR 亦全部成功。排名是編輯研究優先序，並非安裝或採購建議。今日星數可能與 API 總星數差異時間點不同，負增量亦可能由 star 撤回或快照窗口造成；所有推論需再以實測確認。
