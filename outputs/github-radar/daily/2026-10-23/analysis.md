# GitHub AI 趨勢雷達｜2026-10-23

本次優先研究安全稽核 Skill、agent 執行隔離與職務流程外掛；另保留與 know metabiz wiki 直接相關的圖譜、記憶與文件整編專案。下列順序為編輯判斷，綜合今日星數、快照成長／相對成長、更新、release、README、issue 與 Adam 的實用情境，並非總星數排名。

## 資料口徑與收集狀態

- 目標日期：2026-10-23（前一個 Asia/Taipei 日曆日）；實際執行：2026-10-24T00:11:00.664371+08:00。GitHub API 與 Trending 是執行時觀測，並非重建 10/23 午夜的歷史截面。
- 來源：[GitHub Trending daily](https://github.com/trending?since=daily)、GitHub repository／README／latest release API，以及最近更新的 issue/PR 清單。Trending 的 stars today 為 GitHub 顯示的滾動口徑，不等同台北單日新增星數。
- Δ 為與最近可用快照 2026-10-21 的星數差；跨兩個目標日期，實際觀測間距未正規化。相對成長 = Δ／前次總星數，不能稱為單日成長率。新收錄且無前值者一律顯示「未測」。未上 Trending 者顯示「—」，不等同 0。
- 搜尋每組最多 10 筆，按 GitHub 搜尋總星數排序，因此有成熟專案偏差；再合併 Trending 與歷史追蹤，分析改用動能、可用性與情境重排。
- Issue 樣本每庫取最近更新 10 筆 issue/PR 後移除 PR，不代表全部 issue 活動；open_issues_count 包含 PR，也不等同缺陷數。issue 內容皆為回報，未自行重現。release 缺值僅代表未取得 latest release，不推定沒有開發活動。
- 未偵測到 GitHub API 限流；使用 --limit 10 完成，未觸發 --limit 5 重跑。
- 差值校正：原收集器遇到 10/22 資料夾缺 repos.json 時未回溯可用前值，本次僅校正今日輸出，改以最近可用的 10/21 完整資料重算 Δ，未改動收集器或舊日產物。
- 舊資料沿用：BarberNumber/Midjourney-Software (HTTP 404)、hanshaze/Awesome-Prediction-Market-Trading-Tools (HTTP 404)、mingrath/obsidian-ai-knowledge-agent (HTTP 404)、tonhowtf/omniget (HTTP 404)。這些項目未取得本次 metadata，已標記 metadata_stale，不作為今日維護動能證據。
- 範圍校正：排除純排盤、通用代理、service mesh 觀測、安全函式庫清單與通用節點 UI；補入收集器關鍵字漏掉的 AI 語音專案 OpenBMB/VoxCPM。原始 Trending 卡片保留在 snapshots/trending-daily.json 供核對；只將相關專案保留於 repos.json 與 report.md。
- 未安裝、執行任何候選 repo 的程式或 Skill；以下採用建議為研究判斷，並非已完成實測。

## 值得投入的 10 個專案

| 專案 | 分類 | 總 stars | Trending stars today | Δ vs 10/21 | 相對成長 |
|---|---|---:|---:|---:|---:|
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Skill candidate | 41,326 | 2706 | +5,918 | +16.71% |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Deep research | 18,487 | 1240 | +1,532 | +9.04% |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Demo content | 32,039 | 643 | +950 | +3.06% |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Watch | 12,938 | — | +808 | +6.66% |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 133,693 | — | +2,495 | +1.90% |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Deep research | 77,626 | — | +533 | +0.69% |
| [stablyai/orca](https://github.com/stablyai/orca) | Demo content | 103,517 | — | +2,692 | +2.67% |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Deep research | 20,921 | — | +65 | +0.31% |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | Demo content | 25,187 | — | +35 | +0.14% |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Watch | 40,095 | 144 | 未測 | 未測 |

### 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — Skill candidate

- **用途／README**：將安全稽核分成探索、覆蓋追蹤、候選驗證與獨立複核，輸出結構化 findings。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-09-14T19:29:02Z`（UTC），latest release `未取得`／`—`。API 開啟 issue/PR 合計 81；本次取得 3 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：可把「可追溯證據與反證」做成 Adam 的 coding agent 課程與短內容；metabiz 可研究售前／交付程式碼檢核 Skill，know metabiz wiki 可存放經驗證的發現與修復紀錄。
- **風險與採用門檻**：熱度不代表稽核準確率；最新 push 與今日熱度須分開判讀。issue #94 回報輸出路徑與舊報告污染問題，尚未自行重現，正式採用前需驗證。
- **一手證據**：[README](https://github.com/cloudflare/security-audit-skill#readme)、[releases](https://github.com/cloudflare/security-audit-skill/releases)、[issue #94](https://github.com/cloudflare/security-audit-skill/issues/94)。 該 issue 狀態 `open`，更新 `2026-10-23T15:47:42Z`。

### 2. [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) — Deep research

- **用途／README**：提供 AI agent 執行沙箱、檔案與網路政策，以及憑證隔離機制。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-23T16:06:46Z`（UTC），latest release `v0.1.5`／`2026-10-20T17:28:32Z`。API 開啟 issue/PR 合計 567；本次取得 1 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：適合 Adam 講解 agent 權限邊界；AI 辦公自動化可研究限制 CRM／文件任務的存取範圍，know metabiz wiki 可建立執行政策與操作紀錄頁。
- **風險與採用門檻**：README 的隔離與政策驗證屬專案主張，未做本機實測；PTY 存取問題顯示互動工具相容性需要驗證。issue #749 已關閉，仍需確認部署版本是否涵蓋修復。
- **一手證據**：[README](https://github.com/NVIDIA/OpenShell#readme)、[releases](https://github.com/NVIDIA/OpenShell/releases)、[issue #749](https://github.com/NVIDIA/OpenShell/issues/749)。 該 issue 狀態 `closed`，更新 `2026-10-23T15:19:57Z`。

### 3. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — Demo content

- **用途／README**：將職務流程包成 skills、連接器、指令與 subagents，涵蓋生產力、銷售、客服等知識工作。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-23T07:38:30Z`（UTC），latest release `未取得`／`—`。API 開啟 issue/PR 合計 136；本次取得 2 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：最適合 Adam 的 AI 辦公課程示範：公開樣本客服問題轉知識文章、會議準備與銷售資料整理；可參考建立 know metabiz wiki 的職務 SOP。
- **風險與採用門檻**：連接器實際可用性與平台安裝方式需驗證；issue #1381 回報相對路徑 CONNECTORS.md 在 claude.ai 安裝時缺失，不能只展示 README 的完整流程。
- **一手證據**：[README](https://github.com/anthropics/knowledge-work-plugins#readme)、[releases](https://github.com/anthropics/knowledge-work-plugins/releases)、[issue #1381](https://github.com/anthropics/knowledge-work-plugins/issues/1381)。 該 issue 狀態 `open`，更新 `2026-10-23T03:51:45Z`。

### 4. [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) — Watch

- **用途／README**：讓 Claude Code、Codex、Cursor 等工具共享工作記憶與任務交接脈絡。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-23T01:47:40Z`（UTC），latest release `v3.2.2`／`2026-10-23T00:17:51Z`。API 開啟 issue/PR 合計 30；本次取得 5 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：適合 Adam 比較多 agent 交接與記憶治理；辦公任務可研究交接待辦，know metabiz wiki 可記錄已確認決策，但不應直接匯入未審核的對話偏好。
- **風險與採用門檻**：issue #1648 回報一次性 SDK prompt 被提升成跨專案預設偏好；此類污染可能跨任務擴散，先追蹤修復與隔離測試。
- **一手證據**：[README](https://github.com/akitaonrails/ai-memory#readme)、[releases](https://github.com/akitaonrails/ai-memory/releases)、[issue #1648](https://github.com/akitaonrails/ai-memory/issues/1648)。 該 issue 狀態 `open`，更新 `2026-10-23T15:43:42Z`。

### 5. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research

- **用途／README**：把程式碼、文件等來源轉成可查詢知識圖譜，區分來源明示與推論關係。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-22T16:19:38Z`（UTC），latest release `v0.9.94`／`2026-10-22T16:19:50Z`。API 開啟 issue/PR 合計 1626；本次取得 1 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：可做 Adam 的「圖譜與向量檢索」比較課；metabiz 可用公開 SOP、schema 與範例文件探索跨來源關係，know metabiz wiki 可評估來源追溯與更新成本。
- **風險與採用門檻**：README 的節省 token 與雲端能力未獨立驗證；issue #4711 回報特定 TypeScript decorator 解析會漏掉後續 symbols，圖譜缺項會影響結論可靠度。
- **一手證據**：[README](https://github.com/Graphify-Labs/graphify#readme)、[releases](https://github.com/Graphify-Labs/graphify/releases)、[issue #4711](https://github.com/Graphify-Labs/graphify/issues/4711)。 該 issue 狀態 `open`，更新 `2026-10-23T14:54:42Z`。

### 6. [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) — Deep research

- **用途／README**：在送入 LLM 前壓縮工具輸出、log、程式碼與 RAG 內容，提供 library、proxy 與 MCP 介面。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-22T14:23:37Z`（UTC），latest release `v0.41.0`／`2026-10-14T22:46:09Z`。API 開啟 issue/PR 合計 601；本次取得 3 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：適合 Adam 示範 token 成本與答案品質的取捨；辦公報表與 know metabiz wiki 檢索可用固定題集比較壓縮前後的引用完整度。
- **風險與採用門檻**：壓縮率與答案不退化是 README 主張，需自行測量；issue #3017 仍有 Claude Code 包裝後 API 錯誤回報，需分開檢查相容性、成本與正確性。
- **一手證據**：[README](https://github.com/headroomlabs-ai/headroom#readme)、[releases](https://github.com/headroomlabs-ai/headroom/releases)、[issue #3017](https://github.com/headroomlabs-ai/headroom/issues/3017)。 該 issue 狀態 `open`，更新 `2026-10-23T15:29:40Z`。

### 7. [stablyai/orca](https://github.com/stablyai/orca) — Demo content

- **用途／README**：在獨立 worktree 中並行管理 Codex、Claude Code 等 coding agents，提供桌面與行動協作介面。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-23T16:18:13Z`（UTC），latest release `v1.4.237`／`2026-10-21T07:25:23Z`。API 開啟 issue/PR 合計 9066；本次取得 1 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：適合 Adam 製作多 agent 平行開發示範與課程；metabiz 可研究工作分派、審查與交付流程，know metabiz wiki 可存任務決策與交接結果。
- **風險與採用門檻**：平行執行仍有衝突、資源與審核成本；issue #15784 有共享專案 Tasks 篩選錯誤回報。先以隔離範例驗證，不能由星數推論團隊效率。
- **一手證據**：[README](https://github.com/stablyai/orca#readme)、[releases](https://github.com/stablyai/orca/releases)、[issue #15784](https://github.com/stablyai/orca/issues/15784)。 該 issue 狀態 `open`，更新 `2026-10-23T16:11:01Z`。

### 8. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) — Deep research

- **用途／README**：將文件增量整理成互連 wiki，提供來源追溯、文件匯入與選用向量檢索。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-21T11:17:29Z`（UTC），latest release `v0.6.13`／`2026-10-22T01:21:07Z`。API 開啟 issue/PR 合計 282；本次取得 7 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：與 know metabiz wiki 最直接相關：比較來源原文、生成頁與更新衝突；Adam 可做「RAG 與持久 wiki」課程／內容，辦公自動化可示範會議資料到 SOP。
- **風險與採用門檻**：issue #828 回報本地 Ollama 大批 embedding 逾時，#231 仍要求 headless／服務化能力；需驗證繁中、權限、版本衝突與部署方式。
- **一手證據**：[README](https://github.com/nashsu/llm_wiki#readme)、[releases](https://github.com/nashsu/llm_wiki/releases)、[issue #828](https://github.com/nashsu/llm_wiki/issues/828)。 該 issue 狀態 `open`，更新 `2026-10-22T23:50:12Z`。

### 9. [activepieces/activepieces](https://github.com/activepieces/activepieces) — Demo content

- **用途／README**：以視覺流程與 TypeScript pieces 串接應用，並讓 pieces 可作為 MCP 工具。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-23T15:57:02Z`（UTC），latest release `0.92.3`／`2026-10-12T18:43:34Z`。API 開啟 issue/PR 合計 786；本次取得 2 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：適合 Adam 的非工程職 AI 辦公課：公開表單資料整理、摘要與知識文章草稿；metabiz 可研究 CRM／文件流程，know metabiz wiki 可保存流程 SOP 與錯誤處理。
- **風險與採用門檻**：授權與企業功能範圍需逐項確認；連接器數量在 README 與描述中有不同口徑。issue #16788 是日文翻譯同步遺失回報，繁中介面與連接器仍需實測。
- **一手證據**：[README](https://github.com/activepieces/activepieces#readme)、[releases](https://github.com/activepieces/activepieces/releases)、[issue #16788](https://github.com/activepieces/activepieces/issues/16788)。 該 issue 狀態 `open`，更新 `2026-10-23T13:49:48Z`。

### 10. [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) — Watch

- **用途／README**：開源語音生成專案；README 描述 VoxCPM2 支援多語 TTS、聲音設計與可控聲音複製。
- **動能與維護**：上表列出總星數、今日星數與相對成長；最新 push `2026-10-08T03:26:41Z`（UTC），latest release `2.0.3`／`2026-05-11T11:59:20Z`。API 開啟 issue/PR 合計 139；本次取得 1 筆非 PR issue 樣本。
- **Adam／metabiz 關聯**：可列為 Adam 課程旁白與短影音的候選 Demo；辦公自動化可研究公開通知語音，know metabiz wiki 可收錄聲音品質、資源需求與來源紀錄，與 wiki 核心架構關聯較低。
- **風險與採用門檻**：需測繁中發音、推論成本與聲音使用授權；issue #419 回報缺 C compiler 時 optimize 模式首次生成失敗。未執行模型或驗證 README 的效能主張。
- **一手證據**：[README](https://github.com/OpenBMB/VoxCPM#readme)、[releases](https://github.com/OpenBMB/VoxCPM/releases)、[issue #419](https://github.com/OpenBMB/VoxCPM/issues/419)。 該 issue 狀態 `open`，更新 `2026-10-23T14:27:56Z`。

## 明日觀察清單（2026-10-24）

1. **security-audit-skill**：今日 +2,706 的熱度是否延續；追蹤 #94 的路徑／舊報告污染回報，確認最新 push 與修復狀態。通過隔離範例驗證後再考慮移植 Skill。
2. **OpenShell**：追蹤 +1,240 stars today 後的相對成長與新 release；驗證互動 CLI、權限政策及 PTY 需要的設定，先整理成課程研究筆記。
3. **knowledge-work-plugins**：追蹤 +643 stars today 與 #1381 的 connector 文件安裝問題，挑一個客服／生產力外掛，用公開樣本做可重複的辦公 Demo。
4. **ai-memory／headroom／graphify**：分別追蹤 #1648、#3017、#4711；用同一組公開任務比較交接污染、token 成本／答題正確性與圖譜缺漏。
5. **llm_wiki／activepieces**：先設計 20 題繁中 SOP 與來源追溯評估，追蹤 embedding 逾時、headless 部署與翻譯流程；評估 know metabiz wiki 接入前的更新與權限成本。
6. **Orca／VoxCPM**：前者驗證 worktree 審查與任務篩選，後者測繁中旁白與編譯環境。兩者皆以可完成的小型 Demo 為採用門檻。

## 可重現性

- 查詢：`mcp server ai`；`model context protocol`；`agent skills coding agent`；`claude code template`；`codex skills`；`coding agent llm`；`rag knowledge base`；`ai wiki knowledge management`；`llm orchestration agent`；`developer automation ai`。
- 收集參數：`--limit 10 --include-trending-daily --include-readme --snapshot-date 2026-10-23 --out outputs/github-radar/daily/2026-10-23`；限流與執行結果見 `collection-status.json`。
- `repos.json` 與 `snapshots/repos-2026-10-23.json` 內容一致；`snapshots/editorial-evidence.json` 保存 README 與近期 issue 觀測，`report.md` 保存範圍校正後的量化報告。
