# GitHub AI 趨勢雷達｜2026-11-08

目標日期：**2026-11-08（Asia/Taipei 前一日）**。收集完成：**2026-11-09T00:22:56+08:00**。

本次精選 9 個專案，優先研究瀏覽器自動化、企業語意脈絡層與可驗證的 Skills。OpenMausBot 與長脈絡壓縮呈現較高相對成長；wiki 雖動能較低，仍因 know metabiz wiki 的直接需求入選。以下順序是編輯判斷，不是總星數排名。

## 觀測口徑與完整性

- 已用指定十組查詢、`--limit 10 --include-trending-daily --include-readme` 執行收集器；原始 423 筆，合併 11 筆轉址重複、排除 23 筆過期／範圍外資料後保留 **389 個專案**。詳見 collection.json。
- [GitHub Trending daily](https://github.com/trending?since=daily) 本次解析 9 張卡片，人工審核保留 6 個；billion-context 因簡單關鍵字漏判而補納。原始卡片、排除理由與觀測時間見 trending-daily.json。
- **stars today** 是 Trending 當次頁面的滾動窗口數值；**快照增量** 是本次總星數減去目標日 2026-11-07 的快照；**相對成長** 是增量／前次總星數。三者不可相加，也不代表精確的昨日午夜或固定 24 小時新增量。未上榜記「—」，不是零；新項目無基準時不推算增長。
- 本次即時數據歸檔至前一個台北日曆日，並非歷史還原。搜尋按總星數排序存在大型專案偏差；精選另外比較短期動能、近期 push、README、release 與 issue／PR 樣本。
- **API rate limit：未觀察到錯誤，未啟動 `--limit 5` 重試。** 7 個回傳 404 的歷史名稱全部排除，避免把舊資料誤標成本次觀測。
- README 全文與 SHA-256、metadata、最近 3 筆 release、最近更新的 8 筆 issue／PR 保存於 readmes/ 與 editorial-evidence.json。各項補查時間不同；下列星數統一採最終 repos.json。API open_issues_count 含未關閉 PR，不是純 issue 數。
- 用途依第一方資料整理；課程、內容、辦公自動化與 wiki 導入建議為分析判斷。本次未安裝或執行候選工具；提報與 PR 不等於缺陷已重現或修正已合併。

## 精選與動能

| 專案 | 用途 | 總 stars | stars today | 快照增量 | 相對成長 | 建議 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 以 Rust CLI 讀取瀏覽器無障礙樹並操作元素，適合逐步驗證網站工作流。 | 47,371 | 812 | +793 | +1.70% | **Demo content** |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 在聊天式介面調度 Claude／Codex 等多個 bots，為代理提供獨立電腦與應用連接。 | 17,909 | 1437 | +1,341 | +8.09% | **Demo content** |
| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | 在 agent 與模型 API 間壓縮與重寫脈絡，支援長時間 coding session。 | 4,961 | 460 | +472 | +10.51% | **Watch** |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | 從企業 metadata 建立語意與圖譜脈絡層，透過 MCP、CLI 與 API 供代理查詢名詞、定義與關係。 | 10,093 | — | +435 | +4.50% | **Deep research** |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 以多階段代理進行偵察、覆蓋追蹤、漏洞候選驗證與結構化稽核報告。 | 66,513 | — | +1,356 | +2.08% | **Deep research** |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 將工程設計、需求釐清與開發方法整理成可組合的 agent skills。 | 318,285 | — | +904 | +0.28% | **Skill candidate** |
| [anthropics/skills](https://github.com/anthropics/skills) | 提供動態載入指令、腳本與資源的 Agent Skills 範例，涵蓋文件、設計與企業工作流。 | 189,307 | 793 | +813 | +0.43% | **Skill candidate** |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 將多格式來源持續匯入為互連 wiki，支援來源追溯、知識圖譜與增量更新。 | 21,494 | — | +49 | +0.23% | **Deep research** |
| [google/skills](https://github.com/google/skills) | 彙整 Google 產品與技術的 Agent Skills，包含 Cloud IAM、解決方案與產品工作流。 | 23,668 | — | +494 | +2.13% | **Reference only** |

## 逐項判斷與應用

### 1. vercel-labs/agent-browser — Demo content

**用途：** 以 Rust CLI 讀取瀏覽器無障礙樹並操作元素，適合逐步驗證網站工作流。

**動能與維護：** 總星數 47,371；stars today 812；快照增量 +793、相對成長 +1.70%。最近 push（UTC）：2026-11-08T10:03:53Z；release：v0.41.2／2026-11-03T23:46:27Z。未關閉項目（含 PR）512；最近更新的 8 筆樣本中，4 個 issue、4 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** Adam 可製作「查詢→填寫→驗證結果」的 AI 辦公自動化教案；metabiz 可用匿名測試資料示範後台操作。

**風險：** iframe、冷啟動與卡住分頁仍有相容性回報；#2472 描述跨來源 iframe 無法定位，須以自己的網站重現。避免把成功呼叫當成操作完成。

**下一步：** 以登入後測試頁驗證 iframe 與頁面改版後 ref 是否失效，記錄成功率與重試次數。

來源：[專案與 README](https://github.com/vercel-labs/agent-browser)、[release 紀錄](https://github.com/vercel-labs/agent-browser/releases)、[具體 issue](https://github.com/vercel-labs/agent-browser/issues/2472)。

### 2. milind-soni/OpenMausBot — Demo content

**用途：** 在聊天式介面調度 Claude／Codex 等多個 bots，為代理提供獨立電腦與應用連接。

**動能與維護：** 總星數 17,909；stars today 1437；快照增量 +1,341、相對成長 +8.09%。最近 push（UTC）：2026-11-08T15:45:20Z；release：v0.1.149／2026-11-08T12:36:46Z。未關閉項目（含 PR）802；最近更新的 8 筆樣本中，2 個 issue、6 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** 適合 Adam 的 AI 辦公室系列：研究、整理資料與產出報告分工；metabiz 可先模擬知識整理交接。

**風險：** 版本快速變動、外部連接器與電腦權限增加維護面；#4913 回報背景任務完成後多 bot 工作流仍停滯，不能預設長任務可無人值守。

**下一步：** 在隔離測試環境跑兩個代理交接，驗證背景工作完成通知、權限與取消流程。

來源：[專案與 README](https://github.com/milind-soni/OpenMausBot)、[release 紀錄](https://github.com/milind-soni/OpenMausBot/releases)、[具體 issue](https://github.com/milind-soni/OpenMausBot/issues/4913)。

### 3. ranxianglei/billion-context — Watch

**用途：** 在 agent 與模型 API 間壓縮與重寫脈絡，支援長時間 coding session。

**動能與維護：** 總星數 4,961；stars today 460；快照增量 +472、相對成長 +10.51%。最近 push（UTC）：2026-11-08T16:16:20Z；release：v0.1.213／2026-11-07T23:25:08Z。未關閉項目（含 PR）920；最近更新的 8 筆樣本中，2 個 issue、6 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** Adam 可製作長任務的成本與記憶品質比較；know metabiz wiki 可借鏡摘要分層，但不直接拿對話摘要取代來源文件。

**風險：** README 的節省成本與 benchmark 是專案主張，本次未重跑；#5968 回報 fork 後保留的壓縮區塊遺失，API 串流、工具呼叫與模型切換需驗證。授權辨識為 NOASSERTION。

**下一步：** 固定模型與任務，比較原始對話、壓縮與 RAG 的關鍵事實保留率、token 與錯誤率。

來源：[專案與 README](https://github.com/ranxianglei/billion-context)、[release 紀錄](https://github.com/ranxianglei/billion-context/releases)、[具體 issue](https://github.com/ranxianglei/billion-context/issues/5968)。

### 4. NVIDIA/auto-ontology — Deep research

**用途：** 從企業 metadata 建立語意與圖譜脈絡層，透過 MCP、CLI 與 API 供代理查詢名詞、定義與關係。

**動能與維護：** 總星數 10,093；stars today —；快照增量 +435、相對成長 +4.50%。最近 push（UTC）：2026-11-07T21:54:29Z；release：本次未取得 latest release（不代表沒有其他發行方式）。未關閉項目（含 PR）87；最近更新的 8 筆樣本中，7 個 issue、1 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** 直接對應 know metabiz wiki 的欄位口徑與跨系統關係；Adam 可用匿名 CRM 欄位示範 RAG 與語意資料層的差異。

**風險：** 跨資料源定義對齊需要人工維護；#463 回報 PostgreSQL connector 遺漏跨 schema 外鍵，#462 關注無法回答時的判斷。README 表示目前不接受外部貢獻，須評估修復依賴。

**下一步：** 以兩個 schema 的匿名資料測試外鍵、口徑衝突與來源追溯，觀察 connector 修復。

來源：[專案與 README](https://github.com/NVIDIA/auto-ontology)、[release 紀錄](https://github.com/NVIDIA/auto-ontology/releases)、[具體 issue](https://github.com/NVIDIA/auto-ontology/issues/463)。

### 5. cloudflare/security-audit-skill — Deep research

**用途：** 以多階段代理進行偵察、覆蓋追蹤、漏洞候選驗證與結構化稽核報告。

**動能與維護：** 總星數 66,513；stars today —；快照增量 +1,356、相對成長 +2.08%。最近 push（UTC）：2026-09-14T19:29:02Z；release：本次未取得 latest release（不代表沒有其他發行方式）。未關閉項目（含 PR）120；最近更新的 8 筆樣本中，2 個 issue、6 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** 適合 Adam 的進階 coding-agent 課與 metabiz 稽核研究：用已知缺陷程式測試證據、覆蓋與誤報。

**風險：** 本次星數持續上升，但最近 push 仍在九月；#135 的驗證器與測試失敗回報仍值得追查。PR #141 提議強制逐字證據，不代表主分支已修復。

**下一步：** 追蹤 #141 與 #138 的合併情況，以已知案例量測誤報及證據可重現性。

來源：[專案與 README](https://github.com/cloudflare/security-audit-skill)、[release 紀錄](https://github.com/cloudflare/security-audit-skill/releases)、[具體 issue](https://github.com/cloudflare/security-audit-skill/issues/135)。

### 6. mattpocock/skills — Skill candidate

**用途：** 將工程設計、需求釐清與開發方法整理成可組合的 agent skills。

**動能與維護：** 總星數 318,285；stars today —；快照增量 +904、相對成長 +0.28%。最近 push（UTC）：2026-11-05T10:40:01Z；release：v1.3.2／2026-10-29T10:27:41Z。未關閉項目（含 PR）223；最近更新的 8 筆樣本中，8 個 issue、0 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** 適合 Adam 的 Skills 封裝與工程工作流課程；可挑單一需求釐清技能，轉成 metabiz 內部需求訪談教材。

**風險：** 高總星數不等同高相對成長；#1399 回報 implement-spec 留下標籤與 ticket 殘留，#1398 回報 grilling 脈絡遺失。安裝前應按平台檢查工具依賴。

**下一步：** 挑單一技能檢查輸入、輸出與停止條件，驗證任務完成後 ticket／標籤清理。

來源：[專案與 README](https://github.com/mattpocock/skills)、[release 紀錄](https://github.com/mattpocock/skills/releases)、[具體 issue](https://github.com/mattpocock/skills/issues/1399)。

### 7. anthropics/skills — Skill candidate

**用途：** 提供動態載入指令、腳本與資源的 Agent Skills 範例，涵蓋文件、設計與企業工作流。

**動能與維護：** 總星數 189,307；stars today 793；快照增量 +813、相對成長 +0.43%。最近 push（UTC）：2026-11-06T22:32:32Z；release：本次未取得 latest release（不代表沒有其他發行方式）。未關閉項目（含 PR）1,495；最近更新的 8 筆樣本中，2 個 issue、6 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** 適合 Adam 的文件自動化與 Skills 入門；以匿名報價表、簡報與報告設計可重複的驗收案例。

**風險：** 範例仍需環境驗證；#2155 是拒絕重算含 Excel data tables 工作簿的修正提案，#1352 回報評估工作者交叉配對。API 未辨識到授權；README 宣稱多數與文件技能採 Apache 2.0，實際採用前仍應核對各子目錄 LICENSE。

**下一步：** 觀察試算表與技能評估修正是否合併，再用含資料表的測試檔驗證輸出。

來源：[專案與 README](https://github.com/anthropics/skills)、[release 紀錄](https://github.com/anthropics/skills/releases)、[具體 PR](https://github.com/anthropics/skills/pull/2155)。

### 8. nashsu/llm_wiki — Deep research

**用途：** 將多格式來源持續匯入為互連 wiki，支援來源追溯、知識圖譜與增量更新。

**動能與維護：** 總星數 21,494；stars today —；快照增量 +49、相對成長 +0.23%。最近 push（UTC）：2026-10-21T11:17:29Z；release：v0.6.13／2026-10-22T01:21:07Z。未關閉項目（含 PR）299；最近更新的 8 筆樣本中，1 個 issue、0 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** 與 know metabiz wiki 最直接相關；Adam 可用同一批匿名文件比較傳統 RAG 與持久 wiki 的維護成本與答案可追溯性。

**風險：** 最近程式 push 與 release 比熱門代理工具慢；#837 回報重新匯入縮短頁面並產生重複，#847 回報 Linux 啟動依賴。API 授權為 NOASSERTION，未核定商用條款。

**下一步：** 測試重複匯入、來源刪除、長文件與匯出還原；追蹤分段匯入 PR #846。

來源：[專案與 README](https://github.com/nashsu/llm_wiki)、[release 紀錄](https://github.com/nashsu/llm_wiki/releases)、[具體 issue](https://github.com/nashsu/llm_wiki/issues/837)。

### 9. google/skills — Reference only

**用途：** 彙整 Google 產品與技術的 Agent Skills，包含 Cloud IAM、解決方案與產品工作流。

**動能與維護：** 總星數 23,668；stars today —；快照增量 +494、相對成長 +2.13%。最近 push（UTC）：2026-11-07T14:41:39Z；release：本次未取得 latest release（不代表沒有其他發行方式）。未關閉項目（含 PR）32；最近更新的 8 筆樣本中，7 個 issue、1 個 PR 在觀測前 48 小時內更新，僅代表樣本活動。

**Adam／metabiz 關聯：** Adam 可參考官方技能目錄與情境寫法；對辦公自動化的價值取決於實際使用的 Google 產品，Cloud 技能不直接等同 Workspace 自動化。

**風險：** #245 回報過寬 IAM 建議，#244 質疑 eval 動態執行；均是尚未重現的提報。應逐個技能檢查依賴與權限，不能只因官方來源而整包採用。

**下一步：** 優先檢查與現有工具相關的單一技能，追蹤 IAM 與動態執行回報的處理。

來源：[專案與 README](https://github.com/google/skills)、[release 紀錄](https://github.com/google/skills/releases)、[具體 issue](https://github.com/google/skills/issues/245)。

## 明日觀察清單（2026-11-09 目標日）

下次於 2026-11-10 台北日期執行時，優先確認以下變化；未出現新證據的項目維持觀察。

- **vercel-labs/agent-browser：** 以登入後測試頁驗證 iframe 與頁面改版後 ref 是否失效，記錄成功率與重試次數。
- **milind-soni/OpenMausBot：** 在隔離測試環境跑兩個代理交接，驗證背景工作完成通知、權限與取消流程。
- **ranxianglei/billion-context：** 固定模型與任務，比較原始對話、壓縮與 RAG 的關鍵事實保留率、token 與錯誤率。
- **NVIDIA/auto-ontology：** 以兩個 schema 的匿名資料測試外鍵、口徑衝突與來源追溯，觀察 connector 修復。
- **cloudflare/security-audit-skill：** 追蹤 #141 與 #138 的合併情況，以已知案例量測誤報及證據可重現性。
- **mattpocock/skills：** 挑單一技能檢查輸入、輸出與停止條件，驗證任務完成後 ticket／標籤清理。
- **anthropics/skills：** 觀察試算表與技能評估修正是否合併，再用含資料表的測試檔驗證輸出。
- **nashsu/llm_wiki：** 測試重複匯入、來源刪除、長文件與匯出還原；追蹤分段匯入 PR #846。
- **google/skills：** 優先檢查與現有工具相關的單一技能，追蹤 IAM 與動態執行回報的處理。

## 十組搜尋查詢

- `mcp server ai`
- `model context protocol`
- `agent skills coding agent`
- `claude code template`
- `codex skills`
- `coding agent llm`
- `rag knowledge base`
- `ai wiki knowledge management`
- `llm orchestration agent`
- `developer automation ai`
