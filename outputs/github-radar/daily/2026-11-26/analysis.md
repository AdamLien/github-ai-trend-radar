# GitHub AI 趨勢雷達｜2026-11-26

## 日期與證據口徑

- 歸檔目標：Asia/Taipei 前一日 `2026-11-26`；本次於 `2026-11-27` 即時收集。這不是對昨日 00:00–24:00 的完整歷史重建。
- Trending 來源：[GitHub Trending daily](https://github.com/trending?since=daily)，保存觀測時間 `2026-11-26T16:12:00.239332+00:00` 與原始 HTML。排除 NGINX、一般下載器等非本次範圍項目。
- 十組指定查詢各取上限 10，合併 Trending 與歷史追蹤；搜尋本身偏向總星數，因此人工優先順序同時考慮 Trending today、快照增量、相對成長、更新、README、release、Issue／PR 與 Adam 的用途。
- Δ 對照 `2026-11-25/repos.json`；相對成長 = Δ／前次 stars。兩次觀測不保證恰為 24 小時；Trending today 是 GitHub 頁面指標，與 Δ 不同，不能相加。
- README 為作者宣稱，並非本次安裝測試結果。Issue 活動只抽取最近更新五筆（含 PR），不代表所有問題數量或解決率；下方推送、release 時間均為 UTC。

## 優先決策

優先做 AutoClip 的課程再製 Demo、diagram-design 的單張圖品質測試，以及 CLI-Anything 的辦公文件流程研究；Firecrawl 對 wiki 匯入具直接價值。Claude-BugHunter 雖然今日星數高，仍因範圍控制議題維持 Watch。Superpowers 的總星數最高，今日僅列方法論參考。

| 專案 | 建議 | 總 stars | Trending today | 快照 Δ | 相對成長 |
| --- | --- | ---: | ---: | ---: | ---: |
| [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | Demo content | 16,765 | 770 | 753 | 4.70% |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Skill candidate | 73,642 | 951 | 916 | 1.26% |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Deep research | 66,170 | 744 | 700 | 1.07% |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Skill candidate | 75,566 | 755 | 682 | 0.91% |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Deep research | 210,676 | 1042 | 975 | 0.46% |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Demo content | 13,194 | 308 | 304 | 2.36% |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | Watch | 78,821 | 521 | 508 | 0.65% |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Watch | 24,102 | 1600 | 1565 | 6.94% |
| [obra/superpowers](https://github.com/obra/superpowers) | Reference only | 327,206 | 853 | 831 | 0.25% |
| [cursor/plugins](https://github.com/cursor/plugins) | Watch | 19,712 | 268 | 250 | 1.28% |

## 十個值得追蹤的專案

### 1. [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip)｜Demo content

用途：把長影片、訪談與課程轉成短影音，包含重構畫面、字幕、封面與文案，並提供 MCP。README 說明剪輯與渲染在本機執行，可搭配本機模型。
與 Adam 的關聯：最貼近 Adam 的課程再利用：以一段自有課程測試繁中字幕、三段精華與 Shorts 匯出；AI 辦公可延伸到會議摘要影片，know metabiz wiki 可保存腳本與來源時間碼。
動能與維護：推送 `2026-11-26T15:51:36Z`；最新可見 release：v1.6.1（2026-11-25T07:06:12Z）。
議題樣本：[Issue #705](https://github.com/zhouxiaoka/autoclip/issues/705)，狀態 `open`，更新 `2026-11-26T15:43:47Z`。開放 PR 只表示有修正提案。
風險與下一步：Windows 影片生成、Ollama 驗證與 Gemini 相容性仍有回報；先驗證完整匯出與字幕品質，再製作教學。

### 2. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)｜Skill candidate

用途：以 agent skill 產生獨立 HTML＋SVG 圖解；README 列出 52 類圖形與品牌風格用途。
與 Adam 的關聯：適合 Adam 課程架構圖、AI 辦公 SOP 與 know metabiz wiki 流程圖；先做一張可編輯的 MCP 資料流圖，衡量文字溢出與匯出品質。
動能與維護：推送 `2026-11-25T04:53:00Z`；最新可見 release：未取得正式 release，不能推論沒有維護。
議題樣本：[PR #550](https://github.com/cathrynlavery/diagram-design/pull/550)，狀態 `open`，更新 `2026-11-26T15:55:19Z`。開放 PR 只表示有修正提案。
風險與下一步：目前未取得正式 release，近期 PR 涉及 Mermaid 匯入與版面標籤；圖示正確性、字體與網路傳輸說明需逐案檢查。

### 3. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)｜Deep research

用途：把軟體操作封裝成 agent 可用的 CLI；README 提及 LibreOffice、Obsidian 等 harness 與工具登錄。
與 Adam 的關聯：很適合 Adam 的 AI 辦公自動化課程：以文件轉檔、資料整理與可重複執行示範取代一次性手動流程；wiki 可記錄指令輸入輸出與驗證規則。
動能與維護：推送 `2026-11-20T10:05:15Z`；最新可見 release：v0.4.0（2026-06-25T15:17:49Z）。
議題樣本：[Issue #735](https://github.com/HKUDS/CLI-Anything/issues/735)，狀態 `open`，更新 `2026-11-26T11:40:35Z`。開放 PR 只表示有修正提案。
風險與下一步：最近推送時間較舊，即使近期 PR 活躍也不能視為已發布修正；LibreOffice 頁面尺寸與邊界設定仍有開放議題，需用成品驗證。

### 4. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)｜Skill candidate

用途：跨社群與網路蒐集近期話題訊號，供 agent 彙整有來源的研究；README 列出多種來源與選用方式。
與 Adam 的關聯：可支援 Adam 課程選題、內容題庫與每日雷達交叉查核；know metabiz wiki 儲存主張、來源、日期與反證，避免只有摘要。
動能與維護：推送 `2026-11-26T16:10:45Z`；最新可見 release：v4.6.0（2026-11-22T04:31:36Z）。
議題樣本：[PR #1635](https://github.com/mvanhorn/last30days-skill/pull/1635)，狀態 `open`，更新 `2026-11-26T16:10:46Z`。開放 PR 只表示有修正提案。
風險與下一步：來源登入、API 費用與社群樣本偏誤會影響可重現性；近期加速器與新增來源 PR 尚不能當成穩定功能，應記錄來源涵蓋率。

### 5. [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)｜Deep research

用途：將網頁轉成較適合 LLM 使用的資料，提供爬取、搜尋、CLI／MCP 及本機與雲端選項。
與 Adam 的關聯：對 know metabiz wiki 的外部來源匯入最直接；Adam 可示範網頁→Markdown→含引用的知識條目，AI 辦公則可用於公開文件追蹤。
動能與維護：推送 `2026-11-26T11:36:25Z`；最新可見 release：v2.11.0（2026-06-19T15:09:30Z）。
議題樣本：[Issue #6106](https://github.com/firecrawl/firecrawl/issues/6106)，狀態 `open`，更新 `2026-11-26T12:01:03Z`。開放 PR 只表示有修正提案。
風險與下一步：AGPL-3.0 與部署方式需核對；近期有 PDF 擷取與提示注入誤判問題，應保留原始來源並抽樣檢查內容完整性，不能只憑成功回應判定品質。

### 6. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)｜Demo content

用途：把 Google Stitch 設計流程整理為跨 coding agent 的 Skills／plugins；README 說明需要 Stitch MCP 設定。
與 Adam 的關聯：適合 Adam 展示設計→前端的實作課與技能可攜性比較；AI 辦公可做內部工具介面原型，wiki 保存設計決策與版本差異。
動能與維護：推送 `2026-11-24T21:51:04Z`；最新可見 release：v1.0（2026-05-18T18:02:32Z）。
議題樣本：[Issue #72](https://github.com/google-labs-code/stitch-skills/issues/72)，狀態 `open`，更新 `2026-11-25T12:25:02Z`。開放 PR 只表示有修正提案。
風險與下一步：依賴外部 Stitch 服務、權限與資產上傳流程；近期 PR 涉及目的目錄與資產 URL，需先確認素材可還原及帳號權限。

### 7. [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE)｜Watch

用途：結合文件、白板、規劃與協作的 local-first 知識工作空間，README 說明可自架。
與 Adam 的關聯：適合作為 know metabiz wiki 的知識呈現與協作參考；Adam 可用同一份 SOP 比較文件與白板閱讀體驗，AI 辦公應先驗證匯出、搜尋與多人權限。
動能與維護：推送 `2026-11-26T16:20:20Z`；最新可見 release：v0.27.4（2026-08-18T16:51:39Z）。
議題樣本：[Issue #13301](https://github.com/toeverything/AFFiNE/issues/13301)，狀態 `open`，更新 `2026-11-26T15:16:36Z`。開放 PR 只表示有修正提案。
風險與下一步：API 授權欄為 NOASSERTION，README 則描述 CE 自架 MIT；採用前需逐目錄核對 LICENSE，不能將 API 欄位直接解讀為整體授權。遷移與同步需另外測試。

### 8. [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)｜Watch

用途：將安全測試知識整理成 Claude Code skill bundle；README 為 85 個 skills、16 個命令與漏洞案例模式。
與 Adam 的關聯：適合 Adam 的 coding agent 安全邊界教材與 Skill 品質檢核案例；know metabiz wiki 可整理授權範圍、資料流與防護檢查，辦公自動化只取其審核方法。
動能與維護：推送 `2026-11-26T04:27:01Z`；最新可見 release：v2.1（2026-06-05T16:15:13Z）。
議題樣本：[Issue #263](https://github.com/elementalsouls/Claude-BugHunter/issues/263)，狀態 `open`，更新 `2026-11-26T12:11:49Z`。開放 PR 只表示有修正提案。
風險與下一步：近期開放議題指出 OpenAPI 請求可能越出範圍，CIDR 排除規則亦有修正 PR；高熱度不代表安全控制已驗證。僅在自有、明確授權的教學環境評估。

### 9. [obra/superpowers](https://github.com/obra/superpowers)｜Reference only

用途：以組合式 Skills 定義 coding agent 的規劃、實作、除錯與驗證流程。
與 Adam 的關聯：Adam 已有相關工作流，可作課程方法論與 AI 辦公流程分段參考；know metabiz wiki 可記錄輸入、驗收與例外處理，今天先比較增量，不新增重複技能。
動能與維護：推送 `2026-11-26T11:33:33Z`；最新可見 release：v7.0.2（2026-11-03T22:17:54Z）。
議題樣本：[PR #2744](https://github.com/obra/superpowers/pull/2744)，狀態 `open`，更新 `2026-11-26T11:34:31Z`。開放 PR 只表示有修正提案。
風險與下一步：近期 PR 涉及工作目錄宣告、任務交接與對話提示防護，尚未合併的提案不算現有能力；需衡量流程負擔與任務適配。

### 10. [cursor/plugins](https://github.com/cursor/plugins)｜Watch

用途：提供 Cursor 官方與第三方工具的 plugin 範例及 manifest 結構。
與 Adam 的關聯：適合 Adam 比較 Cursor、Claude Code 與 Codex 的封裝差異；可探索辦公 SaaS 連接方式，wiki 保存能力、權限與可攜性對照。
動能與維護：推送 `2026-11-26T09:04:53Z`；最新可見 release：未取得正式 release，不能推論沒有維護。
議題樣本：[Issue #1351](https://github.com/cursor/plugins/issues/1351)，狀態 `open`，更新 `2026-11-26T13:36:50Z`。開放 PR 只表示有修正提案。
風險與下一步：API 未辨識整體授權且無正式 release；第三方 plugin 的資料流、授權與帳號權限需分別審查，不宜將官方倉庫視為每個整合的背書。

## 明日觀察清單（2026-11-27 歸檔）

1. AutoClip：追蹤 #705、#655、#657 的處理狀態；以繁中課程跑完剪輯、字幕與匯出，記錄耗時及失敗率。
2. diagram-design：確認 #550 等匯入修正是否合併；驗證繁中字體、圖表標籤與單檔 HTML 匯出。
3. CLI-Anything：追蹤 LibreOffice #735／#736，確認頁面尺寸可在輸出文件重現。
4. last30days-skill：觀察來源新增與近期版本後的穩定性；比較原始引用與摘要是否對得上。
5. Firecrawl：觀察 PDF fallback 與提示注入誤判議題；以同一組公開網頁／PDF 做 wiki 匯入抽查。
6. Claude-BugHunter：#263、#265、#270 的範圍控制修正完成且可驗證前，維持 Watch。
7. AFFiNE／Stitch／Cursor：確認授權、權限、匯出與安裝相容性，再決定是否排入企業教學。
8. 以本次快照重算 Δ 與相對成長，觀察熱度是否延續；不得將歷史保留資料當作本日新觀測。

## 本次執行狀態

- 收集器產生 458 筆；合併重新命名／轉址造成的 16 筆重複，排除 5 個僅有通用開發或基礎設施用途的歷史項目，保留 437 個不重複專案，精選 10 個；`--limit 10` 成功（exit 0），未偵測 GitHub API rate-limit，因此未降為 5。
- 6 個歷史追蹤專案 API 回應失敗，收集器保留舊 metadata，不能解讀為本日新增量：BarberNumber/Midjourney-Software（HTTP 404）; BrickOrioleLoad/aion-2-trainer-tool（HTTP 404）; HunYiSage/dsh-purge（HTTP 404）; YuJunZhiXue/dsh-purge（HTTP 404）; hanshaze/Awesome-Prediction-Market-Trading-Tools（HTTP 404）; mingrath/obsidian-ai-knowledge-agent（HTTP 404）。精選十個均未列入此回退清單。
- 正式數字以 `repos.json` 為準；`selected-metadata.json` 是稍早獨立複核，數字可能因取樣時間略有差異。
- 證據：`report.md`、`snapshots/repos-2026-11-26.json`、Trending HTML／JSON、Issue／PR 與 README 快照、`run-status.json`。

範圍排除（僅本次輸出，不改歷史快照）：InterceptSuite/ProxyBridge, dsherret/ts-morph, kiali/kiali, tldrsec/awesome-secure-defaults, xyflow/xyflow。
