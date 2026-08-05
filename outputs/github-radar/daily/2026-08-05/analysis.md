# GitHub AI 趨勢雷達｜2026-08-05（台灣目標日）

## 摘要與資料界線

- 本次以 2026-08-06 00:11（Asia/Taipei）執行；目標日為前一台灣日期 **2026-08-05**。
- Collector 以十組指定 AI/MCP/Agent/Skills/RAG/Wiki 查詢取得 **89** 個去重候選。其 snapshot 檔名為 `snapshots/repos-2026-08-06.json`，代表**執行日**，不是目標日。
- GitHub Trending daily 頁於收集時可讀到「today」榜單入口，但不提供可回溯的 8/05 歷史排名；因此下述動能採 8/04 與本次資料夾的相鄰快照比較（約 23 小時），**不是** Trending 的「stars today」。89 個 repo 全數重疊，故可比較。
- Collector 本次資料夾內的 `stars_delta=0` 是新資料夾基線；本報告改以跨資料夾總 stars 差額排序。用途均先以 README 或官方 repo 描述確認；星數是開發者注意力，不是採購或商業需求證明。

## 最值得追的 8 個 repo

| Repo／分類 | 用途與維護訊號 | 動能（相鄰快照）／總 stars | 對 Adam 的可用性與風險 |
|---|---|---:|---|
| [Graphify](https://github.com/Graphify-Labs/graphify) — **Deep research** | README 說明可把程式、PDF、Markdown、圖片產成可查詢圖與可導航 wiki；輸出邊標示 EXTRACTED / INFERRED / AMBIGUOUS，8/05 有 push。 | **+573**／102,900 | 最適合以 10–20 份去識別 metabiz wiki 筆記做 provenance PoC；Apache-2.0。但主 README 的安裝指向 Claude Code/Python，需先驗證 Codex 整合與外送影像/文件的資料邊界。 |
| [Pi Agent Harness](https://github.com/earendil-works/pi) — **Deep research** | README 確認包含 coding-agent CLI、tool/state runtime 與 multi-provider API；8/05 持續 push。 | **+657**／84,097 | 可作「不同 agent harness 的權限與可觀測性」課程比較；MIT。其 README 明示**沒有內建**檔案/程序/網路/憑證權限系統，任何實驗都必須先用容器或 sandbox。 |
| [Headroom](https://github.com/headroomlabs-ai/headroom) — **Demo candidate** | README 確認提供 library、proxy、MCP 與 Claude/Codex 等 wrapper，用於壓縮工具輸出、log、RAG chunk；8/05 有 push。 | **+297**／64,971 | 可做「工具回傳壓縮前後：成本、答案完整性、漏欄位」的短 demo；Apache-2.0。60–95%/15–20% 為其主張，不能直接當作 Adam 工作流結果，且高壓縮可能遺失關鍵欄位。 |
| [Superpowers](https://github.com/obra/superpowers) — **Skill candidate** | README 定位為 coding agent 的可組合開發方法與 skills，含規格、TDD、subagent 工作方式，並列出 Codex 安裝路徑。 | **+819**／267,107 | 高動能的「技能怎樣強制規格—驗證—交付」教材對照組；先採一個 skill 做人工 code review，勿整包覆蓋現有 AGENTS/skill 規則。 |
| [agent-skills](https://github.com/addyosmani/agent-skills) — **Skill candidate** | README 提供 24 個工程 lifecycle skills、可逐個安裝與 Codex plugin 說明；最近 push 為 8/04。 | **+267**／81,868 | 可萃取現有工作區欠缺的可驗證 checklist，而不是直接複製；MIT。README 明示單一 skill 安裝可能缺 repo-level references，採用前需保留相依文件與 license。 |
| [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) — **Deep research** | README 確認是連接 agent/IDE/企業資料庫的 MCP server，並支援 restricted access、structured query 與 semantic search；8/05 有 push。 | 本輪持平／16,126 | 最貼近 AI 辦公室自動化與 mCRM/Odoo 的「讀取型、allowlist、稽核」研究；Apache-2.0。禁止以 production credentials 直接試跑；先用 mock/唯讀 DB、最小權限與 query policy。 |
| [DeerFlow 2.0](https://github.com/bytedance/deer-flow) — **Watch** | README 確認是由 sub-agents、memory、sandboxes 與 skills 編排的 super-agent harness，且 2.0 是與 1.x 不相容的重寫；8/05 有 push。 | **+84**／79,358 | 適合 deep-research orchestration 架構拆解與 demo script 參考；MIT。平台大、導入摩擦高，README 也導向特定模型與 BytePlus 服務，先做隔離比較，勿當成可直接上線的營運代理。 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) — **Demo candidate** | README 確認是 Claude Code/Codex 的 Remotion 產品影片 skill，有 shot cards、preview gallery 與安裝指令；8/05 有 push。 | **+105**／3,606 | 很適合 Adam 的課程／內容素材：用一個去識別產品頁做 30–40 秒 demo；Apache-2.0。應先確認生成素材、音效與輸入頁面的商用權利，並在本機 preview 後才發布。 |

## 其餘分類與判斷

- **Reference only：**[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)（+89／71,859）適合做發現清單，不是可直接採用的實作；license 欄位空白、最近 push 為 7/24，需逐一回到原 repo 審查。
- **Watch：**[0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)（10,824）雖是 MIT 且 MCP/agent 議題熱，但用途是自動化滲透與漏洞探索；不納入一般 AI 辦公室或客戶環境的 demo。
- **Watch：**[FastGPT](https://github.com/labring/FastGPT)（+108／29,263）是活躍的 RAG/workflow 產品參考，但 collector 的 license 為 `NOASSERTION`；不可在確認正式 license、資料處理與部署責任前採用。

## 對課程、內容、AI 辦公室與 metabiz wiki 的行動翻譯

1. **Deep research：**Graphify 的 10–20 筆去識別 wiki 資料 PoC：驗證來源連結、EXTRACTED/INFERRED 標記、刪除更新與重新建圖成本；不接客戶 vault、不寫回正式 wiki。
2. **Demo content：**Headroom 用三條真實但去識別的工具輸出，記錄 token、答案完整度與遺漏重要欄位；video-shotcraft 用已授權的產品畫面製作一支短片。
3. **Skill candidate：**以 Superpowers 與 agent-skills 對照既有 skill：只挑一項可重複的品質門檻（例如測試或 code review），以人工審閱後的 project-local 版本驗證，避免覆蓋現行規則。
4. **AI 辦公室自動化：**MCP Toolbox 僅規劃「mock DB → 唯讀 allowlist → audit log → 人工核准」的隔離垂直切片；不做任何 production 寫入。
5. **課程定位：**Pi 與 DeerFlow 可形成「agent 很會做事之前，誰限制它、誰留下證據」的比較課；不可把 stars 當作可靠性或企業採用證據。

## 明日追蹤清單

- 比較 Graphify、Pi、Headroom、MCP Toolbox 的下一日 stars 差額、push/release/issue 改變；若差額只是單日尖峰，降級為 Watch。
- 實作前確認 Graphify 的 Codex 使用路徑與任何模型/API 的資料外送；保存可刪除的測試輸出。
- 以 mock schema 檢視 MCP Toolbox 的 restricted access、結構化查詢與稽核紀錄，任何缺一項即不連 production。
- 對 Headroom 以固定資料集量測壓縮與答案正確性；保留未壓縮版本供比對與回滾。
- 檢查 video-shotcraft 的輸入素材、音效與產出授權，再決定是否納入商用課程/行銷工作流。
