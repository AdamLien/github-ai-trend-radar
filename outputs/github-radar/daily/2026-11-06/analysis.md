# GitHub AI 趨勢雷達 — 2026-11-06

本報告於 2026-11-07（Asia/Taipei）補跑，目標日期為前一個台北日曆日。GitHub Trending 與 API 是執行時即時觀察，不是 11 月 6 日封存資料；stars today 是 GitHub 頁面的滾動訊號，不代表台北日曆日新增星數。星數差值依前次快照計算，不能直接視為完整 24 小時增量。

選題優先考慮當日動能、相對成長、程式碼推送、README 是否清楚、release 與近期 issue／PR，再判斷對 Adam 課程、內容、AI 辦公自動化及 know metabiz wiki 的適用性。下列應用均為編輯建議，尚未完成實際部署驗證。

## 本輪判讀與資料品質

Collector 使用全部 10 組指定查詢、`--limit 10`、daily Trending 與 README，最終保留 392 個不重複專案（含歷史追蹤）。沒有觀察到 API rate-limit；未觸發 `--limit 5` 重跑。排除清單、去重與資料回退見 [run-status.json](run-status.json)。

本輪為既有資料回退的專案：BarberNumber/Midjourney-Software、BrickOrioleLoad/aion-2-trainer-tool、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget。這些資料不可作為新鮮的成長證據。搜尋按總星數取得候選會偏向大型專案，因此精選另納入相對成長及與課程／wiki 的實際關聯。

相對成長＝快照增量 ÷（目前總星數－增量）；本輪精選的對照快照皆為 2026-11-05。`—` 代表沒有本次 Trending 訊號，並非零成長。Issue 活動只抽樣最近更新五筆，可能混含 PR；open_issues 欄位也混含 PR，不能當成缺陷數。API 無 latest release 可能是未發布或端點不可用。

## 精選專案（研究與應用優先順序，非總星數排行）

| 專案 | 分類 | 總星數 | Trending today | 快照 Δ | 相對成長 |
| --- | --- | ---: | ---: | ---: | ---: |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | Deep research | 8,580 | 2005 | +1,842 | 27.34% |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Skill candidate | 63,228 | 2524 | +2,502 | 4.12% |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 316,328 | 2058 | +1,720 | 0.55% |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Demo content | 17,881 | — | +1,472 | 8.97% |
| [google/skills](https://github.com/google/skills) | Watch | 22,704 | 532 | +504 | 2.27% |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Demo content | 98,692 | — | +1,089 | 1.12% |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Watch | 140,345 | — | +594 | 0.43% |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Deep research | 48,216 | — | +54 | 0.11% |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Watch | 21,427 | — | +26 | 0.12% |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | Skill candidate | 3,679 | — | +2 | 0.05% |

### 1. NVIDIA/auto-ontology — Deep research

用途：將企業 metadata、語義定義與資料來源建立為 ontology／圖譜脈絡，透過 MCP、CLI、API 供 agent 使用。

動能與證據：README 直接指出資料定義、來源與可用性的問題，適合用來研究單純文件 RAG 不易解決的語義一致性。 最近推送 `2026-11-06T15:49:14Z`；release：未取得（無日期）；最近 issue／PR 樣本更新 `2026-11-06T13:11:56Z`。

應用關聯：know metabiz wiki：建議用去識別化的產品、流程與名詞資料做小型概念驗證；課程可比較文件檢索與語義層查詢。

風險：尚無可取得的 latest release；近期 PR 涉及依賴安全更新，應驗證實際合併狀態。高相對成長不等於查詢正確率。

來源：[專案與 README](https://github.com/NVIDIA/auto-ontology)、[issue／PR 活動](https://github.com/NVIDIA/auto-ontology/issues)、[releases](https://github.com/NVIDIA/auto-ontology/releases)。

### 2. cloudflare/security-audit-skill — Skill candidate

用途：用多階段 agent 流程進行偵察、漏洞搜尋、候選驗證與獨立紀錄核驗，產出結構化稽核結果。

動能與證據：當日星數與快照增量都高，但 pushed_at 仍停在 9 月，須區分關注熱度與程式碼維護。 最近推送 `2026-09-14T19:29:02Z`；release：未取得（無日期）；最近 issue／PR 樣本更新 `2026-11-06T04:44:48Z`。

應用關聯：Adam 課程：可拆成「AI 稽核結果如何覆核」單元；內容示範用小型公開測試專案，研究可重用的覆蓋與驗證流程。

風險：近期有 coverage ledger／CLI 測試失敗的開啟 issue；README 的獨立驗證設計不代表結果已可靠。未完成驗證前不宜直接移植整套流程。

來源：[專案與 README](https://github.com/cloudflare/security-audit-skill)、[issue／PR 活動](https://github.com/cloudflare/security-audit-skill/issues)、[releases](https://github.com/cloudflare/security-audit-skill/releases)。

### 3. mattpocock/skills — Skill candidate

用途：將日常工程方法整理為 coding agent 可重用的 skills。

動能與證據：README 定位明確，增量高且有近期版本；相對成長仍低於新興小型專案，不以總星數取得最高研究順位。 最近推送 `2026-11-05T10:40:01Z`；release：v1.3.2（2026-10-29T10:27:41Z）；最近 issue／PR 樣本更新 `2026-11-06T14:51:35Z`。

應用關聯：Adam 課程與內容：選一個教學／開發 skill，比較加入前後的輸出品質與人工修正量；適合規劃可驗證的技能設計教材。

風險：近期 teach skill 有測驗選項與回饋品質的 issue；需逐項審閱依賴與流程，避免一次載入大量技能造成上下文成本。

來源：[專案與 README](https://github.com/mattpocock/skills)、[issue／PR 活動](https://github.com/mattpocock/skills/issues)、[releases](https://github.com/mattpocock/skills/releases)。

### 4. vercel-labs/agent-desktop — Demo content

用途：讓 AI agent 經由作業系統 accessibility tree 檢視並操作桌面應用。

動能與證據：README 說明跨平台桌面操作，近期 release 與 PR 都活躍；相對成長高，適合快速驗證。 最近推送 `2026-11-06T08:13:25Z`；release：v1.2.0（2026-11-05T02:43:54Z）；最近 issue／PR 樣本更新 `2026-11-06T15:53:28Z`。

應用關聯：AI 辦公自動化：規劃桌面表單與資料轉錄的去識別化示範，記錄操作成功率、失敗回復與人工介入點。

風險：近期 PR 持續修補 macOS 選單操作，不能把單一平台示範視為跨平台成熟度；桌面操作也可能受權限與 UI 狀態影響。

來源：[專案與 README](https://github.com/vercel-labs/agent-desktop)、[issue／PR 活動](https://github.com/vercel-labs/agent-desktop/issues)、[releases](https://github.com/vercel-labs/agent-desktop/releases)。

### 5. google/skills — Watch

用途：Google 產品與技術的 agent skills 集合，README 說明安裝及更新方式。

動能與證據：同時有 Trending 當日動能、正向快照增量與近期推送，適合追蹤產品技能如何打包與維護。 最近推送 `2026-11-05T22:00:15Z`；release：未取得（無日期）；最近 issue／PR 樣本更新 `2026-11-05T19:39:02Z`。

應用關聯：Adam 課程／AI 辦公自動化：可挑與現有 Google 技術情境相符的單一技能做示範；不預設包含 Gmail 或 Workspace 的完整辦公功能。

風險：近期 issue 指出 Genkit skills 執行未驗證遠端安裝器；這是待核實的回報，選用前需讀取實際安裝流程。未取得 latest release。

來源：[專案與 README](https://github.com/google/skills)、[issue／PR 活動](https://github.com/google/skills/issues)、[releases](https://github.com/google/skills/releases)。

### 6. D4Vinci/Scrapling — Demo content

用途：支援單次擷取到完整爬取流程的網頁資料收集框架，README metadata 標示 MCP 整合。

動能與證據：快照增量明顯，11 月 4 日有 v0.5.1；雖本輪沒有 Trending 訊號，仍適合以可用性測試決定內容價值。 最近推送 `2026-11-05T18:01:47Z`；release：v0.5.1（2026-11-04T20:29:16Z）；最近 issue／PR 樣本更新 `2026-11-06T10:43:49Z`。

應用關聯：AI 辦公與內容：用公開資料建立「擷取→整理→引用」示範；know metabiz wiki 可評估來源匯入與去重流程。

風險：近期抽樣五筆皆為 PR，不能推論沒有問題；網頁改版、動態內容及來源引用完整性都需測試。

來源：[專案與 README](https://github.com/D4Vinci/Scrapling)、[issue／PR 活動](https://github.com/D4Vinci/Scrapling/issues)、[releases](https://github.com/D4Vinci/Scrapling/releases)。

### 7. garrytan/gstack — Watch

用途：用 Markdown 與斜線指令把 coding agent 組合為產品、設計、審查、QA 與發版等角色流程。

動能與證據：README 的角色分工可用於課程設計；有近期 release 和推送，動能為正但相對增長不高。 最近推送 `2026-11-06T16:16:27Z`；release：v1.96.0.0（2026-11-05T14:05:48Z）；最近 issue／PR 樣本更新 `2026-11-06T16:11:18Z`。

應用關聯：Adam 課程：比較單 agent 與角色流程在同一任務的成本、品質與人類決策點；公司辦公可借鑑審閱交接機制。

風險：角色數量與宣稱的生產力不是成效證據；近期 PR 包含 ship-policy 與 CI health 調整，應檢查流程是否符合現有專案。

來源：[專案與 README](https://github.com/garrytan/gstack)、[issue／PR 活動](https://github.com/garrytan/gstack/issues)、[releases](https://github.com/garrytan/gstack/releases)。

### 8. DeusData/codebase-memory-mcp — Deep research

用途：把程式碼、文件與基礎設施放入持久圖譜，透過 MCP 提供結構查詢與變更感知能力。

動能與證據：星數增幅較小，但 README 與 MCP 能力直接對應 coding agent 理解大型專案的需求，因此保留深研順位。 最近推送 `2026-11-04T23:21:44Z`；release：v0.12.1（2026-10-16T23:35:48Z）；最近 issue／PR 樣本更新 `2026-11-06T15:40:50Z`。

應用關聯：Adam 課程：設計「圖譜查詢＋原始碼覆核」實驗；know metabiz wiki 可研究程式與文件間的引用關係，避免把知識圖譜當完整事實。

風險：近期 issue 回報 Linux Landlock 造成 MCP 初始化前退出；另有儲存資源限制 PR。應驗證索引覆蓋率、過期資料與環境相容性。

來源：[專案與 README](https://github.com/DeusData/codebase-memory-mcp)、[issue／PR 活動](https://github.com/DeusData/codebase-memory-mcp/issues)、[releases](https://github.com/DeusData/codebase-memory-mcp/releases)。

### 9. nashsu/llm_wiki — Watch

用途：跨平台桌面知識庫，讓 LLM 將文件逐步整理為互連、可持續維護的 wiki。

動能與證據：README 清楚說明 persistent wiki 路線；增量與相對成長有限，近期 issue 比星數更有判讀價值。 最近推送 `2026-10-21T11:17:29Z`；release：v0.6.13（2026-10-22T01:21:07Z）；最近 issue／PR 樣本更新 `2026-11-05T05:45:43Z`。

應用關聯：know metabiz wiki：可研究增量寫入、來源追溯與衝突處理；Adam 內容可比較傳統 RAG 查詢與預先編纂 wiki。

風險：API 授權欄位為 NOASSERTION，不能視為已確認授權；Linux 啟動缺依賴問題仍在回報。最近推送較舊，不應因桌面包裝就直接導入。

來源：[專案與 README](https://github.com/nashsu/llm_wiki)、[issue／PR 活動](https://github.com/nashsu/llm_wiki/issues)、[releases](https://github.com/nashsu/llm_wiki/releases)。

### 10. SamurAIGPT/llm-wiki-agent — Skill candidate

用途：以 coding agent skill 讀取 raw 來源，抽取知識並維護持久互連的 Markdown wiki。

動能與證據：README 直接展示 raw→wiki 的資料流；星數增量很小，保留它是因與 wiki 工作流程高度相關。 最近推送 `2026-11-02T11:11:47Z`；release：未取得（無日期）；最近 issue／PR 樣本更新 `2026-10-20T12:40:51Z`。

應用關聯：know metabiz wiki：研究來源匯入、索引、變更紀錄與矛盾標記的最小 skill；可與桌面型 llm_wiki 做課程對照。

風險：未取得 latest release，issue／PR 更新較慢；來源內容可能不可信，匯入時應維持資料／指令邊界，並以人工覆核防止錯誤累積。

來源：[專案與 README](https://github.com/SamurAIGPT/llm-wiki-agent)、[issue／PR 活動](https://github.com/SamurAIGPT/llm-wiki-agent/issues)、[releases](https://github.com/SamurAIGPT/llm-wiki-agent/releases)。

## 明日觀察清單（下一輪收集）

- **NVIDIA/auto-ontology**：觀察高相對成長是否延續，核對資料定義、來源追溯與查詢正確性的小型測試能否跑通。
- **cloudflare/security-audit-skill**：追蹤 coverage ledger／CLI 測試回報與久未推送的落差，確認修正是否合併；先評估再移植。
- **google/skills**：追蹤遠端安裝器驗證的 issue 回覆及相關修正，再選擇適合課程的單一技能。
- **vercel-labs/agent-desktop**：追蹤選單操作修正與下一版，評估跨平台桌面表單實測成功率。
- **DeusData/codebase-memory-mcp**：追蹤 Linux 初始化與索引資源限制問題，記錄環境要求及圖譜覆蓋缺口。
- **nashsu/llm_wiki／SamurAIGPT/llm-wiki-agent**：比較來源連結、衝突標記、人工覆核與回復能力；授權未確認的項目先釐清。
- **新增候選**：檢視下一輪 Trending 新進項目與搜尋未覆蓋的小型專案，不以熱門榜重複名單作為唯一來源。

本輪沒有安裝或執行外部專案。README 與 issue 僅作證據，未當作操作指令。快照見 [repos.json](repos.json)，補充 issue／release 證據見 [editorial-evidence.json](editorial-evidence.json)，Trending 來源為 [GitHub Trending daily](https://github.com/trending?since=daily)，實際擷取紀錄見 [trending-daily-source.json](trending-daily-source.json)。
