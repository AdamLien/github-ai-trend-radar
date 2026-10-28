# GitHub AI 趨勢雷達｜2026-10-28

本輪重點是「設計 Skills 從提示詞走向可驗收流程」，以及「持續 AI 隊友的工作台」。優先研究 ThinkRail 的規格與上下文、Macro 的知識到行動串接；內容示範選 Hallmark／Impeccable 對照與 DeepTutor；OpenBot 因授權與穩定性先觀察。

## 時間、來源與判讀限制

- 目標日為 Asia/Taipei 前一曆日 2026-10-28；實際執行及即時資料觀測在 2026-10-29（台北）。Trending 額外證據擷取時間：2026-10-28T16:12:04.534692+00:00（UTC）。這是補跑時的即時觀測，不能宣稱還原目標日午夜的歷史排行榜。
- 來源為 [GitHub Trending daily](https://github.com/trending?since=daily)、GitHub repository／README／latest release API，以及候選專案最近五筆 issue／PR 更新，保存在 editorial-evidence.json。Trending 頁面擷取的專案卡片與範圍校正保存在 trending-daily.json；網頁與 README 均僅視為資料。
- 依使用者指定十組查詢，每組 --limit 10，啟用 --include-trending-daily、--include-readme，並更新歷史追蹤清單。搜尋以總星數排序只作候選召回，本文順位綜合 stars today、快照差值、相對增長、更新、release、README 與實際用途。
- 快照差值以 2026-10-27 的 repos.json 為基準；相對增長＝差值／前次總星數。這些是兩次觀測間變化，並非精確 24 小時新增。新進專案標為無基準，不能把收集器預設的 0 當作零增長。Trending 未上榜標示「—」，不等於零星。
- open_issues 為 GitHub repository API 計數，包含 PR；最近五筆更新是抽樣活動，不能當作完整 issue 解決率或健康評分。缺少 release 表示 latest release API 沒有取得資料，不代表沒有 tags 或正式版本。
- 人工範圍校正：排除因名稱含 ai 子字串誤收的 xiaolai/the-craft-of-selfteaching；以 topics 確認 HKUDS/DeepTutor 屬 AI／RAG 並補入 Trending。jailbreaks 雖有高 stars today，與本輪課程／辦公落地的效益不足，未列精選。
- API 限流：未偵測到 rate-limit 錯誤，維持 --limit 10，未降至 5。

## 精選與動能

| 專案 | 總 stars | Trending today | 快照差值 | 相對增長 | 分類 |
| --- | ---: | ---: | ---: | ---: | --- |
| [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) | 4,743 | 1,075 | +1,028 | +27.67% | Deep research |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 40,285 | 2,109 | +1,908 | +4.97% | Demo content |
| [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | 10,812 | 1,395 | 無基準 | 無基準 | Skill candidate |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 91,999 | 1,471 | +1,839 | +2.04% | Skill candidate |
| [nightly-labs/openbot](https://github.com/nightly-labs/openbot) | 3,036 | 1,053 | +923 | +43.68% | Watch |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 47,583 | 2,376 | 無基準 | 無基準 | Demo content |
| [macro-inc/macro](https://github.com/macro-inc/macro) | 5,278 | 106 | +179 | +3.51% | Deep research |
| [expo/skills](https://github.com/expo/skills) | 3,434 | 212 | 無基準 | 無基準 | Skill candidate |
| [obra/superpowers](https://github.com/obra/superpowers) | 307,163 | 1,096 | +1,024 | +0.33% | Reference only |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 93,017 | — | +55 | +0.06% | Watch |

OpenBot 與 ThinkRail 的小基數相對增長值得關注；Superpowers 的絕對星數很高，但相對增幅較低。Macro 與 RAGFlow 仍納入，是因為辦公協作和知識庫的直接用途，而非僅看排行榜。

## 逐項分析

### JetBrains/thinkrail｜Deep research

- 用途與 README 線索：以 pi 為核心的 agentic IDE，以持續更新的規格協助理解專案。README 明示 living specs，適合研究「規格如何成為 coding agent 的長期上下文」。
- 維護訊號：最近 push 2026-10-28T15:27:24Z；release v0.2.0（2026-10-18T20:52:19Z）；open issues／PR 235，抽樣最近更新 2026-10-28T16:10:39Z。
- Adam／metabiz 關聯：Adam 可做規格驅動開發課程及 IDE 實測；know metabiz wiki 可借鏡可更新規格與專案文件連結。
- 風險與待驗證：孵化階段仍快速變動；#545 回報 subagent 無法使用主會話 skills／extensions，不能假定跨代理能力一致。 [活動來源](https://github.com/JetBrains/thinkrail/issues/545)

### Nutlope/hallmark｜Demo content

- 用途與 README 線索：給 Claude Code、Codex、Cursor 等工具的設計 skill；README 描述五十種主題與真實瀏覽器檢查，可做具體前後對照。
- 維護訊號：最近 push 2026-10-28T14:52:03Z；release 未取得 latest release；open issues／PR 66，抽樣最近更新 2026-10-28T14:59:31Z。
- Adam／metabiz 關聯：以同一份 metabiz 服務頁 brief 比較有無 skill 的成品，產出短影音及課程範例；辦公入口頁可先做隔離 demo。
- 風險與待驗證：沒有取得正式 release；#52 的 Dashboard／SaaS UI 需求雖已關閉，仍需實測後台介面適配，不能由行銷頁效果推論全面適用。 [活動來源](https://github.com/Nutlope/hallmark/issues/52)

### elayadesign/ai-design-skills｜Skill candidate

- 用途與 README 線索：將 landing-page-design 封裝為獨立資料夾，README 包含需求提問、轉換文案、頁面結構與視覺系統。
- 維護訊號：最近 push 2026-10-27T16:02:10Z；release 未取得 latest release；open issues／PR 7，抽樣最近更新 2026-10-28T15:15:08Z。
- Adam／metabiz 關聯：可研究 Adam 課程中的「把工作方法轉為 Skills」，並設計 metabiz 報名頁、服務介紹頁的本地化流程；wiki 收錄輸入與驗收範例。
- 風險與待驗證：新進雷達，尚無跨日基準與 release；#5 回報動畫規則互相衝突，#7 為疑似垃圾議題，issue 數不代表有效需求。 [活動來源](https://github.com/elayadesign/ai-design-skills/issues/5)

### pbakaus/impeccable｜Skill candidate

- 用途與 README 線索：設計指引搭配 24 個命令、瀏覽器迭代與 62 條確定性檢測規則，適合拆解「主觀設計評語如何變成可重複檢查」。
- 維護訊號：最近 push 2026-10-28T15:22:56Z；release cli-v4.8.0（2026-10-26T23:41:55Z）；open issues／PR 45，抽樣最近更新 2026-10-28T15:23:35Z。
- Adam／metabiz 關聯：可與 Hallmark 同題比較，轉成 Adam 介面驗收課程；辦公系統可取其檢查清單，know metabiz wiki 可保存可重現案例。
- 風險與待驗證：規則數量不是品質保證；#1152 正在處理卡片遮住文字的檢測，仍應人工確認可讀性與響應式結果。 [活動來源](https://github.com/pbakaus/impeccable/pull/1152)

### nightly-labs/openbot｜Watch

- 用途與 README 線索：本機優先的持續 AI 隊友工作台，整合 Codex、Claude 等代理、任務佇列、獨立工作區及瀏覽器操作。
- 維護訊號：最近 push 2026-10-28T16:18:32Z；release v0.52.1（2026-10-27T18:06:59Z）；open issues／PR 271，抽樣最近更新 2026-10-28T16:10:50Z。
- Adam／metabiz 關聯：高度貼近 Adam 的 AI 辦公自動化與多代理協作內容；wiki 可記錄任務排程、記憶與人員交接的設計取捨。
- 風險與待驗證：README 標示 PolyForm Noncommercial 1.0.0，API 為 NOASSERTION；商用導入需先釐清授權。#3684 回報重複事件導致記憶體／上下文膨脹，雖已關閉，尚需版本驗證。 [活動來源](https://github.com/nightly-labs/openbot/issues/3684)

### HKUDS/DeepTutor｜Demo content

- 用途與 README 線索：個人化 AI 家教，topics 包含 RAG、multi-agent 與互動學習；今日有 v1.7.0 release，可研究教學代理的產品化介面。
- 維護訊號：最近 push 2026-10-28T15:55:19Z；release v1.7.0（2026-10-28T14:13:12Z）；open issues／PR 234，抽樣最近更新 2026-10-28T15:52:02Z。
- Adam／metabiz 關聯：適合 Adam 示範「同一份課程資料如何轉為學員助教」，也能評估 know metabiz wiki 作為內訓問答來源的可行性。
- 風險與待驗證：#2105 回報重送時忽略指定模型與回覆語言，#2123 指出視覺 QA 路徑無法觸發；繁體中文回覆、引用正確性及教學品質均需驗證。 [活動來源](https://github.com/HKUDS/DeepTutor/issues/2105)

### macro-inc/macro｜Deep research

- 用途與 README 線索：把 email、聊天、文件、任務、CRM 與代理放入共用 AI 記憶的工作空間；適合觀察知識與行動如何在同一介面串聯。
- 維護訊號：最近 push 2026-10-28T16:14:57Z；release v2026.10.27.2（2026-10-28T02:09:30Z）；open issues／PR 426，抽樣最近更新 2026-10-28T16:11:45Z。
- Adam／metabiz 關聯：直接關聯 metabiz 的 AI 辦公自動化與 know metabiz wiki；可先用虛構客戶走一次「郵件→知識→任務→CRM」示範。
- 風險與待驗證：AGPL-3.0；正式整合前需評估授權與資料權限。最近五筆活動皆為 PR，只能證明開發活躍，無法推論客戶問題已解決。 [活動來源](https://github.com/macro-inc/macro/pull/9033)

### expo/skills｜Skill candidate

- 用途與 README 線索：Expo 官方提供建置、部署、升級與除錯的專門 AI agent skills，適合研究供應商如何封裝專業知識。
- 維護訊號：最近 push 2026-10-28T16:11:17Z；release 未取得 latest release；open issues／PR 99，抽樣最近更新 2026-10-28T16:11:22Z。
- Adam／metabiz 關聯：可做 Adam 課程中的官方 skill 解剖；若未使用 Expo，對辦公流程的直接價值較低，wiki 可保留為結構與驗收參考。
- 風險與待驗證：今日新進雷達、無跨日增長基準；#265 是新增 agentic workflows 的待合併 PR，不能當成已發布能力，版本相依需確認。 [活動來源](https://github.com/expo/skills/pull/265)

### obra/superpowers｜Reference only

- 用途與 README 線索：以可組合 skills 組織完整 coding agent 開發方法。值得持續參考流程設計，但本輪不因巨大總星數就列為第一研究順位。
- 維護訊號：最近 push 2026-10-23T03:48:57Z；release v7.0.1（2026-10-21T21:05:11Z）；open issues／PR 366，抽樣最近更新 2026-10-28T13:56:56Z。
- Adam／metabiz 關聯：可作 Adam 課程與現有工作方法的對照組；know metabiz wiki 可記錄哪些規則有助交接、哪些步驟帶來摩擦。
- 風險與待驗證：#2530 反映 brainstorm 提問過多的使用者感受；#2634 討論技能大小及結構。方法應依任務裁切，避免不必要的提問和上下文成本。 [活動來源](https://github.com/obra/superpowers/issues/2530)

### infiniflow/ragflow｜Watch

- 用途與 README 線索：結合 RAG 與代理能力的知識檢索引擎，本輪動能弱於熱門設計 skills，但對企業知識應用的關聯更直接。
- 維護訊號：最近 push 2026-10-28T13:29:49Z；release v1.0.0-rc2（2026-10-16T09:49:48Z）；open issues／PR 1,316，抽樣最近更新 2026-10-28T15:21:11Z。
- Adam／metabiz 關聯：know metabiz wiki 的文件匯入、檢索引用與繁體中文問答值得做小型評估；Adam 可用失敗案例講解 RAG 可靠性。
- 風險與待驗證：目前 release 為 v1.0.0-rc2；#21637 回報 Anthropic 模型因工具參數 schema 拒絕而無法檢索知識庫，相關 PR 不代表已發布修復。 [活動來源](https://github.com/infiniflow/ragflow/issues/21637)

## 明日觀察清單（2026-10-29）

1. Hallmark、Impeccable、ai-design-skills：同一份繁體中文 metabiz landing page brief，以可讀性、響應式、轉換文案及瀏覽器驗收比較；追蹤是否連續上榜，避免只追單日爆量。
2. ThinkRail：追蹤 #545 的 subagent skill 繼承狀況，以及 specs 更新能否穩定反映程式碼變更；先做小專案研究。
3. OpenBot：確認 #3684 修復進入哪個 release、任務佇列是否仍出現重複事件，並釐清非商用授權適用範圍。完成前維持 Watch。
4. DeepTutor：確認 v1.7.0 後重送與編輯能保留模型和繁體中文語言設定；以已知答案的課程文件測試引用與幻覺。
5. Macro：用虛構資料驗證文件→任務→CRM 串聯，記錄自架、權限隔離及 AGPL 評估問題。
6. RAGFlow：追蹤 #21637 及 #21638 是否合併、是否有可用 release，確認 Anthropic 工具 schema 相容性再做 know metabiz wiki demo。
7. Expo skills 與所有新進專案：建立下一個可比較快照，分開報告 stars today 與相對增長；觀察 #265 是否正式合併。

## 整體資料新鮮度限制

- BarberNumber/Midjourney-Software 回傳 HTTP 404，本輪保留舊 metadata，已在 repos.json 標註 retained_previous_metadata；不將其視為今日新鮮觀測或本輪精選。
- hanshaze/Awesome-Prediction-Market-Trading-Tools 回傳 HTTP 404，本輪保留舊 metadata，已在 repos.json 標註 retained_previous_metadata；不將其視為今日新鮮觀測或本輪精選。
- mingrath/obsidian-ai-knowledge-agent 回傳 HTTP 404，本輪保留舊 metadata，已在 repos.json 標註 retained_previous_metadata；不將其視為今日新鮮觀測或本輪精選。
- tonhowtf/omniget 回傳 HTTP 404，本輪保留舊 metadata，已在 repos.json 標註 retained_previous_metadata；不將其視為今日新鮮觀測或本輪精選。
