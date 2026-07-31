# GitHub AI Trend Radar 分析 — 2026-07-31

## 結論

今天最明確的訊號不是再多一個通用 Agent framework，而是「可攜的技能包 + 可查證的研究流程 + 可控的 coding-agent harness」。優先做兩個小型驗證：以 `last30days-skill` 研究流程做成可審計內容/課程工作流；以 `Pi` 或 `Superpowers` 驗證技能治理與受控交付。知識庫產品則先比較 KAG 與既有 Wiki/RAG 架構，不要因 Dify/FastGPT 的高星數直接換底座。

- GitHub Trending daily 於本次執行時擷取；篩選後的顯著 AI/skills 項目有 `different-ai/openwork`（796 stars today）、`mvanhorn/last30days-skill`（660）、`zhaoxuya520/reverse-skill`（612）與 `microsoft/AI-For-Beginners`（1,592）。
- 搜尋 collector 先以匿名 API 執行，在最後查詢收到 403 rate limit；已改用本機 `gh` 登入 token、每查詢 `--limit 5` 重跑，得到 44 個去重 repo 與 README 摘要。
- 這是此 target directory 的首次快照，所有 `stars_delta` 為 0，不可解讀為沒有成長。下一次對同一目錄重跑才有日增量；本次以 Trending stars-today、近期 push/release、README 與議題負荷排序。
- collector 依主機日期寫入 `snapshots/repos-2026-08-01.json`；它是 7/31 radar 的執行快照，日期差異已保留而未竄改資料。

## 值得追的 10 個 repo

| 分類 | Repo | 動能與用途 | 本次指標 | 對 Adam 的可用性 / 風險 |
| --- | --- | --- | --- | --- |
| Deep research | [different-ai/openwork](https://github.com/different-ai/openwork) | Claude Cowork 的開源替代，建於 opencode；Trending 當日強勢。 | 1,944 stars；796 today | 可做「本機協作 Agent vs SaaS Cowork」demo。先檢查權限邊界、模型/API 成本與資料留存，不能直接用於客戶資料。 |
| Skill candidate | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 跨 Reddit、X、YouTube、HN、Polymarket、Web 的研究 skill，產出帶依據摘要。 | 55,996 stars；660 today | 很適合把課程選題、每日雷達與 AI 辦公室 research 做成「來源清單 + 引用 + 結論」的 reusable skill；先驗證來源品質、登入需求與成本。 |
| Skill candidate | [obra/superpowers](https://github.com/obra/superpowers) | 面向 Coding agent 的組合式 skills 與 SDLC 方法；README 明列 Codex、Claude Code、Cursor、Pi 等入口。 | 264,351 stars；7/24 v6.2.0；MIT | 可抽取其 planning/TDD/review 的可遷移習慣，與既有 Codex 規範比較；不要整包覆蓋本地 AGENTS/RTK 與既有 skill 治理。 |
| Demo candidate | [earendil-works/pi](https://github.com/earendil-works/pi) | 統一 LLM API、agent loop、TUI 與 coding-agent CLI；7/29 發 v0.83.0，7/31 仍有 push。 | 81,382 stars；88 open issues；MIT | 可作「同一 task 在 Codex / Pi 的受控交付」內容比較。適合沙盒 demo，不適合未驗證下接客戶憑證。 |
| Reference only | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP steering group 的少量 reference servers 與 SDK 示範。 | 89,093 stars；7/10 release；479 issues | 是 mOffice/know metabiz wiki 串接的協定參照，不是可直接選型的 server catalog；README 也明確提醒其為 reference implementation。 |
| Deep research | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 長任務 SuperAgent harness，覆蓋 sandbox、memory、tools、skills、subagents。 | 78,386 stars；6/25 v2.0.0；7/31 push；943 issues；MIT | 可研究任務分解、記憶與交接，作為 AI 辦公室自動化架構參考；高 issue 數與較重 runtime 代表先做隔離 POC。 |
| Demo candidate | [labring/FastGPT](https://github.com/labring/FastGPT) | RAG、資料處理、可視化 workflow 與 Agent 平台；7/31 發 v4.15.6。 | 29,211 stars；164 issues；license 欄位 NOASSERTION | 可用於「企業知識問答快速 demo」比較，但授權需在採用前由法務/原始 LICENSE 文件確認；不可只根據 GitHub API 欄位判斷。 |
| Deep research | [OpenSPG/KAG](https://github.com/OpenSPG/KAG) | 將 logical form / knowledge graph 用於專業領域檢索與多跳問答，補足純向量 RAG。 | 8,945 stars；174 issues；Apache-2.0；最後 push 2026-01-28 | 對 know metabiz wiki 的可追溯查詢最有研究價值；但 release 停在 2025-06、push 較舊，先以小型產品/契約資料集 benchmark，不做核心依賴。 |
| Watch | [langgenius/dify](https://github.com/langgenius/dify) | 協作式 Agent workflow、RAG、MCP 與多模型平台；7/28 有 bug/security release，7/31 持續 push。 | 150,909 stars；935 issues；license 欄位 NOASSERTION | 適合作為現成低碼 workflow 的市場基準與教學比較；平台龐大、升級與授權要先釐清，不能替代受控 wiki evidence pipeline。 |
| Demo content | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 週、24 課的 AI 教材，在 Trending 今日取得最大相關增量。 | 55,081 stars；1,592 today | 可拆解課程節奏、練習與教學敘事，轉化為繁中 AI 辦公室/Agent 入門內容；它是課綱參考，不是技術底座。 |

## 可直接轉成行動

### Deep research

1. **KAG × know metabiz wiki**：用一個已有來源與版本的商務資料夾做 20 題問答基準，評估引用可追溯性、多跳關係與維運成本；成功門檻是答案能回到原始證據，不是回答看起來更流暢。
2. **DeerFlow**：只在隔離環境跑一條「研究 → 草稿 → human approval」流程，量測完成時間、人工介入點、token/工具成本與失敗復原。
3. **Openwork**：研究其 Cowork/opencode 整合與安全模型；不得輸入客戶帳密、私有 repo 或 production token。

### Demo content

1. 「一天內 796 顆星的 Openwork：Claude Cowork 開源替代值得碰嗎？」— 比較資料邊界與實際交付，不做採用承諾。
2. 「AI 研究不是搜尋：用 last30days-skill 做可回查的選題 brief」— 示範來源、假設、結論與待驗證項目。
3. 「MCP reference server 不等於 production server」— 用官方 reference、社群 catalog 與自建 server 的責任邊界做一張對照圖。

### Skill candidate

1. 建立 `research-brief-with-sources`：固定輸出來源 URL、擷取時間、結論、反證、成本/授權、待確認事項；借鏡 `last30days-skill`，但將來源驗證放在本地規範。
2. 建立 `agent-delivery-gates`：把 Superpowers 的 planning/TDD/review 思想映射到既有 Codex AGENTS/RTK gate，不覆寫現有規範。

## 風險與非訊號

- **Trending 是注意力，不是採用證據。** `reverse-skill` 雖有 612 stars today，涵蓋逆向/滲透工具鏈；它不在本次推薦採用清單，僅提示安全類 coding-agent skills 正在升溫。導入第三方 skill 前必須審查指令、下載行為與權限。
- **首次快照沒有可用 star delta。** 本次不能以 collector 的 0 delta 排名，也不應把搜尋排序（依總 stars）當成熱度排名。
- **license 欄位 NOASSERTION。** Dify、FastGPT、MCP servers 的 API 欄位不能單獨判定商用權利；任何採用前仍需讀 repo 的 LICENSE、相依套件與部署條款。
- **issue 負荷提示維運成本。** DeerFlow 943、Dify 935、MCP servers 479 個 open issues；這是需驗證的維護訊號，不是品質定論。

## 明日追蹤清單

1. 對同一輸出目錄重跑並計算實際 `stars_delta`；將今日選出的 10 個 repo 固定列入比對。
2. 追蹤 Openwork、last30days-skill、Pi 是否仍在 Trending，以及新增 release、issue/PR 處理速度。
3. 補做 KAG 與 FastGPT/Dify 的 README install path、授權檔、self-hosted 需求與資料保留比較。
4. 為 `research-brief-with-sources` 寫一個只讀、可審計的最小 spec；先決定資料來源與 human-approval gate，再實作。
