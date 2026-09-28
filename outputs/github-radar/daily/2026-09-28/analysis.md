# GitHub AI 趨勢雷達｜2026-09-28

目標日期以 Asia/Taipei 前一個日曆日計算。實際收集完成時間：2026-09-29T00:19:50.759374+08:00。本報為 9 月 29 日執行時的即時觀測，歸檔至 9 月 28 日；不是歷史收盤快照。

## 今日判讀

優先研究 agent 記憶與工作管理，優先示範多 agent 協作與 AI 辦公文件。排序綜合 Trending stars today、快照增量、相對成長、近期推送、README、release 與 issue／PR；並保留 wiki 應用價值較高的低動能候選，未按總星數排名。

共收集 327 筆紀錄。10 組指定查詢皆使用 `--limit 10`、`--include-trending-daily`、`--include-readme`；未偵測到 GitHub API rate-limit，無須以 5 筆重試。查詢內容、收集狀態與 404 名單見 [collection-status.json](collection-status.json)。

[GitHub Trending daily](https://github.com/trending?since=daily) 保留 6 個主題相關項目；排除硬體雷達與一般系統程式教材。AI 學習指南 byoungd/up 保留在資料但未入精選；VoiceStudio 經語意判讀補入 Trending 來源。

「Δ」為相對 2026-09-27 快照的星數差；「相對成長」= Δ ÷ 前次星數。Trending today 的計算窗口與快照不同，兩者不能相加；缺值不代表 0。首次觀測且無基準者不能宣稱零成長。

| 優先 | 專案 | Stars today | Δ stars | 相對成長 | 總星數 | 建議 |
|---|---|---:|---:|---:|---:|---|
| 1 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 4413 | +4,288 | 11.88% | 40,389 | Deep research |
| 2 | [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | 781 | +758 | 101.74% | 1,503 | Demo content |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 3185 | +3,109 | 3.49% | 92,097 | Deep research |
| 4 | [dream-num/univer](https://github.com/dream-num/univer) | 1105 | +1,079 | 5.40% | 21,066 | Demo content |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 3274 | +3,590 | 9.17% | 42,747 | Demo content |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 未入本次榜單 | +559 | 0.21% | 268,773 | Skill candidate |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | 未入本次榜單 | +318 | 0.11% | 292,428 | Skill candidate |
| 8 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 未入本次榜單 | +73 | 0.08% | 91,432 | Watch |

## vectorize-io/hindsight — Deep research

**用途與關聯：** Agent 長期記憶，適合研究跨任務保留經驗的機制。 Adam 可製作「記憶與 RAG 差異」課程；AI 辦公助理可測試跨次任務記憶，know metabiz wiki 則可評估知識來源與記憶的分工。

**動能與維護：** 本期 +4,288 stars；最近 push `2026-09-28T16:10:50Z`。最新 release [v0.10.1](https://github.com/vectorize-io/hindsight/releases/tag/v0.10.1)（2026-09-21T15:24:30Z）。[README](https://github.com/vectorize-io/hindsight#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，6 筆為 issue、4 筆為 PR；[#4891：hindsight doesn't work with gpt-6](https://github.com/vectorize-io/hindsight/issues/4891) 更新於 `2026-09-28T16:01:51Z`，狀態 `open`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** 需驗證錯誤記憶的修正、刪除與不同客戶資料隔離；熱門與 benchmark 連結不代表企業情境已驗證。

## mvschwarz/openrig — Demo content

**用途與關聯：** 以 YAML 定義 agent 團隊，整合 Claude Code 與 Codex 工作階段。 適合 Adam 示範雙 agent 分工開發；辦公自動化可先試文件整理／校對的任務交接，wiki 可記錄可重現的流程。

**動能與維護：** 本期 +758 stars；最近 push `2026-09-28T10:36:40Z`。最新 release [v0.5.17](https://github.com/mvschwarz/openrig/releases/tag/v0.5.17)（2026-09-27T07:43:24Z）。[README](https://github.com/mvschwarz/openrig#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，5 筆為 issue、5 筆為 PR；[#96：Slack: let an update item post into an earlier item's thread (--reply-to), decisions unchanged](https://github.com/mvschwarz/openrig/issues/96) 更新於 `2026-09-28T13:20:53Z`，狀態 `open`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** 小基期放大成長率；多 agent 的成本、狀態同步與 Slack 執行邊界需實測，不能把待合併 PR 當成已發布能力。

## paperclipai/paperclip — Deep research

**用途與關聯：** 管理工作中的 AI agents，重點是任務與協作管理。 可作為 Adam 的 AI 辦公營運課程案例，研究人員審核、agent 任務追蹤與 wiki 工作規範的連接。

**動能與維護：** 本期 +3,109 stars；最近 push `2026-09-28T16:14:19Z`。最新 release [v2026.916.1](https://github.com/paperclipai/paperclip/releases/tag/v2026.916.1)（2026-09-21T21:22:44Z）。[README](https://github.com/paperclipai/paperclip#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，1 筆為 issue、9 筆為 PR；[#14421：2026.916.1 fails to start against an existing instance: Blocking relations cannot contain cycles](https://github.com/paperclipai/paperclip/issues/14421) 更新於 `2026-09-28T16:08:50Z`，狀態 `open`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** 近期 review gate 修正 PR 顯示審核流程仍在演進；應驗證完成狀態與人工核准是否一致。大量 open issues 數包含 PR，不等同缺陷數。

## dream-num/univer — Demo content

**用途與關聯：** 以統一 Office SDK 與 Facade API 操作試算表、文件和簡報，支援嵌入式生產力工具。 優先示範 AI 生成週報／業務表單，是 Adam AI 辦公自動化課程與 metabiz 文件工具的具體題材；wiki 可保存資料到報表的操作規範。

**動能與維護：** 本期 +1,079 stars；最近 push `2026-09-28T13:11:29Z`。最新 release [v1.0.2](https://github.com/dream-num/univer/releases/tag/v1.0.2)（2026-09-24T11:32:24Z）。[README](https://github.com/dream-num/univer#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，4 筆為 issue、6 筆為 PR；[#7775：[Bug] protocol isError() treats falsy code 0 (UNDEFINED) as success](https://github.com/dream-num/univer/issues/7775) 更新於 `2026-09-28T15:56:06Z`，狀態 `open`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** README 明列 PDF coming soon，不能當作已可用；錯誤碼 0 被當成功的 issue 值得追蹤，另需實測檔案格式往返保真度。

## debpalash/VoiceStudio — Demo content

**用途與關聯：** 本機語音合成、轉錄、配音與有聲內容工具；多語言涵蓋為專案宣稱。 Adam 可用自有聲音素材示範課程配音與字幕流程；辦公場景可評估會議轉錄，逐字稿再整理到 know metabiz wiki。

**動能與維護：** 本期 +3,590 stars；最近 push `2026-09-28T13:59:06Z`。最新 release [v0.5.6](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)（2026-09-23T08:53:32Z）。[README](https://github.com/debpalash/VoiceStudio#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，6 筆為 issue、4 筆為 PR；[#2399：Streaming preview (web build): every take is cut at both ends and carries a faint whistle; the saved WAV is clean](https://github.com/debpalash/VoiceStudio/issues/2399) 更新於 `2026-09-28T15:15:29Z`，狀態 `open`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** 繁中發音、轉錄準確度與硬體需求尚未實測；repo 標示 AGPL-3.0，產品整合前需另行確認適用條件與模型授權。

## affaan-m/ECC — Skill candidate

**用途與關聯：** 整理 coding agent 的 skills、記憶、安全與研究優先的開發方法。 適合 Adam 拆解成小型可重用 skill 教材；辦公自動化可借用任務前檢查與紀錄方式，wiki 保存經實測的版本與依賴。

**動能與維護：** 本期 +559 stars；最近 push `2026-09-28T11:26:13Z`。最新 release [v2.2.1](https://github.com/affaan-m/ECC/releases/tag/v2.2.1)（2026-09-08T17:52:08Z）。[README](https://github.com/affaan-m/ECC#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，1 筆為 issue、9 筆為 PR；[#3169：hooks.json: Claude Code warns "unknown keys" for id/description on all 24 matcher groups](https://github.com/affaan-m/ECC/issues/3169) 更新於 `2026-09-28T13:02:12Z`，狀態 `open`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** README 前 700 字多為徽章，無法單憑摘要確認功能；observer 儲存路徑修正與跨 agent 轉譯 PR 仍需確認合併／發布狀態。

## obra/superpowers — Skill candidate

**用途與關聯：** 以可組合 skills 建立 coding agent 軟體開發方法，README 列出多個 agent 平台。 適合 Adam 課程中的需求澄清、規劃與審查練習；可把文件更新與 wiki 品質檢查整理成可重現的工作流程。

**動能與維護：** 本期 +318 stars；最近 push `2026-09-27T02:37:47Z`。最新 release [v6.4.2](https://github.com/obra/superpowers/releases/tag/v6.4.2)（2026-09-25T18:08:09Z）。[README](https://github.com/obra/superpowers#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，6 筆為 issue、4 筆為 PR；[#2054：subagent-driven-development: reviewer prompts pay subagent turns for mechanical facts the controller can settle in one command](https://github.com/obra/superpowers/issues/2054) 更新於 `2026-09-28T14:42:08Z`，狀態 `open`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** 流程本身可能增加 agent 回合與成本；近期 reviewer prompts 討論正涉及此問題，應以同一任務比較品質與耗時。

## infiniflow/ragflow — Watch

**用途與關聯：** 結合 RAG 與 Agent 的知識檢索／上下文引擎。 雖然短期星數動能較低，仍直接對應 know metabiz wiki 的匯入與引用檢索；Adam 可用合成公司文件示範知識庫問答與來源核對。

**動能與維護：** 本期 +73 stars；最近 push `2026-09-28T13:17:57Z`。最新 release [v0.27.2](https://github.com/infiniflow/ragflow/releases/tag/v0.27.2)（2026-09-10T11:11:35Z）。[README](https://github.com/infiniflow/ragflow#readme) 已取得摘要；摘要截斷／徽章不視為完整功能驗證。

**近期活動：** 最新 10 筆 issue／PR 抽樣中，3 筆為 issue、7 筆為 PR；[#20091：[Bug]: OpenDataLoader, TCADP and SoMark PDF parsers label text that is not <table> markup as doc_type_kwd "table"](https://github.com/infiniflow/ragflow/issues/20091) 更新於 `2026-09-28T15:26:59Z`，狀態 `closed`。這是混合活動抽樣，不是每日新增 issue 總量。

**風險與下一步：** 匯入 token 正規化與檢索 highlight 仍有近期 PR；需測試繁中切分、權限、刪除同步與引用準確度，先做小型驗證。

## 資料限制

4 個歷史項目回傳 404，collector 沿用舊資料，已標示 `metadata_stale` 並設為 Reference only：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。它們不參與本報推薦，表面 Δ=0 不代表實際沒有成長。

搜尋端依總星數排序，可能漏掉新興小專案；以 Trending 補充但仍非 GitHub 全量。所有建議為根據 README 摘要、repo metadata 與近期 issue／PR 的編輯判斷，未安裝或執行候選專案。資料來源詳見 [repos.json](repos.json)、[Trending 擷取](trending-daily.json)、[issue／PR 活動](issue-activity.json) 與 [原始彙整](report.md)。

## 明日觀察清單

1. **openrig**：確認相對成長是否延續，追蹤 Slack thread issue #96 與 daemon 修正 #91 的發布情況；做一次 Claude Code／Codex 分工成本與恢復能力比較。
2. **hindsight／paperclip**：追蹤 memory curation hooks 與 review gate 修正是否合併；以合成文件驗證記憶刪除及人工審核流程。
3. **Univer**：追蹤 #7775 錯誤碼判定；準備一份含繁中、公式及合併儲存格的週報做往返測試，確認 PDF 是否仍標示 coming soon。
4. **VoiceStudio**：以自有音訊測繁中配音／轉錄與硬體耗用，再決定是否製作短影音示範。
5. **ECC／superpowers**：各選一個小 skill，比較固定任務的回合、時間與品質，再決定課程採用範圍。
6. **RAGFlow**：以 know metabiz wiki 的合成文件集測引用、繁中切分與刪除同步，追蹤匯入及檢索 PR。
7. **資料品質**：重查 4 個 404 repo，避免把失效或搬移造成的缺資料解讀成趨勢停滯。
