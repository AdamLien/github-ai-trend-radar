# GitHub AI 趨勢雷達｜2026-10-11

本次優先試用 diagram-design，並研究 rea 的異常高增長；Skills 課程候選以 agent-skills 與 mattpocock/skills 為主。知識庫方向先用 llm-wiki-agent 做小型來源匯入實驗，llm_wiki 則等同步與長文件問題確認後再評估。以上為基於公開資料的判斷，本次未安裝或實測候選工具。

## 資料範圍與判讀

- 目標日為台北時間前一天 2026-10-11；實際觀測與 API 收集在台北時間 2026-10-12 執行。目標資料夾是報表歸屬日，不能視為補取了歷史 Trending。
- 已執行指定 10 組查詢，每組 limit 10，包含 daily Trending 與 README；合併歷史追蹤及 pinned watchlist，共 351 個專案。Trending 取得 8 張卡片，保留 3 個符合 AI／agent／LLM 範圍的專案。
- 來源：[GitHub Trending daily](https://github.com/trending?since=daily)、GitHub repository／README／latest release API、候選最近 5 筆 issue／PR 更新；原始證據見 repos.json、trending-daily.json 與 activity-evidence.json。
- 「Trending today」是即時頁面數值；「快照增量」比較 2026-10-10 與本次快照，兩者觀測時間窗不同，不應混算。相對增長＝增量÷前次總星數；首次觀測的零增量代表沒有基線，不代表沒有成長。
- 選擇順序綜合即時增星、快照增量、相對增長、push、README、release、issue／PR 活動與 Adam 的工作適配度；用途與風險比星數排名更重要。open_issues 包含 PR，最近 5 筆活動只是樣本，不能推算全部維護品質。
- 未偵測到 API rate-limit 錯誤，因此未使用 limit 5 重試。4 個歷史專案 API 404 保留舊資料，已標記 metadata_reused，未列入精選：`BarberNumber/Midjourney-Software`, `hanshaze/Awesome-Prediction-Market-Trading-Tools`, `mingrath/obsidian-ai-knowledge-agent`, `tonhowtf/omniget`。

## 精選 10 個專案

| 專案 | 總星數 | Trending today | 快照增量 | 相對增長 | 分類 |
| --- | ---: | ---: | ---: | ---: | --- |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 49,867 | 1,083 | +1,234 | 2.54% | Skill candidate |
| [morluto/rea](https://github.com/morluto/rea) | 93,419 | 25,585 | +28,072 | 42.96% | Deep research |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 104,797 | — | +419 | 0.40% | Skill candidate |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 285,763 | — | +1,795 | 0.63% | Skill candidate |
| [stablyai/orca](https://github.com/stablyai/orca) | 89,589 | — | +568 | 0.64% | Demo content |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 20,469 | — | +42 | 0.21% | Watch |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 3,614 | — | +0 | 0.00% | Skill candidate |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | 24,999 | — | +22 | 0.09% | Demo content |
| [langgenius/dify](https://github.com/langgenius/dify) | 158,149 | — | +65 | 0.04% | Deep research |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | 36,239 | 541 | 無基線 | 無基線 | Watch |

### 1. cathrynlavery/diagram-design — Skill candidate

用途：將圖表設計規則包成 agent skill，輸出單一 HTML＋SVG，README 宣稱支援 44 種圖表。

動能與成熟度：最近 push 2026-10-10T21:10:14Z；release 本次 latest release API 未取得版本，不能據此推論完全沒有發布；API 授權欄位 MIT。README 摘錄已收集。近期[issue #401](https://github.com/cathrynlavery/diagram-design/issues/401)於 2026-10-11T14:06:19Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：最適合把 AI 課程架構、辦公流程、know metabiz wiki 關係圖製成示範內容；可先用一張真實課程圖測試。

風險：匯出目錄不可寫的例外與縮放相容性仍有待處理；目前無 latest release 記錄，需固定版本後驗證中文字型、匯出品質。

### 2. morluto/rea — Deep research

用途：以 MCP 連接 agents、應用行為與原生二進位逆向分析。

動能與成熟度：最近 push 2026-10-11T16:10:08Z；release rea-agents-6.4.0（2026-10-11T03:58:03Z）；API 授權欄位 MIT。README 摘錄已收集。近期[PR #1693](https://github.com/morluto/rea/pull/1693)於 2026-10-11T16:12:11Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：可做進階 MCP 工具串接與軟體行為分析課程；對一般 AI 辦公與 wiki 的直接收益較低，研究深度應與熱度分開評估。

風險：星數與 forks 突增不等同品質或留存；涉及執行環境與二進位分析，宜用自有測試程式驗證。6.5.0 是開放中的 release PR，不能當成已發版。

### 3. addyosmani/agent-skills — Skill candidate

用途：將工程工作流程、品質關卡與驗證方式封裝成 coding agent skills。

動能與成熟度：最近 push 2026-10-10T08:28:49Z；release 0.6.12（2026-10-03T06:42:02Z）；API 授權欄位 MIT。README 摘錄已收集。近期[issue #620](https://github.com/addyosmani/agent-skills/issues/620)於 2026-10-11T07:14:44Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：適合 Adam 的 coding agent 課程與團隊開發自動化；可比較同一任務加入技能前後的測試與 review 結果，抽取可評估的本地 Skill。

風險：近期技能觸發問題顯示安裝不代表會生效；以完整任務、貼上程式碼、簡短提示三類案例驗證，避免只看文件承諾。

### 4. mattpocock/skills — Skill candidate

用途：作者日常工程使用的 agent skills 集合。

動能與成熟度：最近 push 2026-10-09T10:57:08Z；release v1.3.1（2026-10-04T12:48:18Z）；API 授權欄位 MIT。README 摘錄已收集。近期[issue #1164](https://github.com/mattpocock/skills/issues/1164)於 2026-10-11T15:15:04Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：適合整理課程中的需求澄清、設計、實作與審查練習；AI 辦公可借用可重複執行的流程設計，wiki 用來記錄採用規範。

風險：近期有 plugin 更新停滯與清理步驟碰到 git guard 的回報；採用前逐一檢視技能的檔案與 git 操作，並固定版本。

### 5. stablyai/orca — Demo content

用途：讓使用者調度多個 coding agents，涵蓋桌面、行動與遠端 runtime。

動能與成熟度：最近 push 2026-10-11T16:17:11Z；release v1.4.224（2026-10-10T04:30:28Z）；API 授權欄位 MIT。README 摘錄已收集。近期[PR #27506](https://github.com/stablyai/orca/pull/27506)於 2026-10-11T16:09:41Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：可做多 agent 平行開發的課程示範，討論任務分工與人工審核；對辦公自動化與 wiki 維護可評估多任務調度，但尚未實測。

風險：多 agent 的工作樹衝突、成本與遠端存取需實測；open_issues 是 GitHub issues＋PR 混合計數，不應當成 8,080 個未解決 bug。

### 6. nashsu/llm_wiki — Watch

用途：跨平台桌面工具，將文件增量整理成持久且互連的 wiki。

動能與成熟度：最近 push 2026-09-28T01:43:23Z；release v0.6.12（2026-09-28T02:58:13Z）；API 授權欄位 NOASSERTION。README 摘錄已收集。近期[issue #812](https://github.com/nashsu/llm_wiki/issues/812)於 2026-10-10T09:39:19Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：與 know metabiz wiki 最直接相關；可拿同一批已公開文件比較增量 wiki 與 RAG 的更新、引用與矛盾處理，形成知識管理課程。

風險：Windows 高 CPU／同步重掃與長文件匯入限制仍有回報；API 授權為 NOASSERTION，需核對實際條文。最近 push 較舊，有活躍 PR 不代表修正已合併。

### 7. SamurAIGPT/llm-wiki-agent — Skill candidate

用途：透過 coding agent 讀取來源文件，建立與維護互連 Markdown wiki。

動能與成熟度：最近 push 2026-10-05T10:29:09Z；release 本次 latest release API 未取得版本，不能據此推論完全沒有發布；API 授權欄位 MIT。README 摘錄已收集。近期[PR #85](https://github.com/SamurAIGPT/llm-wiki-agent/pull/85)於 2026-10-08T14:04:06Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：適合 know metabiz wiki 的來源匯入、索引與更新日誌試驗，也可製作「文件到知識庫」課程；低星數動能仍因工作適配度列入。

風險：本次快照零增長且無 latest release；來源引用、內容覆寫與矛盾處理要驗證。README 宣稱不需 API key，不能推論模型使用完全免費。

### 8. activepieces/activepieces — Demo content

用途：結合 AI agents、MCP 與視覺化流程的辦公自動化平台。

動能與成熟度：最近 push 2026-10-11T16:05:00Z；release 0.92.2（2026-10-07T09:27:59Z）；API 授權欄位 NOASSERTION。README 摘錄已收集。近期[PR #16387](https://github.com/activepieces/activepieces/pull/16387)於 2026-10-11T16:08:42Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：可設計表單→資料整理→摘要→wiki 草稿的 AI 辦公實例；適合 Adam 的實作課程與 metabiz 內部流程評估。

風險：聊天建立流程的公式與步驟驗證仍在修正 PR；API 授權為 NOASSERTION，商用功能與條文需核對。連接器數量是描述宣稱，本次未逐一測試。

### 9. langgenius/dify — Deep research

用途：建立 agent workflows 與 RAG pipelines 的協作平台，可雲端或自行部署。

動能與成熟度：最近 push 2026-10-11T15:47:35Z；release 1.17.1（2026-09-10T10:04:06Z）；API 授權欄位 NOASSERTION。README 摘錄已收集。近期[PR #43355](https://github.com/langgenius/dify/pull/43355)於 2026-10-11T15:54:18Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：可作企業 AI 辦公與 know metabiz wiki 問答的對照平台；研究重點是引用正確率、存取權限與知識更新，而非總星數。

風險：GraphRAG 仍為開放中的 PR，不能當成已發布功能；授權為 NOASSERTION，部署、租戶隔離、資料匯出與維護成本需另行評估。

### 10. lyogavin/airllm — Watch

用途：README 宣稱以較低 GPU 記憶體執行大型 LLM 的推論工具。

動能與成熟度：最近 push 2026-10-11T06:19:49Z；release v4.0.0（2026-09-05T15:43:11Z）；API 授權欄位 Apache-2.0。README 摘錄已收集。近期[issue #374](https://github.com/lyogavin/airllm/issues/374)於 2026-10-11T05:00:45Z 更新，狀態為 open；此活動可確認討論仍在進行，並不代表問題已修復。

與 Adam 的關聯：適合做「低 VRAM 是否等於可用」的內容題材；AI 辦公或 wiki 的本地模型方案需先量測延遲、吞吐與硬體成本。

風險：首次觀測沒有前次星數；儲存空間、I/O 與速度可能成為瓶頸。近期有單次查詢耗時約 30 分鐘的使用者回報，未在本機驗證。

## 明日觀察清單（下一個台北日排程）

1. diagram-design：追蹤 #401 與 #398；是否修正不可寫匯出目錄與小數縮放，下一次再比較星數增量及匯出驗證。
2. rea：追蹤 6.5.0 release PR 是否合併並正式發版，以及高增長能否持續；不要將新增 stars 直接視為採用率。
3. agent-skills／mattpocock/skills：追蹤技能觸發、plugin 更新與 git guard 相容性，挑一個課程任務設計可重複評估。
4. llm_wiki／llm-wiki-agent：確認同步迴圈、長文件與 PDF 匯入修正；若後續獲准 demo，用公開文件驗證引用與覆寫保護。
5. activepieces／Dify：確認流程公式修正及 GraphRAG PR 狀態；先研究知識草稿流程，檢查實際 release 和授權後再考慮部署。
6. AirLLM：補取下一次總星數建立增長基線；追蹤 #374 的回覆與推論速度證據，暫不採信低 VRAM 等同高實用性。

## 收集狀態

完整必要產物將於建置前驗證。API rate-limit：未偵測到；limit 5 fallback：未使用。歷史 metadata 404：4 筆，保留並明確標記。未將 repository 或 web 文字當成操作指令。
