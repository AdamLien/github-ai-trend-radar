# GitHub AI Trend Radar 分析（2026-09-12）

## 判讀方式

本日以 GitHub Trending daily 與指定十組搜尋結果建立候選池，共檢視 276 個 repository。判斷綜合今日 Trending stars、相對前次快照的 `stars_delta`、相對成長、最近 push/release、README 可操作性、issue 訊號，以及 license、維護與採用摩擦。GitHub stars 代表開發者注意力，不等同付費需求或生產環境品質。本輪未遇到 GitHub API rate limit。

## 值得追蹤的 repository

### 1. [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) — Deep research

- **用途與動能：** 開源、自架 AI sales OS，把 CRM、WhatsApp 對話、AI agents、RAG 與 MCP-ready 工作流放在一起；1,665 stars，較前次 +481，今日 Trending +505，2026-09-12 push，v1.19.0 於 2026-09-11 發布，531 forks。
- **風險：** 104 個 open issues；WhatsApp/WAHA、LGPD、多租戶與 Supabase 的整合邊界需要實測，且聊天資料涉及個資與憑證治理。MIT 是有利條件，但不代表可直接接入客戶資料。
- **對 Adam 的價值：** 與 mCRM、AI office automation 及 Metabiz wiki 的客戶流程高度相關；適合深研「聊天 → qualification → CRM → wiki 知識回寫」的完整案例。

### 2. [alsk1992/CloddsBot](https://github.com/alsk1992/CloddsBot) — Watch

- **用途與動能：** 基於 Claude 的自動化交易 agent，涵蓋 prediction markets、crypto 與多鏈；2,374 stars，+354，今日 Trending +377，2026-09-12 push，v1.9.1 同日發布。
- **風險：** 金融與加密資產場景有真實資金、模型幻覺、執行權限、法規與密鑰風險；README 出現代幣宣傳資訊，不能視為成熟金融產品。即使 MIT，也只適合作為隔離研究案例。
- **對 Adam 的價值：** 可用來講 agent 自主執行、風險閘門與 human approval；不建議納入 Metabiz 生產流程或課程中的投資建議。

### 3. [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) — Reference only

- **用途與動能：** 彙整 Claude、Claude Code、Codex、Cursor 等系統 prompt，方便觀察 agent 產品的行為設計；65,177 stars，今日 Trending +357，2026-09-09 push，10,707 forks，CC0-1.0。
- **風險：** 內容的來源、時效、真實性與再散布倫理需逐項核查；高 stars 是注意力訊號，不是可靠規格文件。避免把疑似內部 prompt 當成官方承諾或複製到公司系統。
- **對 Adam 的價值：** 可作為課程的 prompt architecture、權限邊界與「如何驗證 agent 行為」參考；對 Metabiz wiki 僅保留來源註記與觀察，不存放敏感內容。

### 4. [jihe520/MathModelAgent](https://github.com/jihe520/MathModelAgent) — Demo content

- **用途與動能：** 以 agent 與 skills 自動完成數學建模、分析與論文草稿；5,076 stars，+286，今日 Trending +264，2026-09-10 push，v0.0.19 同日發布，README 提供桌面版與中英文件。
- **風險：** license 欄位未聲明；「可直接提交」的輸出仍須人工驗算、引用查核與學術誠信審查，且 43 個 open issues 顯示仍在快速演進。
- **對 Adam 的價值：** 適合示範「問題拆解 → 工具/skill → 可審核文件」；可轉成課程中的研究自動化單元，但不把生成論文當成免審核成果。

### 5. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — Demo content

- **用途與動能：** 收集 100+ AI agents、agent skills 與 RAG app，支援多模型；137,467 stars，+267，今日 Trending +237，2026-09-12 push，20,224 forks，Apache-2.0。
- **風險：** 範例集合的品質、依賴與 API key 需求不一；12 個 issue 偏少不等於每個 app 都有完整測試。要逐個確認資料流、成本、license 與版本鎖定。
- **對 Adam 的價值：** 是課程與內容選題的高密度素材庫，可挑選 CRM、RAG、辦公自動化小案例，並把可重現安裝與成本拆解同步到 Metabiz wiki。

### 6. [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) — Watch

- **用途與動能：** 自架、可自主執行複雜滲透測試的多 agent 系統；23,226 stars，今日 Trending +193，2026-09-10 push，3,046 forks，MIT。
- **風險：** offensive security 能力可能造成越權或誤測；57 個 issues，最新 release 為 2026-05-29，顯示 release 節奏需再觀察。只可在明確授權、隔離環境與人工閘門下 demo。
- **對 Adam 的價值：** 可做 agent governance、工具權限與安全自動化的反面教材；與 AI office automation 的共通點是「高風險工具必須有 scope、approval、audit log」。

### 7. [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) — Demo content

- **用途與動能：** YuE2 以 symbolic planning、zero-shot cover 與 agentic editing 做音樂生成；7,142 stars，今日 Trending +193，2026-09-11 push，v0.1.6 於 2026-09-09 發布，Apache-2.0。
- **風險：** voice/music cloning 的著作權、訓練資料、風格模仿與算力成本需先釐清；README 的 frontier quality 宣稱仍應以可重現樣本驗證。
- **對 Adam 的價值：** 可示範多模態 agent 如何把規劃、生成與編輯串成內容 pipeline；適合內容課程 demo，不宜直接把生成音訊放入商業素材而不做權利清查。

### 8. [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) — Skill candidate

- **用途與動能：** 讓 coding agent 用更聚焦、較不埋沒答案的格式輸出；43,125 stars，+2,427，2026-09-10 push，2,453 forks，MIT；本日以 tracked repo 續追，未在 Trending daily 卡片中取得今日 stars。
- **風險：** 主要是互動/輸出體驗改善，實際生產力收益需用真實任務比較；60 個 issues，且沒有 latest release，不能只因成長快就全域套用。
- **對 Adam 的價值：** 可直接轉成 Codex/Claude Code 的輸出契約與課程教學技巧，改善研究、報價、wiki 更新與辦公自動化任務的可讀性。

### 9. [tt-a1i/archify](https://github.com/tt-a1i/archify) — Skill candidate

- **用途與動能：** 將 codebase 或系統描述轉成可驗證的 architecture、workflow、sequence、data-flow 與 lifecycle 圖；59,345 stars，+1,068，2026-09-12 push，v2.16.0，3,889 forks，MIT。
- **風險：** 161 個 issues；圖表漂亮不代表架構判斷正確，需核對中文需求、複雜依賴、版本差異與 export 結果。
- **對 Adam 的價值：** 很適合 mCRM/mBeauty 流程、AI office automation 與 Metabiz wiki 的視覺化；可成為「需求 → 可驗證流程圖 → review」的 reusable skill。

### 10. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) — Deep research

- **用途與動能：** 把文件轉成互相連結、持續維護的知識庫，而非每次從零 RAG；19,033 stars，+463，最近 push 為 2026-08-25，v0.6.11 同日發布，2,156 forks。
- **風險：** license 為 `NOASSERTION`，259 個 issues，且最近 push 距今日較久；須先確認授權、刪除/更新語意、引用可追溯性與增量同步可靠度。
- **對 Adam 的價值：** 與 Metabiz wiki、課程知識庫及「把工作文件變成可維護知識」直接相關；值得以非敏感文件做 proof of concept，釐清 license 前不進正式流程。

## 綜合結論

本日最強訊號是「可落地的 agent 工作流」：DeskcommCRM 把聊天銷售與 MCP/RAG 結合，Archify 與 i-have-adhd 代表 skill 的輸出與可視化體驗，awesome-llm-apps 則提供大量可教、可拆解的 RAG/agent 範例。llm_wiki 適合承接 Metabiz wiki 的長期知識維護。CloddsBot 與 PentAGI 雖有明顯 Trending 動能，但應把治理、權限、成本與人工核准放在 demo 前面；system prompts repo 適合做觀察資料，不宜當規格來源。

## 明日 watchlist

1. 重跑相同十組查詢，確認 DeskcommCRM、CloddsBot、MathModelAgent 的 Trending stars 與 star delta 是否仍高於候選池中位數。
2. 追蹤 i-have-adhd、Archify 與 llm_wiki 的連續快照，補看 release、commit/issue 回應與 README 變更；在 license 未釐清前不採用 llm_wiki。
3. 對 DeskcommCRM 做隔離 demo：非敏感 WhatsApp/CRM 假資料、MCP 工具清單、人工核准與 wiki 回寫 audit trail。
4. 從 awesome-llm-apps、MathModelAgent 與 YuE2 各挑一個最小可重現案例，記錄模型、API 成本、輸出品質與授權，評估課程內容化。
5. 觀察 PentAGI 與 CloddsBot 的權限/風險處理、issue 回應與 release 節奏；不把自主執行權限接到公司或客戶環境。

