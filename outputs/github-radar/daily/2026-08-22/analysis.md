# GitHub AI Trend Radar 分析 — 2026-08-22

## 摘要

- 本次以 10 組 AI/MCP/Skills/Agent/RAG/知識庫/開發自動化查詢，加上 GitHub Trending Daily 取得 192 個累積候選；即時蒐集時間為台灣 2026-08-23，故 Trending 是執行時的注意力訊號，不能倒推成 8/22 的歷史日榜。
- 前一日（`2026-08-21`）只留下不完整快照，無法作為可靠基線；本輪 `stars_delta=0` 不代表沒有成長，而是「快照差異未量得」。排名改以 Trending 今日 stars、近期更新、README 用途、授權與 issue 負荷綜合判斷，未以總 stars 排序。
- 6 個首次觀測的 Trending 項目中，`openai/codex`（1,544 stars today）、`Wei-Shaw/sub2api`（278）、`n8n-io/n8n`（149）及 `anthropics/claude-code`（127）有明顯注意力；首次觀測一律標為成長未量測，不顯示為 `+0`。

## 最值得追的專案

| 分類 | 專案 | 用途與動能 | 規模與維護訊號 | 風險／建議 |
| --- | --- | --- | --- | --- |
| Deep research | [openai/codex](https://github.com/openai/codex) | 終端 coding agent；首次 Trending 1,544/day，是本輪最強開發者注意力訊號。 | 114,104 stars、Apache-2.0、8/23 更新、13,502 issues。 | 首次觀測、成長未量測；先做本機工作流與權限邊界比較，不以 issues 數量推論品質。 |
| Skill candidate | [mattpocock/skills](https://github.com/mattpocock/skills) | 可重用工程技能集合，Trending 2,683/day；適合作為課程中「技能包怎樣可驗證」的對照素材。 | 232,629 stars、MIT、8/23 更新、385 issues。 | 總 stars 高不等於可直接採用；抽取一個小技能，檢查相依、授權與可重現性。 |
| Deep research | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Agent harness 的效能、記憶、安全與 research-first 方法；Trending 411/day。 | 242,266 stars、MIT、8/23 更新、148 issues。 | 方法論宣稱須以自己的 benchmark 驗證；先讀 README 的量測條件。 |
| Demo content | [obra/superpowers](https://github.com/obra/superpowers) | Agentic skills 與開發方法論；Trending 592/day，適合做「skill vs. instructions」實作展示。 | 276,338 stars、MIT、8/23 更新、308 issues。 | 作為教學範例，不直接視為企業流程標準；測試與既有 AGENTS/RTK 規範相容性。 |
| Watch | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | 多家訂閱模型的統一中轉；首次 Trending 278/day。 | 38,873 stars、LGPL-3.0、8/23 更新、2,809 issues。 | 涉及帳號、金鑰、共享與用量資料；不接入 metabiz 或客戶帳號，需先做資安、條款與授權審查。 |
| Demo content | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 可視化自動化與 AI 工作流；首次 Trending 149/day，適合辦公室自動化 demo。 | 201,938 stars、fair-code（API 顯示 NOASSERTION）、8/23 更新、1,069 issues。 | 自架與雲端的資料留存、credential 管理與商業授權要分開評估。 |
| Reference only | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Agentic coding CLI；首次 Trending 127/day，可作為 Codex/Claude Code/Cursor 課程比較基線。 | 142,643 stars、授權未明示、8/23 更新、15,105 issues。 | 不將高注意力等同採用；需逐項比較模型成本、資料處理和團隊治理。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 把 code、文件、SQL、設定與 PDF 建成本地可查詢圖譜，直接對應 know metabiz wiki 的程式脈絡需求。 | 109,636 stars、Apache-2.0、8/23 更新、1,047 issues。 | 先用非敏感 sample repo 驗證圖譜品質與索引成本；不將客戶 PDF 直接送入未審核環境。 |
| Skill candidate | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | 跨 coding agent 的長期記憶與交接；與 Codex 任務交接和課程示範相關。 | 4,135 stars、MIT、8/23 更新、7 issues。 | 需確認記憶落地位置、刪除機制與敏感資料排除；先做一次性、可刪除的 POC。 |
| Watch | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 將 Agent memory、RAG 與 skills 合成 Context Database，契合企業知識庫研究。 | 32,182 stars、AGPL-3.0、8/23 更新、493 issues。 | AGPL 對企業整合的散布義務需法務確認；先做隔離評估，不納入生產。 |

## 對 Adam 的可用行動

- **課程／內容：** 做一支「技能檔不是提示詞：Codex、Claude Code、superpowers 與 Matt Pocock skills 的驗收差異」短 demo；將 `openai/codex` 的首次 Trending 訊號當開場，而非效果承諾。
- **AI 辦公室自動化：** 用 n8n 的非機密 sandbox 演示「表單 → 人工核准 → 摘要 → 歸檔」；不得匯入真實 mCRM 身分資料或 token。
- **know metabiz wiki：** 對 Graphify 與 OpenViking 建立一次性隔離 POC：選 1 個公開 repo + 10 份可公開 Markdown，量測檢索可追溯性、更新成本及權限模型，再決定是否深入。
- **Skill backlog：** 將 ai-memory 的「交接摘要／下一步／驗證證據」概念改寫成內部技能草案，資料只存本機明確指定目錄並保留清除路徑。

## 明日追蹤清單

1. 確認下一輪能產生完整基線，恢復 `stars_delta` 與相對成長排名；本輪不可用 0 作為成長結論。
2. 追 `openai/codex`、`mattpocock/skills`、ECC、superpowers 的 release、README 變更與 issue/PR 活躍度。
3. 檢查 sub2api、n8n、OpenViking 的授權、資料處理與部署邊界；未完成前維持 Watch。
4. 用公開資料完成 Graphify/ai-memory 的小型 POC，記錄可重現指令、索引時間、結果可追溯性與刪除驗證。

## 資料界線

來源為 GitHub API 與執行時 Trending Daily；stars 是開發者注意力，不是市場需求、營收、資安合規或採購可行性的證明。詳細原始資料見同目錄的 `repos.json`、`report.md` 與 `snapshots/`。
