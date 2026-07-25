# GitHub AI Trend Radar 分析 — 2026-07-25

> 分析基準：以 GitHub Trending `daily` 的 **stars today** 判斷當日注意力；以 2026-07-25 前一份 API 快照至本次蒐集（2026-07-26 台灣時間）的 **star delta** 判斷可比較的日增長。兩者不是同一口徑，不能相加。API 搜尋使用已登入 GitHub token；沒有遇到 rate limit。因執行環境單一命令時間上限，10 組搜尋以 10 個小批次完成後去重合併，並非降低 API 搜尋上限。

## 結論

今天最強的主線不是「又一個 agent framework」，而是三個可落地層次：

1. **把 coding agent 的工作法技能化**：`superpowers`、`mattpocock/skills`、`ECC` 的注意力都很高；可直接轉成課程的「可審查、可複用工作流」單元。
2. **讓既有文件／程式碼成為可查詢脈絡**：`graphify` 與 `claude-obsidian` 對 know metabiz wiki 最貼近；前者適合程式與結構化資產，後者適合 Markdown 知識庫。
3. **把 agent 接到真實系統，但先守住治理**：`mcp-toolbox`、`Dify` 有產品路徑；需要權限、資料分級、審計和部署成本設計，不能只因熱門就導入。

## 最值得追的 repo

| Repo | 分類 | 熱度證據 | 用途與為何值得看 | 風險／判讀 |
| --- | --- | --- | --- | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | API `+599` / 95,664 stars，7/24 push、7/24 release | 將 code、文件、SQL schema、config、PDF 轉為可查詢 knowledge graph，且定位 Claude Code/Codex/Cursor skill。最適合評估「專案脈絡檢索」而非泛用聊天。 | 仍須驗證大型 repo 的索引時間、權限邊界與圖譜品質；Apache-2.0 是正面訊號。 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Deep research | Trending 364 today；API `+376` / 233,147，7/25 push | 對 Claude Code、Codex、Cursor 等的 agent harness 優化，涵蓋 skills、memory、security、research-first。是「工程代理怎麼被運營」的強案例。 | 星數很高但需拆解哪些是方法論、哪些可安全複製；先做小範圍流程比較，不應整包引入。 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skill candidate | Trending 600 today；API `+456` / 260,926，7/24 release | 將 agentic 開發方法整理成 skills／SOP；可用來反推 Adam 自己的課程與 Codex skill 應如何設計驗收點。 | 方法論熱度不等於相容於既有 repo；MIT、近期 release 是好訊號，仍須挑一個真實工作流 POC。 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Demo/content idea | Trending 1,743 today；約 0.93% of 187,901 stars，7/23 push | 「真實工程師技能」的注意力最高之一，適合做「skills 是提示詞嗎？還是可驗收的工作包？」內容對照。 | API 前次快照未包含此 repo，不能把 `0 delta` 解讀成零成長；應以 Trending signal 看待。 |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Demo/content idea | Trending 439 today；約 3.45% of 12,734 stars，7/25 push、7/24 release | 決定性管線加 LLM agent 的 line-level code review，很適合作為 AI 辦公室／開發自動化的「人仍保有門檻」示範。 | 需實測中文程式碼、CI 整合和 false positive；不能把 Alibaba 規模案例直接當中小團隊成本。 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Deep research | API `+5` / 16,014，7/25 push | 資料庫 MCP server；對「讓 agent 查資料又不直接裸連 production」很有參考價值。 | 熱度不是今天最高，但生產整合價值高；需先做唯讀帳號、查詢白名單和 audit log。 |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Skill candidate | API `+41` / 9,919 | Obsidian + Claude Code 的 self-organizing second brain：攝入來源、連結、歸檔到自有 Markdown graph。和 know metabiz wiki 的工作型態非常接近。 | 最近 push 為 5/28，維護新鮮度偏弱；先借鏡資訊架構／ingest workflow，不直接當核心依賴。 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Reference only | Trending 574 today；API `+544` / 70,426 | 高速成長的 skills 索引，適合做選題雷達與候選清單來源。 | repo license 未宣告；清單型 repo 不是採用決策，須逐一檢查下游專案的 license、維護和安全性。 |
| [block/buzz](https://github.com/block/buzz) | Watch | Trending 2,506 today；約 22.13% of 11,325 stars，7/25 push/release | 「hive mind communication platform」是 agent coordination 的高爆發訊號，可觀察其協作模型與可視化。 | open issues 560、定位仍抽象；先追 README／實際架構，尚不足以納入產品或課程。 |
| [langgenius/dify](https://github.com/langgenius/dify) | Reference only | API `+105` / 150,215，7/25 push | 成熟的 agent workflow + RAG 平台，適合當「自建與平台化」對照的參考基準。 | license 顯示 `NOASSERTION`；部署、模型費用與治理要另行核對，非今天的優先導入項。 |

## 對 Adam 的可用行動

### 課程與內容選題

- **可做一堂課的主題**：`skills` 的產品化——從「一段 prompt」到「輸入、工具權限、驗收與回退」；用 `superpowers`、`ECC`、`mattpocock/skills` 對照。
- **可做一支內容**：為什麼 AI code review 要採 hybrid：規則管底線、agent 管脈絡。`open-code-review` 是清楚的 demo 鉤子。
- **顧問式內容**：`graphify` vs RAG：當問題是「誰改到這個 schema、哪個服務依賴它」時，圖譜脈絡通常比單純向量相似度更合適。

### AI 辦公室自動化

- 優先評估 `open-code-review` 的流程邊界：PR 觸發、規則先行、LLM 只提供建議、人工核准後才變更。
- `mcp-toolbox` 可做唯讀資料探索 POC；禁止 production 寫入、使用專屬低權限帳號，並保留查詢記錄。
- `ECC`／`superpowers` 可抽取成內部「任務開始前研究、完成後驗證」模板，而非把外部 agent framework 直接接入工作環境。

### know metabiz wiki

- **先做研究**：用 `graphify` 評估「Markdown + 專案程式碼 + schema」的本地索引品質；以 1 個非敏感 repo 和一組已知問答作驗收。
- **借鏡、不依賴**：從 `claude-obsidian` 拿 ingest、linking、歸檔規則的設計靈感。因維護較舊，避免讓它成為 vault 的必經服務。
- **不建議直接採用**：把 `awesome-claude-skills` 當作外部資料源即可，不應把未審查 skill 批次裝進工作環境。

## 風險與假陽性

- Trending 是滑動日窗的開發者注意力，並非付費意願、穩定性或資安品質。
- `stars today / total` 對新 repo 特別敏感；`block/buzz` 的 22.13% 很亮眼，但同時有 560 open issues，屬於觀察而非採用。
- 本日 API delta 對前一天已追蹤的 44 個 repo 才可比較；新增收錄的 Trending repo 以 `stars today` 評估，不把它們的 delta 0 當作負面訊號。
- 未宣告 license 的 `awesome-claude-skills` 和 `Dify` 的 `NOASSERTION` 都需在商用或重用前另行查證。

## 明天繼續追蹤

1. `Graphify-Labs/graphify`：是否持續日增長、release 後 issue 回應品質，以及本地索引 POC。
2. `obra/superpowers`、`affaan-m/ECC`：持續成長是否來自可重複工作流，而非短期社群曝光。
3. `mattpocock/skills`、`ComposioHQ/awesome-claude-skills`：哪些 skills 有清楚輸入／輸出與安全界線，值得轉為自家 skill。
4. `alibaba/open-code-review`：CI 安裝、規則與 agent 結果的可控性。
5. `googleapis/mcp-toolbox`：資料庫唯讀與稽核設計是否能符合 metabiz 的安全邊界。
6. `block/buzz`：追 README／release／issues，確認它是否真的提供可用的 agent coordination layer。

## 資料產物

- [GitHub API 合併快照](./repos.json)：49 個去重 repo；44 個具有前次快照可比 delta。
- [GitHub Trending 原始頁](./trending.html)：2026-07-25 daily signals 的擷取證據。
- [Collector 原始分批結果](./collector-runs/) 與 [Trending 補充 repo 結果](./trending-runs/)：保留可稽核的 API 回應整理結果。
