# GitHub AI 趨勢雷達分析｜2026-09-16

本日共收集 101 個 AI／MCP／Skills／Agent 與知識庫相關候選。判讀以當日 Trending 星數、相對星數增量、最新 push／release、README 是否清楚描述可驗證工作流，以及 issue 負荷為主；總星數只作成熟度訊號。星數增量是相對於 2026-09-15 快照，首次出現或未在昨日集合中的 repo 不將 0 解讀為沒有成長。

| Repo | 目的與動能 | 總星數 | 風險 | 標記 | 與 Adam／Metabiz 的關聯 |
| --- | --- | ---: | --- | --- | --- |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 把確定性規則與 LLM agent 結合，輸出逐行 code review；Daily Trending +3,215、快照 +3,302，且 9/16 有 push 與 v1.12.4 release，是本日最強的開發自動化訊號。 | 31,050 | 181 個 open issues；需以小型私有 repo 驗證誤報、語言覆蓋與資料外送邊界。 | Deep research | 可做「AI code review 的規則層 + agent 層」課程案例，並評估作為 Metabiz 開發交付前品質關卡。 |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 將 coding agent 的資安稽核拆為偵察、coverage hunting、驗證與機器可讀報告；Trending +1,249、僅 8 個 open issues，README 的六階段流程很清楚。 | 6,246 | 無 release；安全掃描的 finding 仍須人工複核，避免自動化誤判升級為客戶承諾。 | Skill candidate | 可提煉成 Metabiz 專案上線前的 security-review skill 與內容示範。 |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 文件轉 RAG、推理 agent 與自維護 Wiki 的知識平台；Trending +1,201，9/16 有 push，主題涵蓋 RAG、wiki、multi-tenant 與 reranking。 | 25,043 | 授權欄位為 `NOASSERTION`、655 個 open issues；導入前必須確認商用授權、中文文件與維運成本。 | Deep research | 最直接對應 know metabiz wiki：可研究文件入庫、問答、持續更新與權限分層的設計。 |
| [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) | 讓 Claude Code、Codex、Cursor 等 coding agent 變成可做文獻、假設與實驗的 research agent；Trending +1,036、快照 +1,041，9/16 釋出 v0.2.3。 | 4,127 | 專案較新，研究結論與來源品質不能因 agent 產出而免驗證。 | Demo content | 適合製作「從研究到課綱／短影片腳本」工作流示範，連結 Adam 的課程選題。 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 封裝 plan、build、verify、review、ship 的工程技能，支援 Claude Code、Codex、Cursor；Trending +656、快照 +629，README 對品質門檻定位明確。 | 95,224 | 128 個 open issues，且通用技能未必符合本地 Odoo／文件／報價流程。 | Skill candidate | 可作為現有 Codex skills 的對照基線，挑出可移植的 verify／review gate。 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 以本地 AST 建立可查詢知識圖譜，涵蓋 code、docs、SQL、設定與 PDF，不依賴 vector store；快照 +1,336，9/15 有 v0.9.62、9/16 持續 push。 | 118,288 | 1,360 個 open issues；大 repo／多格式解析的效能與結果可信度需實測。 | Deep research | 可探索把 Metabiz 程式、流程文件與 wiki 關聯起來，作為 RAG 前的可解釋檢索層。 |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | Agent skill 生成可驗證、可匯出的架構／流程／資料流互動圖；快照 +1,346、9/16 仍在 push，README 明確支援 Claude Code、Codex、Cursor。 | 64,564 | 143 個 open issues；生成圖必須與實際 code／流程 owner 核對。 | Demo content | 很適合把 Metabiz 系統架構、Odoo 報價流程和 AI office automation 做成易懂內容與內部文件。 |
| [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | Hermes Agent 的長期記憶與模型工作流套件；Trending +74、快照 +109、9/16 有 push，且提供中文 README。 | 2,465 | 生態相依於 Hermes，30 個 open issues；長期記憶的資料保留與隔離需先審核。 | Watch | 可觀察其 memory／skills 組裝方式，作為 Metabiz office automation agent 記憶策略的參考。 |

## 明日 watchlist

- **open-code-review**：觀察 v1.12.4 後 issues 是否快速上升，以及 Trending 是否從爆發成為可持續採用。
- **WeKnora**：追蹤授權釐清與 655 個 open issues 的處理速度；若有明確商用條款，再安排本地文件小規模 PoC。
- **security-audit-skill**：用一個非機密示範 repo 檢驗 finding 的可重現性與人工審核成本。
- **OpenResearch**：追蹤 v0.2.3 的 release notes、來源引用與實驗可重現性；可準備一個課程研究題作 demo。
- **Graphify / Archify**：以一份 Metabiz 系統文件加小型程式庫測試「圖譜檢索 → 視覺化架構圖」是否能降低 wiki 維護成本。

## 觀察結論

今日訊號集中在「把 agent 工作流產品化」：code review、security audit、research、知識圖譜和架構圖都把可重複的專家步驟封裝成 skills 或 agent pipeline。對 Metabiz 而言，先做可驗證輸出的內部 demo（稽核報告、知識圖譜、架構圖），再決定是否導入完整平台，會比直接採用高星專案更穩健。
