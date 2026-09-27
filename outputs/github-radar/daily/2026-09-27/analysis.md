# GitHub AI 趨勢雷達｜2026-09-27

## 觀測與判讀

歸檔日期為 Asia/Taipei 前一日 2026-09-27；本次即時觀測於 2026-09-28 台北時間執行。Trending daily 是擷取當下的滾動榜，不能當作昨日台北日界的精確新增。

依指定十組查詢收集，包含 Trending daily 與 README。以下精選 8 個專案，排序優先考慮今日熱度、跨快照增量、相對成長、近期 push、README、release／issue 活動與實務相關性；小型新工具與直接相關的知識管理技能也納入，並非總星數排行榜。

今日星數來自 [GitHub Trending daily](https://github.com/trending?since=daily)。Δ 比較前一歸檔日 2026-09-26 快照與本次 API 觀測，相對成長為 Δ／前次星數。未上榜不等於零成長；無基準則不估算快照增量。今日星數／總星數僅供無基準的新項目判讀熱度，不等於成長率。

證據保存在 `selected-evidence.json`、`trending-daily.json` 與 `repos.json`。精選數值使用補查 API 的觀測，可能與主收集器相差數分鐘。README 為摘要，沒有安裝或效能測試；issues API 含 PR，最近五筆只是活動抽樣，不代表回覆速度或缺陷已修復。

## 精選比較

| 專案 | 今日星數 | 快照 Δ | 相對成長 | 總星數 | 建議 |
| --- | ---: | ---: | ---: | ---: | --- |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 4463 | 4861 | +15.57% | 36,082 | Deep research |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 3060 | 未量測 | 未量測 | 39,157 | Demo content |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 2527 | 2514 | +2.91% | 88,974 | Deep research |
| [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | 114 | 未量測 | 未量測 | 741 | Watch |
| [dream-num/univer](https://github.com/dream-num/univer) | 920 | 939 | +4.93% | 19,986 | Demo content |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 848 | 851 | +1.46% | 58,960 | Reference only |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 未上榜 | 33 | +0.07% | 48,937 | Skill candidate |
| [ishicm/llm-wiki-skills](https://github.com/ishicm/llm-wiki-skills) | 未上榜 | 0 | +0.00% | 25 | Reference only |

### 1. vectorize-io/hindsight — Deep research

**用途與 README：** 提供可跨任務使用的 agent 記憶層。

**動能與維護：** 最近 push 2026-09-26T14:14:46Z；release：v0.10.1（2026-09-21T15:24:30Z）；open issues／PR 164。

最近活動抽樣：[Issue：[Windows] pg0 info reports "stopped" (uri=None) for a live, listening instance](https://github.com/vectorize-io/hindsight/issues/4839)，2026-09-27T14:35:49Z，狀態 open。

**Adam／metabiz 關聯：** Adam 可製作 RAG 與長期記憶比較課程；know metabiz wiki 可研究保留來源與決策脈絡。

**風險：** 近期 issue 回報 Windows 執行狀態偵測與 plugin reload 後未自動保存記憶；應驗證寫入、刪除、租戶隔離與錯誤記憶累積。 GitHub API 授權標示為 MIT。

**下一步：** 用公開文件比較無記憶、RAG、記憶層的引用正確率與跨次一致性。

### 2. debpalash/VoiceStudio — Demo content

**用途與 README：** 本機語音生成、配音、轉錄與有聲書工具；README 宣稱支援多語言，實際品質待測。

**動能與維護：** 最近 push 2026-09-27T13:29:55Z；release：v0.5.6（2026-09-23T08:53:32Z）；open issues／PR 12。

最近活動抽樣：[PR：feat(mcp): describe_voice and design_voice tools for agent voice design](https://github.com/debpalash/VoiceStudio/pull/2368)，2026-09-27T16:12:08Z，狀態 open。

**Adam／metabiz 關聯：** Adam 可示範繁中課程配音與字幕流程；metabiz 可評估內部影音內容製作。

**風險：** MCP 語音設計仍有開放 PR，不能當成已發佈功能；AGPL-3.0、模型授權、硬體需求與聲音使用同意需分別核對。 GitHub API 授權標示為 AGPL-3.0。

**下一步：** 以自有或授權聲音測試繁中專有名詞、配音時間與本機記憶體用量。

### 3. paperclipai/paperclip — Deep research

**用途與 README：** 管理工作中的多個 AI agent 與任務協作。

**動能與維護：** 最近 push 2026-09-27T12:25:56Z；release：v2026.916.1（2026-09-21T21:22:44Z）；open issues／PR 5810。

最近活動抽樣：[PR：fix(openclaw-gateway): send agent.timeout in seconds and keep observing accepted runs](https://github.com/paperclipai/paperclip/pull/14245)，2026-09-27T16:02:04Z，狀態 open。

另見公開 [issue #8047](https://github.com/paperclipai/paperclip/issues/8047) 的執行紀錄保密問題回報；這是風險線索，並非本次驗證的漏洞結論。

**Adam／metabiz 關聯：** 適合 Adam 的 AI 辦公室派工內容；metabiz 可研究內容、文件與開發任務的人工覆核流程。

**風險：** 近期公開 issue 回報執行紀錄可能保存原始秘密值，尚未自行重現；另有取消任務後恢復與 gateway timeout 活動，正式導入前須確認版本及修復。 GitHub API 授權標示為 MIT。

**下一步：** 僅以公開資料做三角色派工，觀察成本、取消與恢復行為。

### 4. mvschwarz/openrig — Watch

**用途與 README：** 以 YAML 定義 agent 團隊，協同管理 Claude Code 與 Codex 工作階段。

**動能與維護：** 最近 push 2026-09-27T07:43:07Z；release：v0.5.17（2026-09-27T07:43:24Z）；open issues／PR 40。

新入選小型專案，今日星數／總星數約 15.4%，但缺乏前日快照，不能推定真實日成長率。

最近活動抽樣：[Issue：bun add -g @openrig/cli fails: bundled @openrig/daemon is also listed in dependencies and 404s on the registry](https://github.com/mvschwarz/openrig/issues/66)，2026-09-27T15:28:38Z，狀態 closed。

**Adam／metabiz 關聯：** Adam 可做雙 agent 分工示範；metabiz 可評估開發與文件任務的跨工具協作。

**風險：** 新版本與小基數帶來高相對熱度，但有安裝依賴、工作區定位、Codex seat 卡住等回報；issue 關閉不代表所有環境已修復。 GitHub API 授權標示為 Apache-2.0。

**下一步：** 追蹤 v0.5.17 安裝重現與 seat 卡住問題，再安排短時限 demo。

### 5. dream-num/univer — Demo content

**用途與 README：** 提供可嵌入的試算表、文件等 Office SDK 與 agent 操作介面。

**動能與維護：** 最近 push 2026-09-27T13:11:49Z；release：v1.0.2（2026-09-24T11:32:24Z）；open issues／PR 158。

最近活動抽樣：[PR：fix(network): propagate merged request termination to all subscribers](https://github.com/dream-num/univer/pull/7762)，2026-09-27T16:01:53Z，狀態 open。

**Adam／metabiz 關聯：** 直接對應 Adam AI 辦公自動化課程，metabiz 可示範表單資料轉報表與內嵌編輯器。

**風險：** README 的 PDF 仍標示 coming soon；近期 issue／PR 涉及新資料列篩選與網路請求生命週期，需驗證公式、繁中輸入及檔案往返。 GitHub API 授權標示為 Apache-2.0。

**下一步：** 使用繁中銷售報表檢查公式與新增列篩選結果。

### 6. rohitg00/ai-engineering-from-scratch — Reference only

**用途與 README：** 從基礎實作 AI engineering 的教材與參考專案。

**動能與維護：** 最近 push 2026-09-27T11:54:19Z；release：v2026.10（2026-09-27T10:17:34Z）；open issues／PR 44。

最近活動抽樣：[Issue：Proposal: Create a Discord community for learners and link it from the website + repository](https://github.com/rohitg00/ai-engineering-from-scratch/issues/475)，2026-09-27T13:01:04Z，狀態 open。

**Adam／metabiz 關聯：** 供 Adam 課程單元與作業設計參考；know metabiz wiki 可建立可重現實驗索引。

**風險：** 剛發佈 Edition 2026.10；教材連結與 dataset 設定問題已有關閉紀錄，但仍需乾淨環境重跑；首頁翻譯不等於完整繁中教材。 GitHub API 授權標示為 MIT。

**下一步：** 比較新版本修訂，重跑一個 RAG 或 agent 單元。

### 7. kepano/obsidian-skills — Skill candidate

**用途與 README：** 將 Obsidian CLI、Markdown、Bases 與 JSON Canvas 操作整理成 agent skills。

**動能與維護：** 最近 push 2026-09-15T14:43:57Z；release：未取得（日期未取得）；open issues／PR 73。

最近活動抽樣：[PR：docs(obsidian-cli): add sandbox/IPC troubleshooting](https://github.com/kepano/obsidian-skills/pull/126)，2026-09-26T03:06:02Z，狀態 open。

**Adam／metabiz 關聯：** 可改編為 Adam 知識管理實作，評估 know metabiz wiki 的來源整理與連結維護。

**風險：** 近期 push 較慢；Codex marketplace 支援與 sandbox／IPC 說明仍有開放 PR，不能視為已可用。 GitHub API 授權標示為 MIT。

**下一步：** 先以測試 vault 驗證格式保真與回滾，再挑選單一可重用 skill。

### 8. ishicm/llm-wiki-skills — Reference only

**用途與 README：** 讓 LLM 建立、消化與整理知識庫的 skill 範例。

**動能與維護：** 最近 push 2026-04-13T14:32:12Z；release：未取得（日期未取得）；open issues／PR 1。

最近活動抽樣：[Issue："健康检查，持续维护"，有点标题党](https://github.com/ishicm/llm-wiki-skills/issues/1)，2026-04-15T06:46:21Z，狀態 open。

**Adam／metabiz 關聯：** 與 know metabiz wiki 直接相關，可比較來源引用、增量整理與人工覆核的設計。

**風險：** 只有 25 星且長期未 push，唯一抽樣 issue 質疑持續維護能力；定位為設計參考，不以相關性代替成熟度。 GitHub API 授權標示為 MIT。

**下一步：** 讀取維護與健康檢查實作，確認是否有可執行流程與測試證據。

## 明日觀察名單

- Hindsight：4,463 stars today 的熱度是否延續；plugin reload 後記憶寫入問題與新版 release 是否改善。
- VoiceStudio：3,060 stars today 是否轉化為穩定使用；MCP 語音設計 PR 是否合併並發佈，繁中配音是否可重現。
- Paperclip：追蹤秘密遮罩、取消恢復與 gateway timeout 的修正狀態，再決定辦公室示範範圍。
- OpenRig：建立第二份快照，開始計算可靠增量；查核 v0.5.17 安裝與 Codex seat 卡住問題。
- Univer：新列篩選與網路請求修正是否合併，PDF 仍不可提前承諾。
- AI Engineering from Scratch：核對 Edition 2026.10 教材修復，挑一單元重跑。
- Obsidian Skills／LLM Wiki Skills：追蹤 marketplace／IPC 相容性與可執行維護流程；保持與 know metabiz wiki 的實務比較。

## 收集完整性與限流狀態

收集器以十組指定查詢、每組 limit=10 完成；原始 326 筆，去重與範圍審查後保留 306 個。已補入關鍵字漏收的 VoiceStudio；一般系統工具、非 AI 應用與 4 筆 API 404 舊資料已排除，原因見 repos.json 的 scope_review。

日誌未觀察到 GitHub API 限流錯誤，無需 limit=5 重試；既有收集器會忽略部分 README／release API 錯誤，因此無版本資訊不等於沒有 release，亦不能保證所有被忽略的請求均成功。

開始觀測時間：2026-09-28T00:10:47.593159+08:00。
