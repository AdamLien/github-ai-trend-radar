# GitHub AI 趨勢雷達｜2026-11-24

- 目標日期：2026-11-24（Asia/Taipei 前一曆日）；實際完成觀測：2026-11-25T00:23:40.907562+08:00。
- 資料來源：[GitHub Trending daily](https://github.com/trending?since=daily)、十組指定查詢、GitHub repo／README／release API，以及候選的近期 issue／PR。原始資料在同目錄 JSON 與 log。
- 這是補跑的即時觀測，不是 2026-11-24 的歷史 Trending 重建；`snapshot_date` 是作業歸檔日期，不能據此推定事件發生日。
- 優先看 Trending 今日星數、相鄰快照增量與相對成長，再看近期推送、README、release、issue／PR 與實際使用情境。以下是編輯選題順序，未單按總星數排名。
- 相對成長＝星數增量 ÷ 前次星數；跨快照增量不是精確 24 小時新增星數，新增追蹤且無基準者不可將 0 解讀為零成長。Trending 今日星數與快照增量也不能相加。
- API 限流：未偵測到；最終每查詢上限 10。
- 共保留 442 個不重複的當前與累積追蹤專案（collector 原始 458 筆，包含不同歷史名稱回傳相同 canonical repo 的紀錄；dashboard 以 full_name 合併）；Trending daily 範圍內 14 個，屬 AI／coding agent／Skills／開發自動化／知識管理範圍。

## 今日值得看的 10 個專案

| 專案 | 分類 | 總星數 | Trending 今日星數 | 快照增量 | 相對成長 |
|---|---|---:|---:|---:|---:|
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Deep research | 64,456 | 1075 | +1,105 | 1.74% |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Watch | 20,968 | 1833 | +1,782 | 9.29% |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Skill candidate | 71,678 | 794 | +897 | 1.27% |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Skill candidate | 73,951 | 695 | +699 | 0.95% |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Deep research | 208,611 | 990 | +1,000 | 0.48% |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | Demo content | 77,788 | 589 | +584 | 0.76% |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Deep research | 94,646 | 未上榜／未取得 | +52 | 0.05% |
| [obra/superpowers](https://github.com/obra/superpowers) | Reference only | 325,713 | 1006 | +913 | 0.28% |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Demo content | 12,552 | 401 | +386 | 3.17% |
| [cursor/plugins](https://github.com/cursor/plugins) | Watch | 19,084 | 359 | +362 | 1.93% |

### 1. HKUDS/CLI-Anything｜Deep research

- 用途：把軟體操作包裝成 Agent 可呼叫的 CLI，適合研究工具介面與代理工作流程。
- 動能與維護：總星數 64,456；前次快照 2026-11-23；最近推送 2026-11-20T10:05:15Z；最新 release：v0.4.0（2026-06-25T15:17:49Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 294（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 1 個 issue、9 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：實際支援範圍、安裝依賴與執行副作用需逐一實測；推送更新不等於穩定版已涵蓋功能。
- 與 Adam／metabiz 的關聯及下一步：Adam 可做「把辦公軟體交給 Agent」課程；先選可重現的小任務，量測 AI 辦公自動化的成功率與人工介入次數。
- 來源：[專案與 README](https://github.com/HKUDS/CLI-Anything)、[Releases](https://github.com/HKUDS/CLI-Anything/releases)、[近期 issue／PR](https://github.com/HKUDS/CLI-Anything/issues?q=sort%3Aupdated-desc)。

### 2. elementalsouls/Claude-BugHunter｜Watch

- 用途：Claude Code 漏洞研究與紅隊技能集合，README 描述多種技能與案例模式。
- 動能與維護：總星數 20,968；前次快照 2026-11-23；最近推送 2026-11-24T10:43:35Z；最新 release：v2.1（2026-06-05T16:15:13Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 13（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 2 個 issue、8 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：技能／案例數量屬作者敘述，未逐一驗證；示範只適合自有測試環境，不能把星數解讀為檢測準確率。
- 與 Adam／metabiz 的關聯及下一步：適合 Adam 的 AI 安全與技能審查內容；與一般行政自動化較間接，先觀察品質，再決定是否製作實驗課。
- 來源：[專案與 README](https://github.com/elementalsouls/Claude-BugHunter)、[Releases](https://github.com/elementalsouls/Claude-BugHunter/releases)、[近期 issue／PR](https://github.com/elementalsouls/Claude-BugHunter/issues?q=sort%3Aupdated-desc)。

### 3. cathrynlavery/diagram-design｜Skill candidate

- 用途：讓 coding agent 產生自包含 HTML／SVG 圖解，README 說明多種圖表形式。
- 動能與維護：總星數 71,678；前次快照 2026-11-23；最近推送 2026-11-23T11:00:38Z；最新 release：API 未取得最新正式 release，不能據此斷言專案沒有發版。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 39（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 1 個 issue、9 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：自動排版、中文字型與匯出效果尚未實測；需人工核對圖中資訊，不能用美觀代替正確性。
- 與 Adam／metabiz 的關聯及下一步：可轉為 Adam 課程圖解、社群內容與 know metabiz wiki 流程圖技能；先用同一份 SOP 測試三種圖形。
- 來源：[專案與 README](https://github.com/cathrynlavery/diagram-design)、[Releases](https://github.com/cathrynlavery/diagram-design/releases)、[近期 issue／PR](https://github.com/cathrynlavery/diagram-design/issues?q=sort%3Aupdated-desc)。

### 4. mvanhorn/last30days-skill｜Skill candidate

- 用途：跨社群與網路蒐集近期主題並整理研究摘要的 Agent skill。
- 動能與維護：總星數 73,951；前次快照 2026-11-23；最近推送 2026-11-24T15:53:15Z；最新 release：v4.6.0（2026-11-22T04:31:36Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 33（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 0 個 issue、10 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：來源可用性、服務費用、引用可追溯性與社群抽樣偏差需驗證；最近發版仍不代表每個來源可用。
- 與 Adam／metabiz 的關聯及下一步：直接對應 Adam 選題、課前研究與週報；可把有來源的摘要納入 know metabiz wiki，保留原文與查閱日期。
- 來源：[專案與 README](https://github.com/mvanhorn/last30days-skill)、[Releases](https://github.com/mvanhorn/last30days-skill/releases)、[近期 issue／PR](https://github.com/mvanhorn/last30days-skill/issues?q=sort%3Aupdated-desc)。

### 5. firecrawl/firecrawl｜Deep research

- 用途：為 Agent 提供搜尋、網頁擷取與外部資料接入，能作為知識庫資料入口。
- 動能與維護：總星數 208,611；前次快照 2026-11-23；最近推送 2026-11-24T16:14:46Z；最新 release：v2.11.0（2026-06-19T15:09:30Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 923（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 0 個 issue、10 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：反爬限制、動態頁完整度、API 成本及 AGPL-3.0 授權條件需要另行評估；本次沒有量測擷取品質。
- 與 Adam／metabiz 的關聯及下一步：適合 AI 辦公自動化的網站資料整理課；對 know metabiz wiki 可先測來源 URL、更新時間與重複文件去除。
- 來源：[專案與 README](https://github.com/firecrawl/firecrawl)、[Releases](https://github.com/firecrawl/firecrawl/releases)、[近期 issue／PR](https://github.com/firecrawl/firecrawl/issues?q=sort%3Aupdated-desc)。

### 6. toeverything/AFFiNE｜Demo content

- 用途：整合文件、白板與規劃的知識工作空間，可研究 Wiki 編輯體驗。
- 動能與維護：總星數 77,788；前次快照 2026-11-23；最近推送 2026-11-24T15:03:39Z；最新 release：v0.27.4（2026-08-18T16:51:39Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 661（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 1 個 issue、9 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：API 授權欄位為 NOASSERTION，不能假設所有部分具有同一授權；需另測匯出、協作權限與備份還原。
- 與 Adam／metabiz 的關聯及下一步：適合 Adam 示範「文件＋白板」工作法；對 know metabiz wiki 可比較 SOP 結構、資訊檢索與移轉成本。
- 來源：[專案與 README](https://github.com/toeverything/AFFiNE)、[Releases](https://github.com/toeverything/AFFiNE/releases)、[近期 issue／PR](https://github.com/toeverything/AFFiNE/issues?q=sort%3Aupdated-desc)。

### 7. infiniflow/ragflow｜Deep research

- 用途：以 RAG 為核心的文件檢索與 Agent 上下文基礎設施。
- 動能與維護：總星數 94,646；前次快照 2026-11-23；最近推送 2026-11-24T13:09:47Z；最新 release：v1.0.0（2026-11-06T12:31:31Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 1305（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 2 個 issue、8 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：解析、切塊、向量檢索與部署資源都會影響成果；未進行繁體中文文件與權限隔離測試。
- 與 Adam／metabiz 的關聯及下一步：對 know metabiz wiki 最直接；用同一批 SOP 比較回答引用、查無答案的處理與更新後的檢索結果，亦可做 RAG 課程案例。
- 來源：[專案與 README](https://github.com/infiniflow/ragflow)、[Releases](https://github.com/infiniflow/ragflow/releases)、[近期 issue／PR](https://github.com/infiniflow/ragflow/issues?q=sort%3Aupdated-desc)。

### 8. obra/superpowers｜Reference only

- 用途：以可組合 skills 定義 coding agent 的開發方法與流程。
- 動能與維護：總星數 325,713；前次快照 2026-11-23；最近推送 2026-11-03T23:24:58Z；最新 release：v7.0.2（2026-11-03T22:17:54Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 359（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 4 個 issue、6 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：近期熱門不代表核心程式同日更新；額外流程可能增加上下文與執行成本，須按任務規模選用。
- 與 Adam／metabiz 的關聯及下一步：可作 Adam 的 coding agent 流程課參考，檢視既有技能的需求釐清、驗證與交付方式；暫不因總星數高而優先導入。
- 來源：[專案與 README](https://github.com/obra/superpowers)、[Releases](https://github.com/obra/superpowers/releases)、[近期 issue／PR](https://github.com/obra/superpowers/issues?q=sort%3Aupdated-desc)。

### 9. google-labs-code/stitch-skills｜Demo content

- 用途：配合 Stitch MCP 的設計技能與外掛集合，描述支援多種 coding agent。
- 動能與維護：總星數 12,552；前次快照 2026-11-23；最近推送 2026-11-23T18:42:27Z；最新 release：v1.0（2026-05-18T18:02:32Z）。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 25（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 0 個 issue、10 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：依賴外部 Stitch 服務、MCP 相容性與使用配額；跨 Agent 的行為一致性尚未測試。
- 與 Adam／metabiz 的關聯及下一步：適合 Adam 的設計到程式示範與課程頁面原型；可評估 AI 辦公流程中的表單與內部工具介面產出。
- 來源：[專案與 README](https://github.com/google-labs-code/stitch-skills)、[Releases](https://github.com/google-labs-code/stitch-skills/releases)、[近期 issue／PR](https://github.com/google-labs-code/stitch-skills/issues?q=sort%3Aupdated-desc)。

### 10. cursor/plugins｜Watch

- 用途：Cursor 官方外掛與規格集合，提供工具整合與可重用能力的封裝參考。
- 動能與維護：總星數 19,084；前次快照 2026-11-23；最近推送 2026-11-24T10:37:37Z；最新 release：API 未取得最新正式 release，不能據此斷言專案沒有發版。
- README／議題訊號：已取得 README 摘要，僅作功能描述證據，尚未安裝驗證；API 未關閉項目 694（可能包含 PR）。按更新排序的最近 10 項樣本中，近 7 天有 2 個 issue、8 個 PR 更新；這是有限樣本，不能推算整體處理率。
- 風險：API 未回報明確 SPDX 授權；不同外掛的依賴、權限與版本需分開檢查，不能直接假設可跨工具搬用。
- 與 Adam／metabiz 的關聯及下一步：可支援 Adam 的 Cursor／Codex／Claude Code 技能封裝比較內容；挑一個與辦公 SaaS 相關的外掛做後續研究。
- 來源：[專案與 README](https://github.com/cursor/plugins)、[Releases](https://github.com/cursor/plugins/releases)、[近期 issue／PR](https://github.com/cursor/plugins/issues?q=sort%3Aupdated-desc)。

## 明日觀察清單

1. CLI-Anything、Claude-BugHunter：觀察今日星數與下一次增量是否延續；把高相對成長與可驗證成果分開評估。
2. diagram-design、last30days-skill：各挑一個繁體中文教學任務，檢驗輸出是否可直接成為課程素材；優先追 release 與修正 PR。
3. Firecrawl → RAGFlow → know metabiz wiki：建立小型來源擷取、文件更新與回答引用實驗；先訂正確率與可追溯性門檻。
4. AFFiNE：看同步／匯出問題是否有後續維護動作，再決定是否錄製知識管理 Demo。
5. Superpowers、Cursor plugins、Stitch skills：留意相容性、規格與新版本，避免只因高總星數擴大導入。

## 資料限制與可追溯性

- README 是作者主張；本輪沒有安裝、執行或驗證任何候選專案。分類是選題與研究建議，不代表導入完成。
- issue-activity.json 保存每個候選最近 10 筆 issue／PR 的更新時間與連結；不是完整七日活動統計，未分析修復時間或關閉比例。
- run-status.json 保存實際觀測時間、查詢、限流與退出狀態；collector-limit-*.log 保存 collector 訊息。trending-observation.json 是另外一次即時取樣，與 collector 可能有些微時間差。
- repos.json 與 snapshots/ 保留 collector 的逐項數據；report.md 為自動報表，本檔才是人工編輯的選題判斷。

- 注意：collector 有 6 筆沿用歷史資料的紀錄，該等專案不可當成最新觀測；詳見 log。

- 歷史資料沿用明細：`BarberNumber/Midjourney-Software`（HTTP 404）、`BrickOrioleLoad/aion-2-trainer-tool`（HTTP 404）、`HunYiSage/dsh-purge`（HTTP 404）、`YuJunZhiXue/dsh-purge`（HTTP 404）、`hanshaze/Awesome-Prediction-Market-Trading-Tools`（HTTP 404）、`mingrath/obsidian-ai-knowledge-agent`（HTTP 404）。10 個精選專案均未發生這項基本資料回退。
