# GitHub AI Trend Radar 分析（2026-08-26）

## 今日結論

本次收集 212 個候選 repository；以今日 Trending、snapshot 的 star delta、相對成長、最近 push/release、README 可操作性，以及 issue 活躍度綜合判斷。最值得 Adam 深入的是「可攜式 Agent Skills」、「Claude/Codex coding agent 工作流」與「可擁有的 AI wiki / knowledge graph」。總 stars 只作背景，不作唯一排名依據。

## 值得追蹤的 repos

### 1. [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Deep research

- **目的：** 以 Claude Code + Obsidian 建立可擁有的 AI second brain；把來源整理成連結的 Markdown 知識圖譜，並支援 grounded retrieval。
- **動能：** 13,220 stars；snapshot +759、今日 Trending +812；2026-08-26 push，前一日發布 v2.1.1。136 open issues 顯示需求與維護負擔都不低。
- **風險：** MIT，但 Obsidian/Claude Code 整合、模型成本與 vault migration 仍需實測；issue 數偏高。
- **對 Adam 的價值：** 與 know metabiz wiki、課程研究資料庫、個人知識管理高度重疊。可做「來源 → 原子筆記 → wiki 問答」示範。

### 2. [mattpocock/skills](https://github.com/mattpocock/skills) — Skill candidate

- **目的：** 分享日常工程工作的 Agent Skills，讓 coding agent 依可重用的流程執行真實工程任務。
- **動能：** 237,677 stars；snapshot +1,284、forks +100；2026-08-26 更新，最近 release 為 v1.2.3。412 issues 與 20,226 forks 反映強烈採用與討論。
- **風險：** MIT；技能品質、適用的 agent runtime 與版本相容性需逐項驗證，不能直接全量套用。
- **對 Adam 的價值：** 最適合拆解成「AI office automation skill design」課程案例，並比較哪些重複工作值得沉澱成 metabiz 專用 skill。

### 3. [openai/codex](https://github.com/openai/codex) — Deep research

- **目的：** 在終端機本機執行的 coding agent，亦可連接 IDE 與桌面使用情境。
- **動能：** 118,704 stars；snapshot +767、forks +116；2026-08-26 push，最近 release `rust-v0.149.1`。13,925 issues 是重要的治理與相容性訊號。
- **風險：** Apache-2.0，但產品/CLI 變動快；issue 量大，企業導入需鎖版本、限制權限並檢查資料邊界。
- **對 Adam 的價值：** 可作 Codex Skills、repo-aware automation、內部 wiki 維護的主教材，連接課程與 know metabiz 的實作場景。

### 4. [obra/superpowers](https://github.com/obra/superpowers) — Skill candidate

- **目的：** 以 composable skills 與明確開發方法論，規範 coding agent 的軟體開發流程。
- **動能：** 277,933 stars；snapshot +509、forks +52；2026-08-26 更新，README 涵蓋 Claude Code、Codex、Cursor 等多個 agent。318 issues，最近 release v6.3.0。
- **風險：** MIT；方法論可能與團隊既有 SOP 重疊，跨 agent 支援不代表每個整合都同樣成熟。
- **對 Adam 的價值：** 可做「把 AI 辦公室流程變成可審核 SOP」的課程模組，並作為 metabiz skills 的設計參考。

### 5. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Demo content

- **目的：** 將程式碼、文件、SQL schema、設定與 PDF 轉成可查詢 knowledge graph，提供 Claude Code、Cursor、Codex 等 `/graphify` skill。
- **動能：** 110,924 stars；snapshot +552、forks +38；2026-08-25 push 並發布 v0.9.50，README 清楚定位為 local、可解釋的 AST parsing。1,130 issues 需留意維護規模。
- **風險：** Apache-2.0；大型或異質 codebase 的解析完整性、圖譜更新成本與 issue backlog 應先用小型 repo 驗證。
- **對 Adam 的價值：** 很適合示範「把 metabiz wiki / 專案 repo 變成可問答的結構化知識」，也能比較 graph RAG 與 vector RAG。

### 6. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) — Reference only

- **目的：** 163 個科學研究 skills 與 100+ 資料庫整合，支援 Cursor、Claude Code、Codex 等 Agent Skills 標準。
- **動能：** 34,608 stars；本次首次進入 daily Trending，今日 +130；2026-08-26 更新，最近 release v2.64.0；僅 10 open issues。snapshot delta 尚無法計算，故今日動能可信度低於有歷史基線者。
- **風險：** MIT；README 的使用者數與技能效果需獨立驗證，醫療/生物內容不可直接當作專業結論。
- **對 Adam 的價值：** 作為「技能目錄、資料源與可驗證研究流程」的參考樣本；可移植其結構到課程研究與企業知識工作。

### 7. [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) — Watch

- **目的：** 面向 Claude Code、Cursor、Codex 的 production-oriented skills 集合，涵蓋 web design、knowledge retrieval、image generation 等。
- **動能：** 10,822 stars；首次進入 daily Trending，今日 +136；2026-08-26 更新但最近 push 為 2026-07-12，最新 release 亦在 2026-07-12。16 issues，需觀察是否為短期曝光。
- **風險：** MIT；近期 commit 與今日熱度不一致，技能的實際品質及長期維護尚未證明。
- **對 Adam 的價值：** 可作 skills taxonomy 與跨 agent 相容性比較，挑選其中 knowledge retrieval / content workflow 做小型 demo。

### 8. [53AI/53AIHub](https://github.com/53AI/53AIHub) — Watch

- **目的：** 企業 AI portal / knowledge base，管理知識、agents、prompts 與 AI tools，並串接 Coze、Dify、FastGPT、RAGFlow。
- **動能：** 4,634 stars；snapshot +2、forks 未增；2026-08-26 更新，最近 release v0.5.0。20 issues，但 license 欄位為 `NOASSERTION`。
- **風險：** 授權需直接審閱；雲端服務與本地部署的功能差異、中文生態依賴、整合維護成本都可能影響導入。
- **對 Adam 的價值：** 可用來比較 know metabiz wiki 與「企業 AI 入口」的產品邊界，適合做競品/架構研究，不宜直接採用。

### 9. [browser-use/browser-use](https://github.com/browser-use/browser-use) — Demo content

- **目的：** 讓 AI agent 以自然語言操作網站，將瀏覽器任務自動化。
- **動能：** 110,740 stars；首次進入 daily Trending，今日 +135；2026-08-26 push，最近 release 0.13.8。389 issues；snapshot delta 尚無基線。
- **風險：** MIT；網站 UI 變動、登入/個資、反自動化條款與錯誤操作是 office automation 的主要風險。
- **對 Adam 的價值：** 可做瀏覽器自動化 demo（資料查找、表單草稿、研究彙整），但必須加入人工確認、最小權限與敏感資料遮罩。

## 今日內容與課程切角

- 「AI wiki 的三種路線」：`claude-obsidian` 的檔案擁有權、`graphify` 的 knowledge graph、`53AIHub` 的企業入口。
- 「Skills 不是 prompt pack」：比較 `mattpocock/skills`、`obra/superpowers`、`garden-skills` 的目錄、觸發條件、驗證與版本治理。
- 「Codex / Claude Code 辦公室自動化」：以 `openai/codex` 搭配 repo-aware skill，示範研究、文件更新、wiki 同步與人審節點。
- 「可控的瀏覽器 agent」：以 `browser-use` 示範任務分解、dry run、權限邊界與失敗復原。

## 明日 watchlist

1. 追蹤 `claude-obsidian`、`mattpocock/skills`、`openai/codex`、`obra/superpowers` 的下一日 star delta、release 與 issue/PR 變化。
2. 確認今日新進 Trending 的 `garden-skills`、`scientific-agent-skills`、`browser-use` 是否有第二日持續性，而非單日曝光。
3. 審閱 `53AIHub` 的實際 license 與本地部署文件，再決定是否值得做 metabiz wiki 競品拆解。
4. 對 `graphify` 做一個小型 metabiz repo / 文件 corpus demo，記錄解析覆蓋率、更新成本、查詢品質與是否需要 vector store。
5. 檢查 Claude Code / Codex / Cursor skill 的安裝格式與相容性，整理成可重用的 metabiz skill 評估表。

## 判讀限制

本日 star delta 是相對上一份 snapshot 的 GitHub API 觀測值；`trending_stars_today` 僅對被 daily Trending 擷取到的 repo 有值。GitHub stars 代表開發者注意力，不等於課程購買意願、企業安全合規或 production readiness。
