# GitHub AI Trend Radar 分析｜2026-07-30（台灣）

## 結論

今天最值得立刻投入的不是再新增一套 agent framework，而是把「可重複的 Codex/Claude Code 開發方法」與「可治理的 MCP / 知識檢索」接到 Adam 現有的課程、AI 辦公室自動化與 metabiz wiki。優先順序是：`ECC` / `superpowers` 的開發工作流、`googleapis/mcp-toolbox` 的受治理 MCP 資料連線、`claude-obsidian` 的可引用知識工作流。

本次指定 collector 在未提供 `GITHUB_TOKEN` 的狀態先遭 GitHub API 403 rate limit；已按規則降為每 query 5 筆，並於單次重跑時使用本機已登入 GitHub CLI 的短暫憑證。此輸出是第一個可用 baseline，因此 `stars_delta` 全為 0，不能把總 stars 當成今日成長；下列動能優先採 GitHub Trending 的「stars today」、2026-07-30 push/release 與 README/定位訊號。

GitHub Trending daily 的範圍相關項目：`book-to-skill`（+1,421 today）、`ECC`（+857）、`huggingface/speech-to-speech`（+827）、`obra/superpowers`（+616）、`alibaba/open-code-review`（+359）、`different-ai/openwork`（+97）。其中前三個 coding-agent / skill 相關訊號最強；語音代理另列為內容題材，不列入本日主要採用清單。

## 最值得追的 10 個 repo

| 分類 | Repo | 用途與動能 | 總 stars / 今日或近期訊號 | 風險與 Adam 可用性 |
| --- | --- | --- | --- | --- |
| Deep research | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Claude Code、Codex、Cursor 的 agent harness：skills、memory、安全、research-first。Trending +857；2026-07-27 發布 v2.1.0，7/29 有 push。 | 236,079；Trending +857 today | MIT、但 scope 很大，先萃取可移植規範。可作「多 agent 開發治理」課程與 AI 辦公室標準作業。 |
| Deep research | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | MCP 資料庫工具箱；7/28 發布 v1.8.0、7/30 仍更新。 | 16,077；241 open issues | Apache-2.0；需先評估資料庫權限、審計與 metabiz 生產資料隔離。最適合做受治理 MCP POC。 |
| Deep research | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 把 Obsidian 內容變成 Claude 可查證的工作脈絡；7/29 推 v2.0.0，重點是可靠性與 evidence。 | 10,120；7/29 v2.0.0 | MIT；先在 vault 副本測試，不能直接放行 iCloud 原始資料與寫回。對 know metabiz wiki 最直接。 |
| Demo content | [obra/superpowers](https://github.com/obra/superpowers) | Agentic skills 框架與軟體開發方法；Trending +616，7/24 v6.2.0。 | 263,832；Trending +616 today | MIT；方法論很吸睛但不可把 stars 當企業採用證據。適合「Skills 不只是 prompt」示範。 |
| Demo content | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 把技術書 PDF 轉為 Claude Code skill；Trending +1,421，今日所有範圍項中最高。 | 13,380；Trending +1,421 today | 需先檢查授權與 PDF 版權；適合做「資料不能直接變 skill」的反例與治理 demo。 |
| Skill candidate | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Claude Code agents/commands/skills 範本；7/30 有 push。 | 30,007；7/30 活躍 | MIT；模板品質與權限規則須逐一審。可萃取成 Adam 的內部 skill scaffold，不直接整包匯入。 |
| Skill candidate | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | deterministic pipeline 加 LLM code-review agent；Trending +359。 | 16,348；Trending +359 today | 使用第三方模型或服務前須確認程式碼外流與規則誤報。可形成「PR review before merge」課程 demo。 |
| Watch | [different-ai/openwork](https://github.com/different-ai/openwork) | Open-source Claude Cowork 替代品（opencode）；Trending +97。 | 18,283；Trending +97 today | 新興定位，尚未在本輪 collector 取到 release / issue 健康資料；先試用，不列入基礎設施選型。 |
| Watch | [labring/FastGPT](https://github.com/labring/FastGPT) | RAG / workflow 平台；7/30 發 v4.15.5、仍有 commit。 | 29,202；164 open issues | 非標準 SPDX 授權標記；需確認商用條款、中文文件與 multi-tenant 邊界。適合比較 RAG 管理介面，不先取代既有 wiki。 |
| Reference only | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP 官方 servers 與相容性基線；7/10 release、7/29 push。 | 89,055；479 open issues | 非 SPDX 授權標記且有大量 issue；作協定/範例參考，生產用連接器仍要獨立 security review。 |

## 對 Adam 工作的可用性

- 課程：做一條「Skills → agent harness → 有審計的 MCP」的實作課，而不是只教 repository 安裝。ECC、superpowers、claude-code-templates 各取一個小任務對照即可。
- Content / Deep research：`book-to-skill` 的今日暴增很適合短內容鉤子；核心觀點是「PDF 轉 skill 的真正門檻是權利、來源、版本與評估，不是轉換速度」。
- AI 辦公室自動化：優先用 `mcp-toolbox` 研究資料存取 allowlist、read-only role、audit log；未通過前不連 ERP、Odoo 或客戶資料。
- know metabiz wiki：先做 `claude-obsidian` 的隔離 POC，要求答案附檔案/段落出處、只讀索引與人工核對，再考慮寫回或 agent 自動化。

## 明日追蹤清單

1. 以同一輸出目錄重新 collector，取得第一個實際 `stars_delta`；把 0 delta baseline 從排名信號中移除。
2. 對 ECC、superpowers、claude-obsidian 各跑一個 30 分鐘隔離 demo，記錄安裝時間、權限、可重現性與引用品質。
3. 補查 `openwork` 的 license、最新 release、issue/PR response；未補齊前維持 Watch。
4. 對 mcp-toolbox 建立「read-only + synthetic database」測試，先驗證 access control、logging 與撤銷流程。
5. 保留 GitHub Trending daily 的 stars-today 作獨立欄位；不要和 collector 的跨快照 star delta 混算。

## 資料與限制

- Collector：44 個去重後 repo；查詢結果在 [repos.json](repos.json)，原始彙整在 [report.md](report.md)，快照在 [snapshots/](snapshots/)。
- 來源：2026-07-31 00:12–00:16 台灣時間取得的 GitHub REST metadata 與 GitHub Trending daily；Trending 是當時「Today」頁面，非可回溯的 2026-07-30 歷史快照，因此只作執行時動能參考。
- 本日未能以舊快照計出 valid `stars_delta`；所有「動能」都明確標成 Trending 今日 stars、push、release 或 issue 活躍訊號。
