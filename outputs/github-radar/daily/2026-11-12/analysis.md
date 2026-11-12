GitHub AI 趨勢雷達｜2026-11-12（Asia/Taipei 目標日）

本次實際收集於 2026-11-13T00:11:45.815569+08:00 開始，2026-11-13T00:25:44.979837+08:00 完成整理。目標日是執行日的前一個台北日曆日；API 星數與 Trending「stars today」是執行當下的讀值，不能視為 11 月 12 日午夜結算值。

完整執行 10 組指定查詢，合併 GitHub Trending daily 與既有追蹤。篩選後保留 418 個項目；本次 Trending 頁面解析出 13 個項目，其中 8 個符合範圍。搜尋以總星數排序只作發現入口，以下編輯選題另外考慮當日熱度、快照增量、相對成長、近期推送、README、release、Issue／PR 與 Adam 的實際用途。

配額狀態：未觀察到 GitHub API rate-limit 錯誤；--limit 10 完成，未啟用 --limit 5 重跑。補充證據查詢亦未發現 rate-limit 錯誤。

本次建議優先研究 Codex Security 與 OpenBot 的證據及控制流程；內容示範選 Orca、Astryx 與 Activepieces；技能候選選工程 skills、安全稽核 skill 與 wiki agent。Qwen Code 與桌面 LLM Wiki 維持觀察。這是依應用價值排列的選題順序，不是總星數排行榜。

數據口徑：快照 Δ＝本次星數－2026-11-11 目標日快照星數；相對成長＝Δ／前次星數。這是兩次實際抓取間的變動，未保證恰好 24 小時。Trending 今日星數是另一個獨立指標，不與 Δ 相加；「—」代表未上本次 Trending daily，不代表當日零成長。新收錄項目沒有基準，不能把 collector 的零增量當成真實零成長。dashboard 沿用既有相對成長計算（Δ／本次星數），與本分析分母不同。

| 選題順序／專案 | 判斷 | 總星數 | Trending 今日星數 | 快照 Δ | 相對成長 |
|---|---|---:|---:|---:|---:|
| 1. [openai/codex-security](https://github.com/openai/codex-security) | Deep research | 12,198 | 663 | +682 | +5.92% |
| 2. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Skill candidate | 116,471 | 812 | +788 | +0.68% |
| 3. [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | Deep research | 11,356 | 291 | +374 | +3.41% |
| 4. [stablyai/orca](https://github.com/stablyai/orca) | Demo content | 123,210 | — | +1,070 | +0.88% |
| 5. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Skill candidate | 70,911 | — | +892 | +1.27% |
| 6. [meta/astryx](https://github.com/meta/astryx) | Demo content | 26,191 | 1789 | +1,702 | +6.95% |
| 7. [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | Watch | 29,647 | 151 | 未量測（新收錄） | 未量測 |
| 8. [activepieces/activepieces](https://github.com/activepieces/activepieces) | Demo content | 25,499 | — | +20 | +0.08% |
| 9. [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | Skill candidate | 3,693 | — | +5 | +0.14% |
| 10. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Watch | 21,609 | — | +32 | +0.15% |

分類使用 Deep research / Demo content / Skill candidate / Watch / Reference only；以下判斷是文件與活動訊號評估，尚未安裝或執行這些專案。

**1. [openai/codex-security](https://github.com/openai/codex-security) — Deep research**

用途：以 CLI、SDK 與自動化流程進行漏洞搜尋、驗證、修補與結構化報告。

動能：總星數 12,198；Trending 今日星數 663；快照 Δ +682、相對成長 +5.92%。0.10.0 新增 Standard scan 續跑與批次掃描預算；有明確功能進展，可與 skill 型稽核工作流比較。

維護訊號：最近推送 2026-11-12T10:06:19Z；release npm-v0.10.0（2026-11-12T02:18:52Z）；API open_issues_count 為 142（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 0 個 Issue、5 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：掃描仍可能誤報或漏報；需量測成本、覆蓋與修補驗證，避免把產生報告當作完整安全保證。 本次 API 授權標示：Apache-2.0。

與 Adam 的關聯：Adam 課程／內容：展示「發現→驗證→修補」的證據鏈；AI 辦公：限工程稽核場景；know metabiz wiki：保存範圍、版本與修補紀錄。

證據：[README](https://github.com/openai/codex-security/blob/main/README.md)、[release](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0)、[PR #2630](https://github.com/openai/codex-security/pull/2630)、[PR #2589](https://github.com/openai/codex-security/pull/2589)。

**2. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — Skill candidate**

用途：把規格、規劃、實作、測試、審查與交付整理成 coding agent 可重用的工程 skills。

動能：總星數 116,471；Trending 今日星數 812；快照 Δ +788、相對成長 +0.68%。Trending 熱度應與程式推送日期分開看；0.6.15 修正 staged-secret 檢查輸出及品質閘門，適合挑單一流程測試。

維護訊號：最近推送 2026-11-01T19:24:49Z；release 0.6.15（2026-10-31T06:40:31Z）；API open_issues_count 為 137（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 2 個 Issue、3 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：既有 skills、hooks 與斜線指令可能重複或衝突；README 對品質的宣稱需用自己的任務驗證。 本次 API 授權標示：MIT。

與 Adam 的關聯：Adam 課程／內容：示範把工程原則轉成可執行技能；AI 辦公：借用清單與驗證流程；know metabiz wiki：整理 skill 對照表、適用條件與測試紀錄。

證據：[README](https://github.com/addyosmani/agent-skills/blob/main/README.md)、[release](https://github.com/addyosmani/agent-skills/releases/tag/0.6.15)、[PR #785](https://github.com/addyosmani/agent-skills/pull/785)、[Issue #225](https://github.com/addyosmani/agent-skills/issues/225)。

**3. [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) — Deep research**

用途：可自架的 AI 同事工作空間，整合模型、agent 與各自的電腦／工具環境。

動能：總星數 11,356；Trending 今日星數 291；快照 Δ +374、相對成長 +3.41%。有近期 release 與 PR，可用一個受控的瀏覽器研究→整理報告流程驗證；熱度與企業可用性分開評估。

維護訊號：最近推送 2026-11-12T15:44:46Z；release v1.0.2（2026-11-11T08:45:38Z）；API open_issues_count 為 82（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 1 個 Issue、4 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：1.0.2 的升級說明涉及 Podman machine、Docker／Podman 更新及舊版資料庫遷移；升級前需檢查資料備份與隔離。 本次 API 授權標示：MIT。

與 Adam 的關聯：Adam 課程／內容：AI coworker 操作與審批案例；AI 辦公：資料蒐集、報表草稿與操作紀錄；know metabiz wiki：評估任務證據與知識歸檔銜接。

證據：[README](https://github.com/CopilotKit/OpenBot/blob/main/README.md)、[release](https://github.com/CopilotKit/OpenBot/releases/tag/v1.0.2)、[PR #1422](https://github.com/CopilotKit/OpenBot/pull/1422)、[Issue #1513](https://github.com/CopilotKit/OpenBot/issues/1513)。

**4. [stablyai/orca](https://github.com/stablyai/orca) — Demo content**

用途：以獨立 worktree 平行調度 Claude Code、Codex 等 coding agents，結合聊天、終端、差異與瀏覽器。

動能：總星數 123,210；Trending 今日星數 未列榜；快照 Δ +1,070、相對成長 +0.88%。1.4.257 聚焦多個長對話同時串流的效能與瀏覽器回饋保存；適合用相同任務比較單 agent 與編排流程。

維護訊號：最近推送 2026-11-12T16:12:56Z；release v1.4.257（2026-11-12T01:20:37Z）；API open_issues_count 為 8253（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 1 個 Issue、4 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：agent 數量增加可能放大費用、訂閱配額與合併衝突；產品名稱的效率宣稱不是本次實測結果。 本次 API 授權標示：MIT。

與 Adam 的關聯：Adam 課程／內容：多 agent 分工與合併示範；AI 辦公：偏工程交付編排；know metabiz wiki：記錄分工、決策與可重現的驗證結果。

證據：[README](https://github.com/stablyai/orca/blob/main/README.md)、[release](https://github.com/stablyai/orca/releases/tag/v1.4.257)、[PR #41598](https://github.com/stablyai/orca/pull/41598)、[Issue #41597](https://github.com/stablyai/orca/issues/41597)。

**5. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — Skill candidate**

用途：用分階段、隔離的 agents 執行偵察、覆蓋導向搜尋、候選驗證與結構化安全稽核報告。

動能：總星數 70,911；Trending 今日星數 未列榜；快照 Δ +892、相對成長 +1.27%。README 描述獨立複核與 coverage ledger；近期 #148／#149 聚焦目標工作區信任，值得先讀再決定是否採用。

維護訊號：最近推送 2026-09-14T19:29:02Z；release 未取得 latest release（API 404；不能據此判定沒有任何 tag）；API open_issues_count 為 126（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 2 個 Issue、3 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：沒有 latest release；稽核本身接觸不可信工作區與輸出，需以固定 commit、隔離樣本驗證其信任邊界。 本次 API 授權標示：MIT。

與 Adam 的關聯：Adam 課程／內容：與 Codex Security 比較方法、成本及證據品質；AI 辦公：適用工程審查；know metabiz wiki：建立稽核覆蓋與待驗證項目模板。

證據：[README](https://github.com/cloudflare/security-audit-skill/blob/main/README.md)、[Issue #148](https://github.com/cloudflare/security-audit-skill/issues/148)、[PR #149](https://github.com/cloudflare/security-audit-skill/pull/149)。

**6. [meta/astryx](https://github.com/meta/astryx) — Demo content**

用途：供人與 agents 共用的設計系統，包含可組合的 React 元件、主題、模板與 CLI。

動能：總星數 26,191；Trending 今日星數 1789；快照 Δ +1,702、相對成長 +6.95%。Trending 動能與 0.7.14 的具體元件改善一起看；屬於 agent 開發工具鏈，不是獨立 LLM 平台。

維護訊號：最近推送 2026-11-12T16:18:44Z；release v0.7.14（2026-11-11T19:54:54Z）；API open_issues_count 為 619（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 0 個 Issue、5 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：仍標示 Beta，使用 React 19+，整合前需測試版本相容性、無障礙與既有樣式架構。 本次 API 授權標示：MIT。

與 Adam 的關聯：Adam 課程／內容：用設計系統約束 coding agent 的 UI 輸出；AI 辦公：內部工具與報表介面；know metabiz wiki：保存元件用法與設計決策。

證據：[README](https://github.com/meta/astryx/blob/main/README.md)、[release](https://github.com/meta/astryx/releases/tag/v0.7.14)、[PR #9739](https://github.com/meta/astryx/pull/9739)、[PR #9777](https://github.com/meta/astryx/pull/9777)。

**7. [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) — Watch**

用途：跨終端、編輯器、桌面與瀏覽器的開源 AI coding agent。

動能：總星數 29,647；Trending 今日星數 151；快照 Δ 未量測（新收錄）、相對成長 未量測。本次新增追蹤，以 Trending 今日星數建立初始動能；latest release 是 TypeScript SDK 標籤，不能當成 CLI 的最新穩定版。

維護訊號：最近推送 2026-11-12T16:13:32Z；release sdk-typescript-v0.1.32（2026-11-10T20:18:32Z）；API open_issues_count 為 2220（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 0 個 Issue、5 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：沒有前次快照，不能估算日增幅；1.0 Preview、CLI 與 SDK 的版本線不同，功能和模型成本需逐項確認。 本次 API 授權標示：Apache-2.0。

與 Adam 的關聯：Adam 課程／內容：多 coding agent 的同題比較；AI 辦公：評估中文任務與工具整合；know metabiz wiki：保存安裝版本、模型與權限測試。

證據：[README](https://github.com/QwenLM/qwen-code/blob/main/README.md)、[release](https://github.com/QwenLM/qwen-code/releases/tag/sdk-typescript-v0.1.32)、[PR #17049](https://github.com/QwenLM/qwen-code/pull/17049)、[PR #16866](https://github.com/QwenLM/qwen-code/pull/16866)。

**8. [activepieces/activepieces](https://github.com/activepieces/activepieces) — Demo content**

用途：以 TypeScript pieces 串接 AI、自動化流程與 MCP 工具的視覺化平台。

動能：總星數 25,499；Trending 今日星數 未列榜；快照 Δ +20、相對成長 +0.08%。0.93.0 與近期整合 PR 顯示持續交付；即使星數增量較小，與辦公自動化的直接關聯仍使其值得入選。

維護訊號：最近推送 2026-11-12T16:03:34Z；release 0.93.0（2026-11-08T14:30:22Z）；API open_issues_count 為 919（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 0 個 Issue、5 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：API 授權為 NOASSERTION，README 卻標示 MIT，需逐目錄核對 LICENSE 與企業功能；連接器權限、資料流向及雲端／自架差異也需確認。 本次 API 授權標示：NOASSERTION。

與 Adam 的關聯：Adam 課程／內容：來源資料→AI 摘要→人工審閱的流程；AI 辦公：整合表單、CRM 與報表；know metabiz wiki：把審閱後的產物接入知識整理流程。

證據：[README](https://github.com/activepieces/activepieces/blob/main/README.md)、[release](https://github.com/activepieces/activepieces/releases/tag/0.93.0)、[PR #17440](https://github.com/activepieces/activepieces/pull/17440)、[PR #17376](https://github.com/activepieces/activepieces/pull/17376)。

**9. [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) — Skill candidate**

用途：讓 coding agent 從 raw 來源建立與維護互相連結的 Markdown wiki，保留來源頁、索引、操作紀錄與圖譜。

動能：總星數 3,693；Trending 今日星數 未列榜；快照 Δ +5、相對成長 +0.14%。優先看知識工作流契合度，而非總星數；沒有 latest release，近期抽樣 Issue／PR 更新也較舊，適合小樣本驗證。

維護訊號：最近推送 2026-11-09T11:35:34Z；release 未取得 latest release（API 404；不能據此判定沒有任何 tag）；API open_issues_count 為 13（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 1 個 Issue、4 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：需防止重複匯入、錯誤引用、來源指令注入與矛盾知識擴散；「不需額外 API key」不代表既有 agent 沒有使用成本。 本次 API 授權標示：MIT。

與 Adam 的關聯：Adam 課程／內容：從資料夾長出知識庫的實作；AI 辦公：文件整理與交接；know metabiz wiki：直接對照 raw、sources、概念頁、日誌及回溯引用。

證據：[README](https://github.com/SamurAIGPT/llm-wiki-agent/blob/main/README.md)、[PR #86](https://github.com/SamurAIGPT/llm-wiki-agent/pull/86)、[PR #85](https://github.com/SamurAIGPT/llm-wiki-agent/pull/85)。

**10. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) — Watch**

用途：跨平台桌面知識庫，以增量方式把文件編譯成 wiki，提供圖譜、來源檢索與本機 API／MCP。

動能：總星數 21,609；Trending 今日星數 未列榜；快照 Δ +32、相對成長 +0.15%。release 停在 0.6.13；相較當日星數，#849 的 MinerU 403、#806 的 PDF 解析偏差與 #848 的寫回失敗更影響是否適合導入。

維護訊號：最近推送 2026-10-21T11:17:29Z；release v0.6.13（2026-10-22T01:21:07Z）；API open_issues_count 為 301（包含未結 PR，不是純 Issue 數）。依 updated 排序抽樣最近 5 筆，含 4 個 Issue、1 個 PR；這是活動樣本，不是解決率或完整安全評估。

風險：授權 API 為 NOASSERTION；解析正確率、雲端文件上傳、寫回可靠性與來源追溯需先驗證。 本次 API 授權標示：NOASSERTION。

與 Adam 的關聯：Adam 課程／內容：比較持久 wiki 與每次檢索的工作模式；AI 辦公：多格式文件整理；know metabiz wiki：以去識別樣本對照現有流程，尚不建議直接搬入正式資料。

證據：[README](https://github.com/nashsu/llm_wiki/blob/main/README.md)、[release](https://github.com/nashsu/llm_wiki/releases/tag/v0.6.13)、[Issue #849](https://github.com/nashsu/llm_wiki/issues/849)、[PR #845](https://github.com/nashsu/llm_wiki/pull/845)、[PDF 解析偏差 #806](https://github.com/nashsu/llm_wiki/issues/806)、[寫回問題 #848](https://github.com/nashsu/llm_wiki/issues/848)。

**明日觀察清單**

下一期目標日為 2026-11-13（若明日台北日曆日 11 月 14 日執行）。

- Codex Security／Cloudflare skill：追蹤續跑、成本控制與不可信工作區相關修正；先設計同一測試倉庫的覆蓋、誤報、驗證成本比較，再決定課程示範。來源：[Security release](https://github.com/openai/codex-security/releases)、[Cloudflare #148](https://github.com/cloudflare/security-audit-skill/issues/148)。
- Orca／OpenBot：看新版效能、任務隔離與升級回報；內容方向是「多 agent 分工如何留下可審閱證據」，不以平行數量代替成果品質。來源：[Orca releases](https://github.com/stablyai/orca/releases)、[OpenBot releases](https://github.com/CopilotKit/OpenBot/releases)。
- agent-skills／Astryx：確認熱度是否延續、是否伴隨實質更新，再挑一個工程流程與一個 UI 任務做可重現 Demo。來源：[Agent Skills](https://github.com/addyosmani/agent-skills)、[Astryx](https://github.com/meta/astryx)。
- Qwen Code：建立第二次星數基準，分清 SDK／CLI／Preview 版本；再比較同一中文開發任務的成功率、權限與成本。來源：[Qwen Code releases](https://github.com/QwenLM/qwen-code/releases)。
- know metabiz wiki：比較 llm-wiki-agent 的 Markdown 流程與 llm_wiki 桌面方案；重點是來源可回溯、刪除同步、矛盾標記、PDF 正確率及授權，不直接導入正式文件。來源：[Wiki Agent](https://github.com/SamurAIGPT/llm-wiki-agent)、[LLM Wiki issues](https://github.com/nashsu/llm_wiki/issues)。
- Activepieces：核對授權與具體連接器權限，選一條需要人工審閱的資料整理流程；不要只按 connector 數量判斷導入價值。來源：[README](https://github.com/activepieces/activepieces#readme)、[release](https://github.com/activepieces/activepieces/releases/tag/0.93.0)。
- 推論工具維持次級觀察：TensorFold 與 llama.cpp 雖上榜，但先等待本機測速、模型相容與硬體成本證據；free-claude-code 的免費用量宣稱未獨立驗證，且前次授權不明，不列入本次推薦採用。來源：[Trending daily](https://github.com/trending?since=daily)。

**資料範圍與限制**

原始 Trending 擷取摘要在 trending-daily.json；README（每項最多 22,000 字元）、release 摘錄與最近五筆 Issue／PR 在 review-evidence.json；查詢與配額重跑紀錄在 run-status.json；逐項抓取紀錄在 collector log。純代理工具、規則式股票篩選與 README 實為遊戲外掛的項目已排除；改名倉庫以 canonical full_name 合併重複記錄，理由在 scope-audit.json。先前各日產物未改動。

收集器沿用歷史 metadata 的項目數：6。若非零，這些項目不能視為本次成功更新；名稱另存 repos.json 的 carried_forward_repositories。未上榜、沒有 release、低星數或低 Issue 數都不單獨代表品質較差。授權不明與問題回報是待查證風險，不等於已確認缺陷影響所有使用者。

候選來源：[GitHub Trending daily](https://github.com/trending?since=daily)；各專案數值以當次 GitHub REST API 回應為準。快照前期目標日：2026-11-11；本期目標日：2026-11-12；觀察時間：2026-11-13T00:25:44.979837+08:00。
