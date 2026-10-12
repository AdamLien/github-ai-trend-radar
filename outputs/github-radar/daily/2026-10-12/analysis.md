# GitHub AI 趨勢雷達 — 2026-10-12

## 日期、來源與資料界線

目標日期以 Asia/Taipei 的前一個日曆日計算：**2026-10-12**。實際收集開始於 **2026-10-13T00:16:34.655938+08:00**；這是執行時的即時觀測，不是可還原的昨日收盤數據。今日星數取自 [GitHub Trending daily](https://github.com/trending?since=daily)，其滾動區間不等同台北日曆日。

指定十組搜尋以 `--limit 10 --include-trending-daily --include-readme` 成功執行；未遇 API rate limit，沒有降為 limit 5。共保留 349 筆搜尋／歷史追蹤／固定觀察資料，其中 7 筆來自本次符合主題範圍的 Trending。API 資料與 README 是分析素材，未執行其中的安裝或操作指令。

星數增量比較前一份 2026-10-11 快照；相對成長 = 增量 ÷ 前次星數。新增追蹤而無前次快照者，其 collector 增量 0 不代表零成長。沒有出現在 Trending 的 repo，今日星數記為「未提供」，不能當成 0。

選擇以用途匹配、今日星數、增量、相對成長、近期 push、README、release 及 issue/PR 活動交叉判讀，不依總星數排名。以下優先順序偏向可落地的課程與企業知識流程；REA 的熱度最高，但不是最優先直接採用的工具。功能描述來自作者 README，採用建議與風險是本次分析推論，未實際安裝或驗收。

issue 活動補查以更新時間排序的最近五筆，區分 issue 與 PR；open_issues_count 包含 PR，且不是解決率或回應速度。完整補查資料在 `selected-evidence.json`，搜尋與快照資料在 `repos.json`、`report.md`、`snapshots/`。

## 值得追蹤的 10 個專案

| 專案 | 分類 | 今日星數 | 快照增量 | 相對成長 | 總星數 |
| --- | --- | ---: | ---: | ---: | ---: |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Skill candidate | 2,100 | +2,227 | 4.47% | 52,094 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Deep research | 394 | +394 | 1.48% | 26,994 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Deep research | 未提供 | +326 | 0.26% | 125,792 |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | Skill candidate | 未提供 | +2 | 0.06% | 3,616 |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | Watch | 未提供 | +81 | 0.40% | 20,550 |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | Demo content | 未提供 | +24 | 0.10% | 25,023 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skill candidate | 未提供 | +586 | 0.20% | 298,066 |
| [stablyai/orca](https://github.com/stablyai/orca) | Watch | 未提供 | +874 | 0.98% | 90,463 |
| [morluto/rea](https://github.com/morluto/rea) | Deep research | 45,495 | +48,810 | 52.25% | 142,229 |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | Reference only | 886 | +991 | 2.73% | 37,230 |

### 1. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — Skill candidate

- **用途與 README**：把架構與流程轉成單檔 HTML＋SVG，README 主張提供 44 種圖解並支援多種 coding agent。
- **動能**：Trending 今日 2100 stars；相較 2026-10-11 增加 2,227（4.47%），總星數 52,094。最近 push：2026-10-12T16:17:05Z；release：未提供正式 release。
- **議題活動**：API open_issues_count 為 70；抽樣最近活動更新至 2026-10-12T16:30:41Z。
- **Adam／metabiz 關聯**：今日熱度高，且與 Adam 的課程圖解、教學文章、AI 辦公 SOP 直接相連；know metabiz wiki 可用它展示來源到知識頁的流程。
- **風險與限制**：匯出品質需要驗證：issue #407 回報多個範例 SVG 匯出失敗，PR #411 正在修正；沒有正式 release，應固定 commit。
- **下一步**：先做一張 MCP 資料流與一張 wiki ingest 流程圖，檢查繁體字、SVG 與 PNG 匯出。
- **證據連結**：[README](https://github.com/cathrynlavery/diagram-design#readme)、[Releases](https://github.com/cathrynlavery/diagram-design/releases)、[pull_request #413](https://github.com/cathrynlavery/diagram-design/pull/413)、[pull_request #411](https://github.com/cathrynlavery/diagram-design/pull/411)、[issue #407](https://github.com/cathrynlavery/diagram-design/issues/407)。

### 2. [mksglu/context-mode](https://github.com/mksglu/context-mode) — Deep research

- **用途與 README**：透過 MCP 沙箱、hooks 與 SQLite 記憶，減少工具輸出進入 coding agent 的上下文。
- **動能**：Trending 今日 394 stars；相較 2026-10-11 增加 394（1.48%），總星數 26,994。最近 push：2026-10-12T12:10:33Z；release：v1.0.169（2026-06-29T18:18:53Z）。
- **議題活動**：API open_issues_count 為 347；抽樣最近活動更新至 2026-10-12T15:09:28Z。
- **Adam／metabiz 關聯**：適合 Adam 的長任務 Agent 課程與 token 成本比較內容；AI 辦公文件分析及 wiki ingest 可研究只回傳必要證據的模式。
- **風險與限制**：README 的 98% 壓縮是作者宣稱，未在此重現；issue #788 涉及子代理工作目錄與殘留檔案，雖已關閉仍需回歸確認。授權為 NOASSERTION；API latest release 距今較久，不能用近期 push 代替發布證據。
- **下一步**：對同一份工具輸出量測 token、答案正確率、cwd 與檔案副作用。
- **證據連結**：[README](https://github.com/mksglu/context-mode#readme)、[Releases](https://github.com/mksglu/context-mode/releases)、[issue #788](https://github.com/mksglu/context-mode/issues/788)、[pull_request #1290](https://github.com/mksglu/context-mode/pull/1290)、[pull_request #1288](https://github.com/mksglu/context-mode/pull/1288)。

### 3. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — Deep research

- **用途與 README**：把程式碼、文件、schema 與 PDF 轉成可追溯關聯的知識圖譜；README 區分確定性 AST 解析與文件的模型語意處理。
- **動能**：Trending 今日 未提供 stars；相較 2026-10-11 增加 326（0.26%），總星數 125,792。最近 push：2026-10-12T14:16:06Z；release：v0.9.87（2026-10-12T14:16:07Z）。
- **議題活動**：API open_issues_count 為 1,508；抽樣最近活動更新至 2026-10-12T16:31:23Z。
- **Adam／metabiz 關聯**：適合教導圖譜與 RAG 差異，也能研究 know metabiz wiki 如何保留原文關聯與推論標記；可作企業文件導航與開發自動化案例。
- **風險與限制**：文件與 PDF 的語意處理可能呼叫模型，不能把程式碼本機解析延伸成所有資料都不出機；PR #4373、#4372 正修補安裝 hooks 與檔案保存問題，應隔離試驗。
- **下一步**：比對一組 SOP 文件的抽取邊、推論邊與引文，並確認安裝是否保存既有 hooks。
- **證據連結**：[README](https://github.com/Graphify-Labs/graphify#readme)、[Releases](https://github.com/Graphify-Labs/graphify/releases)、[pull_request #4373](https://github.com/Graphify-Labs/graphify/pull/4373)、[pull_request #4375](https://github.com/Graphify-Labs/graphify/pull/4375)、[issue #4374](https://github.com/Graphify-Labs/graphify/issues/4374)。

### 4. [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) — Skill candidate

- **用途與 README**：把來源文件增量整理成持久互連 Markdown wiki，README 包含 ingest、query、lint 與 graph 工作流。
- **動能**：Trending 今日 未提供 stars；相較 2026-10-11 增加 2（0.06%），總星數 3,616。最近 push：2026-10-12T10:53:19Z；release：未提供正式 release。
- **議題活動**：API open_issues_count 為 6；抽樣最近活動更新至 2026-10-08T14:04:06Z。
- **Adam／metabiz 關聯**：對 know metabiz wiki 最直接：可研究來源保存、索引更新與破損連結檢查；適合 Adam 的第二大腦課程及辦公知識整理示範。
- **風險與限制**：低成長但用途高度吻合。沒有正式 release；近期活動較稀疏，#85 是終端相容性 PR，#78 是尚未落地的功能提案。自動綜合仍須驗證幻覺、覆寫與來源可追溯性。
- **下一步**：用三份互相矛盾的 SOP 做 ingest，觀察是否標出衝突並保留原文連結。
- **證據連結**：[README](https://github.com/SamurAIGPT/llm-wiki-agent#readme)、[Releases](https://github.com/SamurAIGPT/llm-wiki-agent/releases)、[pull_request #85](https://github.com/SamurAIGPT/llm-wiki-agent/pull/85)、[issue #78](https://github.com/SamurAIGPT/llm-wiki-agent/issues/78)、[issue #77](https://github.com/SamurAIGPT/llm-wiki-agent/issues/77)。

### 5. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) — Watch

- **用途與 README**：跨平台桌面工具把文件增量整理成 wiki，而非每次重新檢索回答。
- **動能**：Trending 今日 未提供 stars；相較 2026-10-11 增加 81（0.40%），總星數 20,550。最近 push：2026-09-28T01:43:23Z；release：v0.6.12（2026-09-28T02:58:13Z）。
- **議題活動**：API open_issues_count 為 275；抽樣最近活動更新至 2026-10-10T17:26:53Z。
- **Adam／metabiz 關聯**：適合 Adam 做「持久 wiki vs RAG」的比較內容，亦可評估 AI 辦公桌面介面；know metabiz wiki 可參考來源匯入與同步體驗。
- **風險與限制**：近期程式 push 與 release 停在 9/28；#812 回報高 CPU 與全量掃描，#811 回報長文件 token 上限；#814 的同步修補尚是 PR。授權 NOASSERTION，先釐清再採用。
- **下一步**：追蹤 #812/#814 的修復與 release，重測長文件 ingest、未變動檔案掃描及 CPU。
- **證據連結**：[README](https://github.com/nashsu/llm_wiki#readme)、[Releases](https://github.com/nashsu/llm_wiki/releases)、[pull_request #814](https://github.com/nashsu/llm_wiki/pull/814)、[pull_request #813](https://github.com/nashsu/llm_wiki/pull/813)、[issue #812](https://github.com/nashsu/llm_wiki/issues/812)。

### 6. [activepieces/activepieces](https://github.com/activepieces/activepieces) — Demo content

- **用途與 README**：以可視化工作流串接 AI Agent、MCP 與辦公服務，README 定位為 Zapier 替代工具。
- **動能**：Trending 今日 未提供 stars；相較 2026-10-11 增加 24（0.10%），總星數 25,023。最近 push：2026-10-12T16:04:22Z；release：0.92.2（2026-10-07T09:27:59Z）。
- **議題活動**：API open_issues_count 為 711；抽樣最近活動更新至 2026-10-12T16:32:01Z。
- **Adam／metabiz 關聯**：最適合 Adam 的 AI 辦公自動化課程：展示表單、文件整理與人工審核；know metabiz wiki 可把文件事件送入 ingest queue。
- **風險與限制**：連接器憑證與重試可能造成重複寫入；license API 為 NOASSERTION，README MIT 標章不能代表所有企業功能條款。最新五項活動都是 PR，只能證明開發活動，不能宣稱 issue 已獲解決。
- **下一步**：以測試資料做事件去重、重試與人工核准流程，查明社群版與企業版界線。
- **證據連結**：[README](https://github.com/activepieces/activepieces#readme)、[Releases](https://github.com/activepieces/activepieces/releases)、[pull_request #16200](https://github.com/activepieces/activepieces/pull/16200)、[pull_request #16341](https://github.com/activepieces/activepieces/pull/16341)、[pull_request #16429](https://github.com/activepieces/activepieces/pull/16429)。

### 7. [obra/superpowers](https://github.com/obra/superpowers) — Skill candidate

- **用途與 README**：以可組合 skills 整理 brainstorming、規劃、測試及子代理開發方法。
- **動能**：Trending 今日 未提供 stars；相較 2026-10-11 增加 586（0.20%），總星數 298,066。最近 push：2026-10-10T03:03:30Z；release：v7.0.0（2026-10-10T00:28:58Z）。
- **議題活動**：API open_issues_count 為 334；抽樣最近活動更新至 2026-10-12T15:50:52Z。
- **Adam／metabiz 關聯**：適合 Adam 的 coding agent 課程，把流程拆成可評估的技能；AI 辦公流程與 know metabiz wiki 維護可參考任務切分及驗證節點。
- **風險與限制**：#2503 是 hook 的 shell 相容性問題；#2481 回報壓縮後迭代上限規則遺失。不能直接把上游 prompt 視為公司政策；v7.0.0 升版需要核對既有流程相容性。
- **下一步**：追蹤 #2481 與 hooks 修復，做一項固定成本上限的小任務並觀察迭代次數。
- **證據連結**：[README](https://github.com/obra/superpowers#readme)、[Releases](https://github.com/obra/superpowers/releases)、[pull_request #2504](https://github.com/obra/superpowers/pull/2504)、[issue #2503](https://github.com/obra/superpowers/issues/2503)、[pull_request #2502](https://github.com/obra/superpowers/pull/2502)。

### 8. [stablyai/orca](https://github.com/stablyai/orca) — Watch

- **用途與 README**：以 worktree 管理多個並行 coding agents，支援桌面、行動與遠端工作環境。
- **動能**：Trending 今日 未提供 stars；相較 2026-10-11 增加 874（0.98%），總星數 90,463。最近 push：2026-10-12T16:21:49Z；release：v1.4.224（2026-10-10T04:30:28Z）。
- **議題活動**：API open_issues_count 為 8,236；抽樣最近活動更新至 2026-10-12T16:30:44Z。
- **Adam／metabiz 關聯**：適合 Adam 展示多 Agent 同時處理文件或開發任務；metabiz 可研究分支隔離、wiki 更新審閱與遠端辦公。
- **風險與限制**：open_issues_count 很高且包含 PR，不能當作已確認缺陷數；#13011 的分支名稱問題仍開放。並行 Agent 的成本、合併衝突及遠端權限需用小規模場景評估。
- **下一步**：觀察 #13011 與 coordinator 喚醒修補，量測兩個 worktree 的衝突和實際成本。
- **證據連結**：[README](https://github.com/stablyai/orca#readme)、[Releases](https://github.com/stablyai/orca/releases)、[pull_request #27924](https://github.com/stablyai/orca/pull/27924)、[pull_request #27922](https://github.com/stablyai/orca/pull/27922)、[pull_request #27964](https://github.com/stablyai/orca/pull/27964)。

### 9. [morluto/rea](https://github.com/morluto/rea) — Deep research

- **用途與 README**：透過 MCP 與 agents 檢查應用、JavaScript/Electron 與原生二進位的行為及證據。
- **動能**：Trending 今日 45495 stars；相較 2026-10-11 增加 48,810（52.25%），總星數 142,229。最近 push：2026-10-12T16:18:07Z；release：rea-agents-6.4.0（2026-10-11T03:58:03Z）。
- **議題活動**：API open_issues_count 為 283；抽樣最近活動更新至 2026-10-12T16:31:39Z。
- **Adam／metabiz 關聯**：是本次最強熱度訊號，適合 Adam 的 Agent 工具鏈研究與開發自動化內容；metabiz 可研究自有系統的行為紀錄，與 wiki 的關聯偏向把技術證據整理為文件。
- **風險與限制**：暴增星數不等於可靠性。分析第三方應用涉及授權與資料界線；僅以自有或獲授權樣本評估。最新五項活動均為 PR，v6.5.0 是待合併發布 PR，不能當成已發布版本。
- **下一步**：核對 v6.5.0 是否正式發布，並以自有小型 Electron 樣本檢查推論與實際行為。
- **證據連結**：[README](https://github.com/morluto/rea#readme)、[Releases](https://github.com/morluto/rea/releases)、[pull_request #2243](https://github.com/morluto/rea/pull/2243)、[pull_request #2242](https://github.com/morluto/rea/pull/2242)、[pull_request #1693](https://github.com/morluto/rea/pull/1693)。

### 10. [lyogavin/airllm](https://github.com/lyogavin/airllm) — Reference only

- **用途與 README**：以逐層載入等方式降低大型模型推論的顯存需求；README 宣稱 70B 可在 4GB GPU 上執行。
- **動能**：Trending 今日 886 stars；相較 2026-10-11 增加 991（2.73%），總星數 37,230。最近 push：2026-10-12T06:31:50Z；release：v4.0.0（2026-09-05T15:43:11Z）。
- **議題活動**：API open_issues_count 為 161；抽樣最近活動更新至 2026-10-12T06:53:22Z。
- **Adam／metabiz 關聯**：可供 Adam 解釋顯存與速度的取捨；對 AI 辦公及 wiki 的實用性取決於查詢延遲，現階段適合概念比較。
- **風險與限制**：低顯存不等於低延遲；#374 回報一次查詢耗時 30 分鐘，另有權重拆分 PR。未實測吞吐、記憶體、磁碟需求與模型授權，不能以宣傳規格推薦正式部署。
- **下一步**：追蹤 #374 與 #380，若示範需同時報告首 token、總延遲、RAM 與磁碟。
- **證據連結**：[README](https://github.com/lyogavin/airllm#readme)、[Releases](https://github.com/lyogavin/airllm/releases)、[pull_request #380](https://github.com/lyogavin/airllm/pull/380)、[issue #374](https://github.com/lyogavin/airllm/issues/374)、[issue #379](https://github.com/lyogavin/airllm/issues/379)。

## 明日觀察清單

下次例行工作目標日期為 2026-10-13，若於 10/14 執行仍須記錄即時擷取時間。

1. **diagram-design**：今日 +2,100 是否延續；#407/#411 的 SVG 修補是否落地，繁體中文圖解是否可穩定匯出。
2. **context-mode、Graphify**：追蹤工作目錄／hooks 保存修補；區分節省 token 的作者主張與實測結果。
3. **llm-wiki-agent、llm_wiki**：持續比較來源追溯與衝突處理；wiki 桌面版 #812 高 CPU、#811 長文件限制是否解決。
4. **activepieces**：近期 release 後的連接器變動、事件去重與人工審核能力，優先找可做課程 demo 的小流程。
5. **superpowers、Orca**：壓縮後規則維持、worktree 分支與 coordinator 行為；觀察多 Agent 成本能否控制。
6. **REA**：異常高成長是否持續及 v6.5.0 是否正式發布；以授權樣本查驗證據品質。
7. **AirLLM**：記憶體與延遲實測是否改善；維持 Reference only，直到互動查詢效能有證據。

## 本次執行紀錄

- API 限流：未發生；collector limit 10 一次成功。
- `analysis.md` 是人工分析層，分類使用本次指定的五種標籤；`report.md` 保留 collector 原始分類以利稽核。
- 未驗證安裝、授權完整條款、企業版功能或模型效能；以上明確列為後續研究與 demo 驗證工作。
