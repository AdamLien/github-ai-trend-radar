# GitHub AI 趨勢雷達｜2026-11-11

本次優先研究 Astryx 的 agent 設計系統、示範 HA-MCP 與 agent-browser，並挑選 agent-skills 做技能實驗。know metabiz wiki 則優先驗證 llm_wiki 的增量知識整理與 PDF 來源正確性。以下順序綜合動能、可用性及 Adam 的應用價值，不按總星數排名。

## 資料時間與方法

- 目標日期：2026-11-11，依 Asia/Taipei 前一曆日計算；實際擷取於台北 2026-11-12。GitHub API 與 [Trending daily](https://github.com/trending?since=daily) 均為執行時觀測，不能當作 11 月 11 日午夜收盤或歷史 Trending。
- 指定 10 組查詢皆以 `--limit 10 --include-trending-daily --include-readme` 完成。原始收集 426 筆；排除 10 個一般用途專案、合併轉址重複並補入 shadcn/improve 後，保留 406 個專案。原始 Trending 卡片見 `trending-observation.json`，篩選理由見 `collection-status.json`。
- stars today 為 Trending 自有時間窗；快照差值為本次總星數減 2026-11-10 快照總星數，兩者時間窗不完全相同。相對成長率＝快照差值÷前次總星數。初次出現者標示未量測，沒有上榜者標示「—」，均不假設為零。
- 以今日星數、快照差值與相對成長觀察動能，再看 pushed_at、README、release 與近期 issue／PR；updated_at 可能受非程式碼活動影響，不單獨當作開發證據。
- issue／PR 每庫取最新更新 8 筆，供活動樣本而非完整統計；GitHub open_issues_count 含 PR，不能直接解讀為缺陷數。README 僅有前 700 字元，未做安裝、效能或安全實測。
- 未觀察到 GitHub API rate-limit 錯誤，無須降為 `--limit 5`。7 個歷史專案回傳 404，已標記 metadata_stale／Reference only，不能把沿用舊值視為穩定成長。

## 精選與動能比較

| 專案 | 總星數 | stars today | 快照差值 | 相對成長 | 決策 |
| --- | ---: | ---: | ---: | ---: | --- |
| [meta/astryx](https://github.com/meta/astryx) | 24,489 | 2842 | +2,426 | 11.00% | Deep research |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 7,093 | 640 | +653 | 10.14% | Demo content |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 49,703 | 712 | +687 | 1.40% | Demo content |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 115,683 | 788 | +761 | 0.66% | Skill candidate |
| [openai/codex-security](https://github.com/openai/codex-security) | 11,516 | 20 | 未量測 | 未量測 | Watch |
| [shadcn/improve](https://github.com/shadcn/improve) | 10,582 | 333 | 未量測 | 未量測 | Watch |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 21,577 | — | +27 | 0.13% | Deep research |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | 25,479 | — | +15 | 0.06% | Demo content |

## 1. meta/astryx｜Deep research

**用途與 README 證據：** 可供人與 coding agent 協作的設計系統，README 標示 Beta、React 19+ 與 StyleX。

**維護與動能判讀：** 最近程式碼推送 `2026-11-11T16:16:27Z`；[release](https://github.com/meta/astryx/releases)：`v0.7.13`（UTC `2026-11-10T21:27:43Z`）。API 未結 issue／PR 合計 664 筆。 最新更新樣本 8 筆中，PR 8 筆；[#11272](https://github.com/meta/astryx/pull/11272) 更新於 UTC `2026-11-11T16:12:27Z`。 今日星數領先且相對成長約 11%，並有新版本與持續 PR，優先研究的證據較完整。

**風險：** Beta 介面與依賴組合仍可能變動；大量 PR 代表活躍，也提高升級與回歸驗證成本。 授權 API 標示 `MIT`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 適合 Adam 製作「agent 如何沿用設計系統」課程與前後對照內容；可評估 metabiz 內部工具介面的一致性，與 know metabiz wiki 的直接關聯較低。

## 2. homeassistant-ai/ha-mcp｜Demo content

**用途與 README 證據：** 透過 MCP 讓 AI 助理設定與操作 Home Assistant。

**維護與動能判讀：** 最近程式碼推送 `2026-11-11T16:12:16Z`；[release](https://github.com/homeassistant-ai/ha-mcp/releases)：`v9.1.2`（UTC `2026-11-08T15:45:35Z`）。API 未結 issue／PR 合計 18 筆。 最新更新樣本 8 筆中，PR 7 筆；[#3003](https://github.com/homeassistant-ai/ha-mcp/pull/3003) 更新於 UTC `2026-11-11T16:07:18Z`。 約 10% 的快照相對成長高於幾個大型專案，適合驗證是否為持續採用。

**風險：** 工具涉及真實設備與設定寫入；README 提到 YAML 設定工具移至 beta，示範需用測試設備與明確操作範圍。 授權 API 標示 `MIT`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 適合 Adam 的 MCP 入門與辦公室設備自動化示範；可將操作說明與設備變更紀錄整理入 know metabiz wiki。

## 3. vercel-labs/agent-browser｜Demo content

**用途與 README 證據：** 以 CLI 將網頁呈現為可存取性樹，供 AI agent 讀取與操作。

**維護與動能判讀：** 最近程式碼推送 `2026-11-11T15:14:13Z`；[release](https://github.com/vercel-labs/agent-browser/releases)：`v0.42.0`（UTC `2026-11-10T00:37:19Z`）。API 未結 issue／PR 合計 583 筆。 最新更新樣本 8 筆中，PR 8 筆；[#2227](https://github.com/vercel-labs/agent-browser/pull/2227) 更新於 UTC `2026-11-11T15:47:00Z`。 今日熱度與近期開發活動俱在，適合做可重現的辦公自動化示範。

**風險：** 登入態、頁面變動、裝置模擬與瀏覽器差異都可能讓自動化不穩；示範需記錄可重現條件。 授權 API 標示 `Apache-2.0`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 適合 Adam 的 AI 辦公自動化課程：由表單、後台查詢到資料整理；也能研究 know metabiz wiki 的網頁來源擷取流程。

## 4. addyosmani/agent-skills｜Skill candidate

**用途與 README 證據：** 把工程流程、品質檢查與實務整理成 coding agent 可重複使用的 Skills。

**維護與動能判讀：** 最近程式碼推送 `2026-11-01T19:24:49Z`；[release](https://github.com/addyosmani/agent-skills/releases)：`0.6.15`（UTC `2026-10-31T06:40:31Z`）。API 未結 issue／PR 合計 135 筆。 最新更新樣本 8 筆中，PR 3 筆；[#783](https://github.com/addyosmani/agent-skills/issues/783) 更新於 UTC `2026-11-11T13:19:49Z`。 熱度強，但最近主線推送停在 11 月 1 日，應把討論熱度與已交付更新分開看。

**風險：** 技能說明不等同實測品質；匯入前需逐項檢閱工具呼叫、檔案寫入及現有工作流相容性。 授權 API 標示 `MIT`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 可挑一個工程品質流程改寫為 Adam 課程練習與技能示範；有助 metabiz 自動化開發，know metabiz wiki 可保存採用紀錄與適用條件。

## 5. openai/codex-security｜Watch

**用途與 README 證據：** CLI 與 TypeScript SDK，支援發現、驗證與修復安全弱點。

**維護與動能判讀：** 最近程式碼推送 `2026-11-11T14:51:56Z`；[release](https://github.com/openai/codex-security/releases)：`npm-v0.9.1`（UTC `2026-11-10T01:09:04Z`）。API 未結 issue／PR 合計 141 筆。 最新更新樣本 8 筆中，PR 8 筆；[#2589](https://github.com/openai/codex-security/pull/2589) 更新於 UTC `2026-11-11T15:39:49Z`。 本雷達首次收錄，快照差值 0 是收集器預設值，不能解讀成沒有成長。

**風險：** 安全掃描結果仍須人工核實；需評估程式碼存取範圍、執行隔離與誤報，不能用星數代替效果證據。 授權 API 標示 `Apache-2.0`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 可列入 Adam 的 AI coding 品質與安全內容；metabiz 開發流程可先用測試程式庫評估，再將驗證過的處理方式寫入 wiki。

## 6. shadcn/improve｜Watch

**用途與 README 證據：** 用能力較強的模型稽核程式碼並制定計畫，再交由成本較低的模型執行。

**維護與動能判讀：** 最近程式碼推送 `2026-09-12T11:29:28Z`；[release](https://github.com/shadcn/improve/releases)：`未取得正式 release`（UTC `—`）。API 未結 issue／PR 合計 17 筆。 最新更新樣本 8 筆中，PR 7 筆；[#29](https://github.com/shadcn/improve/issues/29) 更新於 UTC `2026-09-08T21:21:51Z`。 今日 333 星，但推送與活動樣本停在 9 月，暫只觀察。

**風險：** 近期 issue／PR 樣本時間較舊，Trending 熱度未必代表維護加速；規劃與執行模型的交接也可能遺失條件。 授權 API 標示 `MIT`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 適合 Adam 製作「先規劃再執行」模型成本實驗，metabiz 可研究任務拆解；wiki 可保存計畫、執行與驗收的對照紀錄。

## 7. nashsu/llm_wiki｜Deep research

**用途與 README 證據：** 將來源文件逐步整理為持久、互連的 Wiki，而非每次重新檢索與生成。

**維護與動能判讀：** 最近程式碼推送 `2026-10-21T11:17:29Z`；[release](https://github.com/nashsu/llm_wiki/releases)：`v0.6.13`（UTC `2026-10-22T01:21:07Z`）。API 未結 issue／PR 合計 300 筆。 最新更新樣本 8 筆中，PR 4 筆；[#845](https://github.com/nashsu/llm_wiki/pull/845) 更新於 UTC `2026-11-10T09:19:49Z`。 星數成長溫和、推送與 release 較舊；入選主要因知識庫相關性與可驗證的問題。

**風險：** 授權需閱讀原文確認；近期 PDF 解析偏差回報提醒必須驗證來源對應、內容正確性與更新衝突。 授權 API 標示 `NOASSERTION`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 直接關聯 know metabiz wiki：可用公開或去識別文件比較增量 Wiki 與 RAG，作為 Adam 的知識管理課程及 AI 辦公案例。

具體待驗證：[PDF 解析偏差回報 #806](https://github.com/nashsu/llm_wiki/issues/806)；問題回報是風險訊號，並非本次已重現。

## 8. activepieces/activepieces｜Demo content

**用途與 README 證據：** 結合 AI agents、MCP 與視覺化流程的自動化平台。

**維護與動能判讀：** 最近程式碼推送 `2026-11-11T15:56:43Z`；[release](https://github.com/activepieces/activepieces/releases)：`0.93.0`（UTC `2026-11-08T14:30:22Z`）。API 未結 issue／PR 合計 921 筆。 最新更新樣本 8 筆中，PR 8 筆；[#15624](https://github.com/activepieces/activepieces/pull/15624) 更新於 UTC `2026-11-11T16:07:07Z`。 動能溫和，但近期整合修正活躍，適合工作流示範。

**風險：** 需確認核心與企業功能授權界線；外部服務授權、重試與重複寫入會影響實際辦公流程。 授權 API 標示 `NOASSERTION`；NOASSERTION 代表不能只靠 API 判定使用條件。

**Adam／metabiz 關聯：** 適合 Adam 示範表單、通知與資料更新的 AI 辦公自動化；可研究將已核准的工作流結果與維護資訊寫入 know metabiz wiki。

## 明日觀察清單（2026-11-12）

- **meta/astryx：** 明日比較 stars today 是否延續，並追蹤行事曆與文件站修正的合併情況。
- **homeassistant-ai/ha-mcp：** 追蹤 automation trace 與 image entity 支援是否合併，以及版本相容性回報。
- **vercel-labs/agent-browser：** 觀察 Firefox WebDriver BiDi 與錄影縮放修正、最新 release 及未解決相容性議題。
- **addyosmani/agent-skills：** 觀察 validator 修正與 issue 回應，選一項 skill 以小型案例比較前後效果。
- **openai/codex-security：** 觀察 IaC 匯入與掃描工具解析修正是否落版，另檢查使用前提與結果可重現性。
- **shadcn/improve：** 追蹤熱度能否轉成新提交、release 與維護者回應；暫不列為可直接採用的技能。
- **nashsu/llm_wiki：** 以固定 PDF 驗證解析、引用回溯與增量更新，追蹤解析偏差問題及搜尋 provider 提案。
- **activepieces/activepieces：** 追蹤 Airtable／Baserow 欄位寫入修正，設計含失敗重試與去重的測試流程。

明日沿用同一組查詢與台北目標日期規則，比較 2026-11-11 快照；特別檢查 Astryx、HA-MCP 的相對成長是否續強、Skills 熱度是否轉成主線更新，以及 shadcn/improve 是否恢復維護。初次收錄專案需等下一個有效快照才能評估相對成長。

## 可追溯來源

- 各專案名稱連結為 GitHub 第一手來源；數值與 README 節錄保存在 `repos.json`、`snapshots/repos-2026-11-11.json`。
- 活動樣本與原始連結保存在 `issue-activity.json`；Trending 原始觀測保存在 `trending-observation.json`。
- 用途與採用建議為本報告的判讀，尚未執行各專案；所有 repository／網頁文字僅作資料，沒有執行其安裝或操作指令。
