# GitHub AI 趨勢雷達｜2026-11-28

本次執行：2026-11-29T00:10:51.886527+08:00 至 2026-11-29T00:22:43.728804+08:00（Asia/Taipei）。目標日期為執行日前一個台北日曆日。

## 判讀方法與資料邊界

- 已從專案根目錄執行全部 10 組指定查詢，每組 `--limit 10`，包含 Trending daily 與 README。共取得 458 筆累積追蹤資料；Trending 16 筆中保留 14 筆，排除 NGINX 與一般下載器。
- [GitHub Trending daily](https://github.com/trending?since=daily) 是執行當下的滾動頁面，stars today 不是台北 11/28 的完整日增量；此次按 11/28 歸檔，並未重建歷史午夜快照。頁面擷取的專案卡片與篩選清單見 `trending-evidence.json`；不保留含暫態網頁欄位的 HTML。
- 快照星差以 2026-11-27 為基準，代表兩次實際採集間的差值；相對成長＝星差 ÷ 前次總星數。新進且缺基準者標為未測得；未登 Trending 者的 stars today 為未上榜，並非零。
- 優先綜合 stars today、星差、相對成長、近期 push、release、README 摘要及最近更新的 issue／PR；再以 Adam 的課程／內容、AI 辦公與 know metabiz wiki 實用性決定處置。下列是編輯建議順序，並非總星數榜。
- README 僅取得前 700 字元，部分為圖片與徽章，無法取代完整文件審查或實際安裝測試。open_issues 計數包含 PR；最新更新的 5 筆 issue／PR 只是活動樣本，不能推論回覆速度或整體品質。
- 本次未觀察到 GitHub API rate-limit 錯誤，無需降至 `--limit 5`。7 個歷史項目 404 而沿用舊中繼資料，已在 JSON 標註，詳見文末；精選 10 筆均非此類項目。

## 10 個值得投入的專案

| 專案 | 總 stars | stars today | 快照星差 | 相對成長 | 處置 |
|---|---:|---:|---:|---:|---|
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 67,332 | 561 | +515 | 0.77% | Demo content |
| [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | 17,960 | 517 | +503 | 2.88% | Demo content |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 74,777 | 499 | +473 | 0.64% | Skill candidate |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 76,693 | 519 | +475 | 0.62% | Demo content |
| [obra/superpowers](https://github.com/obra/superpowers) | 328,857 | 809 | +773 | 0.24% | Skill candidate |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 212,085 | 717 | +626 | 0.30% | Deep research |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 79,751 | 495 | +469 | 0.59% | Deep research |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 3,737 | 未上榜 | +4 | 0.11% | Deep research |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 13,797 | 293 | +297 | 2.20% | Watch |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 26,912 | 1,372 | +1,291 | 5.04% | Watch |

### 1. HKUDS/CLI-Anything — Demo content

**用途與關聯：**將既有軟體包成 agent 可呼叫的 CLI，適合拆解工具介面與可驗證操作。 Adam 可示範「一句話辦公任務 → CLI → 可檢查結果」；AI 辦公自動化先選可復原的小任務，將流程與失敗案例寫入 know metabiz wiki。

**維護動能：**最近 push：2026-11-20T10:05:15Z；最新 release：[v0.4.0](https://github.com/HKUDS/CLI-Anything/releases/tag/v0.4.0)（2026-06-25T15:17:49Z）。 未結 issue／PR 合計 342；授權欄位 `Apache-2.0`。
來源：[儲存庫與 README](https://github.com/HKUDS/CLI-Anything)、[本次 API 中繼資料](https://api.github.com/repos/HKUDS/CLI-Anything)。

**風險：**近期 PR 修復 CLI-Hub 安裝無限等待；實際軟體版本、依賴與操作可靠度仍需逐項驗證。

近期活動樣本：
- [PR #728](https://github.com/HKUDS/CLI-Anything/pull/728)：更新於 2026-11-28T13:54:14Z，狀態 open。
- [PR #750](https://github.com/HKUDS/CLI-Anything/pull/750)：更新於 2026-11-28T08:49:17Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 2. zhouxiaoka/autoclip — Demo content

**用途與關聯：**把長影片轉為短片、字幕、封面與發布文案，提供桌面與 MCP 使用情境。 適合 Adam 課程精華與短影音製作，先用自有課程影片跑一次繁中流程；把剪輯規則、字幕校正與素材來源存入 know metabiz wiki。

**維護動能：**最近 push：2026-11-28T15:53:02Z；最新 release：[v1.6.3](https://github.com/zhouxiaoka/autoclip/releases/tag/v1.6.3)（2026-11-28T08:22:05Z）。 未結 issue／PR 合計 27；授權欄位 `MIT`。
來源：[儲存庫與 README](https://github.com/zhouxiaoka/autoclip)、[本次 API 中繼資料](https://api.github.com/repos/zhouxiaoka/autoclip)。

**風險：**近期 issue 回報日文被判成其他語言及 Shorts 輸出不符期待；繁中字幕、切點與引用授權必須人工驗收。

近期活動樣本：
- [issue #722](https://github.com/zhouxiaoka/autoclip/issues/722)：更新於 2026-11-28T14:19:20Z，狀態 open。
- [issue #721](https://github.com/zhouxiaoka/autoclip/issues/721)：更新於 2026-11-28T12:39:51Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 3. cathrynlavery/diagram-design — Skill candidate

**用途與關聯：**以 agent skill 產出 HTML／SVG 圖解，支援多種 coding agent。 可做 Adam 教學圖解與 AI 辦公 SOP 圖；know metabiz wiki 可收可編輯 SVG 與圖意來源，適合抽成課程圖解 skill。

**維護動能：**最近 push：2026-11-26T19:48:58Z；最新 release：API 未取得公開 release，不能推論沒有更新。 未結 issue／PR 合計 37；授權欄位 `MIT`。
來源：[儲存庫與 README](https://github.com/cathrynlavery/diagram-design)、[本次 API 中繼資料](https://api.github.com/repos/cathrynlavery/diagram-design)。

**風險：**近期 PR 涉及圖型路由與驗證器修正；視覺正確不代表流程與數值正確，輸出仍需逐圖確認。

近期活動樣本：
- [PR #557](https://github.com/cathrynlavery/diagram-design/pull/557)：更新於 2026-11-28T15:55:58Z，狀態 closed。
- [PR #555](https://github.com/cathrynlavery/diagram-design/pull/555)：更新於 2026-11-28T12:57:28Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 4. mvanhorn/last30days-skill — Demo content

**用途與關聯：**跨社群與網站蒐集近期討論並綜合研究，支援內容選題。 可用於 Adam 課程更新與影音題材研究；AI 辦公的競品／工具掃描可保存來源、時間窗與待查證事項到 know metabiz wiki。

**維護動能：**最近 push：2026-11-28T07:31:47Z；最新 release：[v4.8.1](https://github.com/mvanhorn/last30days-skill/releases/tag/v4.8.1)（2026-11-28T07:33:36Z）。 未結 issue／PR 合計 14；授權欄位 `MIT`。
來源：[儲存庫與 README](https://github.com/mvanhorn/last30days-skill)、[本次 API 中繼資料](https://api.github.com/repos/mvanhorn/last30days-skill)。

**風險：**近期 PR 仍調整研究規劃與來源平台讀取；API 費用、樣本偏差及來源可用性影響結論。

近期活動樣本：
- [PR #1431](https://github.com/mvanhorn/last30days-skill/pull/1431)：更新於 2026-11-28T14:50:50Z，狀態 closed。
- [PR #1379](https://github.com/mvanhorn/last30days-skill/pull/1379)：更新於 2026-11-28T14:23:32Z，狀態 closed。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 5. obra/superpowers — Skill candidate

**用途與關聯：**把 coding agent 開發流程整理成可組合 skills 與方法論。 適合 Adam 的 agent 工作流課程，擷取驗證與交接模式；AI 辦公自動化可沿用完成條件，know metabiz wiki 記錄有效與無效的實測案例。

**維護動能：**最近 push：2026-11-28T05:13:56Z；最新 release：[v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2)（2026-11-03T22:17:54Z）。 未結 issue／PR 合計 377；授權欄位 `MIT`。
來源：[儲存庫與 README](https://github.com/obra/superpowers)、[本次 API 中繼資料](https://api.github.com/repos/obra/superpowers)。

**風險：**近期 issue 回報視覺輔助服務失敗及技能未觸發；流程遵循與上下文成本須以任務結果衡量，不能只看提示規則。

近期活動樣本：
- [issue #2757](https://github.com/obra/superpowers/issues/2757)：更新於 2026-11-28T16:06:51Z，狀態 open。
- [issue #2660](https://github.com/obra/superpowers/issues/2660)：更新於 2026-11-28T13:28:26Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 6. firecrawl/firecrawl — Deep research

**用途與關聯：**提供搜尋、網頁擷取與資料存取介面，作為 agent 的外部知識輸入。 可做 Adam「網頁到知識庫」課程與 AI 辦公資料整理；know metabiz wiki 保留來源網址、擷取時間與原始證據，再交給人工核對摘要。

**維護動能：**最近 push：2026-11-28T13:04:53Z；最新 release：[v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0)（2026-06-19T15:09:30Z）。 未結 issue／PR 合計 843；授權欄位 `AGPL-3.0`。
來源：[儲存庫與 README](https://github.com/firecrawl/firecrawl)、[本次 API 中繼資料](https://api.github.com/repos/firecrawl/firecrawl)。

**風險：**近期 PR 包含 RateLimitError 重試與相依安全修正；網頁擷取權限、成本、提示注入與來源品質仍需控制。

近期活動樣本：
- [PR #6129](https://github.com/firecrawl/firecrawl/pull/6129)：更新於 2026-11-28T15:55:13Z，狀態 open。
- [PR #6131](https://github.com/firecrawl/firecrawl/pull/6131)：更新於 2026-11-28T13:06:36Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 7. toeverything/AFFiNE — Deep research

**用途與關聯：**整合文件、白板與規劃的知識工作空間，可評估團隊知識管理情境。 可作 Adam 知識管理課程比較與 AI 辦公協作示範；know metabiz wiki 優先比較來源可追溯、搜尋、匯出與還原能力。

**維護動能：**最近 push：2026-11-28T16:17:26Z；最新 release：[v0.27.4](https://github.com/toeverything/AFFiNE/releases/tag/v0.27.4)（2026-08-18T16:51:39Z）。 未結 issue／PR 合計 659；授權欄位 `NOASSERTION`。
來源：[儲存庫與 README](https://github.com/toeverything/AFFiNE)、[本次 API 中繼資料](https://api.github.com/repos/toeverything/AFFiNE)。

**風險：**近期 PR 涉及空間加入與模型標籤；API 授權欄位若為 NOASSERTION，代表授權尚未在此確認，亦需實測權限、匯出與自架維運。

近期活動樣本：
- [PR #14670](https://github.com/toeverything/AFFiNE/pull/14670)：更新於 2026-11-28T15:39:27Z，狀態 closed。
- [PR #15961](https://github.com/toeverything/AFFiNE/pull/15961)：更新於 2026-11-28T14:53:44Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 8. SamurAIGPT/llm-wiki-agent — Deep research

**用途與關聯：**讓 coding agent 把來源文件逐步整理成持久、互連的 wiki。 最貼近 know metabiz wiki：以少量公開文件做增量匯入、更新、刪除來源與回歸檢查；可轉成 Adam 的 AI 辦公知識治理實作課。

**維護動能：**最近 push：2026-11-23T12:47:33Z；最新 release：API 未取得公開 release，不能推論沒有更新。 未結 issue／PR 合計 8；授權欄位 `MIT`。
來源：[儲存庫與 README](https://github.com/SamurAIGPT/llm-wiki-agent)、[本次 API 中繼資料](https://api.github.com/repos/SamurAIGPT/llm-wiki-agent)。

**風險：**近期 issue 指出多字實體檔名與連結不一致造成重複產生；需驗證重跑冪等性、連結修復與來源歸屬。

近期活動樣本：
- [issue #87](https://github.com/SamurAIGPT/llm-wiki-agent/issues/87)：更新於 2026-11-27T06:55:53Z，狀態 open。
- [PR #86](https://github.com/SamurAIGPT/llm-wiki-agent/pull/86)：更新於 2026-10-20T12:40:51Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 9. google-labs-code/stitch-skills — Watch

**用途與關聯：**提供搭配 Stitch MCP 的 agent skills／plugins，用於設計與介面工作流。 適合 Adam 展示設計到頁面的 agent 協作；AI 辦公可用於內部表單原型，know metabiz wiki 記錄工具設定與可重現的輸入輸出。

**維護動能：**最近 push：2026-11-28T05:15:18Z；最新 release：[v1.0](https://github.com/google-labs-code/stitch-skills/releases/tag/v1.0)（2026-05-18T18:02:32Z）。 未結 issue／PR 合計 27；授權欄位 `Apache-2.0`。
來源：[儲存庫與 README](https://github.com/google-labs-code/stitch-skills)、[本次 API 中繼資料](https://api.github.com/repos/google-labs-code/stitch-skills)。

**風險：**近期 PR 修復跨來源 iframe 合併與上傳路徑處理；外部服務相依、跨來源內容及版本相容性需留意。

近期活動樣本：
- [PR #119](https://github.com/google-labs-code/stitch-skills/pull/119)：更新於 2026-11-28T13:43:33Z，狀態 open。
- [PR #118](https://github.com/google-labs-code/stitch-skills/pull/118)：更新於 2026-11-28T12:14:10Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

### 10. elementalsouls/Claude-BugHunter — Watch

**用途與關聯：**以 Claude Code skills 組織漏洞研究與測試流程，作為安全工作流觀察樣本。 Adam 可將其作為 agent 權限與範圍控制的課程案例；AI 辦公僅取其檢查清單設計，know metabiz wiki 記錄授權範圍與證據要求。

**維護動能：**最近 push：2026-11-28T13:35:23Z；最新 release：[v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1)（2026-06-05T16:15:13Z）。 未結 issue／PR 合計 23；授權欄位 `MIT`。
來源：[儲存庫與 README](https://github.com/elementalsouls/Claude-BugHunter)、[本次 API 中繼資料](https://api.github.com/repos/elementalsouls/Claude-BugHunter)。

**風險：**近期 PR 仍修復程式範圍分頁及網域編碼；工具可執行外部測試，僅適用明確授權的隔離標的，熱度不代表掃描準確度。

近期活動樣本：
- [PR #304](https://github.com/elementalsouls/Claude-BugHunter/pull/304)：更新於 2026-11-28T15:21:50Z，狀態 open。
- [PR #303](https://github.com/elementalsouls/Claude-BugHunter/pull/303)：更新於 2026-11-28T14:27:39Z，狀態 open。

上述議題依本次標題與時間判讀；PR 不代表已合併或已發布。

## 明日觀察清單（2026-11-29 目標日）

1. **AutoClip**：對照 v1.6.3 與語言偵測 issue，使用自有繁中課程測試切點、字幕及直式畫面；若需大量修正，先維持 Demo content。
2. **CLI-Anything**：追蹤安裝等待修復是否合併／發布，以單一可復原辦公流程驗證成功率與輸出。
3. **LLM Wiki Agent**：追蹤 #87 實體重複問題，準備 5 份公開來源反覆匯入，檢查冪等性、失效連結與來源追溯；know metabiz wiki 優先研究。
4. **last30days-skill／diagram-design**：觀察新 release 與驗證器修正，規劃「來源研究 → 課程圖解」的小型串接，記錄時間、成本與人工校正量。
5. **Superpowers／Stitch skills**：確認技能觸發與跨來源內容處理問題是否有明確修正，保留可重現的失敗條件再評估導入。
6. **BugHunter**：比較其相對成長是否維持領先；先觀察範圍控制修正，不因星數熱度直接導入辦公流程。
7. **Firecrawl／AFFiNE**：補完整授權與部署文件，評估 know metabiz wiki 的來源擷取、權限、匯出與還原；發布日期較舊不等於停更，仍需交叉核對近期 push／PR。

## 歷史資料未刷新項目

以下 7 筆 API 本次回傳 404，可能涉及刪除、改名或存取限制；原因未確認。JSON 保留歷史數值並標註 `metadata_fetch_status=retained_after_404`；不可將其快照星差解讀為已驗證的本日成長。

- `BarberNumber/Midjourney-Software`
- `BrickOrioleLoad/aion-2-trainer-tool`
- `HunYiSage/dsh-purge`
- `YuJunZhiXue/dsh-purge`
- `hanshaze/Awesome-Prediction-Market-Trading-Tools`
- `mingrath/obsidian-ai-knowledge-agent`
- `onestardao/WFGY`

完整查詢、執行狀態與錯誤摘要見 `run-status.json`、`collector-limit-10.log`；近期活動原始索引見 `issue-activity.json`。
