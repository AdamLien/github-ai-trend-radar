# GitHub AI 趨勢雷達｜2026-10-02

## 觀察口徑與資料品質

目標日期為前一個 Asia/Taipei 日曆日 2026-10-02；實際收集區間為 2026-10-03T00:11:18.041044+08:00 至 2026-10-03T00:22:42.176027+08:00。本次依指定 10 個查詢、每個查詢上限 10 筆，加上 [GitHub Trending daily](https://github.com/trending?since=daily) 與歷史追蹤清單，原始 334 筆經去重與主題篩選後保留 311 個專案，其中 14 個來自本次 Trending。

**Rate-limit 狀態：未觀察到限制錯誤；無須以 --limit 5 重跑。** 4 個歷史專案收到 404，已將沿用資料標記為 metadata_stale，增量設為 null；不作本次動能推薦依據。原始 Trending 證據含被排除項目，正式 repos.json、report.md 與快照只保留範圍內項目。

今日星數是收集時 Trending 頁面的 stars today，不代表精確的臺北昨日 24 小時新增；快照增量以 2026-10-01 的既有快照為基準，兩者觀察窗口不同。相對成長＝快照增量 ÷ 前次總星數。未上榜顯示「—」，不代表零成長。GitHub open_issues 數字包含未關閉 PR，不能直接視為缺陷數。最新 5 筆 issue／PR 僅供活動抽樣，不推論完整回應速度。

排序先看當日動能與相對成長，再考量最近程式推送、README 用途、release、issue／PR 與 Adam 工作關聯。搜尋 API 本身依總星數找候選，有成熟專案偏差；以下編輯排序不依總星數。README 中的效能、安全與成本承諾均視為作者宣稱，本次未安裝或實測。

## 今日判斷

OpenRig 的相對成長最值得追查，Ponytail 與 mattpocock/skills 適合轉成技能設計教材；CodeGraph 與 Context Mode 可研究知識取得與上下文成本。HyperFrames、Agent Reach 較容易製作示範內容。Dify 作知識庫基準；Superpowers 已具高知名度，今日以參考用途為主。

## 10 個值得追蹤的專案

| 專案 | 今日星數 | 快照增量 | 相對成長 | 總星數 | 分類 |
| --- | ---: | ---: | ---: | ---: | --- |
| [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | 691 | +635 | 18.24% | 4,116 | Deep research |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 1429 | +1,293 | 0.86% | 151,346 | Skill candidate |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 955 | +896 | 0.33% | 274,488 | Skill candidate |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | 584 | +494 | 3.58% | 14,308 | Watch |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 584 | +552 | 1.00% | 55,709 | Demo content |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 683 | +915 | 1.05% | 88,153 | Demo content |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 276 | +248 | 1.00% | 24,953 | Deep research |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 241 | +125 | 0.17% | 72,868 | Deep research |
| [langgenius/dify](https://github.com/langgenius/dify) | — | +55 | 0.03% | 157,721 | Watch |
| [obra/superpowers](https://github.com/obra/superpowers) | 561 | +484 | 0.16% | 294,281 | Reference only |

### 1. mvschwarz/openrig — Deep research

**用途與 README 判讀：** 把 Claude Code、Codex、Pi 組成有角色、共享上下文與工作責任的持續 agent 團隊。 [專案／README](https://github.com/mvschwarz/openrig#readme)。

**動能與維護：** 今日星數 691；快照增量 +635；總星數 4,116。最近 push：2026-10-02T16:17:25Z；最新 release：[v0.6.4](https://github.com/mvschwarz/openrig/releases)（2026-10-02T05:45:35Z）。未關閉 issue／PR 合計 115；最近活動抽樣 5 筆。

**活動證據：** [Issue #403](https://github.com/mvschwarz/openrig/issues/403)，狀態 closed，更新於 2026-10-02T15:11:56Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 近期有工作階段恢復與 daemon 關閉相關問題；多 agent 並行成本、狀態一致性尚需實測。 授權 API 標記：Apache-2.0。

**與 Adam 的關聯／下一步：** 適合研究 AI 辦公自動化的任務分派、交接及失敗恢復；先用公開文件整理任務做小型驗證。

### 2. DietrichGebert/ponytail — Skill candidate

**用途與 README 判讀：** 以技能與外掛約束 coding agent 的工程決策，強調減少不必要的程式碼。 [專案／README](https://github.com/DietrichGebert/ponytail#readme)。

**動能與維護：** 今日星數 1429；快照增量 +1,293；總星數 151,346。最近 push：2026-10-02T15:10:00Z；最新 release：[v4.10.1](https://github.com/DietrichGebert/ponytail/releases)（2026-10-02T15:11:38Z）。未關閉 issue／PR 合計 315；最近活動抽樣 5 筆。

**活動證據：** [Issue #644](https://github.com/DietrichGebert/ponytail/issues/644)，狀態 closed，更新於 2026-10-02T15:27:40Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 偏好少寫程式不能替代需求驗證；近期 OpenCode 外掛相容性修正需要版本鎖定。 授權 API 標記：MIT。

**與 Adam 的關聯／下一步：** 適合 Adam 的 agent 工作法課程：以相同需求比較修改範圍、可讀性與測試結果；可萃取為內部 skill 實驗。

### 3. mattpocock/skills — Skill candidate

**用途與 README 判讀：** 將工程師的需求釐清、設計與開發流程整理成可重複使用的 agent skills。 [專案／README](https://github.com/mattpocock/skills#readme)。

**動能與維護：** 今日星數 955；快照增量 +896；總星數 274,488。最近 push：2026-09-29T12:38:37Z；最新 release：[v1.2.3](https://github.com/mattpocock/skills/releases)（2026-08-06T14:05:28Z）。未關閉 issue／PR 合計 544；最近活動抽樣 5 筆。

**活動證據：** [Issue #1153](https://github.com/mattpocock/skills/issues/1153)，狀態 open，更新於 2026-10-02T11:23:00Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** CONTEXT.md 到 GLOSSARY.md 的遷移路徑仍有公開問題；匯入前應比較本地自訂流程。 授權 API 標記：MIT。

**與 Adam 的關聯／下一步：** 直接對應 Adam 的技能設計課程及團隊開發 SOP；可用知識詞彙表遷移做實作教材。

### 4. NVIDIA/OpenShell — Watch

**用途與 README 判讀：** 為自主 AI agent 提供強調隔離與隱私的執行環境。 [專案／README](https://github.com/NVIDIA/OpenShell#readme)。

**動能與維護：** 今日星數 584；快照增量 +494；總星數 14,308。最近 push：2026-10-02T16:09:25Z；最新 release：[v0.1.2](https://github.com/NVIDIA/OpenShell/releases)（2026-09-28T03:58:00Z）。未關閉 issue／PR 合計 536；最近活動抽樣 5 筆。

**活動證據：** [Issue #3802](https://github.com/NVIDIA/OpenShell/issues/3802)，狀態 open，更新於 2026-10-02T16:09:31Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 近期仍有 stdin、虛擬機簽章與依賴修正；宣稱安全不等同已完成對實際部署的安全驗證。 授權 API 標記：Apache-2.0。

**與 Adam 的關聯／下一步：** 與 AI 辦公自動化的受控執行相關；可作企業 agent 權限與沙箱課程研究素材。

### 5. heygen-com/hyperframes — Demo content

**用途與 README 判讀：** 讓 agent 以 HTML 製作並輸出影片，將網頁式編排用於影音產製。 [專案／README](https://github.com/heygen-com/hyperframes#readme)。

**動能與維護：** 今日星數 584；快照增量 +552；總星數 55,709。最近 push：2026-10-02T16:11:23Z；最新 release：[v0.8.112](https://github.com/heygen-com/hyperframes/releases)（2026-10-02T15:42:55Z）。未關閉 issue／PR 合計 146；最近活動抽樣 5 筆。

**活動證據：** [PR #3996](https://github.com/heygen-com/hyperframes/pull/3996)，狀態 open，更新於 2026-10-02T16:11:24Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 大量 CLI 與瀏覽器生命週期修正仍在進行；需測試渲染一致性、字幕字型及長任務資源回收。 授權 API 標記：Apache-2.0。

**與 Adam 的關聯／下一步：** 可把每日雷達轉為短影音樣片，作 Adam 內容自動化課程示範。

### 6. Panniantong/Agent-Reach — Demo content

**用途與 README 判讀：** 讓 agent 透過 CLI 搜尋與讀取多個網站，支援內容蒐集工作。 [專案／README](https://github.com/Panniantong/Agent-Reach#readme)。

**動能與維護：** 今日星數 683；快照增量 +915；總星數 88,153。最近 push：2026-09-15T16:16:24Z；最新 release：[v1.5.0](https://github.com/Panniantong/Agent-Reach/releases)（2026-06-11T12:29:59Z）。未關閉 issue／PR 合計 177；最近活動抽樣 5 筆。

**活動證據：** [Issue #742](https://github.com/Panniantong/Agent-Reach/issues/742)，狀態 open，更新於 2026-10-02T15:39:32Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 近期 YouTube 字幕可能取得機器翻譯而非原文；平台存取穩定性與內容來源品質需逐項確認。 授權 API 標記：MIT。

**與 Adam 的關聯／下一步：** 適合 Adam 展示研究素材蒐集到 know metabiz wiki 的來源整理流程；示範保留來源與引用。

### 7. mksglu/context-mode — Deep research

**用途與 README 判讀：** 透過 MCP、hooks、輸出隔離與會話記憶管理 coding agent 的上下文。 [專案／README](https://github.com/mksglu/context-mode#readme)。

**動能與維護：** 今日星數 276；快照增量 +248；總星數 24,953。最近 push：2026-10-02T12:07:19Z；最新 release：[v1.0.169](https://github.com/mksglu/context-mode/releases)（2026-06-29T18:18:53Z）。未關閉 issue／PR 合計 313；最近活動抽樣 5 筆。

**活動證據：** [Issue #1242](https://github.com/mksglu/context-mode/issues/1242)，狀態 open，更新於 2026-10-02T05:51:54Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 壓縮比例屬專案宣稱，本次未重現；shell 相容性與工作階段歸屬仍有修正，過度壓縮可能損失證據。 授權 API 標記：NOASSERTION（未能由 SPDX 欄位確定授權，採用前須閱讀 LICENSE）。

**與 Adam 的關聯／下一步：** 適合 Adam 的上下文成本課程；可比較知識庫檢索長輸出在 token 用量與答案完整性上的差異。

### 8. colbymchenry/codegraph — Deep research

**用途與 README 判讀：** 建立本地程式碼知識圖譜，讓 coding agent 查詢關聯並隨程式變更更新索引。 [專案／README](https://github.com/colbymchenry/codegraph#readme)。

**動能與維護：** 今日星數 241；快照增量 +125；總星數 72,868。最近 push：2026-10-02T10:41:47Z；最新 release：[v1.6.1](https://github.com/colbymchenry/codegraph/releases)（2026-09-29T05:08:55Z）。未關閉 issue／PR 合計 504；最近活動抽樣 5 筆。

**活動證據：** [Issue #2305](https://github.com/colbymchenry/codegraph/issues/2305)，狀態 open，更新於 2026-10-02T14:52:20Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 程式語言解析覆蓋及索引新鮮度影響答案；近期 VB.NET 引用解析問題代表仍需逐語言驗證。 授權 API 標記：MIT。

**與 Adam 的關聯／下一步：** 可作 know metabiz wiki 的程式碼與文件連結研究；以跨模組查詢比較圖譜與一般文字檢索。

### 9. langgenius/dify — Watch

**用途與 README 判讀：** 以工作流及 RAG 管線建構 AI 應用與文件查詢流程。 [專案／README](https://github.com/langgenius/dify#readme)。

**動能與維護：** 今日星數 未上榜；快照增量 +55；總星數 157,721。最近 push：2026-10-02T16:12:39Z；最新 release：[1.17.1](https://github.com/langgenius/dify/releases)（2026-09-10T10:04:06Z）。未關閉 issue／PR 合計 913；最近活動抽樣 5 筆。

**活動證據：** [PR #43368](https://github.com/langgenius/dify/pull/43368)，狀態 open，更新於 2026-10-02T16:12:57Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 大型平台有部署與升級負擔；本次未驗證權限隔離或檢索品質，授權條件需以原始文件確認。 授權 API 標記：NOASSERTION（未能由 SPDX 欄位確定授權，採用前須閱讀 LICENSE）。

**與 Adam 的關聯／下一步：** 與 AI 辦公自動化及 know metabiz wiki 最直接相關；作文件問答基準，比較引用正確率與維護成本。

### 10. obra/superpowers — Reference only

**用途與 README 判讀：** 提供 agentic 軟體開發方法與可組合 skills，涵蓋規劃、執行與審查。 [專案／README](https://github.com/obra/superpowers#readme)。

**動能與維護：** 今日星數 561；快照增量 +484；總星數 294,281。最近 push：2026-09-27T02:37:47Z；最新 release：[v6.4.2](https://github.com/obra/superpowers/releases)（2026-09-25T18:08:09Z）。未關閉 issue／PR 合計 295；最近活動抽樣 5 筆。

**活動證據：** [Issue #2443](https://github.com/obra/superpowers/issues/2443)，狀態 open，更新於 2026-10-02T15:24:28Z；內容概況已納入下列風險判斷，公開回報不代表本次已重現。

**風險：** 近期有子 agent 提交不該提交的報告、測試紀錄與技能觸發問題；規則存在不代表執行一定可靠。 授權 API 標記：MIT。

**與 Adam 的關聯／下一步：** 可作 Adam 課程的成熟工作流對照，檢查內部 skill 是否具有明確觸發條件與驗證步驟。

## 明日觀察清單

1. **OpenRig**：追蹤今日 +635 快照增量能否延續；檢查工作階段恢復 issue #86 與 daemon 修正，再決定是否做雙 agent 任務交接實驗。
2. **Ponytail、mattpocock/skills**：查看新版本與遷移說明；挑一個真實功能，比較有無 skill 的修改量及測試結果，而非只量 token。
3. **CodeGraph、Context Mode**：觀察語言解析與工作階段歸屬修正；準備 know metabiz wiki 的公開範例，量測引用正確率、漏查率與上下文用量。
4. **HyperFrames、Agent Reach**：追蹤影片渲染資源回收與字幕原文問題；規劃「來源蒐集 → 知識筆記 → 30 秒雷達影片」示範。
5. **OpenShell、Dify**：確認後續 release、已合併修正及授權說明；把執行隔離與 RAG 文件權限列入後續驗證。
6. **資料健康**：複查 4 個 404 專案是否改名、移除或轉私有；補齊新候選基準，持續區分 Trending 指標與快照增量。

## 證據與限制

本目錄 repos.json 與 snapshots/ 保存數值；trending-evidence.json 為頁面原始卡片；activity-evidence.json 保存每個候選最新 5 筆 issue／PR；readme-evidence.json 保存 README 取樣；run-status.json 記錄查詢、時間、篩選及錯誤。各專案連結、release 與 issue／PR 連結可直接回查。分析為候選篩選，並非安裝、採購或正式導入的驗證結果。
