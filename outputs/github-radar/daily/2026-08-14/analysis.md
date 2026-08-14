# GitHub AI 趨勢雷達分析｜2026-08-14

> 蒐集執行於台灣時間 2026-08-15 00:10；GitHub Trending daily 為執行時快照，不能回推為 8/14 的歷史榜單。`stars_delta` 是與 2026-08-14 快照相比，`trending_stars_today` 是當日 Trending 卡片顯示的新增 stars；兩者皆為注意力訊號，非商業需求證明。

本次累積候選池為 **169** 個專案，Daily Trending 新首次觀測到 **4** 個。排序先看 Daily Trending、快照增量、相對成長與 8/14 的推送／release 活躍度，再看 README 清晰度與可落地性，不按總 stars 排名。

## 最值得追蹤（依行動優先度）

| 分類 | 專案與動能 | 用途與對 metabiz 的可用性 | 風險／下一步 |
| --- | --- | --- | --- |
| Deep research | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — 16,777 stars，快照 +3,307，Trending +3,651，8/14 更新 | Claude Code 可產生 29 種 HTML/SVG 編輯式圖表；適合「AI 辦公室把流程／架構圖做成可編輯交付物」的 demo 與課程單元。 | MIT，但先實測中文標註、既有 metabiz 視覺規範與產出可讀性；不可把「無 Mermaid」當成品質保證。 |
| Deep research | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) — 7,377，+1,091，Trending +1,183，8/14 有推送，v0.6.5（8/11） | graph-native context／可追責 AI，直接對應 know metabiz wiki 的證據節點、來源關係與可追溯回答。 | MIT；先做小型本地 corpus 對照，評估 schema、查詢延遲與維運成本。 |
| Skill candidate | [mattpocock/skills](https://github.com/mattpocock/skills) — 217,285，+1,190，8/13 有推送，v1.2.3（8/6） | 工程 agent skill 的高注意力樣本；可萃取成 Adam 課程的「skill contract、驗證與限制」教材。 | MIT；不整包導入。先比對現有 Codex／RTK 規範，挑單一可驗證流程試用。 |
| Deep research | [stablyai/orca](https://github.com/stablyai/orca) — 45,483，+763，8/14 有推送，v1.4.182（8/13） | 固定 watchlist 的平行 coding-agent ADE；可研究多 agent 任務分派與訂閱模型的可移植邊界。 | MIT；先以隔離的非客戶 repo 試跑，驗證成本、工作樹衝突與審核節點，不能直接套入生產流程。 |
| Demo content | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) — 7,052，+718，Trending +769，8/14 有推送 | 整合 Claude Code、Codex、MCP、工具與共享記憶的 agent workspace；適合「AI 辦公室工作台」對照 demo。 | 授權標記 NOASSERTION；需先確認實際 license、資料權限、connector 安全與自架成本。 |
| Skill candidate | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) — 46,194，+706 | Obsidian CLI／Markdown／Bases／Canvas 的 agent skill，是 know metabiz wiki 操作層可借鏡的直接範例。 | MIT，但上游最後推送為 6/8；只取可攜的操作模式，先在複本 vault 做檔案寫入與連結回歸測試。 |
| Deep research | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) — 88,325，+433，Trending +474，8/14 有推送 | RAG 加 agent 的 context layer；可作為現有 LLM Wiki 的外部基準，評估 ingestion、檢索與引用 UX。 | Apache-2.0；體量與基礎設施成本高，先定義 20 份代表文件與答案引用完整率的 benchmark。 |
| Watch | [macro-inc/macro](https://github.com/macro-inc/macro) — 2,905，+432，Trending +435，8/14 有推送與 v2026.8.14.0 release | email/chat/docs/tasks/agents/CRM 共享記憶，產品定位與 mOfficeAI 相鄰；值得做工作流與資料模型研究。 | AGPL-3.0，非直接嵌入候選；追蹤其權限模型、CRM 深度與 self-hosting 限制。 |
| Watch | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) — 新觀測、10,200 stars，Trending +153，8/14 有推送，v1.2.3（8/11） | 可分享登入中的瀏覽器狀態給 Codex／Claude Code 的 browser automation；有明確 demo 潛力。 | MIT，但 session／cookie 與誤操作風險高；只在測試帳號與最小權限環境驗證。 |
| Reference only | [cursor/plugins](https://github.com/cursor/plugins) — 新觀測、2,755 stars，Trending +54，8/13 有推送 | 官方 plugin specification，可作為跨 agent 工具包裝與發佈介面的參考。 | license 欄位缺失；先讀規格，暫不依賴或轉用其資產。 |

## 可轉為內容與課程的題材

- **Deep research**：以 Semantica 與 RAGFlow 比較「知識庫能答」和「答案可追溯」；輸出一份來源／節點／引用完整率 benchmark，供 know metabiz wiki 決策。
- **Demo content**：用 diagram-design 將一個 mOfficeAI 審核流程生成為可編輯 SVG，示範從文字規格到交付圖，而不是只展示漂亮圖。
- **Skill candidate**：以 mattpocock/skills 與 kepano/obsidian-skills 為樣本，整理一個 metabiz skill 最小契約：輸入、權限、輸出、驗證、停止條件。
- **Watch**：Orca、holaOS、Macro、ego-lite 都是工作台／編排方向；先研究隔離與權限模型，不作為立即導入建議。
- **Reference only**：Cursor plugins 與新進的 [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent)（Trending +171、快照成長未量測）可提供生態地圖，但前者 license 未標示、後者為清單型專案，均不應直接當技術選型。

## 明日追蹤清單

1. **diagram-design**：再看 Trending 是否持續、README／範例是否新增中文與商業流程使用情境。
2. **semantica**：追蹤 v0.6.5 後的 issue／release 反應，並決定是否建立 20 份文件的本地 benchmark。
3. **Orca 與 holaOS**：比較其平行 agent、工具授權與 human approval 邊界，避免把 demo 能力誤認為生產可控性。
4. **Obsidian skills**：在複本 vault 驗證檔案寫入、連結修復與可回復性，再決定是否抽取為 know metabiz wiki skill。
5. **新首次觀測項目**：ego-lite、ToolJet、Cursor plugins、awesome-deepseek-agent 的 `stars_delta` 均尚未量測；下一次出現才記錄真實增量，不能標成 `+0`。
