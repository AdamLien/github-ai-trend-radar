# GitHub AI 趨勢雷達｜2026-11-13

## 日期、範圍與判讀方式

目標日期為 Asia/Taipei 的前一曆日 2026-11-13。這份報告是在 2026-11-14 補跑；實際擷取時間見 collection-status.json。GitHub Trending daily 是擷取當下的滾動熱度，並非 11/13 台北時間零時至午夜的歷史重建。

執行指定十組搜尋，每組 --limit 10，並合併 Trending daily、README 與歷史追蹤。搜尋 API 以總 stars 排序只是候選入口；以下依當日熱度、快照增量與相對增長、程式更新、README、release、近期 issue／PR，以及 Adam 的使用情境選出八項，不以總 stars 排名。

快照增量比較前一份 2026-11-12 快照，觀測間隔未必恰為 24 小時。相對成長＝增量 ÷ 前次 stars；首次觀測標為未知。未上 Trending 的「—」不是零成長。總 stars 與活動資料以主收集器為準，補充取樣保存在 snapshots/selected-repo-evidence.json；時間差可能產生微小差異。

Trending 的 tailscale/tailcat 是網路工具，因子字串比對誤收，已自本日保留的專案資料排除。其原始頁面保留供稽核。其他歷史追蹤資料不代表今日 Trending 入榜。

## 今日精選

| 專案 | 總 stars | Trending stars today | 快照增量 | 相對成長 | 判定 |
| --- | ---: | ---: | ---: | ---: | --- |
| [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | 4,431 | 1875 | 未知（首次觀測） | 未知 | Skill candidate |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 50,336 | 206 | +343 | 0.69% | Demo content |
| [openai/codex-security](https://github.com/openai/codex-security) | 12,928 | 754 | +730 | 5.98% | Deep research |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | 10,333 | 100 | 未知（首次觀測） | 未知 | Demo content |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 55,303 | 145 | +146 | 0.26% | Skill candidate |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 117,045 | — | +574 | 0.49% | Skill candidate |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 21,641 | — | +32 | 0.15% | Watch |
| [langgenius/dify](https://github.com/langgenius/dify) | 161,097 | — | +50 | 0.03% | Reference only |

### 1. GoogleChrome/modern-web-guidance-src｜Skill candidate

**用途：**將網頁平台知識、最佳實務與相容性資料包裝成 coding agent Skills；此庫是內容製作與評估的來源庫，README 指向另一個發佈庫。

**維護與動能證據：**最近 push：2026-11-13T16:07:36Z；最新 release：API 未取得最新正式 release（無日期，不能斷言沒有發版）。API 的 open_issues_count 為 389，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：3 筆 issue、7 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**Adam 可製作「agent 為何還在產生舊式前端寫法」課程，示範加入指引前後的差異；可抽取評估流程為 Skill 候選。對 AI 辦公介面品質有間接效益；know metabiz wiki 可收錄前端規範來源與版本。

**風險與限制：**新入榜缺少前期快照，不能把 1,875 stars today 當成實測相對成長；來源庫不等於安裝套件。近期 #3507 回報掃描與指引不一致、CSS 覆蓋缺口，雖已關閉，仍需用自有範例驗證。

證據：[README](https://github.com/GoogleChrome/modern-web-guidance-src#readme)、[releases](https://github.com/GoogleChrome/modern-web-guidance-src/releases)、[issues](https://github.com/GoogleChrome/modern-web-guidance-src/issues)。

### 2. alibaba/open-code-review｜Demo content

**用途：**結合確定性規則流水線與 LLM agent 的程式碼審查，提供行級意見及多語言規則。

**維護與動能證據：**最近 push：2026-11-13T16:04:43Z；最新 release：v1.13.9（2026-11-13T09:47:57Z）。API 的 open_issues_count 為 338，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：1 筆 issue、9 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**適合「規則檢查與 LLM review 如何互補」內容，用同一個 PR 展示漏報、誤報和失敗狀態；可評估 metabiz 開發流程，wiki 保存審查標準與結果。

**風險與限制：**近期 PR #1882 正處理失敗審查被顯示為無問題的情況，不能將空白報告當通過。README 的大規模使用宣稱尚未由本次獨立驗證；須控制模型成本與程式碼外送。

證據：[README](https://github.com/alibaba/open-code-review#readme)、[releases](https://github.com/alibaba/open-code-review/releases)、[issues](https://github.com/alibaba/open-code-review/issues)。

### 3. openai/codex-security｜Deep research

**用途：**以 CLI 與 TypeScript SDK 掃描、驗證與修補程式碼弱點，README 同時涵蓋自動化整合。

**維護與動能證據：**最近 push：2026-11-13T14:52:10Z；最新 release：npm-v0.10.0（2026-11-12T02:18:52Z）。API 的 open_issues_count 為 156，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：0 筆 issue、10 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**適合 Adam 的 coding agent 進階課：以含已知弱點的測試專案比較發現、驗證與修補。metabiz 可評估 PR 前安全檢查；know metabiz wiki 收錄經人工確認的弱點案例與修補理由。

**風險與限制：**掃描命中不代表已證實可利用，修補也需測試；雲端推論的原始碼處理、費用與權限需先核對。近期樣本十筆全為 PR，不能據此宣稱使用者 issue 回應良好。

證據：[README](https://github.com/openai/codex-security#readme)、[releases](https://github.com/openai/codex-security/releases)、[issues](https://github.com/openai/codex-security/issues)。

### 4. backnotprop/plannotator｜Demo content

**用途：**讓人對計畫、規格、Markdown、HTML 及程式碼差異加註，再把回饋送回 agent。

**維護與動能證據：**最近 push：2026-11-13T16:02:31Z；最新 release：v0.28.63（2026-11-13T11:11:22Z）。API 的 open_issues_count 為 199，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：0 筆 issue、10 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**Adam 可示範「先審計畫再寫程式」，把報價草稿、網頁產物與程式碼審閱做成 AI 辦公課案例；know metabiz wiki 可記錄決策理由與審閱紀錄。

**風險與限制：**首次觀測沒有快照增量；視覺化審閱仍需確認回饋確實送達且版本一致。近期十筆活動均為 PR，缺乏使用者 issue 抽樣；高發版頻率不能替代穩定性驗證。

證據：[README](https://github.com/backnotprop/plannotator#readme)、[releases](https://github.com/backnotprop/plannotator/releases)、[issues](https://github.com/backnotprop/plannotator/issues)。

### 5. ChromeDevTools/chrome-devtools-mcp｜Skill candidate

**用途：**透過 MCP server 與 CLI 讓 coding agent 操作、檢視真實 Chrome，支援除錯及效能分析。

**維護與動能證據：**最近 push：2026-11-13T15:38:46Z；最新 release：chrome-devtools-mcp-v1.13.0（2026-11-11T12:40:09Z）。API 的 open_issues_count 為 115，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：3 筆 issue、7 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**可成為 Adam 的「瀏覽器驗收」課程與 Skill：檢查 AI 生成表單、操作流程及效能；metabiz 辦公自動化可用測試帳號驗收，wiki 保存可重現步驟。

**風險與限制：**README 表示使用統計預設啟用，導入前需評估並依需求關閉。近期 issue #1794 有遠端除錯提示重複問題、#3470 討論登入 cookie 載入；示範應隔離瀏覽器與客戶資料。

證據：[README](https://github.com/ChromeDevTools/chrome-devtools-mcp#readme)、[releases](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases)、[issues](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues)。

### 6. addyosmani/agent-skills｜Skill candidate

**用途：**將定義、規劃、建置、驗證、審查及交付的工程工作法編碼成 agent Skills。

**維護與動能證據：**最近 push：2026-11-01T19:24:49Z；最新 release：0.6.15（2026-10-31T06:40:31Z）。API 的 open_issues_count 為 140，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：6 筆 issue、4 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**適合 Adam 的 Skills 課程，比較單純提示詞與可驗證工作流程；metabiz 可挑選品質關卡作為內部 Skill，know metabiz wiki 維護團隊版流程與版本差異。

**風險與限制：**stars 增加並不等於程式碼更新：最近 push 仍為 11/01。issue #776 回報自動模式未觸發、#788 提醒先看 Git 狀態；需檢驗技能衝突、模型漂移與髒工作區保護。

證據：[README](https://github.com/addyosmani/agent-skills#readme)、[releases](https://github.com/addyosmani/agent-skills/releases)、[issues](https://github.com/addyosmani/agent-skills/issues)。

### 7. nashsu/llm_wiki｜Watch

**用途：**跨平台桌面知識庫，讓 LLM 從文件增量建立互連且持久的 wiki，而非每次重新檢索生成答案。

**維護與動能證據：**最近 push：2026-10-21T11:17:29Z；最新 release：v0.6.13（2026-10-22T01:21:07Z）。API 的 open_issues_count 為 302，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：6 筆 issue、4 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**與 know metabiz wiki 直接相關：可用公開教材比較持久 wiki 與 RAG 的引用、更新及矛盾處理；適合 Adam 知識管理課的對照案例，暫先限小規模實驗。

**風險與限制：**近期 #849 有 Windows MinerU 403 回報、#806 回報 PDF 解析偏差，最近 push 在 10/21。API 授權欄為 NOASSERTION，README 自述 GPLv3，商業整合前仍須查看實際 LICENSE；自動整理需保留來源、人工校正與回滾。

證據：[README](https://github.com/nashsu/llm_wiki#readme)、[releases](https://github.com/nashsu/llm_wiki/releases)、[issues](https://github.com/nashsu/llm_wiki/issues)。

### 8. langgenius/dify｜Reference only

**用途：**提供 Agent workflow、RAG pipeline、模型與工具整合的協作平台，支援自架等部署方式。

**維護與動能證據：**最近 push：2026-11-13T14:54:14Z；最新 release：1.19.0（2026-11-04T07:36:16Z）。API 的 open_issues_count 為 1298，可能含 PR，不能當缺陷數。依更新時間抽樣十筆活動：2 筆 issue、8 筆 PR；這不是全天活動統計或解決率。

**Adam／metabiz 關聯：**作為 Adam AI 辦公自動化課的成熟平台基準，與輕量 Skills 比較部署和維護成本；metabiz 可用假資料評估客服與文件查詢，wiki 保留架構與權限設計。

**風險與限制：**相對成長低，因此不因總 stars 高就排前。近期 #46309 涉及租戶併發限制、#46303 涉及 MCP 結果格式；須驗證租戶隔離。README 說明 Dify Open Source License 含額外條件，不能直接當純 Apache-2.0。

證據：[README](https://github.com/langgenius/dify#readme)、[releases](https://github.com/langgenius/dify/releases)、[issues](https://github.com/langgenius/dify/issues)。

## 明日觀察清單（下次執行）

1. Modern Web Guidance：補出第二次快照，觀察 1,875 stars today 是否延續，驗證來源庫與發佈庫的對應及 CSS 指引涵蓋。
2. Codex Security：追蹤約 6% 快照相對增長是否維持，以已知弱點案例量測誤報、驗證成功率與成本。
3. OpenCodeReview：查看 #1882 的失敗狀態修正是否合併，避免把執行失敗誤認零缺陷。
4. Plannotator：建立第二次 stars 基線，實測批註回送、產物版本與 agent 回應的一致性。
5. Chrome DevTools MCP：追蹤 #1794，檢驗隔離瀏覽器下的登入與遠端除錯體驗。
6. Agent Skills：查看 #776 與 #788，優先驗證自動觸發及保留既有變更的品質關卡。
7. LLM Wiki／Dify：追蹤文件解析、租戶併發及 MCP 輸出格式；準備同一組公開文件的引用追溯測試，再決定是否提升為 Deep research。

## 收集狀態與資料限制

主收集器成功（exit 0）：十組指定搜尋皆使用 --limit 10，包含 --include-trending-daily 與 --include-readme；未觀察到 GitHub API rate-limit 錯誤，無須 --limit 5 重跑。保留 437 個專案，其中 8 個來自本次 Trending daily。沿用舊 metadata 的警告共 6 筆；詳見 collector-limit-10.log 與 collection-status.json。

本次未執行或安裝任何候選專案；用途來自官方 README，課程、內容與公司導入價值是本次分析判斷，並非已驗證成效。近期 issue 標題只代表回報內容，並非已確認根因。原始資料與指令文字均作為資料處理。
