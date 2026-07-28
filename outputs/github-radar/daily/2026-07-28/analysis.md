# GitHub AI Trend Radar 分析 — 2026-07-28

> 蒐集日為 2026-07-29（台灣時間），目標日為前一日 2026-07-28。以 authenticated GitHub API 完成十組指定查詢，納入 89 個去重候選；另查閱 GitHub Trending daily 頁面。GitHub 未提供本地可回溯的 7/28 Trending `stars today` 快照，因此不能把本報告當作歷史 Trending 排名。此輪各 repo 的 `stars_delta=0` 是新輸出資料夾尚無前次可比基線，**不代表沒有成長**；排序改以 7/28 push／release、維護訊號、README 定位與 Adam 場景適配性判斷。

## 結論

最值得做下一步驗證的是三條路徑：

1. **可稽核的知識與程式碼脈絡**：`Graphify` 和 `claude-obsidian` 都接近「資料仍由自己持有、可解釋的檢索／連結」，但前者較適合 codebase，後者較適合 Markdown vault。
2. **可替換的 agent runtime**：`pi`、`mcp-toolbox` 與 `headroom` 可分別研究 runtime、資料工具橋接與上下文成本控制；先在隔離 POC 驗證，不能直接接上正式 wiki 或客戶資料。
3. **Skill 的工程化，而非清單化**：`agent-skills`、`superpowers` 與 `learn-claude-code` 有很好的教材／方法論訊號；僅萃取可測試的 I/O、權限與驗收模式，不批次安裝外部 skills。

## 值得追蹤的 repo

| Repo | 分類 | 用途與動能 | 總 stars／風險 |
| --- | --- | --- | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 7/28 push 且發布 `v0.9.29`；把程式、文件、SQL、設定與 PDF 做成可解釋的圖譜，正好可比較 Metabiz AI Workspace 的 grounded retrieval。 | 97,577；Apache-2.0，但 676 open issues。先以只讀的小型 repo 驗證索引正確性與資源成本。 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Deep research | 7/28 push、`v1.8.0` release；是可治理的資料庫／MCP 工具層候選，適合研究 connector 權限與 query audit。 | 16,040；Apache-2.0，249 open issues。禁止以正式資料庫帳號作首輪 POC。 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Skill candidate | 7/28 push；主張在工具輸出、log、檔案與 RAG chunk 送入模型前壓縮，能成為「證據先保留、上下文再裁切」的 Codex skill 評估題。 | 62,911；Apache-2.0，579 open issues。節省 token 的宣稱須以自己的任務集量測，不能只採 README 數字。 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Demo content | 7/28 push，近期 `v0.82.1`；統一 LLM API 與 agent loop，適合演示「runtime 可替換、工作流與證據需持久化」的架構。 | 79,569；MIT，91 open issues。先做 fresh-temp 的單任務 smoke test，勿和既有 Pi Web wiki plugin 混為同一實作。 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Skill candidate | 近期 `0.6.5` release；production-oriented skills 是把課程的 prompt 提升為可驗收工作包的好範本。 | 80,742；MIT，128 open issues。外部 skill 仍要逐一審查 permission、輸入輸出、測試與撤回條件。 |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Deep research | Markdown-first 的 ingest、link、file 工作流最貼近 know metabiz wiki；release/最後 push 為 5/28，故列深研而不是趨勢採用。 | 10,044；MIT，113 open issues。只可用非敏感 vault 複製品且禁止自動寫回正式 wiki。 |
| [langgenius/dify](https://github.com/langgenius/dify) | Watch | 7/28 push 並發布 `1.16.1`；RAG／agent workflow 的產品成熟度可作企業入口與治理邊界比較。 | 150,563；`NOASSERTION`，964 open issues。先釐清授權、隔離、connector 與 audit，不能直接進客戶交付鏈。 |
| [obra/superpowers](https://github.com/obra/superpowers) | Reference only | 高星、近期 `v6.2.0`，能作「agent 開發方法論」課程對照素材。 | 262,563；MIT，327 open issues。總星數不是可採用性；選擇性抽取流程，不把框架視為內部標準。 |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Demo content | 7/28 push，從零打造類 Claude Code harness，適合拆成 agent loop、shell 安全與驗收證據的教學片段。 | 72,492；MIT，65 open issues。學習性專案不等於 production runtime，避免以 demo 直接承載商業流程。 |

## 對 Adam 的可用行動

### 課程與內容

- 做「Skill 是可驗收操作契約，不是 prompt」單元：以 `agent-skills`／`superpowers` 對照同一任務的權限、輸入、測試、輸出證據與 rollback。
- 做「AI 知識庫兩種主張」內容：`claude-obsidian` 的 Markdown-first 對 `Graphify` 的 graph-first，聚焦資料主權、可追溯來源和寫回風險。
- 做一支「MCP 不等於開放資料庫」demo：用無敏感資料的 `mcp-toolbox` POC 展示 allowlist、唯讀帳號與 query audit。

### AI 辦公室自動化與 know metabiz wiki

- 先把 `headroom` 做成一個只讀評測：固定 10 個 wiki／程式問答，比較壓縮前後的引用完整度、token、延遲與錯答率。
- 若研究 `pi`，維持 LLM Wiki 既有的 **Governed** 預設檢索、明確的 **All Evidence** 選項與 append-only audit；runtime 可換，知識和權限模型不可退化。
- `Dify` 僅作非敏感 sandbox 比較；在未完成授權與資料保留審查前，不開 wiki 寫入、不掛客戶 connector。

## 風險與假陽性

- `stars_delta=0` 僅表示 2026-07-28 目錄沒有前一輪基線；下一次應重用相同 daily 與 snapshot 策略，才可得到可比較 delta。
- GitHub Trending daily 是當日動態頁，這次無 7/28 的可回溯 `stars today` 證據；本報告明確不補造數字。
- `0x4m4/hexstrike-ai` 是 offensive security MCP 自動化，雖在範圍內但不列入採用／課程候選；只能當權限和安全治理的反例。
- 清單型 repo（awesome lists、skills collections）只提供 discovery，不能當安全性、維護性或商業授權的背書。

## 明日追蹤清單

1. `Graphify`：`v0.9.29` 在隔離 repo 的圖譜正確性、索引時間與查詢證據。
2. `mcp-toolbox`：`v1.8.0` 的 read-only connector、權限範圍與 audit 行為。
3. `headroom`：固定題組的 token／引用完整度基準，不採納 README 宣稱作結論。
4. `claude-obsidian`：隔離 vault 的 ingest／link 是否可重現，以及 5/28 後維護是否恢復。
5. `Dify`：授權聲明、release 後 issue 壓力與企業資料隔離條件。

## 資料產物

- [Collector 快照](./repos.json)
- [Collector report](./report.md)
- [Snapshot 目錄](./snapshots/)
