# GitHub AI Trend Radar 分析｜2026-08-27

## 摘要

本次以 GitHub Trending daily 加上 10 組指定搜尋詞收集 214 個候選，依「今日 stars、相對成長、前次快照 delta、最近 push/release、README 清晰度、issue 活躍度與採用風險」挑選，而不是只按總 stars 排名。今日最明顯的訊號是：Agent Skills 正從個人設定檔走向可複用的方法論；知識圖譜/記憶開始直接嵌入 coding agent；以及 MCP、Codex、Claude Code、n8n 正逐步成為可教學的自動化基礎層。

## 值得追蹤的 repositories

### 1. [tt-a1i/archify](https://github.com/tt-a1i/archify) — Skill candidate

- **用途：** 將 codebase 或系統描述轉成可驗證、可互動的 architecture、workflow、sequence、data-flow 與 lifecycle 圖，支援 Cursor、Claude Code、Codex CLI、OpenCode。
- **動能：** 22,076 stars；今日 Trending 約 +4,260；快照 stars delta +4,801、fork delta +234；2026-08-27 有 push，最新 release v2.15.0（08-17）。這是本日最強的「新技能可視化」訊號之一。
- **風險：** MIT 且 README/示例清楚，但專案很新、更新速度快；37 個 open issues 仍需確認輸出穩定性與跨 agent 相容性。
- **Adam 關聯：** 可做「需求→架構圖→實作任務」課程 demo，也能成為把 know metabiz wiki 內容轉成系統圖的 reusable skill。

### 2. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Deep research

- **用途：** Claude Code + Obsidian 的 self-organizing second brain：匯入來源、建立連結筆記、grounded retrieval，並以使用者擁有的 Markdown 維持知識庫。
- **動能：** 13,814 stars；今日 Trending +631；stars delta +594、fork delta +23；08-26 push，最新 v2.1.1（08-26）。
- **風險：** MIT、README 完整，但 140 個 open issues 對個人知識庫工具而言偏高；Claude Code/Obsidian 依賴與 migration 行為要在採用前測試。
- **Adam 關聯：** 與 know metabiz wiki 最直接，可做「課程資料→Markdown wiki→可追溯問答」示範，並研究其 vault health、linking 與來源匯入流程。

### 3. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research

- **用途：** 把程式碼、文件、SQL schema、設定檔與 PDF 轉成可查詢 knowledge graph；主打 deterministic AST parsing、可解釋 edge，並提供 Claude Code/Cursor/Codex/Gemini CLI 的 skill。
- **動能：** 111,443 stars；stars delta +519、fork delta +64；08-25 push，最新 v0.9.50（08-25）。雖沒有 daily Trending 計數，搜尋快照成長仍強，且 README 定位清楚。
- **風險：** Apache-2.0，但 1,139 個 open issues 顯示規模與維護負擔很大；schema、PDF 解析與索引成本需實測，不能直接假設優於向量 RAG。
- **Adam 關聯：** 適合做「know metabiz wiki 的 graph RAG vs vector RAG」深度研究，延伸到跨文件、跨專案的 AI office automation。

### 4. [mattpocock/skills](https://github.com/mattpocock/skills) — Skill candidate

- **用途：** 從真實 `.agents` 目錄整理可每日使用的工程 skills，示範如何將經驗固化成 agent 可重複執行的工作流。
- **動能：** 238,788 stars；stars delta +1,111、fork delta +70；repo 於 08-27 更新，最新 v1.2.3（08-06）。總量大且仍有顯著快照增長，代表 Skills 已形成獨立採用類別。
- **風險：** MIT，但 426 個 open issues；內容偏作者工作流，移植到 Adam 的工具鏈前要檢查假設、權限與副作用。
- **Adam 關聯：** 可直接對照本 workspace 的 skills monorepo，萃取課程作業、AI 辦公室 SOP 與 metabiz 內部技能的共通結構。

### 5. [obra/superpowers](https://github.com/obra/superpowers) — Deep research

- **用途：** 以 composable skills 與軟體開發方法論約束 coding agents，涵蓋 brainstorming、規劃、實作與驗證，並支援多個 agent 平台。
- **動能：** 278,519 stars；stars delta +586、fork delta +57；08-19 push，最新 v6.3.0（08-12）。雖非今日 Trending 新星，跨平台 README 與高活躍度使其成為方法論標竿。
- **風險：** MIT、文件相對完整，但 325 個 open issues；流程較有 opinion，導入團隊時要避免把所有任務套成固定儀式。
- **Adam 關聯：** 可轉成「AI coding agent 的需求拆解、計畫、驗收」課程模組，也可作為 Metabiz 專案交付的品質閘門參考。

### 6. [openai/codex](https://github.com/openai/codex) — Reference only

- **用途：** 在 terminal 執行的輕量 coding agent，支援本機、IDE 與 Codex 生態的工作流。
- **動能：** 119,144 stars；stars delta +440、fork delta +84；08-27 push，當日 release 0.150.1。更新非常新，但本次資料沒有 daily Trending 計數，應解讀為持續基礎設施訊號而非單日爆發。
- **風險：** Apache-2.0，但 14,105 個 open issues 是極高的維護/需求訊號；版本快速變動，教學指令與 extension 行為需要鎖版本。
- **Adam 關聯：** 是本 workspace skill、dashboard 與 AI office automation 的核心執行環境參考；可用於課程的 agent safety、repo-aware automation 與交付流程。

### 7. [anthropics/claude-code](https://github.com/anthropics/claude-code) — Demo content

- **用途：** 具備 codebase 理解、例行任務、說明與 Git workflow 的 agentic coding tool，橫跨 terminal、IDE 與 GitHub。
- **動能：** 143,174 stars；stars delta +104、fork delta +13；08-26 push，最新 v2.1.247（08-26）。總量與更新頻率高，但本日成長不如 Skills/知識工具。
- **風險：** GitHub repo 未標示 license；15,167 個 open issues；官方產品變動快且有服務/帳號依賴，課程 demo 必須準備替代路徑。
- **Adam 關聯：** 適合示範「自然語言→檔案修改→測試→Git」及 Claude Code skills，並與 Codex 做實際工作流比較；不應把 GitHub stars 當成商業需求證明。

### 8. [n8n-io/n8n](https://github.com/n8n-io/n8n) — Deep research

- **用途：** 可 self-host 或 cloud 的 AI-native workflow automation，結合 visual canvas、custom code、MCP 與大量整合。
- **動能：** 202,607 stars；stars delta +108、fork delta +21；08-27 push，最新 n8n@2.36.7（08-25）。成長穩定、更新當日且生態成熟，適合從「工具熱度」轉成可執行的辦公自動化。
- **風險：** README 標示 fair-code，API/雲端/整合服務及授權邊界要先審核；1,091 個 open issues，self-host 的升級與 secrets 管理不可忽略。
- **Adam 關聯：** 最適合做 AI office automation 主線：表單/Email/CRM/wiki/MCP 的事件驅動流程，並示範 human approval、錯誤重試與稽核紀錄。

### 9. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — Reference only

- **用途：** MCP 的 reference server 實作與生態資源，協助理解 MCP features、SDK usage 與 server/client 邊界。
- **動能：** 89,909 stars；stars delta +27、fork delta +6；08-27 更新，最新 release 2026.8.18（08-18）。成長不如應用型 repo，但作為協定基準仍有長期價值。
- **風險：** license 欄位為 `NOASSERTION`；README 明確提醒這是 reference implementations，不應直接當成完整 server marketplace；550 個 open issues。
- **Adam 關聯：** 適合支撐 MCP 課程、Metabiz wiki 的協定/安全章節與 AI office automation 的 tool boundary 設計；採用前要逐一檢查 server 的權限與資料外送。

### 10. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — Watch

- **用途：** 跨 session 捕捉 agent 行為、以 AI 壓縮並注入相關上下文，支援 Claude Code、Codex、Gemini、Hermes 等多個 agent。
- **動能：** 今日首次觀察；92,121 stars、Trending +133；08-26 push，最新 v13.16.1（08-26）。因無前次快照，不能把總量誤讀成今日增長。
- **風險：** Apache-2.0，但 311 個 open issues；記憶資料的隱私、保留期限、embedding/SQLite 內容與 prompt injection 面積都需安全審查。
- **Adam 關聯：** 值得觀察是否能補強 know metabiz wiki 與 agent handoff，但先以隔離 demo 驗證可刪除性、來源標記與敏感資料遮罩，不直接放入生產知識庫。

## 明日 watchlist

1. **確認 Archify、claude-obsidian 的第二日 stars 與 fork delta**：若仍維持高相對增長，優先做最小可重現 demo。
2. **追蹤首次出現的 `thedotmack/claude-mem` 與 `JetBrains/go-modern-guidelines`**：補齊第二個快照後再評估是趨勢或一次性曝光。
3. **比較 Graphify、claude-obsidian、claude-mem 的知識/記憶邊界**：記錄資料來源、可追溯性、刪除與本地化能力。
4. **觀察 Skills 生態**：`mattpocock/skills`、`obra/superpowers`、`ComposioHQ/awesome-claude-skills` 與本 workspace skills 是否出現共同 convention 或 breaking change。
5. **檢查 Codex/Claude Code/n8n/MCP 的 release 與 issue 信號**：只把穩定、可驗證且權限邊界清楚的流程納入課程與 AI office automation。
6. **持續排除 false positives**：高 stars 但 license 不清、issue 過多、README 缺少安裝/限制說明或依賴未鎖定的 repo，先列 Watch/Reference only。

## 資料與限制

- Collector 使用指定 10 組 query、`--limit 10`、GitHub Trending daily、README 與 2026-08-27 目標輸出目錄；collector 在 2026-08-28 建立當日快照，因此「今日」欄位指快照觀察日，不等同市場需求。
- 本次未發生 GitHub API rate-limit；過程中有少數候選 repo 回傳 404，collector 依規則保留既有 metadata，未將其列入重點分析。
- Stars 是開發者注意力訊號，不是買方意願；任何採用建議仍需另外做 license、資安、成本與維運驗證。
