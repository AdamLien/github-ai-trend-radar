# GitHub AI 趨勢雷達｜2026-09-29

目標日期為 Asia/Taipei 執行日前一個日曆日；實際收集完成於 2026-09-30T00:19:20.490217+08:00。本報是執行時即時觀測，歸檔到 2026-09-29，並非該日歷史收盤快照。

## 今日判讀

優先製作本機語音與多 agent 協作 Demo，深入研究記憶、執行隔離與結構式 RAG。排序綜合 Trending stars today、快照增量、相對成長、最新 push、README、release 與 issue／PR 活動，並保留與辦公、wiki 關聯高的候選；不按總星數排序。

共 326 筆候選／歷史追蹤紀錄，精選 9 個。10 組指定查詢與 README 收集均已執行。收集紀錄未偵測到 GitHub API rate-limit；使用 --limit 10，未觸發 --limit 5 重試。 [收集狀態](collection-status.json) 記錄執行與例外。

[GitHub Trending daily](https://github.com/trending?since=daily) 經語意篩選保留 9 個相關項目；排除一般媒體下載、系統教材、遊戲相容層、壓測工具與未證實 AI 關聯的部署平台。原始卡片與理由見 [來源紀錄](trending-daily.json)。VoiceStudio 依語音 AI 內容補正，避免只靠關鍵字漏收。

有 4 筆沿用歷史 metadata，已標記 metadata_stale，不能視為今日無成長；名稱見狀態檔。精選皆有本次 API 證據。

Δ 比較 2026-09-28 快照；相對成長 = Δ ÷ 前次星數。缺乏基準者標示「未測」，不能當作 0。stars today 是 GitHub Trending 的另一個時間窗口，不能與 Δ 相加。README 僅取前 700 字，徽章或摘要不構成功能驗證；issue/PR 為最新更新 10 筆抽樣，不是每日新增總數，也未實際安裝測試。

| 優先 | 專案 | Stars today | Δ stars | 相對成長 | 總星數 | 建議 |
|---|---|---:|---:|---:|---:|---|
| 1 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 4712 | +4,331 | 10.13% | 47,078 | Demo content |
| 2 | [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | 733 | +705 | 46.91% | 2,208 | Demo content |
| 3 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 2541 | +1,996 | 4.94% | 42,385 | Deep research |
| 4 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | 978 | 未測 | 未測 | 10,232 | Deep research |
| 5 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 822 | 未測 | 未測 | 36,992 | Deep research |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 2412 | +2,044 | 2.22% | 94,141 | Watch |
| 7 | [dream-num/univer](https://github.com/dream-num/univer) | 692 | +628 | 2.98% | 21,694 | Demo content |
| 8 | [t8y2/dbx](https://github.com/t8y2/dbx) | 460 | +338 | 1.58% | 21,780 | Watch |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 未入榜 | +655 | 0.24% | 269,428 | Skill candidate |

## debpalash/VoiceStudio — Demo content

**用途與關聯：** 本機語音生成、配音與轉錄，專案宣稱支援多語言。 Adam 可示範自有課程音檔配音與字幕；辦公會議逐字稿可整理到 know metabiz wiki。

**維護證據：** 最近 push：2026-09-29T15:45:28Z；最新 release：[v0.5.6](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)（2026-09-23T08:53:32Z）。[README](https://github.com/debpalash/VoiceStudio#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 1 筆 issue、9 筆 PR。[#2434 (Bug) Stories WebVTT import silently drops cues named STYLE or REGION](https://github.com/debpalash/VoiceStudio/issues/2434) 更新於 2026-09-29T15:58:18Z，狀態 open。

**風險與下一步：** 需實測繁中發音與轉錄品質；WebVTT 匯入已有遺漏 cue 的問題回報。AGPL-3.0 與模型授權需於產品整合時另行核對。

## mvschwarz/openrig — Demo content

**用途與關聯：** 以 YAML 定義團隊，將 Claude Code 與 Codex 工作階段整合管理。 適合 Adam 的多 agent 協作課程，先以文件撰寫／校對交接示範，再把可重現步驟存入 wiki。

**維護證據：** 最近 push：2026-09-29T16:16:21Z；最新 release：[v0.6.1](https://github.com/mvschwarz/openrig/releases/tag/v0.6.1)（2026-09-29T13:08:57Z）。[README](https://github.com/mvschwarz/openrig#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 5 筆 issue、5 筆 PR。[#41 Operator recovery cannot reconcile Pi and OMP seats to operator_recovered](https://github.com/mvschwarz/openrig/issues/41) 更新於 2026-09-29T16:06:01Z，狀態 open。

[安全修正 PR #149](https://github.com/mvschwarz/openrig/pull/149) 本次觀測仍為 open。

**風險與下一步：** 小基期放大成長率；PR #149 仍為 open，涉及 SSRF、CSRF 與配對佇列，展示前需確認修補狀態並限制網路暴露。

## vectorize-io/hindsight — Deep research

**用途與關聯：** 為 agent 提供跨任務記憶，重點在記憶保存與提取。 適合 Adam 比較 agent 記憶與 RAG；辦公助理可測試跨次任務承接，wiki 維持有來源的正式知識。

**維護證據：** 最近 push：2026-09-29T16:08:07Z；最新 release：[v0.10.2](https://github.com/vectorize-io/hindsight/releases/tag/v0.10.2)（2026-09-29T10:06:40Z）。[README](https://github.com/vectorize-io/hindsight#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 3 筆 issue、7 筆 PR。[#4941 FullRecallRequest.temporal_window receives a TemporalWindow model instead of the declared (start, end) tuple](https://github.com/vectorize-io/hindsight/issues/4941) 更新於 2026-09-29T15:29:15Z，狀態 open。

**風險與下一步：** 新 release 與時間窗口參數型別回報並存；需驗證錯誤記憶修正、刪除及客戶隔離，不能用人氣代表可靠度。

## NVIDIA/OpenShell — Deep research

**用途與關聯：** 自主 AI agent 的執行環境，主張安全與隱私。 可作為 Adam 辦公 agent 權限邊界課程題材，測試檔案與網路限制，將政策案例納入 know metabiz wiki。

**維護證據：** 最近 push：2026-09-29T16:11:24Z；最新 release：[v0.1.2](https://github.com/NVIDIA/OpenShell/releases/tag/v0.1.2)（2026-09-28T03:58:00Z）。[README](https://github.com/NVIDIA/OpenShell#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 3 筆 issue、7 筆 PR。[#3863 bug(e2e): required Podman e2e lanes cannot pass on macOS hosts and cannot be excluded locally](https://github.com/NVIDIA/OpenShell/issues/3863) 更新於 2026-09-29T16:02:20Z，狀態 open。

**風險與下一步：** 首次觀測缺乏快照增量基準；v0.1.2 仍需實測，macOS Podman 測試通道已有問題回報，品牌不等於隔離保證。

## VectifyAI/PageIndex — Deep research

**用途與關聯：** 以文件結構與推理進行檢索的 RAG，README 主張不需向量資料庫與切塊。 直接對應 know metabiz wiki 的長文件問答；Adam 可用同一批文件比較向量 RAG 與結構式檢索，量測答案引用、成本及延遲。

**維護證據：** 最近 push：2026-09-29T15:50:17Z；最新 release：[v0.2.20](https://github.com/VectifyAI/PageIndex/releases/tag/v0.2.20)（2026-09-28T14:03:36Z）。[README](https://github.com/VectifyAI/PageIndex#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 1 筆 issue、9 筆 PR。[#536 Support ScreenContextAgent observations as a time-aware source](https://github.com/VectifyAI/PageIndex/issues/536) 更新於 2026-09-27T07:41:43Z，狀態 open。

[Windows mutex 修正 PR #456](https://github.com/VectifyAI/PageIndex/pull/456) 本次觀測仍為 open；closed PR 也不能單憑狀態判定已合併發布。

**風險與下一步：** 首次觀測不代表今日才成立；推理成本與中文文件適用性未測。Windows 鎖定行為修正 PR 仍待追蹤。

## paperclipai/paperclip — Watch

**用途與關聯：** 管理工作中的 AI agents 與任務協作。 適合 Adam 的 AI 辦公營運內容，研究任務追蹤、人工核准與 wiki 作業規範如何連動。

**維護證據：** 最近 push：2026-09-29T16:14:42Z；最新 release：[v2026.916.1](https://github.com/paperclipai/paperclip/releases/tag/v2026.916.1)（2026-09-21T21:22:44Z）。[README](https://github.com/paperclipai/paperclip#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 2 筆 issue、8 筆 PR。[#14587 npm distribution ships without pnpm patchedDependencies → codex_local ACP agents have no network access](https://github.com/paperclipai/paperclip/issues/14587) 更新於 2026-09-29T16:04:39Z，狀態 open。

**風險與下一步：** 近期 npm 發佈缺少 patchedDependencies 的回報牽涉 Codex agent 網路能力；應先確認安裝版本與任務恢復流程。

## dream-num/univer — Demo content

**用途與關聯：** 可嵌入的 Office SDK，統一操作試算表、文件與簡報等辦公介面。 優先做 AI 週報／業務表單 Demo，對應 Adam 辦公自動化課程；wiki 可保存資料欄位與核對規則。

**維護證據：** 最近 push：2026-09-29T13:13:36Z；最新 release：[v1.0.3](https://github.com/dream-num/univer/releases/tag/v1.0.3)（2026-09-29T09:06:48Z）。[README](https://github.com/dream-num/univer#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 1 筆 issue、9 筆 PR。[#7793 (Bug) Formula number literals like 12.50, .5, 007 and 1E3 are treated as text](https://github.com/dream-num/univer/issues/7793) 更新於 2026-09-29T15:14:15Z，狀態 open。

**風險與下一步：** 公式數字常值被當文字的 issue 仍 open，修正 PR 不等於發布；金額計算、匯入匯出保真度需先驗證。

## t8y2/dbx — Watch

**用途與關聯：** 跨資料庫管理工具，README 列有內建 AI、MCP server 與 CLI。 適合 Adam 示範以 MCP 查詢測試資料、生成報表；know metabiz wiki 可保存 schema 說明與查詢範本。

**維護證據：** 最近 push：2026-09-29T15:23:20Z；最新 release：[v0.6.27](https://github.com/t8y2/dbx/releases/tag/v0.6.27)（2026-09-28T20:33:25Z）。[README](https://github.com/t8y2/dbx#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 6 筆 issue、4 筆 PR。[#10676 (Bug) Debian配置连接postgres无法保存](https://github.com/t8y2/dbx/issues/10676) 更新於 2026-09-29T16:08:16Z，狀態 open。

**風險與下一步：** Debian 上 PostgreSQL 連線無法保存仍有回報；應先以唯讀測試帳號驗證權限與連線持久性，多資料庫支援為專案宣稱。

## affaan-m/ECC — Skill candidate

**用途與關聯：** 整理 coding agent 的 skills、記憶、安全與研究優先開發方法。 Adam 可拆出單一可測 skill 教材；辦公文件核對與 wiki 維護可借用任務前檢查、證據記錄。

**維護證據：** 最近 push：2026-09-28T11:26:13Z；最新 release：[v2.2.1](https://github.com/affaan-m/ECC/releases/tag/v2.2.1)（2026-09-08T17:52:08Z）。[README](https://github.com/affaan-m/ECC#readme) 已取得摘要。

**近期活動：** 最新 10 筆抽樣有 4 筆 issue、6 筆 PR。[#3260 continuous-learning v1 is inert — evaluate-session.js signals on stderr, which never reaches the model](https://github.com/affaan-m/ECC/issues/3260) 更新於 2026-09-29T15:35:17Z，狀態 open。

**風險與下一步：** README 摘要多為徽章；continuous-learning v1 無效的 issue 尚 open，應驗證 hook 訊號是否真正抵達模型，避免直接整包導入。

## 明日觀察清單

- **VoiceStudio：** 追蹤 WebVTT 匯入修正；用自有繁中音檔測字幕時間軸與配音品質。
- **OpenRig：** 看高相對成長是否延續，確認 #149 合併／release 狀態，再做 Claude Code＋Codex 文件協作示範。
- **Hindsight／PageIndex：** 以同一組 wiki 文件設計記憶與檢索評測；PageIndex 明日才有本雷達首次可比增量。
- **OpenShell：** 建立第二個星數觀測點，確認平台支援與隔離測試是否可重現。
- **Univer／DBX：** 追蹤公式解析及連線保存回報，以合成資料演練週報產出。
- **Paperclip／ECC：** 確認 npm 套件及 hook 問題有無已發布修正，再決定升級為 Demo 或可重用 skill。

## 來源與限制

數值與摘要來自 GitHub repository、README、latest release API；[repos.json](repos.json) 與 [快照](snapshots/repos-2026-09-29.json) 保留完整欄位。[issue-activity.json](issue-activity.json) 保存活動抽樣。[selected-evidence.json](selected-evidence.json) 為精選補充查核，抓取時間不同可能造成星數小幅差异，表格統一採 repos.json。README 的效能、語言數與支援範圍屬專案宣稱。
收集器可能在 release／README endpoint 失敗時留下空值，未取得欄位不代表沒有活動。搜尋 API 原先按總星數找候選，可能漏掉低星新專案，因此使用 Trending 與小基期成長補足，仍不宣稱全 GitHub 完整覆蓋。
