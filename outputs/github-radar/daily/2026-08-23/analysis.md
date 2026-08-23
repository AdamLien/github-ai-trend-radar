# GitHub AI Trend Radar 分析 — 2026-08-23（台灣）

> 蒐集執行於 2026-08-24（台灣），輸出歸檔為前一個台灣日期 `2026-08-23`。GitHub Trending daily 是執行時可取得的當日注意力訊號，不能倒推 8/23 的歷史榜單；`stars_delta` 則比較 8/23 與 8/24 的快照。共檢查 199 個 repo，且本次沒有 API rate-limit，維持每組 query `--limit 10`。

## 本日判讀

今日的核心不是單一 agent framework，而是三條可落地的線：**coding agent 的操作方法**（Codex、skills、ECC）、**知識轉成可重複使用上下文**（OpenViking、Claude Obsidian、book-to-skill），以及**有人審核的辦公室工作流自動化**（n8n）。排序綜合 Trending stars today、跨快照 star delta、近期 push/release、README 的實作邊界與 issue 負載；不是依總 stars 排名。

|優先|專案與分類|動能與維護訊號|用途與可用性|風險／下一步|
|---:|---|---|---|---|
|1|[openai/codex](https://github.com/openai/codex) — Deep research|2,729 Trending stars today、+816；8/23 有 push，8/20 release `0.149.0`|Adam 課程可用作 coding agent 實戰範例；AI 辦公室可做受控的資料蒐集、草稿與驗證工作流|13,547 open issues 不能單獨視作品質；先以現有 RTK、approval boundary 做小型真實任務回歸測試|
|2|[mattpocock/skills](https://github.com/mattpocock/skills) — Skill candidate|2,448 Trending stars today、+815；MIT、8/06 `v1.2.3`|適合作為課程的「skill 包裝與可驗收輸出」反例／範本來源，也可挑選文件與 TypeScript 工作流技巧|388 open issues；只萃取可驗證、無衝突的 skill pattern，勿覆蓋本機既有的 RTK／審核規則|
|3|[volcengine/OpenViking](https://github.com/volcengine/OpenViking) — Deep research|+191；8/23 push、8/21 `v0.4.16`|把 Agent Memory、RAG 與 Skills 納入同一 context database 的設計，最貼近 know metabiz wiki 的架構研究|AGPL-3.0、497 open issues；只做隔離 POC，不能直接混入含客戶資料的 production wiki|
|4|[virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) — Demo content／Skill candidate|423 Trending stars today、+184；MIT、22 open issues|可示範「原始 PDF/教材 → 有來源的 skill」；能加速課程講義與內部 SOP 的半自動整理|須先確認原始文件授權與 OCR/抽取正確性；輸出只能當草稿，需保留原檔和人工驗證|
|5|[affaan-m/ECC](https://github.com/affaan-m/ECC) — Deep research|427 Trending stars today、+158；MIT、7/27 `2.1.0`|其 harness、memory、security 與 research-first 主張適合做 Codex/Claude Code 操作法比較內容|149 open issues；採納前先與現行 team workflow 比對，避免引入其預設流程造成政策或責任邊界衝突|
|6|[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — Deep research|+105；MIT、7/31 `v2.1.0`|與 metabiz 既有 Obsidian vault 最直接相鄰：Markdown 所有權、來源攝取、連結與知識圖譜|8/01 後無 push、133 open issues；只研究資料模型與 ingestion pattern，勿把自動整理直接寫進主 vault|
|7|[n8n-io/n8n](https://github.com/n8n-io/n8n) — Demo content|+157；8/23 push、8/21 `2.35.7`|AI 辦公室流程編排與「自動草稿 → 人工核准 → 正式執行」視覺化教材候選|Fair-code／授權條件須逐案核對，且 1,071 open issues；不將 mCRM send/tag/coupon 等動作設為無人審核|
|8|[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — Watch|443 Trending stars today；首次觀測，成長未量測；MIT、8/21 release、8/23 push|可作為 agent 長期互動與自我改善的研究對象|34,998 open issues 是高風險訊號；僅閱讀架構與 demo，不納入課程主線或 production 評估|
|9|[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — Reference only|237 Trending stars today；首次觀測，成長未量測；MIT、僅 8 open issues|跨 Claude Code、Codex、Cursor 的技能目錄，可當採樣索引|它是 curated list，不是品質保證；任何引用 skill 都要回到原作者、授權與實際內容審查|
|10|[anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) — Reference only|190 Trending stars today；首次觀測，成長未量測；Apache-2.0、8/23 push|用於對照 plugin marketplace 的分發、metadata 與社群提交模式|README 明示為 read-only mirror；不可當成官方維護或安全審核的保證，僅作生態系研究|

## 對 Adam 的行動建議

### 課程

- 用 `book-to-skill` 做一堂「教材不是 prompt：原檔、來源片段、驗收測試、人工複核」的實作示範。
- 以 Codex、ECC、mattpocock/skills 做三方比較：agent 本體、操作方法、可攜 skill；避免把 stars 當學習成效或商業需求。

### Content／Demo

- 製作「一天 2,729 stars 的 Codex 要怎麼看」短內容：展示 Trending、+816 snapshot delta、release/push 與 issue 負載如何共同判讀。
- 製作 `OpenViking vs Claude Obsidian vs know metabiz wiki` 的資料所有權、授權、攝取與人工校對比較，不把 POC 宣稱為既有能力。

### AI 辦公室自動化

- 以 n8n 做一條低風險 prototype：Radar 產物存在檢查 → 分析草稿 → 人工核准 → 發布準備；維持目前的 artifact gate 與 git scoped staging。
- 對外部模型／agent 的輸入採去識別化樣本；含客戶資料的寫入、訊息傳送、標籤、點數與優惠券仍維持 stage → human approval → exact execution/audit。

### know metabiz wiki

- 先在隔離測試 vault 驗證 OpenViking 與 Claude Obsidian 的 ingestion：來源連結、原檔留存、可追溯引用、衝突處理、刪除／更正；通過後才討論是否擴大。
- 不因 AGPL 或開源而推定可併入商用服務；先完成 license、資料出境、索引權限與成本盤點。

## 明日追蹤清單

1. 比較 Codex、mattpocock/skills 的 delta 是否延續，並確認 release／README 是否改變。
2. 驗證 OpenViking 的 issue 回應與 AGPL 部署條件；評估隔離 POC 是否可讀取匿名化 Markdown。
3. 追蹤 `book-to-skill` 對 PDF 來源、引用與測試的處理，選一份可公開教材完成端到端驗收。
4. 檢查新入榜 Hermes Agent、VoltAgent、Claude plugins 是否有第二日成長；首次觀測項目不得以 `+0` 表述。
5. 檢查 n8n 的授權／版本與人審節點，確認 Radar build、commit、push 仍不可被自動化跳過。

## 資料與限制

- 此報告的 repo metadata、README excerpt、release、issue 與快照數字均出自本次 collector；不以 GitHub stars 推論產品採購需求或商業成熟度。
- 一個歷史追蹤 repo 回傳 GitHub API 404 時，collector 已保留最後已知 metadata；該項目未被列入推薦。
- Daily Trending 的首次觀測項目沒有本雷達的前次基線，故只呈現 Trending stars today，snapshot growth 標為未量測。
