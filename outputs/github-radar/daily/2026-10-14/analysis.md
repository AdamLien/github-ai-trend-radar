# GitHub AI 趨勢雷達｜2026-10-14

目標日期為 Asia/Taipei 前一日 2026-10-14；實際收集於 2026-10-15。這是當次即時觀測，並非回溯重建 10 月 14 日完整榜單。GitHub Trending 的 stars today 與相鄰快照星數差是不同觀測窗口，不能相加或視為同一數值。

## 收集與判讀

指定 10 組查詢以 `--limit 10 --include-trending-daily --include-readme` 執行；初次搜尋遭 HTTP 500，相同參數重試成功。未遇 GitHub API rate limit，未啟用 limit=5。共 350 個累積追蹤專案；Trending 人工範圍覆核保留 7 個 AI／agent 相關專案。VoiceStudio 因關鍵字漏收已補回；一般 Node、Rust、Xcode、Windows 建置與非 AI 逆向工具未納入本次 Trending。

4 個舊專案 API 404 沿用舊資料：`BarberNumber/Midjourney-Software`, `hanshaze/Awesome-Prediction-Market-Trading-Tools`, `mingrath/obsidian-ai-knowledge-agent`, `tonhowtf/omniget`。已標記 `metadata_status`，不列入本日推薦；10 個候選皆取得新資料。新進專案缺少比較基準時，以「未量測」表達增量，不把程式的零值解讀為零成長。

挑選先看 stars today、快照差及相對成長，再用最近 push、README 能力、release 與 issue／PR 活動核對；最後依 Adam 課程、內容製作、AI 辦公自動化與 know metabiz wiki 的價值調整。以下是研究／實作優先順序，不是總星數排行。尚未安裝或實際執行候選工具；效能與用戶數宣稱皆待驗證。

## 值得投入的 10 個專案

| 優先 | 專案 | 分類 | 總星數 | Trending 今日 | 快照差 | 相對成長 |
|---|---|---|---:|---:|---:|---:|
| 1 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | Deep research | 28,869 | 946 | +916 | 3.28% |
| 2 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Demo content | 52,300 | 94 | +219 | 0.42% |
| 3 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | Watch | 26,898 | 2,143 | 未量測 | 未量測 |
| 4 | [morluto/rea](https://github.com/morluto/rea) | Watch | 233,404 | 41,187 | +36,941 | 18.80% |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Demo content | 65,428 | 3,547 | +3,287 | 5.29% |
| 6 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skill candidate | 49,074 | 146 | +372 | 0.76% |
| 7 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Skill candidate | 15,528 | — | +25 | 0.16% |
| 8 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Deep research | 20,650 | — | +29 | 0.14% |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | Skill candidate | 299,020 | — | +493 | 0.17% |
| 10 | [langgenius/dify](https://github.com/langgenius/dify) | Reference only | 158,458 | — | +92 | 0.06% |

快照比較基準為 2026-10-13；相對成長＝星數差 ÷ 基準星數。— 表示未取得 Trending 今日星數，並非今日零星。issue API 含 PR；下文區分兩者，最近 8 筆僅為抽樣，不能代表全量吞吐或回覆率。

## 1. mksglu/context-mode｜Deep research

**用途：** 以 MCP、沙箱與 hooks 控制工具輸出和跨回合記憶，減少 coding agent context 膨脹。 [README](https://github.com/mksglu/context-mode/blob/main/README.md)。

**動能：** 總星數 28,869；Trending 今日 946；相對 2026-10-13 快照差 +916、成長 3.28%。最近 push `2026-10-14T15:00:51Z`；GitHub open issues／PR 合計 357。
最近 release [v1.0.169](https://github.com/mksglu/context-mode/releases/tag/v1.0.169)，發布時間 `2026-06-29T18:18:53Z`。
近期更新抽樣 0 筆：issue 0、PR 0。
issue endpoint 本次回傳空集合；與 open issues 計數存在差異，無法確認原因，維護回應品質仍列未知。

**風險：** README 的壓縮比例是作者宣稱，需用相同任務比較 token、延遲與正確率；ELv2 授權與工具路由權限需確認。issue 抽樣為空，不能推論無缺陷。 API 授權識別為 `NOASSERTION`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** Adam 課程可示範長任務成本控制；辦公自動化可測大量文件／工具輸出；know metabiz wiki 可評估查詢摘要是否漏掉來源。

**下一步：** 用固定 20 份文件測 token 節省與答案引用完整性，追蹤是否有比既有 release 更新的正式版本。

## 2. HKUDS/CLI-Anything｜Demo content

**用途：** 把既有軟體包裝成 agent 能呼叫的 CLI，支援可重複、自動化的軟體操作。 [README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)。

**動能：** 總星數 52,300；Trending 今日 94；相對 2026-10-13 快照差 +219、成長 0.42%。最近 push `2026-09-22T02:01:29Z`；GitHub open issues／PR 合計 162。
最近 release [v0.4.0](https://github.com/HKUDS/CLI-Anything/releases/tag/v0.4.0)，發布時間 `2026-06-25T15:17:49Z`。
近期更新抽樣 8 筆：issue 0、PR 8。
- PR [fix(musescore): reject out-of-range transpose intervals instead of wrapping](https://github.com/HKUDS/CLI-Anything/pull/553)：open，更新 `2026-10-14T16:10:33Z`。

**風險：** 近期 PR 涉及格式驗證、HTTP timeout 與轉調邊界，表示整合細節仍需驗證；任意軟體覆蓋範圍是願景，不能直接當成已支援能力。 API 授權識別為 `Apache-2.0`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** 適合 Adam「讓 agent 操作辦公軟體」課程與短影片；metabiz 可挑單一報表匯出流程；wiki 可收錄 CLI 操作與復原 SOP。

**下一步：** 挑一項可逆的報表匯出任務做 demo，確認 JSON 輸出、錯誤處理與現有軟體版本相容。

## 3. ifixai-ai/iFixAi｜Watch

**用途：** 為 agent 執行結果提供獨立稽核，檢查行為是否符合預期。 [README](https://github.com/ifixai-ai/iFixAi/blob/main/README.md)。

**動能：** 總星數 26,898；Trending 今日 2,143；相對 2026-10-13 快照差 未量測、成長 未量測。最近 push `2026-10-14T09:24:48Z`；GitHub open issues／PR 合計 7。
最近 release [v4.1.0](https://github.com/ifixai-ai/iFixAi/releases/tag/v4.1.0)，發布時間 `2026-10-08T06:18:45Z`。
近期更新抽樣 8 筆：issue 0、PR 8。
- PR [fix: preserve all Gemini system message frames](https://github.com/ifixai-ai/iFixAi/pull/285)：closed，更新 `2026-10-14T09:24:49Z`。

**風險：** README 的快速稽核與可靠性宣稱尚未實測；近期 Gemini system message 修正顯示跨模型語意需要回歸驗證，稽核本身也可能錯判。 API 授權識別為 `Apache-2.0`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** Adam 可製作 agent 自評與外部評估比較內容；辦公自動化可評估 CRM／報表完成條件；wiki 可保存任務驗收證據。

**下一步：** 加入成功、漏步驟、錯誤輸出三類樣本，量測稽核誤判，追蹤新 release。

## 4. morluto/rea｜Watch

**用途：** 以 MCP 串接應用程式、二進位與 runtime 行為的逆向分析。 [README](https://github.com/morluto/rea/blob/main/README.md)。

**動能：** 總星數 233,404；Trending 今日 41,187；相對 2026-10-13 快照差 +36,941、成長 18.80%。最近 push `2026-10-14T16:17:15Z`；GitHub open issues／PR 合計 703。
最近 release [rea-agents-6.5.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.5.0)，發布時間 `2026-10-14T12:32:45Z`。
近期更新抽樣 8 筆：issue 1、PR 7。
- Issue [(Bug) Passive browser and Inspector calls can wait indefinitely after successful discovery](https://github.com/morluto/rea/issues/3553)：open，更新 `2026-10-14T16:15:02Z`。
- PR [feat(javascript): resolve package exports and imports wildcard patterns](https://github.com/morluto/rea/pull/2018)：open，更新 `2026-10-14T16:15:04Z`。

**風險：** 極高星數成長代表注意力，未證明成熟度；近期 issue #3553 回報 browser／Inspector 呼叫可能無限等待。只對有權分析的測試程式做驗證。 API 授權識別為 `MIT`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** 適合 Adam agent 工具能力邊界與 debugging 題材；辦公自動化可研究既有軟體介面；know metabiz wiki 可保存可重現的技術分析。

**下一步：** 先確認 #3553 的修復狀態，測 timeout 與取消，再考慮完整 demo。

## 5. debpalash/VoiceStudio｜Demo content

**用途：** 以本地 AI 提供聲音複製、配音、轉錄與有聲內容製作。 [README](https://github.com/debpalash/VoiceStudio/blob/main/README.md)。

**動能：** 總星數 65,428；Trending 今日 3,547；相對 2026-10-13 快照差 +3,287、成長 5.29%。最近 push `2026-10-14T14:57:05Z`；GitHub open issues／PR 合計 162。
最近 release [v0.5.6](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)，發布時間 `2026-09-23T08:53:32Z`。
近期更新抽樣 8 筆：issue 3、PR 5。
- Issue [(Bug) Backend is running but temporarily not responding on port 3900. Waiting for reco](https://github.com/debpalash/VoiceStudio/issues/2840)：open，更新 `2026-10-14T15:14:20Z`。
- PR [fix(clone): skip a passage Whisper filled with a repetition loop (#2836)](https://github.com/debpalash/VoiceStudio/pull/2838)：open，更新 `2026-10-14T15:02:59Z`。

**風險：** AGPL 授權與模型個別授權需確認；後端暫時失去回應及 spawn 故障有近期回報。聲音使用需取得授權，繁體中文效果與硬體需求待實測。 API 授權識別為 `AGPL-3.0`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** 直接服務 Adam 課程旁白、短影片與多語內容；辦公可做會議逐字稿；wiki 可保存逐字稿與來源音檔關聯。

**下一步：** 用 Adam 授權音訊做 60 秒繁體中文樣本，比較轉錄錯字、推論時間與匯出穩定性。

## 6. K-Dense-AI/scientific-agent-skills｜Skill candidate

**用途：** 提供研究與資料分析領域的可組合 skills、工具與資料庫連接範例。 [README](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md)。

**動能：** 總星數 49,074；Trending 今日 146；相對 2026-10-13 快照差 +372、成長 0.76%。最近 push `2026-10-12T09:43:31Z`；GitHub open issues／PR 合計 27。
最近 release [v2.72.0](https://github.com/K-Dense-AI/scientific-agent-skills/releases/tag/v2.72.0)，發布時間 `2026-10-01T22:42:08Z`。
近期更新抽樣 8 筆：issue 0、PR 8。
- PR [Add MNE-Python skill for EEG/MEG analysis](https://github.com/K-Dense-AI/scientific-agent-skills/pull/283)：open，更新 `2026-10-14T16:10:55Z`。

**風險：** README 對使用量與 validated 的敘述屬作者宣稱；不能把研究 workflow 當成醫療建議。近期 PR 包含技能擴充與失效連結修正，外部依賴仍需抽查。 API 授權識別為 `MIT`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** Adam 可拆解專業 skill 的輸入、產物與驗收設計；辦公可參考資料分析流程；wiki 可用技能卡片整理方法與來源。

**下一步：** 抽查一項通用分析 skill 的依賴、引用與輸出格式，避免一次匯入整套技能。

## 7. AgriciDaniel/claude-obsidian｜Skill candidate

**用途：** 讓 Claude Code 將來源整理為互連 Markdown 與 Obsidian 知識圖，形成可維護的第二大腦。 [README](https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md)。

**動能：** 總星數 15,528；Trending 今日 未上本次 Trending／未提供；相對 2026-10-13 快照差 +25、成長 0.16%。最近 push `2026-09-10T17:44:23Z`；GitHub open issues／PR 合計 29。
最近 release [v2.2.0](https://github.com/AgriciDaniel/claude-obsidian/releases/tag/v2.2.0)，發布時間 `2026-09-10T14:49:12Z`。
近期更新抽樣 8 筆：issue 5、PR 3。
- Issue [Permission request: introducing the wiki-query skill on PrompTown (free, not an endorsement)](https://github.com/AgriciDaniel/claude-obsidian/issues/197)：open，更新 `2026-10-13T13:31:49Z`。
- PR [Ptbr](https://github.com/AgriciDaniel/claude-obsidian/pull/198)：closed，更新 `2026-10-14T13:40:18Z`。

**風險：** issue #196 回報 Windows SessionStart／Stop hook timeout；自動連結可能造成錯誤關係或文件改寫，需版本控制、來源追溯與小樣本驗收。 API 授權識別為 `MIT`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** 與 know metabiz wiki 高度相關；Adam 可做從原始資料到 wiki 的課程，辦公可整理會議、產品與流程知識。

**下一步：** 測 10 份去識別化公司文件的來源連結、重複匯入與增量更新，追蹤 hook timeout。

## 8. nashsu/llm_wiki｜Deep research

**用途：** 桌面知識庫將多格式文件增量整理成結構化 wiki，支援來源追溯與多模態 ingestion。 [README](https://github.com/nashsu/llm_wiki/blob/main/README.md)。

**動能：** 總星數 20,650；Trending 今日 未上本次 Trending／未提供；相對 2026-10-13 快照差 +29、成長 0.14%。最近 push `2026-09-28T01:43:23Z`；GitHub open issues／PR 合計 275。
最近 release [v0.6.12](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.12)，發布時間 `2026-09-28T02:58:13Z`。
近期更新抽樣 8 筆：issue 2、PR 6。
- Issue [Windows 桌面持续占用 3-5 核（0.6.12）：周期性全量扫描/哈希放大，附实测与定位](https://github.com/nashsu/llm_wiki/issues/812)：open，更新 `2026-10-10T09:39:19Z`。
- PR [feat: add GitHub Copilot device-auth text provider](https://github.com/nashsu/llm_wiki/pull/815)：open，更新 `2026-10-13T06:25:26Z`。

**風險：** issue #811 回報長文件分析上限，#812 回報背景全量掃描造成負載；公司文件上傳位置、模型成本與資料隔離需要實測確認。 API 授權識別為 `NOASSERTION`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** know metabiz wiki 的直接候選；Adam 可對比 RAG 檢索與持續整理 wiki；辦公可用產品、合約與 SOP 文件做小型 PoC。

**下一步：** 以長 PDF、Office 文件和重複匯入測引用與 CPU 負載，追蹤 #811／#812。

## 9. obra/superpowers｜Skill candidate

**用途：** 以可組合 skills 提供 coding agent 的需求釐清、計畫、測試與交付流程。 [README](https://github.com/obra/superpowers/blob/main/README.md)。

**動能：** 總星數 299,020；Trending 今日 未上本次 Trending／未提供；相對 2026-10-13 快照差 +493、成長 0.17%。最近 push `2026-10-10T03:03:30Z`；GitHub open issues／PR 合計 347。
最近 release [v7.0.0](https://github.com/obra/superpowers/releases/tag/v7.0.0)，發布時間 `2026-10-10T00:28:58Z`。
近期更新抽樣 8 筆：issue 4、PR 4。
- Issue [1% chance skill overfiring](https://github.com/obra/superpowers/issues/2514)：open，更新 `2026-10-14T16:14:17Z`。
- PR [fix(using-git-worktrees): check ignore status on selected directory specifically (#2515)](https://github.com/obra/superpowers/pull/2518)：open，更新 `2026-10-14T14:58:20Z`。

**風險：** 近期 issue #2514 回報 skill 過度觸發，#2515 涉及 worktree ignore 檢查；workflow 不能取代任務本身的授權與驗收。 API 授權識別為 `MIT`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** 適合 Adam 的 AI coding 工作法課程；metabiz 辦公腳本可參考計畫／驗收模板；wiki 可收錄適用條件與交付 SOP。

**下一步：** 檢查 v7.0.0 的 hook／觸發行為，以一個小任務比較耗時與驗收品質。

## 10. langgenius/dify｜Reference only

**用途：** 整合 LLM workflow、agents 與 RAG 的應用平台，作為成熟產品與自架方案比較基準。 [README](https://github.com/langgenius/dify/blob/main/README.md)。

**動能：** 總星數 158,458；Trending 今日 未上本次 Trending／未提供；相對 2026-10-13 快照差 +92、成長 0.06%。最近 push `2026-10-14T16:08:32Z`；GitHub open issues／PR 合計 1,154。
最近 release [1.17.1](https://github.com/langgenius/dify/releases/tag/1.17.1)，發布時間 `2026-09-10T10:04:06Z`。
近期更新抽樣 8 筆：issue 0、PR 8。
- PR [ci: enable Ruff E711](https://github.com/langgenius/dify/pull/44088)：closed，更新 `2026-10-14T16:08:34Z`。

**風險：** 近期抽樣多為 CI／lint PR，不能視為功能品質證據；自架維運、資料隔離、升級相容與授權條件需核對。星數規模大不代表當天動能最高。 API 授權識別為 `NOASSERTION`；`NOASSERTION` 需另讀授權全文確認。

**與 Adam／metabiz 的關聯：** Adam 可用作流程編排教學與競品基準；metabiz 可比較 CRM／客服／報表自動化；wiki 可評估檢索引用及權限控管。

**下一步：** 追蹤比 1.17.1 更新的穩定 release 與 migration，將 wiki PoC 成本和可追溯性列入比較。

## 明日觀察清單（下一次目標日期 2026-10-15）

1. Context Mode：關注今日星數是否延續，實測 context 壓縮的正確率與 ELv2 適用範圍。
2. iFixAi：補上第二筆快照基準，確認 2,143 stars today 是否轉化為穩定成長與稽核品質。
3. REA：追蹤 #3553 無限等待問題與 6.5.0 後續修復；星數熱度不直接提高採用等級。
4. VoiceStudio／CLI-Anything：用單一可重現、可逆辦公或課程任務檢查輸出穩定性。
5. llm_wiki／claude-obsidian：比較長文件引用、重複匯入、背景負載與 hook timeout，作為 know metabiz wiki PoC 的驗收條件。
6. Scientific Agent Skills／Superpowers：抽查一個 skill 的觸發、依賴及驗收，再決定是否拆為 Adam 的技能候選。
7. Dify：保留為平台基準，觀察穩定 release 與升級路徑；持續標記 404 舊資料，避免誤當新動能。

## 可核對來源

- [GitHub Trending daily](https://github.com/trending?since=daily)：保存於 `trending-daily.json`，含觀測時間與排除項目。
- `repos.json`／`snapshots/repos-2026-10-14.json`：總星數、快照差、push、授權與資料新鮮度。
- `selected-evidence.json`：10 個候選的 README、release 與 issue／PR 更新抽樣，來源均為 GitHub API。
- `collection-status.json`、`collector-limit-10.log`、`collector-limit-10-retry.log`：首次 HTTP 500、重試成功與無 rate limit 的紀錄。
