# GitHub AI 趨勢雷達｜2026-11-27

目標日期：前一個 Asia/Taipei 日曆日。實際擷取時間：2026-11-27T16:11:29.738858+00:00（UTC；台北已為 2026-11-28）。本次使用即時 [GitHub Trending daily](https://github.com/trending?since=daily)，並非 11 月 27 日午夜封存榜單。

## 判讀方法與資料邊界

以 stars today、相較前次快照的 star delta／相對成長、更新時間、README、release 及近期 issue／PR 交叉判讀；下列順序按 Adam 可落地用途與研究價值安排，不是總星數排名。stars today 是 GitHub 榜單的滾動訊號；快照差值以 2026-11-26 的已存檔觀測作比較，並非精確台北自然日淨增。相對成長＝快照差值／前次總星數。負值也會如實保留；首次出現的專案不把未知成長當作 0。

README 僅當用途描述來源，不執行其中指令。近期活動樣本為各庫最近更新的 5 筆 issue／PR，不能推論 issue 解決率；open_issues 計數也可能包含 PR。以下建議屬研究判斷，尚未安裝或實測這些專案。

## 值得追蹤的 10 個專案

| 專案 | Stars today | 總 stars | 快照差值 | 相對成長 | 判定 |
|---|---:|---:|---:|---:|---|
| [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | 733 | 17,453 | +688 | 4.10% | Demo content |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 668 | 66,817 | +647 | 0.98% | Deep research |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 731 | 74,303 | +661 | 0.90% | Skill candidate |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 664 | 76,214 | +648 | 0.86% | Skill candidate |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 311 | 13,500 | +306 | 2.32% | Skill candidate |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 833 | 211,458 | +782 | 0.37% | Deep research |
| [obra/superpowers](https://github.com/obra/superpowers) | 916 | 328,078 | +872 | 0.27% | Reference only |
| [cursor/plugins](https://github.com/cursor/plugins) | 242 | 19,948 | +236 | 1.20% | Watch |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 469 | 79,280 | +459 | 0.58% | Watch |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 1,615 | 25,616 | +1,514 | 6.28% | Watch |

### 1. zhouxiaoka/autoclip — Demo content

用途：將長影片自動剪成短片，提供字幕、封面與 MCP 介面。

動能與維護：Trending 顯示 733 stars today；最近 push 為 2026-11-27T16:00:21Z。latest release 為 [v1.6.2](https://github.com/zhouxiaoka/autoclip/releases/tag/v1.6.2)，發布於 2026-11-26T14:07:52Z。 近期活動例如 [PR #718](https://github.com/zhouxiaoka/autoclip/pull/718)，狀態 closed，更新於 2026-11-27T13:04:55Z。

與 Adam／metabiz 的關聯：直接把 Adam 課程或訪談製成 Shorts／Reels 示範；AI 辦公可把會議摘要轉為內訓短片，know metabiz wiki 可保存影片來源與剪輯決策。

風險與限制：本機轉錄品質、中文斷句、算力與輸出路徑相容性仍須實測；README 的零訂閱不等於模型推論零成本。

來源：[README](https://github.com/zhouxiaoka/autoclip#readme)、[近期 issue／PR](https://github.com/zhouxiaoka/autoclip/issues?q=sort%3Aupdated-desc)。

### 2. HKUDS/CLI-Anything — Deep research

用途：將軟體操作能力包成可供 agent 使用的 CLI。

動能與維護：Trending 顯示 668 stars today；最近 push 為 2026-11-20T10:05:15Z。latest release 為 [v0.4.0](https://github.com/HKUDS/CLI-Anything/releases/tag/v0.4.0)，發布於 2026-06-25T15:17:49Z。 近期活動例如 [issue #748](https://github.com/HKUDS/CLI-Anything/issues/748)，狀態 open，更新於 2026-11-27T13:42:11Z。

與 Adam／metabiz 的關聯：適合 Adam 的「代理如何操作現有軟體」課程及內容；AI 辦公可測試重複性資料處理，know metabiz wiki 保存可重現操作流程。

風險與限制：最新 stable release 較舊；Audacity 音訊靜音的未結 issue 顯示不同應用介面品質不一。

來源：[README](https://github.com/HKUDS/CLI-Anything#readme)、[近期 issue／PR](https://github.com/HKUDS/CLI-Anything/issues?q=sort%3Aupdated-desc)。

### 3. cathrynlavery/diagram-design — Skill candidate

用途：以單一 HTML＋SVG 產生圖解，README 提供 52 種圖型。

動能與維護：Trending 顯示 731 stars today；最近 push 為 2026-11-26T19:48:58Z。本次 latest release 查詢未取得正式版本，不能當作沒有維護。 近期活動例如 [PR #552](https://github.com/cathrynlavery/diagram-design/pull/552)，狀態 closed，更新於 2026-11-27T12:50:28Z。

與 Adam／metabiz 的關聯：可製作 Adam 課程架構圖及社群教學圖；AI 辦公用於流程說明，know metabiz wiki 用於系統與 SOP 圖解。

風險與限制：沒有可見的 latest release；近期驗證器與 Mermaid 匯入修補表示輸出仍需視覺檢查，繁中字型也須測試。

來源：[README](https://github.com/cathrynlavery/diagram-design#readme)、[近期 issue／PR](https://github.com/cathrynlavery/diagram-design/issues?q=sort%3Aupdated-desc)。

### 4. mvanhorn/last30days-skill — Skill candidate

用途：跨多個社群與網路來源整理近 30 天研究摘要。

動能與維護：Trending 顯示 664 stars today；最近 push 為 2026-11-27T06:30:50Z。latest release 為 [v4.8.0](https://github.com/mvanhorn/last30days-skill/releases/tag/v4.8.0)，發布於 2026-11-27T04:32:24Z。 近期活動例如 [issue #1649](https://github.com/mvanhorn/last30days-skill/issues/1649)，狀態 open，更新於 2026-11-27T15:48:39Z。

與 Adam／metabiz 的關聯：適合 Adam 的選題雷達與研究方法課程；AI 辦公可整理產業動態，know metabiz wiki 保存引用、日期與原文連結。

風險與限制：跨站來源有 API、成本與資料可用性差異；近期畸形計數及時間戳問題可能影響排序，摘要需逐項查證。

來源：[README](https://github.com/mvanhorn/last30days-skill#readme)、[近期 issue／PR](https://github.com/mvanhorn/last30days-skill/issues?q=sort%3Aupdated-desc)。

### 5. google-labs-code/stitch-skills — Skill candidate

用途：針對 Stitch 的 agent skills／plugins，README 說明跨 coding agent 相容性。

動能與維護：Trending 顯示 311 stars today；最近 push 為 2026-11-24T21:51:04Z。latest release 為 [v1.0](https://github.com/google-labs-code/stitch-skills/releases/tag/v1.0)，發布於 2026-05-18T18:02:32Z。 近期活動例如 [issue #72](https://github.com/google-labs-code/stitch-skills/issues/72)，狀態 open，更新於 2026-11-25T12:25:02Z。

與 Adam／metabiz 的關聯：可設計 Adam「從需求到 UI」課程與短示範；AI 辦公可產生內部工具介面，know metabiz wiki 保存設計規格與可重用提示。

風險與限制：依賴 Stitch 與各 agent 版本；最新 release 與目前 plugin 結構可能有落差，驗證器修補尚待合併。

來源：[README](https://github.com/google-labs-code/stitch-skills#readme)、[近期 issue／PR](https://github.com/google-labs-code/stitch-skills/issues?q=sort%3Aupdated-desc)。

### 6. firecrawl/firecrawl — Deep research

用途：為 agent 擷取、搜尋與整理網頁內容，可作為 RAG／wiki 的來源輸入層。

動能與維護：Trending 顯示 833 stars today；最近 push 為 2026-11-27T00:15:09Z。latest release 為 [v2.11.0](https://github.com/firecrawl/firecrawl/releases/tag/v2.11.0)，發布於 2026-06-19T15:09:30Z。 近期活動例如 [issue #6106](https://github.com/firecrawl/firecrawl/issues/6106)，狀態 closed，更新於 2026-11-27T10:49:00Z。

與 Adam／metabiz 的關聯：Adam 可示範「網頁到知識庫」課程；AI 辦公可整理公開產品資訊，know metabiz wiki 可保留來源、抓取時間與內容更新紀錄。

風險與限制：AGPL-3.0 與部署模式需逐項檢視；網頁抓取品質、服務額度及自架搜尋供應商失敗處理皆須評估。

來源：[README](https://github.com/firecrawl/firecrawl#readme)、[近期 issue／PR](https://github.com/firecrawl/firecrawl/issues?q=sort%3Aupdated-desc)。

### 7. obra/superpowers — Reference only

用途：以可組合 skills 組織 coding agent 的規劃、開發、審查與驗證流程。

動能與維護：Trending 顯示 916 stars today；最近 push 為 2026-11-26T11:33:33Z。latest release 為 [v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2)，發布於 2026-11-03T22:17:54Z。 近期活動例如 [issue #2753](https://github.com/obra/superpowers/issues/2753)，狀態 open，更新於 2026-11-27T07:37:42Z。

與 Adam／metabiz 的關聯：適合 Adam 課程中比較代理流程設計；AI 辦公可參考其交付與驗證步驟，know metabiz wiki 可記錄哪些流程值得精簡採用。

風險與限制：流程成本可能高於小任務收益；近期 fast-track issue 與 code-review 基準修補值得觀察。

來源：[README](https://github.com/obra/superpowers#readme)、[近期 issue／PR](https://github.com/obra/superpowers/issues?q=sort%3Aupdated-desc)。

### 8. cursor/plugins — Watch

用途：Cursor 官方 plugins 集合，含教學、持續學習與團隊開發流程範例。

動能與維護：Trending 顯示 242 stars today；最近 push 為 2026-11-26T09:04:53Z。本次 latest release 查詢未取得正式版本，不能當作沒有維護。 近期活動例如 [issue #278](https://github.com/cursor/plugins/issues/278)，狀態 open，更新於 2026-11-27T09:22:09Z。

與 Adam／metabiz 的關聯：Adam 可比較 Cursor、Codex 與 Claude Code 的擴充方式；AI 辦公可借鏡整合模式，know metabiz wiki 可整理 plugin manifest 與能力對照。

風險與限制：GitHub metadata 未辨識授權且無 latest release，不能推論整庫可直接再散布；近期 statechart 結束訊號問題仍在修補。

來源：[README](https://github.com/cursor/plugins#readme)、[近期 issue／PR](https://github.com/cursor/plugins/issues?q=sort%3Aupdated-desc)。

### 9. toeverything/AFFiNE — Watch

用途：結合文件、白板與規劃的知識工作平台，README 強調 local-first。

動能與維護：Trending 顯示 469 stars today；最近 push 為 2026-11-27T15:28:55Z。latest release 為 [v0.27.4](https://github.com/toeverything/AFFiNE/releases/tag/v0.27.4)，發布於 2026-08-18T16:51:39Z。 近期活動例如 [issue #6364](https://github.com/toeverything/AFFiNE/issues/6364)，狀態 closed，更新於 2026-11-27T06:14:28Z。

與 Adam／metabiz 的關聯：可作 Adam 知識管理課程的比較案例；AI 辦公用於協作筆記，know metabiz wiki 可評估文件與圖解共存的閱讀體驗。

風險與限制：授權欄位為 NOASSERTION，須讀實際授權；資料庫編輯復原與公開分享顯示問題仍有未結 issue，遷移和權限需實測。

來源：[README](https://github.com/toeverything/AFFiNE#readme)、[近期 issue／PR](https://github.com/toeverything/AFFiNE/issues?q=sort%3Aupdated-desc)。

### 10. elementalsouls/Claude-BugHunter — Watch

用途：面向漏洞研究的 Claude Code skills 與案例模式集合。

動能與維護：Trending 顯示 1,615 stars today；最近 push 為 2026-11-27T04:27:28Z。latest release 為 [v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1)，發布於 2026-06-05T16:15:13Z。 近期活動例如 [PR #278](https://github.com/elementalsouls/Claude-BugHunter/pull/278)，狀態 open，更新於 2026-11-27T15:08:16Z。

與 Adam／metabiz 的關聯：適合作為 Adam AI 工具風險意識及案例整理內容；AI 辦公可參考權限邊界設計，know metabiz wiki 可整理防禦性檢查清單。

風險與限制：成長最快但主題較專門；近期多個範圍限制與敏感資訊遮蔽 PR 尚未合併，技能數量與作者成效宣稱不代表已驗證品質。

來源：[README](https://github.com/elementalsouls/Claude-BugHunter#readme)、[近期 issue／PR](https://github.com/elementalsouls/Claude-BugHunter/issues?q=sort%3Aupdated-desc)。

## 明日觀察清單（2026-11-28）

- **zhouxiaoka/autoclip**：比較同一段繁中課程的字幕錯字率、剪輯完整性及人工修正時間。
- **HKUDS/CLI-Anything**：選一個低風險文件或影音工作流，比較 CLI 結果與人工操作。
- **cathrynlavery/diagram-design**：用同一份 metabiz SOP 測試繁中排版、品牌色與可編輯性。
- **mvanhorn/last30days-skill**：追蹤 v4.8.0 與來源解析修補，抽查繁中選題的來源可追溯率。
- **google-labs-code/stitch-skills**：追蹤 plugin 安裝與驗證器 PR，先測一頁內部工具介面。
- **firecrawl/firecrawl**：追蹤自架搜尋錯誤處理 PR，用固定十頁測試抓取完整性與增量更新。
- **obra/superpowers**：追蹤輕量流程需求及 review base 修補；量測小任務的對話輪數與耗時。
- **cursor/plugins**：逐一確認候選 plugin 的授權、版本固定方式與關閉流程行為。
- **toeverything/AFFiNE**：追蹤編輯器 bug，測試 Markdown 匯入匯出、來源連結及小型團隊權限。
- **elementalsouls/Claude-BugHunter**：追蹤 scope fail-closed 與 redaction 修補；只評估文件與隔離教學案例。

## 收集與重現

- 搜尋：依指定的 10 組查詢、`--limit 10`、`--include-trending-daily`、`--include-readme`，在專案根目錄執行；收集器同時保留歷史追蹤集合。
- Trending 共 16 張卡，保留 14 個 AI／Skills／Agent／知識庫等範圍專案；排除 NGINX 與一般下載器。原始卡片留在 `trending-evidence.json` 供核對，不列為雷達候選。
- API 補充核對：`review-evidence.json` 保存此 10 個專案的 README、metadata、release 與近期 issue／PR；總星數可能與主收集器的稍早／稍晚觀測有小幅差異。
- 主收集器以 `--limit 10` 成功完成（exit 0），未偵測到 GitHub API rate-limit，未啟動 `--limit 5` 重試；補充核對亦未出現限流。詳見 `collection-status.json`。
- 收集器合併歷史追蹤後，另排除 8 個明確不符範圍項目，本次保留 450 個候選；排除理由見 `scope-review.json`。


## 資料新鮮度限制

以下 6 個歷史項目 API 回傳 404，沿用舊 metadata；不代表今天仍公開可用，也不能把不變的星數當作已觀測的零成長：`BarberNumber/Midjourney-Software`、`BrickOrioleLoad/aion-2-trainer-tool`、`HunYiSage/dsh-purge`、`YuJunZhiXue/dsh-purge`、`hanshaze/Awesome-Prediction-Market-Trading-Tools`、`mingrath/obsidian-ai-knowledge-agent`。本篇精選 10 個專案均成功取得本次 API 與補充核對資料。
