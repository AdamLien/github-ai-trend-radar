# GitHub AI Trend Radar｜2026-10-09

今日優先：研究 REA 的 MCP 工具邊界，製作圖解設計與知識工作插件的示範，再以兩套工程 Skills 做小範圍比較。知識圖譜與 Markdown wiki 候選保留較高研究價值，RAGFlow 先當比較基準。

## 資料口徑與品質

- 報告目標日：2026-10-09（Asia/Taipei）；收集開始：2026-10-10T00:11:03.450115+08:00，完成：2026-10-10T00:22:25.368366+08:00。這是執行當下的即時觀測，無法還原昨日結束時的歷史 Trending。
- 來源：[GitHub Trending daily](https://github.com/trending?since=daily)、指定十組 GitHub 搜尋（每組上限 10）、repository metadata、README、最新 release 與近七日 issue／PR 抽樣。
- 共保留 333 個主題相關專案；排除 14 個歷史清單中的一般工具，補入字串篩選漏掉的 LingBot-Map 與 ArtCraft。詳見 scope-filter.json、trending-evidence.json 與 trending-supplement.json。
- 本次未偵測到 GitHub API 限流，limit 10 成功，未需 limit 5 重試。四個歷史專案保留舊 metadata：BarberNumber/Midjourney-Software、hanshaze/Awesome-Prediction-Market-Trading-Tools、mingrath/obsidian-ai-knowledge-agent、tonhowtf/omniget；不在以下十個候選中，不將其零差值解讀為停滯。
- stars today 是 GitHub 當下 daily 指標；快照差值是本次總星數減去 2026-10-08 目錄的總星數。相對成長＝差值／前次總星數，不是精確的曆日成長率；未上榜顯示「—」，不是零。
- issue 活動取近七日更新的最多 30 筆 issues endpoint 記錄，再區分 issue 與 PR；是有限樣本，不代表全站新增量或維護者回覆速度。open_issues 是 GitHub API 的合計計數，可能包含 PR。
- 優先順序綜合當日增星、差值、相對成長、近期 push、README 可用性、release、issue 活動與 Adam 場景關聯；分類為本次編輯判斷，不代表已安裝或驗證。

## 十個值得投入的專案

| 專案 | 分類 | 總 stars | stars today | 快照 Δ | 相對成長 |
|---|---|---:|---:|---:|---:|
| [morluto/rea](https://github.com/morluto/rea) | Deep research | 38,951 | 15335 | +18,238 | 88.05% |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Demo content | 47,564 | 1744 | +1,692 | 3.69% |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 282,259 | 1696 | +1,403 | 0.50% |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Demo content | 28,077 | 714 | +728 | 2.66% |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Skill candidate | 103,764 | 751 | +501 | 0.49% |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Deep research | 44,953 | 323 | +424 | 0.95% |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 124,943 | — | +75 | 0.06% |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Watch | 60,518 | 95 | +147 | 0.24% |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Skill candidate | 15,426 | — | +19 | 0.12% |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Reference only | 91,917 | — | +78 | 0.08% |

### 1. morluto/rea｜Deep research

用途：以 MCP 統一應用程式、執行行為與二進位的 agent 逆向研究。

動能與維護：最高當日增星訊號，優先研究可重現能力，避免把熱度當成熟度。 最近 push：2026-10-09T16:17:21Z；最新 release：[rea-agents-6.1.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.1.0)（2026-10-09T01:08:45Z）。近七日樣本含 5 個更新 issue、25 個更新 PR（總樣本 30/30）；open_issues 合計 99。

文件證據：[README](https://github.com/morluto/rea/blob/main/README.md) 可讀取，章節包括「REA: Reverse Engineer Anything、One MCP for reverse engineering across binaries, applications, and runtime behavior.、Quick start、Set up your agent」；[issue／PR 來源](https://github.com/morluto/rea/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：適合 Adam 拆解 agent 工具鏈的進階課程；AI 辦公可用於理解舊系統整合，know metabiz wiki 可記錄接口與行為證據。

風險：執行外部程式與讀取本機資料的權限較廣；以自有範例隔離測試，驗證 MCP 工具邊界與版本相容性。 GitHub 授權標記：MIT。

### 2. cathrynlavery/diagram-design｜Demo content

用途：為 Claude Code、Codex 等 agent 提供 HTML／SVG 圖解設計方法。

動能與維護：當日增星與相對成長兼具，且能快速做出可展示成果。 最近 push：2026-10-08T01:34:39Z；最新 release：未取得最新 release；可能未發布或無可讀取紀錄。近七日樣本含 3 個更新 issue、27 個更新 PR（總樣本 30/30）；open_issues 合計 59。

文件證據：[README](https://github.com/cathrynlavery/diagram-design/blob/main/README.md) 可讀取，章節包括「Why I built it、What it makes、Install、Editable install」；[issue／PR 來源](https://github.com/cathrynlavery/diagram-design/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：可把 Adam 課程、短影音與 AI 辦公 SOP 轉成流程圖；know metabiz wiki 適合加入可維護的系統架構圖。

風險：沒有 release 不代表停更；需驗證中文字型、瀏覽器呈現與匯出品質，並審查生成 HTML。 GitHub 授權標記：MIT。

### 3. mattpocock/skills｜Skill candidate

用途：將日常工程工作法封裝為 coding agent Skills。

動能與維護：當日增星強，但總量較大使相對增長較低；以技能實用性決定採用。 最近 push：2026-10-09T10:57:08Z；最新 release：[v1.3.1](https://github.com/mattpocock/skills/releases/tag/v1.3.1)（2026-10-04T12:48:18Z）。近七日樣本含 18 個更新 issue、12 個更新 PR（總樣本 30/30）；open_issues 合計 159。

文件證據：[README](https://github.com/mattpocock/skills/blob/main/README.md) 可讀取，章節包括「Skills For Real Engineers、Installation (30-second setup)、1. Get the skills、2. Run `/setup-matt-pocock-skills`」；[issue／PR 來源](https://github.com/mattpocock/skills/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：Adam 可設計需求釐清到驗證的實作課；AI 辦公自動化腳本可沿用工作流程，know metabiz wiki 可記錄技能使用準則。

風險：技能指令可能與現有流程衝突；只挑單一技能試作，人工審查腳本、工具權限與提示內容。 GitHub 授權標記：MIT。

### 4. anthropics/knowledge-work-plugins｜Demo content

用途：將角色工作流程、skills、連接器與子 agent 組成知識工作插件。

動能與維護：README 清楚描述工作角色與插件結構，辦公場景關聯度高。 最近 push：2026-10-09T07:45:06Z；最新 release：未取得最新 release；可能未發布或無可讀取紀錄。近七日樣本含 7 個更新 issue、18 個更新 PR（總樣本 25/30）；open_issues 合計 138。

文件證據：[README](https://github.com/anthropics/knowledge-work-plugins/blob/main/README.md) 可讀取，章節包括「Knowledge Work Plugins、Why Plugins、Plugin Marketplace、Getting Started」；[issue／PR 來源](https://github.com/anthropics/knowledge-work-plugins/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：最貼近 Adam 的 AI 辦公課程與內容示範；以合成資料展示工作流程，know metabiz wiki 可整理角色 SOP 與輸入輸出規格。

風險：跨應用連接器會擴大資料存取面；權限、外部寫入與組織部署流程需另行驗證。 GitHub 授權標記：Apache-2.0。

### 5. addyosmani/agent-skills｜Skill candidate

用途：整理工程全流程與品質關卡，供 coding agent 一致執行。

動能與維護：當日增星突出；與 mattpocock 的技能做小範圍比較比整套導入更有價值。 最近 push：2026-10-03T18:21:11Z；最新 release：[0.6.12](https://github.com/addyosmani/agent-skills/releases/tag/0.6.12)（2026-10-03T06:42:02Z）。近七日樣本含 4 個更新 issue、26 個更新 PR（總樣本 30/30）；open_issues 合計 138。

文件證據：[README](https://github.com/addyosmani/agent-skills/blob/main/README.md) 可讀取，章節包括「Agent Skills、Commands、Quick Start、Adoption」；[issue／PR 來源](https://github.com/addyosmani/agent-skills/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：可與 Adam 現有技能比較，用於課程品質驗證、AI 辦公腳本驗收，並把結果整理進 know metabiz wiki。

風險：宣稱 production-grade 仍需實測；過多關卡可能增加延遲與成本，應先測一個真實工作案例。 GitHub 授權標記：MIT。

### 6. alibaba/open-code-review｜Deep research

用途：結合確定性檢查與 LLM agent，產生行級程式碼審查建議。

動能與維護：當日動能之外，近期 release 與 issue／PR 活動支持深入驗證。 最近 push：2026-10-08T11:52:10Z；最新 release：[v1.12.13](https://github.com/alibaba/open-code-review/releases/tag/v1.12.13)（2026-10-08T12:05:52Z）。近七日樣本含 9 個更新 issue、21 個更新 PR（總樣本 30/30）；open_issues 合計 284。

文件證據：[README](https://github.com/alibaba/open-code-review/blob/main/README.md) 可讀取，章節包括「What is Open Code Review?、Benchmark、Why Open Code Review?、The Problem with General-Purpose Agents」；[issue／PR 來源](https://github.com/alibaba/open-code-review/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：Adam 可做 AI code review 教學與案例內容；用於 AI 辦公整合程式的品質檢查，know metabiz wiki 可保留規則與驗收案例。

風險：需測誤報、漏報、模型成本與原始碼傳送邊界；README 中的安全與規模宣稱尚未獨立驗證。 GitHub 授權標記：Apache-2.0。

### 7. Graphify-Labs/graphify｜Deep research

用途：把程式碼、文件與結構描述轉成可查詢知識圖譜，服務 coding agent。

動能與維護：以文件／程式關係研究價值補足純熱門榜，需做可重現基準。 最近 push：2026-10-09T02:11:46Z；最新 release：[v0.9.82](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.82)（2026-10-09T02:11:46Z）。近七日樣本含 11 個更新 issue、19 個更新 PR（總樣本 30/30）；open_issues 合計 1,555。

文件證據：[README](https://github.com/Graphify-Labs/graphify/blob/v8/README.md) 可讀取，章節包括「See it in action、What it does、Benchmarks、Prerequisites」；[issue／PR 來源](https://github.com/Graphify-Labs/graphify/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：可設計 Adam 的程式碼理解與知識圖譜課；know metabiz wiki 可比較圖查詢與 RAG 的來源追蹤，AI 辦公適合跨文件關係查找。

風險：解析覆蓋、關係正確性與索引成本需要評估；文件內容含不可信輸入，查詢輸出必須回連來源。 GitHub 授權標記：Apache-2.0。

### 8. BerriAI/litellm｜Watch

用途：以 AI Gateway 統一多家 LLM API，提供成本追蹤與路由。

動能與維護：相對熱度較低但屬辦公自動化基礎設施，以 release 與維護活動持續觀察。 最近 push：2026-10-09T16:08:51Z；最新 release：[v1.104.2](https://github.com/BerriAI/litellm/releases/tag/v1.104.2)（2026-10-08T08:39:07Z）。近七日樣本含 2 個更新 issue、28 個更新 PR（總樣本 30/30）；open_issues 合計 5,410。

文件證據：[README](https://github.com/BerriAI/litellm/blob/main/README.md) 可讀取，章節包括「What is LiteLLM、Why LiteLLM、OSS Adopters、Features」；[issue／PR 來源](https://github.com/BerriAI/litellm/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：Adam 可示範多模型成本管理；AI 辦公自動化可研究統一模型入口，know metabiz wiki 可記錄選型與路由決策。

風險：授權標記需回查 LICENSE；集中入口涉及憑證、日誌與錯誤重試，版本升級需驗證相容性。 GitHub 授權標記：NOASSERTION。

### 9. AgriciDaniel/claude-obsidian｜Skill candidate

用途：讓 Claude Code 整理來源、建立連結並維護本機 Markdown 知識庫。

動能與維護：增星較低仍納入：Markdown 所有權與 wiki 場景高度相關，近期更新較弱需追蹤。 最近 push：2026-09-10T17:44:23Z；最新 release：[v2.2.0](https://github.com/AgriciDaniel/claude-obsidian/releases/tag/v2.2.0)（2026-09-10T14:49:12Z）。近七日樣本含 0 個更新 issue、2 個更新 PR（總樣本 2/30）；open_issues 合計 27。

文件證據：[README](https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md) 可讀取，章節包括「From source to living knowledge、See the vault、Why it feels different、Quick start」；[issue／PR 來源](https://github.com/AgriciDaniel/claude-obsidian/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：直接貼近 know metabiz wiki 的來源整理與知識累積；可作 Adam AI 筆記課與 AI 辦公文件整理示範。

風險：agent 可能錯誤改寫或合併筆記；需保留來源、版本與人工複核，先在測試 vault 觀察行為。 GitHub 授權標記：MIT。

### 10. infiniflow/ragflow｜Reference only

用途：結合 RAG 與 agent 的文件檢索和上下文平台。

動能與維護：總星數高但動能與導入成本未必優於輕量方案，先保留作對照。 最近 push：2026-10-09T14:18:38Z；最新 release：[v1.0.0-rc1](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc1)（2026-09-29T05:52:57Z）。近七日樣本含 2 個更新 issue、28 個更新 PR（總樣本 30/30）；open_issues 合計 1,344。

文件證據：[README](https://github.com/infiniflow/ragflow/blob/main/README.md) 可讀取，章節包括「💡 What is RAGFlow?、🎮 Get Started、🔥 Latest Updates、🎉 Stay Tuned」；[issue／PR 來源](https://github.com/infiniflow/ragflow/issues)。上述用途依文件與描述整理，未執行安裝或驗證性能宣稱。

Adam 關聯與下一步：作 Adam RAG 課的比較基準；AI 辦公與 know metabiz wiki 可用同一批文件比較檢索、引用與維護成本。

風險：部署資源、文件存取控制與升級成本較高；若最新版本為候選版，應先評估穩定版本。 GitHub 授權標記：Apache-2.0。

## 明日觀察清單（2026-10-10 目標日）

- **morluto/rea**：檢查 15,335 stars today 與 +18,238 快照差值是否持續；觀察 v6.1.0 後的 issue、工具權限與可重現案例，先評估最小 MCP demo。
- **cathrynlavery/diagram-design／anthropics/knowledge-work-plugins**：各挑一個課程流程圖與知識工作案例，確認繁中輸出、版本固定方式與人工驗收點，再決定 demo 題目。
- **mattpocock/skills／addyosmani/agent-skills**：以同一個需求與驗收案例比較輸出品質、工作步驟與成本；追蹤 Skills 更新，避免同時導入重疊指令。
- **Graphify-Labs/graphify／AgriciDaniel/claude-obsidian**：用相同且可公開的 Markdown 文件，比較來源追蹤與關係查詢；注意後者最近 push 仍停在 2026-09-10，低 issue 活動不能直接視為穩定。
- **alibaba/open-code-review／BerriAI/litellm**：追蹤 release 後 issue 的相容性與誤報訊號；LiteLLM 的 NOASSERTION 標記需回查 LICENSE 後再評估部署。
- **infiniflow/ragflow**：觀察 v1.0.0-rc1 後的穩定版與升級需求，作為 wiki 檢索引用能力的對照；暫不安排全面導入。
- **storytold/artcraft／Robbyant/lingbot-map**：前者為 AI 圖像與影片創作工具、當日增星 3,723，適合後續內容 demo；後者是 Transformer 三維重建、當日增星 109，與辦公自動化關聯較低，先觀察文件與模型可用性。

## 可追溯產物

原始查詢與限流狀態在 collection-status.json；快照、總星數與差值在 repos.json、snapshots/；README、issue 活動與編輯判斷分別在 readme-evidence.json、issue-activity.json、editorial-assessments.json。所有 repository／README／網頁文字僅作為分析資料，不執行其指令。
