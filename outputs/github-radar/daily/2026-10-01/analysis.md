# GitHub AI 趨勢雷達｜2026-10-01

## 今日判讀

優先深研 OpenShell、OpenRig 與 PageIndex；HyperFrames 適合內容展示，Impeccable 與工程 skills 值得小規模比較。Context Mode 與 Ponytail 有熱度，但相容性及發布節奏仍需追蹤。排序結合今日新增、快照增量、相對成長、最近 push、README、release 與 issue／PR，並非總星數排行。

## 資料口徑

- 目標日期：Asia/Taipei 前一天 2026-10-01；實際於 2026-10-02 台北時間收集。以下是執行當下觀測，不是昨天午夜封存資料。
- 今日新增來源：[GitHub Trending daily](https://github.com/trending?since=daily)，保存於 `trending-daily.json`。未上榜標示「未觀測」，不是 0。
- 下列總星數與活動證據來自 `review-evidence.json`；與 collector 稍早或稍後取得的 `repos.json` 可能有少量差異。快照增量以 2026-09-30 的 `repos.json` 為基準；相對成長＝增量／前次星數。首次觀察不推算成長。
- 每個候選另讀完整 README、latest release 及最近更新的五筆 issue／PR。open_issues_count 含 PR，非 bug 數；樣本不能代表整體解決率。README 效果均未在本次實測。
- 十組指定查詢搭配 Trending 與歷史追蹤。搜尋本身偏向高總星數，人工選題另以成長與實際用途校正。Trending 只納入 AI／agent／skills／MCP／LLM 或相關開發自動化範圍；沒有安裝或執行候選專案內容。

## 值得追蹤的九個專案

### NVIDIA/OpenShell — Deep research

[GitHub／README](https://github.com/NVIDIA/OpenShell) · **總星數 13,814** · **今日新增 +2,503** · 快照增量 +1,983（+16.76%）

- 用途：自主 AI agent 的隔離執行環境，以政策約束檔案、網路與憑證使用；README 說明核心層控管及政策變更檢查。
- 動能：單日關注與相對成長同時強，近期 push 活躍，值得先研究權限邊界。 最近 push：2026-10-01T16:13:07Z；release：v0.1.2（2026-09-28T03:58:00Z）。[發布頁](https://github.com/NVIDIA/OpenShell/releases)
- 活動證據：[fix(mxc): redact injected secrets from gateway diagnostics](https://github.com/NVIDIA/OpenShell/pull/3853)，open，更新 2026-10-01T16:13:02Z。未關閉 issue／PR 合計 510。
- 風險：診斷資訊遮蔽修正 PR #3853 尚開啟；安全宣稱未經本次實測，不能直接視為企業環境保證。
- Adam／metabiz 關聯：Adam 可設計 AI 辦公代理權限課程；metabiz 先以公開 wiki 測試資料驗證隔離。

### mvschwarz/openrig — Deep research

[GitHub／README](https://github.com/mvschwarz/openrig) · **總星數 3,479** · **今日新增 +640** · 快照增量 +667（+23.72%）

- 用途：以 YAML 組織 Claude Code、Codex 等持續運作的代理團隊；README 有兩代理入門與環境需求。
- 動能：小基數相對成長突出，且 v0.6.3 剛發布，優先於單看總星數的大型清單。 最近 push：2026-10-01T15:52:22Z；release：v0.6.3（2026-09-30T19:32:46Z）。[發布頁](https://github.com/mvschwarz/openrig/releases)
- 活動證據：[fix(restore-check): use SQLite queue and selected Claude hooks (#130)](https://github.com/mvschwarz/openrig/pull/328)，open，更新 2026-10-01T16:12:23Z。未關閉 issue／PR 合計 92。
- 風險：恢復檢查與交接修正仍在 PR；啟動會修改 hooks／工作區信任設定，README 明列原生 Windows 不支援。
- Adam／metabiz 關聯：Adam 多代理課程可示範研究、撰稿分工；AI 辦公流程以可恢復任務驗收，wiki 保存交接紀錄。

### VectifyAI/PageIndex — Deep research

[GitHub／README](https://github.com/VectifyAI/PageIndex) · **總星數 38,377** · **今日新增 未觀測** · 快照增量 +414（+1.09%）

- 用途：以文件樹與 LLM 推理檢索內容，README 提供 local／cloud 模式，不依賴向量資料庫。
- 動能：雖未出現在本次 Trending 篩選，仍有快照成長與新 release；文件樹統一 PR #541 已合併。 最近 push：2026-10-01T15:24:06Z；release：v0.2.21（2026-10-01T15:26:25Z）。[發布頁](https://github.com/VectifyAI/PageIndex/releases)
- 活動證據：[Unify the document tree across local and cloud](https://github.com/VectifyAI/PageIndex/pull/541)，closed，更新 2026-10-01T15:20:10Z。未關閉 issue／PR 合計 115。
- 風險：繁中引用正確率、模型費用、延遲與權限隔離尚未驗證；本機執行不代表模型請求不出網。
- Adam／metabiz 關聯：直接對應 know metabiz wiki：用公開 SOP 比較向量檢索與樹狀檢索，轉成 Adam RAG 課程案例。

### heygen-com/hyperframes — Demo content

[GitHub／README](https://github.com/heygen-com/hyperframes) · **總星數 55,157** · **今日新增 +624** · 快照增量 +629（+1.15%）

- 用途：把 HTML、CSS、媒體與可定位動畫渲染成影片；README 提供 agent skills 與 CLI 製作流程。
- 動能：今日熱度搭配當日 release，且編輯器近期 PR 活躍，適合做可重現短片。 最近 push：2026-10-01T16:13:21Z；release：v0.8.105（2026-10-01T14:38:48Z）。[發布頁](https://github.com/heygen-com/hyperframes/releases)
- 活動證據：[feat(studio): export ColorField and GradientField; a style commit takes a map](https://github.com/heygen-com/hyperframes/pull/4863)，open，更新 2026-10-01T16:09:10Z。未關閉 issue／PR 合計 220。
- 風險：時間軸掉幀修正 PR #4855 尚開啟；字型、繁中字幕、音畫同步與素材授權需另測。
- Adam／metabiz 關聯：Adam 可製作課程開場及產品短片；AI 辦公自動化可把 wiki SOP 改寫為教學影片，保留人工審稿。

### pbakaus/impeccable — Skill candidate

[GitHub／README](https://github.com/pbakaus/impeccable) · **總星數 73,432** · **今日新增 +463** · 快照增量 +573（+0.79%）

- 用途：給 coding agent 的前端設計指引，README 列出設計命令、瀏覽器迭代與確定性檢查規則。
- 動能：有近期 engine release 與整合更新，關注度可轉成具體介面改善實驗。 最近 push：2026-10-01T00:06:24Z；release：engine-v0.1.9（2026-09-30T23:46:03Z）。[發布頁](https://github.com/pbakaus/impeccable/releases)
- 活動證據：[Fix: Grok Windows Stop hook ParserError under PowerShell](https://github.com/pbakaus/impeccable/pull/833)，closed，更新 2026-10-01T16:05:43Z。未關閉 issue／PR 合計 64。
- 風險：安裝失敗 issue #850 尚開啟；自動設計檢查不能替代可用性、無障礙及品牌審查。
- Adam／metabiz 關聯：Adam 可示範 AI 前端設計前後對照；可評估 know metabiz wiki 閱讀介面與辦公表單改善。

### mattpocock/skills — Skill candidate

[GitHub／README](https://github.com/mattpocock/skills) · **總星數 273,590** · **今日新增 +888** · 快照增量 +830（+0.30%）

- 用途：可組合的工程 skills；README 區分受管理 plugin 與可自行修改的檔案安裝方式。
- 動能：今日星數高但相對成長較低，價值在可拆解的工程流程，應逐項比較現有 skills。 最近 push：2026-09-29T12:38:37Z；release：v1.2.3（2026-08-06T14:05:28Z）。[發布頁](https://github.com/mattpocock/skills/releases)
- 活動證據：[[FYI] OpenAI-curated Codex package adds unsupported CHAT product metadata](https://github.com/mattpocock/skills/issues/1131)，open，更新 2026-10-01T15:21:53Z。未關閉 issue／PR 合計 543。
- 風險：近期有套件相容與診斷流程回報；避免重複安裝，先檢查授權、版本與既有技能重疊。
- Adam／metabiz 關聯：Adam 可把需求釐清、診斷與驗證流程做成課程；metabiz 可將可重複 SOP 整理成技能與 wiki 文件。

### mksglu/context-mode — Watch

[GitHub／README](https://github.com/mksglu/context-mode) · **總星數 24,705** · **今日新增 +357** · 快照增量 +339（+1.39%）

- 用途：以 MCP 工具隔離大量原始輸出，搭配 SQLite／FTS5 檢索維持工作階段連續性。
- 動能：持續新增星數且當日有 push，但最新 release 日期較舊；先驗證目前程式與發布版本差異。 最近 push：2026-10-01T12:07:41Z；release：v1.0.169（2026-06-29T18:18:53Z）。[發布頁](https://github.com/mksglu/context-mode/releases)
- 活動證據：[[Bug]: Pi bridge on Bun spins on unfinalized statements — ~150k/day "invalid database connection pointer" per pid, and intermittent "Failed to load extension: disk I/O error"](https://github.com/mksglu/context-mode/issues/1205)，open，更新 2026-10-01T14:18:44Z。未關閉 issue／PR 合計 309。
- 風險：Pi／Bun 資料庫指標錯誤 issue #1205 與恢復工具名稱問題 #1028 尚開啟；節省比例為作者宣稱。
- Adam／metabiz 關聯：AI 辦公長任務與 wiki 大量檢索有需求；Adam 可先測 token、恢復準確率與安裝穩定性，再決定課程示範。

### DietrichGebert/ponytail — Watch

[GitHub／README](https://github.com/DietrichGebert/ponytail) · **總星數 150,056** · **今日新增 +1,179** · 快照增量 +1,234（+0.83%）

- 用途：讓 coding agent 優先利用原生功能、減少不必要程式碼的技能；README 提供對照實驗。
- 動能：今日熱度明顯，但最近 push／release 停在 9 月中，不能把星數成長當成維護加速。 最近 push：2026-09-14T14:34:56Z；release：v4.10.0（2026-09-14T14:38:56Z）。[發布頁](https://github.com/DietrichGebert/ponytail/releases)
- 活動證據：[fix(pi): inject via systemPromptOptions.sections to preserve prompt cache](https://github.com/DietrichGebert/ponytail/pull/963)，open，更新 2026-10-01T15:43:43Z。未關閉 issue／PR 合計 327。
- 風險：Pi 提示快取相容 issue #953 尚開啟；README 效果來自特定模型與少量任務，不可推廣成普遍安全保證。
- Adam／metabiz 關聯：Adam 可做「少寫程式是否仍正確」對照內容；metabiz 自動化只借用簡化原則，wiki 記錄失敗案例。

### cursor/plugins — Reference only

[GitHub／README](https://github.com/cursor/plugins) · **總星數 9,274** · **今日新增 +157** · 快照增量 +148（+1.62%）

- 用途：官方 Cursor plugin 範例集合，README 列出教學、團隊工作流、CLI 設計與文件工具。
- 動能：每日新增星數與近期 push 顯示生態持續更新；未取得 latest release，參考單個 plugin 變更較有意義。 最近 push：2026-09-30T18:08:30Z；release：未取得（無日期）。[發布頁](https://github.com/cursor/plugins/releases)
- 活動證據：[Add WhatSetter third-party MCP plugin](https://github.com/cursor/plugins/pull/389)，open，更新 2026-10-01T14:58:50Z。未關閉 issue／PR 合計 174。
- 風險：集合中的第三方整合各有權限及維護狀態；PR 存在不等於已審核或上架，亦不可直接假定跨 agent 相容。
- Adam／metabiz 關聯：Adam 可用來比較 plugin 包裝與 skills；AI 辦公整合設計及 know metabiz wiki 文件導覽可參考其結構。

## 明日觀察清單

下一期目標日期為 2026-10-02，預計 2026-10-03 台北時間執行；比較本次觀測基準，勿把滾動 Trending 當成固定 24 小時增量。

1. OpenShell：追蹤 PR #3853、#3846 是否合併及發布，確認高成長有無延續。
2. OpenRig：追蹤 v0.6.3 後的恢復與交接修正，以兩代理單一任務測可靠性。
3. PageIndex：檢查 v0.2.21 文件樹變更，用同一組繁中公開文件測引用、延遲、費用。
4. HyperFrames／Impeccable：各選一個可重現輸出，驗證字幕／渲染與安裝流程，再決定內容製作。
5. Context Mode／Ponytail：追蹤上述 SQLite、Pi 快取問題；發布修正前維持 Watch。
6. 工程 skills／Cursor plugins：看具體技能差異與相容性，避免以總星數或清單規模決定安裝。

## 執行狀態

收集器以 --limit 10 完成，共 332 個專案；未偵測到 GitHub API 限流，未啟用 --limit 5 重試。執行記錄保存於 collection-status.json 與 collector-limit-10.log。


資料限制：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget 的 GitHub API 回傳 404，收集器沿用歷史 metadata；不代表本次已成功查得，也不應把其零增量視為實際停滯。四者均未納入本篇九項推薦。
