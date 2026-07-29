# GitHub AI Trend Radar 分析 — 2026-07-29

## 結論

本日不是「看總 stars 最大」的一天，而是三條可立即轉成 Adam 工作流的線同時有訊號：**程式碼知識圖譜（Graphify）**、**agent 開發方法/skills（Superpowers、book-to-skill）**、以及 **LLM 輸入成本控制（Headroom）**。先做 Graphify 與 Headroom 的小型驗證；內容則可先用 `jcode`、`speech-to-speech` 和 `open-code-review` 做 10–15 分鐘 demo。

資料來源：GitHub Trending daily（擷取時的相關日榜候選：airi +676、speech-to-speech +837、jcode +652、VibeVoice +332、superpowers +634、open-code-review +386、book-to-skill +1,428 stars today）及十組 GitHub Search API。`stars_delta` 為與前一日輸出 `2026-07-28/snapshots/repos-2026-07-29.json` 的同 repo 比較；首次出現在本日集合者不可誤讀為 0 成長。collector 本目錄的 snapshot 日期為 2026-07-30（程式以執行日命名）。

## 最值得追的 10 個

| 分類 | Repo | 動能與維護訊號 | 用途與對 Adam 的可用性 | 風險 / 下一步 |
| --- | --- | --- | --- | --- |
| Deep research | [Graphify](https://github.com/Graphify-Labs/graphify) | 98,247 stars，日增 **+670**；7/28 push/release v0.9.29；README 明確涵蓋 AST、docs、SQL、PDF 到可查詢 graph | 最貼近 know metabiz wiki：可比較「本地 deterministic graph + 現有 evidence wiki」；也適合做 Codex/Claude/Cursor codebase-context 課程 | 716 open issues，先以一個非敏感 repo 做索引速度、引用可追溯性與成本 POC；Apache-2.0 |
| Deep research | [obra/superpowers](https://github.com/obra/superpowers) | 263,100 stars，日增 **+537**；7/24 v6.2.0；Trending **+634 today** | 可拆解為 AI 辦公室自動化的「計畫、子任務、驗證」教學骨架，並對照目前 Codex skill 做法 | 高熱度不等於可直接取代現有技能；先抽 1 個 SDLC workflow 做比較；MIT |
| Deep research | [Headroom](https://github.com/headroomlabs-ai/headroom) | 63,151 stars，日增 **+240**；7/29 有 push；README 主張壓縮 logs/files/RAG chunks，支援 proxy/MCP | 對長文件、工具輸出、wiki 查詢特別直接：先測 token 減量是否保留證據與表格語意 | README 效果數字需自行 benchmark；584 issues；Apache-2.0 |
| Deep research | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 15,807 stars；Trending **+386 today**；7/29 push、7/28 v1.8.0 | 可做「規則式檢查 + LLM review」demo，亦可檢視是否能輔助內部 PR 品質流程 | 需驗證語言、CI、資料外傳與 false positives；60 issues；Apache-2.0 |
| Demo content | [1jehuang/jcode](https://github.com/1jehuang/jcode) | 13,229 stars；Trending **+652 today**；7/29 push、7/28 v0.61.1 | Rust terminal coding-agent harness，適合做「輕量 agent 介面與 MCP」比較短片 | 161 issues；不要從 README 的 RAM 宣稱直接推出實測結論；MIT |
| Demo content | [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 7,709 stars；Trending **+837 today**；7/29 push | 可接到 mVoice/語音 agent 課程，示範本地 voice agent 的基本管線 | 模型、GPU/CPU 延遲與中文品質必測；113 issues；Apache-2.0 |
| Skill candidate | [book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 12,386 stars；Trending **+1,428 today**；v1.2.0 支援安裝包與多語章節偵測 | 很適合研究「PDF/手冊 → 可引用 Codex skill」的 intake 範本，與 metabiz 文件型知識工作直接相關 | 7/27 後未見新 push；先用非版權/可用文件驗證 extraction、引用與授權邊界；MIT |
| Watch | [moeru-ai/airi](https://github.com/moeru-ai/airi) | 45,258 stars；Trending **+676 today**；7/29 push，v0.11.3 | 自架 realtime voice companion，可作「本地 voice UX」靈感來源 | 核心是 companion/VTuber 而非辦公室 agent，平台與資源成本高；188 issues；MIT |
| Watch | [multica](https://github.com/multica-ai/multica) | 42,498 stars，日增 **+141**；7/29 push/release | 多 agent orchestration 候選，可對照 Adam 的多工具/多角色流程 | license 為 `NOASSERTION`、1,222 issues；未釐清授權與維護前不採用 |
| Reference only | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 235,365 stars，日增 **+782**；7/27 release | Claude Code 設定/commands 的巨大社群樣本，可當內容選題與結構參考 | 偏模板/設定集合，非可直接放入 production 的核心依賴；MIT |

## 對課程、內容與產品工作流的轉譯

- **Deep research：** 先做 Graphify + Headroom 兩個 90 分鐘 POC。前者驗證 evidence graph 的可追溯查詢，後者在相同 wiki/PDF 查詢上量測 token、答案與引文是否劣化。
- **Demo content：** `jcode` 對比 Codex/Claude Code 的 CLI agent、`speech-to-speech` 做語音 agent 最小 demo、`open-code-review` 展示 deterministic rule 與 LLM reviewer 的分工。切角應是「這能解哪個工作流」，不是星數排行榜。
- **Skill candidate：** book-to-skill 的流程可轉成內部「合規 PDF → source-aware skill」規格：保留來源頁碼、授權、可重跑 extraction 和人工驗收；不可把客戶資料或未授權書籍直接送進去。
- **AI 辦公室自動化：** Superpowers 可作任務分解/驗證 checklist 的參考；Headroom 可先放在大量工具輸出的邊界，而非改動資料源或決策權限。
- **know metabiz wiki：** Graphify 值得比對，但不應取代既有 evidence 分層。先確認每個 graph node 能回到原始檔、段落或資料表，並維持敏感資料的本地範圍。

## 風險與假陽性

- GitHub Trending 的 `stars today` 是注意力訊號，不是企業需求或可導入性的證明。
- Search API 的結果以總 stars 排序，故本報告用日增、Trending、push/release、README 清晰度、授權與 issue load 二次篩選。
- 本日 `repos.json` 有 95 個去重 repo；每日輸出新資料夾沒有同目錄舊 snapshot，表內跨資料夾 delta 才是可比較值。
- 未因高星而推薦採用：無明確授權（multica）或偏靈感/模板集合者已降為 Watch/Reference。

## 明日追蹤清單

1. 重跑相同十組 query，確認 Graphify、Superpowers、Headroom 是否連續 2 日上升。
2. 追蹤 `open-code-review` v1.8.0 的 issue/PR 回應與可支援語言，再決定是否做 repo-level demo。
3. 用一份已授權、非敏感 PDF 對 book-to-skill 測試引用、繁中章節與結果可重現性。
4. 對 Headroom 做 baseline/壓縮後的答案品質、token、延遲三欄 benchmark，不採 README 宣稱作決策。
5. 若 multica 仍有動能，先確認 SPDX license 與治理狀態；未確認前維持 Watch。
