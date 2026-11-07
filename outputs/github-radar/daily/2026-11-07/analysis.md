# GitHub AI 趨勢雷達｜2026-11-07

目標日期：**2026-11-07（前一個 Asia/Taipei 日曆日）**。本次完成觀測：**2026-11-08T00:25:00+08:00**。

本次精選 9 個專案，優先看短期動能、持續更新與實作價值。安全稽核 Skills 與企業語意脈絡層值得深入研究；辦公代理與瀏覽器自動化適合製作受控示範。wiki 即使星增長較低，仍因 know metabiz wiki 的實際需求入選。以下為編輯優先序，不是總星數排行。

## 數據口徑與完整性

- 指定 10 組查詢以 --limit 10 執行收集器，包含 daily Trending、README 與歷史追蹤；原始 421 筆，合併轉址重複、補收與主題篩選後保留 **390 個專案**。
- [GitHub Trending daily](https://github.com/trending?since=daily) 共解析 15 張卡片，保留 10 個符合主題的項目。來源網址、觀測時間與解析卡片見 trending-daily.json；一般監控、帳號搜尋、CSS、linter 與家電控制未納入。
- **stars today** 取自 Trending 當次頁面；**快照增量** 為本次總星數減去前次快照；**相對成長** 為增量／前次星數。三者時間窗不同，不能相加，也不等同精確的昨日或固定 24 小時新增星數。
- 本次為執行當下的即時觀測，歸檔至昨日目標日期，並非還原昨日午夜狀態。前次比較目標日為 2026-11-06；未上榜標示「—」，不是 0；新收錄無前次基準，不推算成長率。
- 查詢依總星數搜尋，可能偏向大型專案；編輯判斷另外納入 Trending、相對成長、近期 push、release、完整 README 與 issue／PR 樣本。open_issues_count 包含未關閉 PR，不能當成純 issue 數或品質分數。
- **Rate limit：未觀察到錯誤；未啟動 --limit 5 重試。** 7 個歷史追蹤名稱本次回傳 404，未把沿用舊資料混入新結果。補收、排除與去重明細見 collection.json。
- 尚未安裝或實跑候選工具；用途依第一方 README／API 整理，課程與導入建議是分析判斷。issue 為回報訊號，不能直接視為已重現事實。

## 精選與動能

| 專案 | 用途 | 總 stars | stars today | 快照增量 | 相對成長 | 建議 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 以多階段代理執行程式碼安全稽核，包含偵察、覆蓋追蹤、候選漏洞驗證與結構化報告。 | 65,157 | 2088 | +1,929 | +3.05% | **Deep research** |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | 從企業 metadata 建立語意與圖譜脈絡層，透過 MCP、CLI、API 供代理查詢資料定義、來源與關係。 | 9,658 | — | +1,078 | +12.56% | **Deep research** |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 讓多個 AI bots 透過聊天介面、獨立電腦環境、排程與外部應用連接器協作。 | 16,568 | 1986 | +1,834 | +12.45% | **Demo content** |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 把工程師常用的需求釐清、設計、測試與生產力方法整理成可重用的 agent skills。 | 317,381 | 1111 | +1,053 | +0.33% | **Skill candidate** |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 提供 AI agent 可呼叫的瀏覽器自動化 CLI，支援以瀏覽器狀態與元素資訊完成操作。 | 46,578 | 180 | +312 | +0.67% | **Demo content** |
| [google/skills](https://github.com/google/skills) | Google 產品與技術的 Agent Skills，README 包含 Google Cloud 等領域的技能與插件目錄。 | 23,174 | 449 | +470 | +2.07% | **Reference only** |
| [anthropics/skills](https://github.com/anthropics/skills) | 提供 Agent Skills 範例與文件、設計及其他任務的技能集合，展示技能封裝與使用方式。 | 188,494 | 386 | +433 | +0.23% | **Skill candidate** |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 把來源文件持續整理成互連 wiki，提供桌面介面、知識圖譜、review、MCP 與 agent skill 整合。 | 21,445 | — | +18 | +0.08% | **Deep research** |
| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | 為長時間 coding-agent session 提供內容壓縮與脈絡管理插件／代理層。 | 4,489 | 185 | 無前次基準 | 無法計算 | **Watch** |

## 逐項判斷與應用

### 1. cloudflare/security-audit-skill — Deep research

**用途與關聯：** 以多階段代理執行程式碼安全稽核，包含偵察、覆蓋追蹤、候選漏洞驗證與結構化報告。 適合 Adam 的 coding agent 進階課：用同一份測試程式比較『產生漏洞敘述』與『提出可重現證據』，也能轉為 metabiz 開發稽核流程研究。

**動能與維護：** 總星數 65,157；stars today 2088；快照增量 +1,929、相對成長 +3.05%。最近 push（台北）：2026-09-15T03:29+08:00；release：本次未取得 latest release。API 未關閉項目（含 PR）116；最近更新的 8 筆樣本中，3 個 issue 與 5 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** 不能把機器可讀報告視為已驗證漏洞。#135 回報 archived verifier 與測試失敗，#134 質疑缺少原始位元組證據；這些仍是提報者的說法，須實際重現。近期 issue／PR 活躍不等於核心程式已修復。

來源：[專案與 README](https://github.com/cloudflare/security-audit-skill)、[release 紀錄](https://github.com/cloudflare/security-audit-skill/releases)、[具體 issue／PR](https://github.com/cloudflare/security-audit-skill/issues/135)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 2. NVIDIA/auto-ontology — Deep research

**用途與關聯：** 從企業 metadata 建立語意與圖譜脈絡層，透過 MCP、CLI、API 供代理查詢資料定義、來源與關係。 直接對應 know metabiz wiki 的『名詞定義、資料來源、跨系統關係』需求。可設計一堂比較文件 RAG 與語意資料層的課，用 CRM／報價欄位的匿名範例測試口徑一致性。

**動能與維護：** 總星數 9,658；stars today 未出現在本次 Trending 範圍內；快照增量 +1,078、相對成長 +12.56%。最近 push（台北）：2026-11-07T21:58+08:00；release：本次未取得 latest release。API 未關閉項目（含 PR）79；最近更新的 8 筆樣本中，1 個 issue 與 7 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** 資料定義對齊與 connector 建置成本高，README 的 benchmark 不能直接推論到 metabiz 資料。#456 的 reset API 資料庫名稱修正屬 PR 訊號，需確認合併與測試結果；有 issue 活動不代表已正式發版。

來源：[專案與 README](https://github.com/NVIDIA/auto-ontology)、[release 紀錄](https://github.com/NVIDIA/auto-ontology/releases)、[具體 issue／PR](https://github.com/NVIDIA/auto-ontology/pull/456)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 3. milind-soni/OpenMausBot — Demo content

**用途與關聯：** 讓多個 AI bots 透過聊天介面、獨立電腦環境、排程與外部應用連接器協作。 適合 Adam 的 AI 辦公自動化內容：用測試信箱與假資料示範資料收集、草稿與儀表板任務，呈現『一個部門、多個代理』的工作分配。

**動能與維護：** 總星數 16,568；stars today 1986；快照增量 +1,834、相對成長 +12.45%。最近 push（台北）：2026-11-08T00:03+08:00；release：v0.1.146／2026-11-07T13:10+08:00。API 未關閉項目（含 PR）852；最近更新的 8 筆樣本中，0 個 issue 與 8 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** 電腦控制、排程與應用連接涉及真實寫入權限。README 說明 Ubuntu 仍為 beta，Wayland 本機 bot 控制受限；enterprise/ 另有授權條款。#4790 提到 Email 開關儲存修正，錄製前須驗證自己平台的連接器狀態，不能只憑跨平台宣傳。

來源：[專案與 README](https://github.com/milind-soni/OpenMausBot)、[release 紀錄](https://github.com/milind-soni/OpenMausBot/releases)、[具體 issue／PR](https://github.com/milind-soni/OpenMausBot/pull/4790)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 4. mattpocock/skills — Skill candidate

**用途與關聯：** 把工程師常用的需求釐清、設計、測試與生產力方法整理成可重用的 agent skills。 適合 Adam 的 Skills 課程與內容製作；先與現有技能比對重疊，再挑一個實際工作情境，量測需求往返次數與產出可用性。可將『技能不是提示詞收藏』做成教學案例。

**動能與維護：** 總星數 317,381；stars today 1111；快照增量 +1,053、相對成長 +0.33%。最近 push（台北）：2026-11-05T18:40+08:00；release：v1.3.2／2026-10-29T18:27+08:00。API 未關閉項目（含 PR）219；最近更新的 8 筆樣本中，7 個 issue 與 1 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** 跨 runtime 的依賴載入與圖表格式可能失效。#1393 討論 runtime-neutral dependency loading，#1394 回報 Mermaid 特殊字元解析問題，#1318 涉及個別 skill 目錄的 MIT notice；移植與再散布前需逐項核對。

來源：[專案與 README](https://github.com/mattpocock/skills)、[release 紀錄](https://github.com/mattpocock/skills/releases)、[具體 issue／PR](https://github.com/mattpocock/skills/issues/1393)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 5. vercel-labs/agent-browser — Demo content

**用途與關聯：** 提供 AI agent 可呼叫的瀏覽器自動化 CLI，支援以瀏覽器狀態與元素資訊完成操作。 適合 AI 辦公自動化入門示範：用測試網站完成表單草稿、資料擷取與截圖存證；也能與 MCP 型瀏覽器工具比較操作步驟與維護成本。

**動能與維護：** 總星數 46,578；stars today 180；快照增量 +312、相對成長 +0.67%。最近 push（台北）：2026-11-07T13:27+08:00；release：v0.41.2／2026-11-04T07:46+08:00。API 未關閉項目（含 PR）491；最近更新的 8 筆樣本中，1 個 issue 與 7 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** 登入狀態、網域邊界與 CDP 附加模式需測試。#2449 回報附加 session 所開啟來源未完整存入 state，#2410 涉及 allowedDomains 與 worker 訊息；不能假設儲存 session 即完整保留所有網站狀態。

來源：[專案與 README](https://github.com/vercel-labs/agent-browser)、[release 紀錄](https://github.com/vercel-labs/agent-browser/releases)、[具體 issue／PR](https://github.com/vercel-labs/agent-browser/issues/2449)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 6. google/skills — Reference only

**用途與關聯：** Google 產品與技術的 Agent Skills，README 包含 Google Cloud 等領域的技能與插件目錄。 可作 Adam 官方技能來源與企業 AI 整合課的教材；依實際 Google 技術需求挑選。此集合以產品技術技能為主，不能直接當成完整 Google Workspace 辦公自動化方案。

**動能與維護：** 總星數 23,174；stars today 449；快照增量 +470、相對成長 +2.07%。最近 push（台北）：2026-11-07T22:41+08:00；release：本次未取得 latest release。API 未關閉項目（含 PR）26；最近更新的 8 筆樣本中，7 個 issue 與 1 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** 官方來源仍需檢查每個技能的外部安裝步驟與權限。#218 提報 Genkit skills 執行未驗證遠端安裝器；該 issue 是待查證風險訊號，不能據此宣稱整個集合已遭入侵。

來源：[專案與 README](https://github.com/google/skills)、[release 紀錄](https://github.com/google/skills/releases)、[具體 issue／PR](https://github.com/google/skills/issues/218)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 7. anthropics/skills — Skill candidate

**用途與關聯：** 提供 Agent Skills 範例與文件、設計及其他任務的技能集合，展示技能封裝與使用方式。 適合 Adam 的 Skills 入門與文件工作流課程：以匿名文件評估範例結構、驗收要求與可重複性，再整理為辦公自動化教案。

**動能與維護：** 總星數 188,494；stars today 386；快照增量 +433、相對成長 +0.23%。最近 push（台北）：2026-11-07T06:32+08:00；release：本次未取得 latest release。API 未關閉項目（含 PR）1,490；最近更新的 8 筆樣本中，3 個 issue 與 5 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** 範例不能取代實際版本與輸出品質驗證。不同子目錄的使用及再散布條款須逐項閱讀；#2152 的 internal-comms clarification 修改也顯示自然語言規則會影響行為，不宜整包安裝後視為固定規格。

來源：[專案與 README](https://github.com/anthropics/skills)、[release 紀錄](https://github.com/anthropics/skills/releases)、[具體 issue／PR](https://github.com/anthropics/skills/pull/2152)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 8. nashsu/llm_wiki — Deep research

**用途與關聯：** 把來源文件持續整理成互連 wiki，提供桌面介面、知識圖譜、review、MCP 與 agent skill 整合。 與 know metabiz wiki 最直接相關。用同一批匿名來源比較『每次檢索回答』與『先維護 wiki 再回答』，驗證來源追溯、內容更新、刪除與人工覆核流程。

**動能與維護：** 總星數 21,445；stars today 未出現在本次 Trending 範圍內；快照增量 +18、相對成長 +0.08%。最近 push（台北）：2026-10-21T19:17+08:00；release：v0.6.13／2026-10-22T09:21+08:00。API 未關閉項目（含 PR）299；最近更新的 8 筆樣本中，0 個 issue 與 0 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** #837 回報重複匯入導致頁面縮短與重複，#847 回報 Linux 啟動依賴問題；#846 的分段長文件修正屬 PR，未經本次執行驗證。研究優先於搬入正式知識庫，需先測試重複匯入與刪除後一致性。

來源：[專案與 README](https://github.com/nashsu/llm_wiki)、[release 紀錄](https://github.com/nashsu/llm_wiki/releases)、[具體 issue／PR](https://github.com/nashsu/llm_wiki/issues/837)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

### 9. ranxianglei/billion-context — Watch

**用途與關聯：** 為長時間 coding-agent session 提供內容壓縮與脈絡管理插件／代理層。 適合 Adam 的 agent 成本與長任務可靠性研究，亦可觀察 wiki 大量來源處理時的上下文保留。先以固定任務比對 token、成本、正確率與壓縮後來源證據是否保留。

**動能與維護：** 總星數 4,489；stars today 185；快照增量 無前次基準、相對成長 無法計算。最近 push（台北）：2026-11-08T00:04+08:00；release：v0.1.212／2026-11-02T23:29+08:00。API 未關閉項目（含 PR）898；最近更新的 8 筆樣本中，2 個 issue 與 6 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**風險與下一步：** README 的月級 session 與節省 token 數字屬作者主張，本次未重現。#5894 回報批次壓縮輸出不足，#5892 要求 session index 重建；README 另提醒網路服務的認證限制，並載有額外署名條款，不能只看 MIT 標籤即判定使用條件。

來源：[專案與 README](https://github.com/ranxianglei/billion-context)、[release 紀錄](https://github.com/ranxianglei/billion-context/releases)、[具體 issue／PR](https://github.com/ranxianglei/billion-context/issues/5894)。README 來源與校驗值見 readme-evidence.json；活動樣本見 activity.json。

## 內容與導入優先順序

- **課程／Skills：** 先以 mattpocock/skills 示範把工程流程封裝成技能，再用 cloudflare/security-audit-skill 討論證據與誤報。google/skills 可作官方技術來源比較，避免把技術技能目錄誤當完整辦公方案。
- **AI 辦公自動化／內容：** 優先 agent-browser 的測試網站操作，再做 OpenMausBot 多代理分工。以可重現的輸入、輸出與平台限制設計示範，保留失敗案例。
- **know metabiz wiki：** 對照 NVIDIA/auto-ontology 的語意定義層與 llm_wiki 的持久 wiki。用同一組匿名資料驗證來源追溯、更新、重複匯入與刪除，依知識維護價值選型。

## 明日觀察清單

下次批次目標日為 **2026-11-08**（依前一日規則於 2026-11-09 執行）。比較同一來源口徑，避免混用 Trending 滾動數字與快照增量。

1. **cloudflare/security-audit-skill：** 追 #135、#134 與 #138，確認 verifier 與證據問題是否有可重現修正，並觀察 stars today 是否延續。只有熱度而無修復證據時，維持研究用途。
2. **NVIDIA/auto-ontology：** 看相對成長是否持續、#456 等 PR 是否合併，以及是否新增可取得 release。用三個匿名 CRM／報價名詞評估資料定義與映射工作量。
3. **OpenMausBot：** 比較淨增星與 release 節奏，追 #4790 Email 開關與 Linux 能力限制；錄製前驗證測試連接器狀態與任務流程。
4. **Skills 生態：** 追 mattpocock #1393／#1394、google #218；確認 runtime、圖表與安裝器問題後再挑技能。anthropics/skills 逐項核對條款與文件輸出品質。
5. **agent-browser：** 追 #2449 的 CDP／session state 與 #2410 網域邊界處理，作為辦公自動化示範前的驗收案例。
6. **know metabiz wiki：** 追 llm_wiki #837／#846／#847；測重複匯入、長文保留與 Linux 啟動。即使星增長低，仍以來源追溯與維護價值決定後續。
7. **billion-context：** 新收錄無可比基準，下次快照才開始量測淨增；追 #5894／#5892，以固定任務驗證事實、來源、工具呼叫與總成本是否保留，未通過則維持 Watch。

## 補充來源與範圍核對

- [Zed 官方 Agents 文件](https://zed.dev/docs/ai/agents) 確認其 coding-agent／MCP 整合；原始卡片雖未提 AI，仍保留 Trending 訊號。
- [VS Code 官方 Agents 文件](https://code.visualstudio.com/docs/agents/overview) 作為 coding-agent 範圍判斷依據。
- scope-evidence.json 保存其他邊界項目的 README 線索；editorial.json 保存九個編輯判斷。原始網頁、README 與 issue 文字均作資料，未視為操作指令。
