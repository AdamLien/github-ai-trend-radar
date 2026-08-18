# GitHub AI Trend Radar 分析｜2026-08-18

> 蒐集執行：2026-08-19 00:10 後（台灣時間）。目標日為 2026-08-18；GitHub Trending daily 為執行時的即時注意力訊號，不能倒推成目標日的歷史榜單。首次觀測一律標示「未量測」，不寫成 `+0`。首次以每查詢 10 筆收集時遇到未驗證 API 的 403/429；已改用 GitHub CLI 已登入權杖並降至每查詢 5 筆完成，故本日廣度較常態窄。

## 今日結論

- 歷史池只增不減，現有 **181** 個候選；Daily Trending 有 **7** 個範圍內項目，新增 `bojieli/ai-agent-book`、`volcengine/OpenViking`、`chaitanyagiri/munder-difflin` 三項，皆先以未量測 Watch 處理。
- 最強的可轉譯動能不是總 stars，而是 `MoneyPrinterTurbo` 的 Trending 2,306／快照 +2,500、可視化交付的 `diagram-design` +1,141、工程技能規範的 `mattpocock/skills` +1,138，以及可跨 agent 保存 handoff 的 `ai-memory` +717。
- 優先做可回復 POC：假資料測影片／圖表生成；非敏感 sample repo 測記憶、圖譜與 agent handoff；模型路由與本機推論只在隔離環境比較。不得輸入客戶資料、登入 session 或 know metabiz wiki 原始證據。

## 優先追蹤（按動能、近期更新與可用性，不按總 stars 排名）

| 優先 | Repo | 分類 | 本次訊號 | 對 Adam 的可用性 | 主要風險 |
| --- | --- | --- | --- | --- | --- |
| 1 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Demo content | 108,062 ★；快照 **+2,500**；Trending **2,306 today**；8/18 更新；MIT；v1.3.4 | 用主題到短片的全流程做 AI 內容產線課程 demo；以自有或授權素材測成本、字幕與可編輯性。 | 生成影片的素材權利、事實正確性與外部模型費用；不把一次成功視為商用交付。 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Demo content | 21,473 ★；**+1,141**；8/18 更新；MIT；33 issues | 將 mCRM「讀取→草稿→人工核准→執行／稽核」畫為可編輯 HTML/SVG，是課程與 AI 辦公室流程圖的立即素材。 | 無正式 release；圖表內容、品牌與版權仍須人工核對。 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 221,219 ★；**+1,138**；8/17 更新；MIT；v1.2.3；363 issues | 萃取明確輸入、可驗收輸出、權限 stop line，補強 metabiz 既有技能與 developer automation。 | 不可整包全域啟用；每個 skill 先審核指令、資料讀寫與相依工具。 |
| 4 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Deep research | 2,572 ★；**+717**；Trending **730 today**；8/18 更新；MIT；v1.28.0；10 issues | 以 sample repo 測 Codex／Claude Code 跨工具 handoff 能否保留已試方案、失敗路徑與待決策。 | 記憶跨 workspace／團隊可能外洩；先驗證儲存位置、清除、隔離與人工覆核。 |
| 5 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Watch | 50,306 ★；**+669**；8/18 更新；MIT；v3.8.49；351 issues | 做 Codex、Claude Code、Cursor 的成本、模型選擇與 fallback 對照 demo。 | provider key、配額、資料外送與免費額度均不可假設；先用隔離 key。 |
| 6 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Deep research | 8,906 ★；**+471**；8/18 更新；MIT；v0.6.5；100 issues | 研究「來源→主張→決策→驗證時間」的圖譜 context，貼近 know metabiz wiki 的可追溯需求。 | 早期 schema 可能不合 Obsidian evidence；需驗證回鏈、刪除與重建。 |
| 7 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 107,791 ★；**+390**；8/17 更新；Apache-2.0 | 可從程式、文件、SQL、設定與 PDF 建成可查詢知識圖譜，適合驗證本地 evidence 導覽層。 | 資源耗用與索引品質未驗證；只可用無敏感 repo 作 POC。 |
| 8 | [jundot/omlx](https://github.com/jundot/omlx) | Watch | 19,286 ★；**+400**；Trending **366 today**；8/18 更新；Apache-2.0；v0.6.1 | Apple Silicon 本機推論／快取可做「本地模型與雲端模型」成本、延遲、資料邊界內容實驗。 | 912 issues；先測模型相容性、資源回收和離線失敗情境。 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | Watch | 48,037 ★；固定 watchlist；**+845**；8/18 更新；MIT；v1.4.184 | 研究平行 coding-agent 的任務拆分、人工審核與執行證據呈現。 | 4,091 issues；不可由 UI demo 推論 production orchestration 穩定。 |
| 10 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Reference only | 28,943 ★；**+754**；Trending **726 today**；Apache-2.0；v1.3.0 | 可作安全技能結構與權限 stop line 的研究樣本。 | 安全／攻擊內容不應連到客戶環境或自動執行；更新日為 8/08，先檢查維護脈絡。 |

## 對 Adam 工作的可執行轉譯

### 課程與內容

1. 用 `MoneyPrinterTurbo` 做「腳本→素材→字幕→人工審片」教學，但只用自有素材；驗收為輸出可追溯來源、可人工改稿與可列出成本。
2. 用 `diagram-design` 生成 mCRM 人工核准與 wiki evidence flow；驗收為學員能指出資料讀取、送出、稽核三個邊界。
3. 用 `omlx` 與雲端模型做同一任務的本機／雲端比較，完整記錄設備、模型、延遲、品質和失敗原因。

### AI 辦公室自動化與 Skills

1. 從 `mattpocock/skills` 只抽取規格框架，將每個 metabiz skill 明定 Given/When/Then、可見成功、邊界案例、scope/out of scope 與人工核准點。
2. `ai-memory` 以單一無敏感 sample repo 測 handoff；boundary case 是清除後不得找回私密任務脈絡。
3. `Orca` 與 `OmniRoute` 僅在隔離帳號做任務分派與 fallback POC；不得自動帶入客戶憑證或 session。

### know metabiz wiki

1. 以 `Graphify`／`Semantica` 對同一小型公開資料集驗證「原始檔→主張→查詢回答」是否可回鏈；圖譜僅為導覽層，原始 evidence 才是事實依據。
2. 必測排除敏感來源、索引刪除、重建後舊資料不可被查回，以及查詢回覆是否能標示來源與時間。

## 新增 Trending 與反訊號

- `bojieli/ai-agent-book`（556 today）、`volcengine/OpenViking`（298）、`chaitanyagiri/munder-difflin`（256）為首次觀測，快照成長尚未量測；明日先看 README、release、issue 與相同範圍的第二日 delta，再決定是否升級。
- `MoneyPrinterTurbo` 的高日增長是內容自動化注意力，不是影片品質、版權合規或課程購買需求的證明。
- `holaOS` 的 +626 雖有動能，但授權為 `NOASSERTION`；在取得明確授權與安全邊界前，不列採用候選。
- 大量 issues（Orca、omlx、Graphify）不是直接拒用理由，卻要求 POC 之外另測升級、失敗復原與維運負擔。
- GitHub stars 反映開發者注意力，不能推論客戶需求、production 安全、法律可行性或商業價值。

## 明日追蹤清單

1. 追 `MoneyPrinterTurbo`、`diagram-design`、`mattpocock/skills`、`ai-memory` 的第二日 delta，區分短期 Trending 與可重複使用的動能。
2. 對三個新增 Trending 項目建立第二日基線；沒有 README、release／issue 健康度與範圍吻合證據前維持 Watch。
3. 對 `ai-memory` 做清除／隔離 POC；失敗即不進入任何真實 repository 或客戶流程。
4. 對 `Graphify`／`Semantica` 用公開資料驗證回鏈、敏感來源排除、刪除和重建；保留可重現測試紀錄。
5. 保留 `stablyai/orca` 固定 watchlist 與全部歷史候選，避免搜尋結果變動讓趨勢曲線斷裂。
