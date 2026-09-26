# GitHub AI 趨勢雷達｜2026-09-26

## 觀測範圍與判讀

本報告歸檔日期為台北前一日 **2026-09-26**；即時觀測始於 **2026-09-27T00:11:21.137430+08:00**。GitHub Trending daily 並非可按台北日期回查的歷史榜，本報告不將今日觀測冒充昨日精確新增。

依指定十組查詢執行，收集器每組 limit=10，包含 Trending daily 與 README。範圍審查後保留 306 個專案，以下精選 9 個；排序兼顧 stars today、快照增量、相對成長、最近 push、README、release、issue／PR 活動與實務相關性，並非總星數榜。

stars today 來自 [GitHub Trending daily](https://github.com/trending?since=daily)；Δ 與相對成長來自前次快照，間隔見各項說明。未上榜不代表零新增；缺乏比較基準不等於零成長。issue 數含 PR，最近五筆活動只是抽樣，不能推論維護者回覆速度。README 僅收集摘要，未進行安裝或效能驗證。

**限流狀態：** No rate-limit error observed in collector logs; limit 10 used. 收集器會忽略部分 release／README API 錯誤，因此未取得版本資訊不等於沒有 release。

## 精選專案

| 專案 | Stars today | 快照 Δ | 相對成長 | 總星數 | 建議 |
| --- | ---: | ---: | ---: | ---: | --- |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 2,589 | +2,461 | +2.93% | 86,460 | Deep research |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 2,152 | +2,097 | +7.20% | 31,221 | Deep research |
| [dream-num/univer](https://github.com/dream-num/univer) | 845 | +814 | +4.46% | 19,047 | Demo content |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 828 | +857 | +1.50% | 58,109 | Reference only |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | 143 | 未量測 | 未量測 | 7,173 | Demo content |
| [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) | 15 | 未量測 | 未量測 | 9,016 | Demo content |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 未上榜 | +34 | +0.07% | 48,904 | Skill candidate |
| [ishicm/llm-wiki-skills](https://github.com/ishicm/llm-wiki-skills) | 未上榜 | +0 | +0.00% | 25 | Skill candidate |
| [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | 409 | +358 | +0.95% | 37,852 | Watch |

### 1. paperclipai/paperclip — Deep research

**用途：** 管理工作中的多個 AI agent，適合研究任務分派與團隊協作。

**動能與維護：** 快照基準 2026-09-25 → 2026-09-26，Δ +2,461、相對成長 +2.93%；最新 push 2026-09-26T16:13:56Z。最新 release：v2026.916.1（2026-09-21T21:22:44Z）。目前 open issues／PR 共 5716。最近抽樣：[Issue #14140](https://github.com/paperclipai/paperclip/issues/14140)，更新 2026-09-26T16:10:56Z；標題：Custom MCP servers whose 401 lacks WWW-Authenticate never get OAuth discovery (e.g. Lucid)。

**Adam／metabiz 關聯：** Adam 可做『AI 辦公室如何派工』課程；metabiz 可研究文件整理、內容製作與開發任務的協作流程。

**風險與證據限制：** 近期 issue 回報部分 MCP 服務的 OAuth discovery 相容性問題；須驗證登入、權限與任務成本，不能以高星數當成企業可用性證明。 GitHub API 授權標示：MIT；實際採用仍須核對所用元件授權。

**下一步：** 用公開資料做三角色派工示範，量測成功率、人工介入與費用。

### 2. vectorize-io/hindsight — Deep research

**用途：** 提供 agent 可持續使用與學習的記憶層。

**動能與維護：** 快照基準 2026-09-25 → 2026-09-26，Δ +2,097、相對成長 +7.20%；最新 push 2026-09-26T14:14:46Z。最新 release：v0.10.1（2026-09-21T15:24:30Z）。目前 open issues／PR 共 143。最近抽樣：[PR #4816](https://github.com/vectorize-io/hindsight/pull/4816)，更新 2026-09-26T15:43:03Z；標題：fix(embed): don't leak parent PYTHONPATH into the daemon child。

**Adam／metabiz 關聯：** 適合 Adam 的『RAG 與 Agent 記憶差別』內容；可評估 know metabiz wiki 如何保留來源、決策與跨次任務脈絡。

**風險與證據限制：** 近期活動涉及 Hermes 整合與子程序環境修正；記憶寫入、錯誤資訊累積、刪除與使用者隔離仍須實測。 GitHub API 授權標示：MIT；實際採用仍須核對所用元件授權。

**下一步：** 以同一批公開文件比較無記憶、RAG、記憶層三種回答的來源正確率。

### 3. dream-num/univer — Demo content

**用途：** 可嵌入的辦公 SDK，結合試算表、文件與 agent 操作介面。

**動能與維護：** 快照基準 2026-09-25 → 2026-09-26，Δ +814、相對成長 +4.46%；最新 push 2026-09-24T14:02:42Z。最新 release：v1.0.2（2026-09-24T11:32:24Z）。目前 open issues／PR 共 147。最近抽樣：[PR #7749](https://github.com/dream-num/univer/pull/7749)，更新 2026-09-26T13:37:00Z；標題：fix(sheets-ui): keep IME input on the selected cell before editing。

**Adam／metabiz 關聯：** 與 AI 辦公自動化最直接：可製作表單資料轉報表的課程，並評估 metabiz 內部文件編輯介面。

**風險與證據限制：** 近期有 IME 輸入修正與啟動錯誤回報；繁體中文輸入、公式與匯入匯出要驗證。README 將 PDF 標示為 coming soon，不能承諾已完整支援。 GitHub API 授權標示：Apache-2.0；實際採用仍須核對所用元件授權。

**下一步：** 示範一份繁體中文銷售報表，檢查公式結果與檔案往返保真度。

### 4. rohitg00/ai-engineering-from-scratch — Reference only

**用途：** 從基礎實作 AI engineering 的教材與參考專案。

**動能與維護：** 快照基準 2026-09-25 → 2026-09-26，Δ +857、相對成長 +1.50%；最新 push 2026-09-26T08:12:38Z。最新 release：v2026.09（2026-09-07T11:42:35Z）。目前 open issues／PR 共 47。最近抽樣：[Issue #493](https://github.com/rohitg00/ai-engineering-from-scratch/issues/493)，更新 2026-09-26T12:36:50Z；標題：fix: Wikipedia dataset config '20220301.en' no longer exists。

**Adam／metabiz 關聯：** 可作 Adam 課程架構與作業設計參考；將可重現的範例整理成 know metabiz wiki 的學習索引。

**風險與證據限制：** 近期 issue 提到 Wikipedia dataset 設定失效，表示教材步驟可能隨外部依賴改變；翻譯首頁不代表所有內容都有完整繁中版本。 GitHub API 授權標示：MIT；實際採用仍須核對所用元件授權。

**下一步：** 挑一個基礎單元乾淨安裝重跑，再決定是否改編成課程。

### 5. mobile-next/mobile-mcp — Demo content

**用途：** 透過 MCP 操作 iOS、Android 與模擬器，支援行動端自動化。

**動能與維護：** 快照基準 無 → 2026-09-26，Δ 未量測、相對成長 未量測；最新 push 2026-09-23T15:38:57Z。最新 release：1.0.4（2026-09-13T20:24:38Z）。目前 open issues／PR 共 43。最近抽樣：[Issue #303](https://github.com/mobile-next/mobile-mcp/issues/303)，更新 2026-09-25T15:26:49Z；標題：WebDriverAgent fails to start on iOS 26.2 / Xcode 26.2 simulator。

**Adam／metabiz 關聯：** 可做 Adam 的跨裝置 AI 助理示範；metabiz 可評估 App 測試、介面檢查與行動辦公流程。

**風險與證據限制：** 近期回報 iOS 26.2／Xcode 26.2 的 WebDriverAgent 啟動問題；裝置版本、權限與文字輸入特殊字元都可能影響成功率。 GitHub API 授權標示：Apache-2.0；實際採用仍須核對所用元件授權。

**下一步：** 先用測試裝置跑固定的讀取與截圖流程，記錄失敗與重試。

### 6. anthropics/claude-code-action — Demo content

**用途：** 把 Claude Code 整合進 GitHub Actions，支援開發協作自動化。

**動能與維護：** 快照基準 無 → 2026-09-26，Δ 未量測、相對成長 未量測；最新 push 2026-09-25T21:52:11Z。最新 release：v1（2025-08-26T17:01:10Z）。目前 open issues／PR 共 805。最近抽樣：[PR #1861](https://github.com/anthropics/claude-code-action/pull/1861)，更新 2026-09-26T07:04:31Z；標題：Keep reading after a result while background agents are still running。

**Adam／metabiz 關聯：** 適合 Adam 的 AI 開發工作流內容；metabiz 可先演示 issue 分析與 PR 摘要。

**風險與證據限制：** 近期 PR 涉及背景 agent 尚未結束時的結果讀取；需確認 workflow 權限、費用與不受信任 PR 的處理方式。 GitHub API 授權標示：MIT；實際採用仍須核對所用元件授權。

**下一步：** 在測試 repository 用唯讀分析工作流驗證觸發、完成狀態與輸出品質。

### 7. kepano/obsidian-skills — Skill candidate

**用途：** 讓相容 Agent Skills 的工具操作 Obsidian 與其開放格式。

**動能與維護：** 快照基準 2026-09-25 → 2026-09-26，Δ +34、相對成長 +0.07%；最新 push 2026-09-15T14:43:57Z。最新 release：未取得最新 release。目前 open issues／PR 共 73。最近抽樣：[PR #126](https://github.com/kepano/obsidian-skills/pull/126)，更新 2026-09-26T03:06:02Z；標題：docs(obsidian-cli): add sandbox/IPC troubleshooting。

**Adam／metabiz 關聯：** 適合 Adam 的個人知識管理教學；可作 know metabiz wiki 的 Markdown、連結與資料結構操作候選技能。

**風險與證據限制：** 技能相容不等於每個 agent 的行為相同；批次改寫可能造成連結錯誤，須以可回復的測試 vault 驗證。 GitHub API 授權標示：MIT；實際採用仍須核對所用元件授權。

**下一步：** 用十篇公開筆記檢查連結、屬性與格式往返，再整理成本地技能候選。

### 8. ishicm/llm-wiki-skills — Skill candidate

**用途：** 以 AI 原生知識庫工作法整理、匹配與維護 wiki 內容。

**動能與維護：** 快照基準 2026-09-25 → 2026-09-26，Δ +0、相對成長 +0.00%；最新 push 2026-04-13T14:32:12Z。最新 release：未取得最新 release。目前 open issues／PR 共 1。最近抽樣：[Issue #1](https://github.com/ishicm/llm-wiki-skills/issues/1)，更新 2026-04-15T06:46:21Z；標題："健康检查，持续维护"，有点标题党。

**Adam／metabiz 關聯：** 與 know metabiz wiki 方向直接相關；可作 Adam 的『資料收集到可追溯知識』示範。

**風險與證據限制：** README 摘要較短且含大量徽章，不能據此判定完整品質；自動整理需檢查出處、重複頁與推論是否被誤當成事實。 GitHub API 授權標示：MIT；實際採用仍須核對所用元件授權。

**下一步：** 把相同十份公開來源交給它與既有整理流程比較，檢查引用和更新差異。

### 9. zhaoxuya520/reverse-skill — Watch

**用途：** 以技能路由方式組織逆向工程與授權安全研究工具。

**動能與維護：** 快照基準 2026-09-25 → 2026-09-26，Δ +358、相對成長 +0.95%；最新 push 2026-09-22T06:43:21Z。最新 release：v1.0.1（2026-08-08T10:16:19Z）。目前 open issues／PR 共 22。最近抽樣：[Issue #138](https://github.com/zhaoxuya520/reverse-skill/issues/138)，更新 2026-09-26T13:44:42Z；標題：-。

**Adam／metabiz 關聯：** Adam 可研究按需載入工具與技能路由的設計；對辦公自動化與 know metabiz wiki 的直接優先度較低。

**風險與證據限制：** 安全研究工具鏈的執行權限與依賴範圍較大；熱度不能代替程式碼審查，候選價值主要是路由架構。 GitHub API 授權標示：MIT；實際採用仍須核對所用元件授權。

**下一步：** 只研究技能分流與知識累積設計，觀察下一次成長是否延續。

## 明日觀察清單

- Paperclip、Hindsight：比較下一次 stars today 與快照成長是否延續，追蹤 MCP／Hermes 整合問題。
- Univer：追蹤繁中 IME 與啟動問題的合併／修復狀態，確認 PDF 功能是否仍在預告階段。
- Mobile MCP、Claude Code Action：觀察裝置相容性與背景 agent 完成狀態相關修正是否進入 release。
- Obsidian Skills、LLM Wiki Skills：以知識來源正確率、連結完整度與可回復性驗證價值，低熱度不直接淘汰。
- AI Engineering 教材：追蹤失效 dataset 範例是否修正；reverse-skill 先觀察熱度與路由設計，不因榜單名次擴大導入。

## 可重現性與限制

原始即時榜單保存在 trending-daily.html；API metadata、README 摘要、release 存於 repos.json 與 snapshots/；issue／PR 抽樣存於 issue-activity.json；查詢、嘗試次數、範圍排除與舊資料沿用清單存於 collection-status.json。

本次排除 15 筆與範圍缺乏直接關聯的歷史追蹤資料，合併 3 筆重新命名造成的 canonical repo 重複；不修改舊日期檔案。

沿用舊 metadata 的專案：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent。不以這些數字評估本次動能。

搜尋 API 以總星數取每組前 N 筆，仍存在大型專案偏差；補入 Trending 與 wiki 技能人工精選可改善但不能消除。本文建議屬依公開資料的編輯判斷，不代表已實測產品。
