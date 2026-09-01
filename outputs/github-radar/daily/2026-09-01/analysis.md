# GitHub AI 趨勢雷達分析（2026-09-01）

## 今日摘要

本日收集 235 個符合查詢或 GitHub Trending daily 的候選專案。最值得注意的訊號不是單純的累積 star，而是「可組裝的 Agent skills」與「把教學/知識工作產品化」正在同時升溫：`THU-MAIC/OpenMAIC` 今日 Trending 3,122 stars，`tt-a1i/archify` 的快照 star delta 為 +3,702，顯示互動課程與可驗證視覺化都具備很強的內容示範價值。另一方面，`affaan-m/ECC`、`mattpocock/skills`、`K-Dense-AI/scientific-agent-skills` 把技能、記憶、研究流程封裝成可重用資產，與 Codex/Claude Code/Metabiz wiki 的工作方式高度相容。

數字需保守解讀：star delta 是相對前一日快照的差值，Trending stars today 是 GitHub Trending 當日欄位；兩者不是同一個統計口徑，也不代表買方需求。風險欄特別標出授權、維護、issue 規模及部署摩擦。

## 值得追蹤的專案

### 1. [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — Deep research

- 目的：用多 Agent 產生沉浸式互動課堂，README 提供中英使用指南；近期 release 為 `v1.0.0`。
- 動能：29,165 stars；快照 delta `+2,813`；Trending 今日 `3,122`；9 月 1 日仍有 push，239 個 open issues。
- 風險：專案快速成長且 issue 量不低，互動課程品質、模型成本、中文/英文內容一致性仍需實測；使用飛書 wiki 作為部分文件入口，也要評估外部服務依賴。
- Adam/Metabiz 關聯：可作為「AI 如何把課程變成可互動教學代理」的深度研究案例，並連接課程產品、企業 onboarding 與 know metabiz wiki 的知識導覽。
- 明日觀察：是否出現新 release、demo 可否自架、課程生成是否支援匯出/評量，以及 issues 是否集中在部署與內容品質。

### 2. [tt-a1i/archify](https://github.com/tt-a1i/archify) — Skill candidate

- 目的：把程式碼或系統描述轉成可驗證、可互動的 architecture/workflow/sequence/data-flow 圖；支援 Cursor、Claude Code、Codex CLI、OpenCode。
- 動能：41,370 stars；快照 delta `+3,702`，為本批最高；9 月 1 日更新，最新 `v2.16.0`（8 月 30 日）；2,618 forks、89 open issues。
- 風險：圖表美感可能掩蓋架構推論錯誤；需核對驗證機制、輸出可攜性與商用授權邊界，避免把生成圖當成真實系統規格。
- Adam/Metabiz 關聯：很適合做成 Codex skill，將需求、wiki 條目與 repo 自動轉成流程圖，改善課程投影片、顧問交付與 Metabiz 知識庫的導覽。
- 明日觀察：README/版本是否新增繁中支援、是否能由現有 markdown/wiki 批次產圖，以及圖表驗證失敗案例。

### 3. [affaan-m/ECC](https://github.com/affaan-m/ECC) — Deep research

- 目的：以 skills、instincts、memory、security 與 research-first development 組成跨 Claude Code、Codex、OpenCode、Cursor 的 agent harness。
- 動能：245,611 stars；快照 delta `+556`；Trending 今日 `621`；8 月 28 日 release `v2.2.0`，9 月 1 日更新；37,077 forks、128 open issues。
- 風險：功能面很廣，導入後的規則衝突、上下文成本與安全邊界需要逐項測試；高 star 不能等同於每個 skill 都適合生產使用。
- Adam/Metabiz 關聯：可作為 AI office automation 的「代理作業系統」研究基線，拆解哪些 memory/security/research pattern 值得回寫成 Metabiz 自有 skills。
- 明日觀察：新版本是否改善 guided setup、Codex 相容性與權限隔離；挑 1–2 個 workflow 做小型 benchmark。

### 4. [mattpocock/skills](https://github.com/mattpocock/skills) — Skill candidate

- 目的：分享真實工程日常使用的 agent skills，強調可直接放進 `.agents` 工作流。
- 動能：243,707 stars；快照 delta `+1,056`；8 月 24 日更新，最新 `v1.2.3`（8 月 6 日）；20,713 forks、445 open issues。
- 風險：技能品質與適用情境高度依賴作者工作流；距離上次 push 有間隔，且大量 forks 可能造成版本分裂，需逐一審查 prompt、工具權限與測試方式。
- Adam/Metabiz 關聯：可直接拿來與現有 skills monorepo 對照，提煉課程中的「技能設計、觸發條件、驗證」教學，也可補強 CRM、wiki、內容生產的 office automation patterns。
- 明日觀察：是否有新技能或相容性更新；比較其 skill metadata、驗證 SOP 與本工作區的結構，找出可移植片段。

### 5. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) — Demo content

- 目的：提供 163+ 個科學研究 skills、100+ 資料庫整合，讓 Cursor、Claude Code、Codex 等 Agent 執行研究工作。
- 動能：41,366 stars；快照 delta `+876`；Trending 今日 `914`；8 月 31 日 push，最新 `v2.65.0`（8 月 29 日）；MIT、3,813 forks、27 open issues。
- 風險：科學/醫療領域的引用正確性與資料庫授權需要人工審核；README 的使用者數等宣稱應視為專案自述，不能直接當成成效證據。
- Adam/Metabiz 關聯：適合示範「把研究 SOP 封裝成 skill」的課程單元，並轉譯成 Metabiz wiki 的市場研究、競品研究、資料整理模板；不宜未審核就用於高風險決策。
- 明日觀察：新增 skill 的測試/引用規範、外部資料庫可用性與繁中研究流程的可行性。

### 6. [openai/codex](https://github.com/openai/codex) — Reference only

- 目的：在終端機執行的輕量 coding agent，可處理 codebase 理解、例行任務與 git workflow。
- 動能：120,656 stars；快照 delta `+250`；9 月 1 日更新並發布 `0.152.0`；18,482 forks、14,764 open issues；Apache-2.0。
- 風險：open issues 數大，版本與功能變動快；本身是基礎平台而非完整 office automation 解決方案，權限、資料外洩與命令執行仍須環境級治理。
- Adam/Metabiz 關聯：作為本 radar、skills monorepo 與 dashboard 的基準平台；課程可示範「coding agent + 專用 skill + wiki context」的組合，而不是只介紹工具本身。
- 明日觀察：下一版本是否改變 skill/IDE 行為、release notes 與 issue 中的穩定性問題。

### 7. [infiniflow/ragflow](https://github.com/infiniflow/ragflow) — Watch

- 目的：開源 RAG engine，結合文件理解、檢索與 Agent，建立 LLM 的 context layer；README 有繁中入口。
- 動能：89,832 stars；快照 delta `+84`；9 月 1 日更新，最新 `v0.27.1`（8 月 28 日）；10,589 forks、1,710 open issues；Apache-2.0。
- 風險：累積 star 很高但今日增長相對有限，issue 規模大；自架所需的基礎設施、索引品質、升級成本與文件權限隔離都可能成為導入瓶頸。
- Adam/Metabiz 關聯：是 know metabiz wiki/RAG 的重要參考架構，可用來比較文件解析、權限、引用與 Agent workflow；目前先觀察，不直接承諾採用。
- 明日觀察：release 是否修正檢索/解析問題、繁中文件表現、部署資源需求，以及 issue 關閉速度。

### 8. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — Watch

- 目的：主打會隨使用者成長的個人 Agent，提供 Agent loop、工具與長期互動能力。
- 動能：239,381 stars；快照 delta `+520`；9 月 1 日更新，最新 `v0.21.0`（8 月 31 日）；48,878 forks、38,438 open issues。
- 風險：open issues 極多，個人化記憶與工具權限涉及資料安全；「會成長」的產品敘事需要用可重現 benchmark 驗證，不能只看社群熱度。
- Adam/Metabiz 關聯：可觀察其個人 Agent、記憶與多工具協作是否能轉化成企業行政助理或 wiki 維護流程；目前適合做比較研究與 demo，不宜直接放入生產流程。
- 明日觀察：release 穩定性、記憶匯出/刪除、權限模型、self-host 成本與 issue 處理趨勢。

## 明日 watchlist

1. 追蹤 `OpenMAIC` 的 release、部署文件與實際互動課程 demo，優先判斷是否能轉成一個 Adam 課程模組。
2. 對 `archify` 與 `mattpocock/skills` 做 30 分鐘可重現測試：同一份 Metabiz wiki/需求，觀察圖表與 skill 輸出的正確性、可維護性和成本。
3. 檢查 `ECC`、`openai/codex` 的版本變更，整理可安全移植到本工作區的 memory/security/research-first pattern。
4. 以一小組繁中 wiki 文件對比 `RAGFlow` 與現有知識流程，記錄引用、權限、索引更新和失敗案例；不以 star 數作採用依據。
5. 續看 `scientific-agent-skills` 的測試與授權細節，評估是否能抽象成「企業研究 skill」而非直接使用科學領域內容。

## 資料與限制

本分析依 `repos.json`、`report.md`、README 摘要、GitHub repository metadata、release 與 issue 訊號撰寫。collector 使用 10 組指定查詢、`--limit 10`、`--include-trending-daily`、`--include-readme`；本次未發生 rate-limit，因此沒有使用降級的 `--limit 5` 重跑。star delta 依快照計算，首次出現的 Trending 專案沒有可比 delta。
