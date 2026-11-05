# GitHub AI 趨勢雷達｜2026-11-05

本日優先研究企業知識的語意層與可操作 agent；內容方向則以桌面自動化、Skills 素材產線與並行開發示範最具體。以下是編輯判斷與可驗證的下一步，尚未安裝或實測這些專案。

## 日期、來源與限制

- 目標日期：2026-11-05（執行時 Asia/Taipei 的前一日）；實際開始觀測：2026-11-06T00:11:16.720802+08:00。
- 本報使用執行當下的 [GitHub Trending daily](https://github.com/trending?since=daily) 與 GitHub API，不是假設已還原昨日完整 00:00–24:00 的星標事件。Trending 原始卡片摘要見 `trending-evidence.json`。
- 依指定 10 組查詢、每組最多 10 筆，合併相關 Trending、固定觀察與歷史追蹤；歷史追蹤不代表今天仍在 Trending。查詢依 GitHub stars 排序，存在大專案偏差，因此本文優先比較 stars today、增量、相對增幅、更新與活動。
- 本次保留 395 個相關候選；另排除 10 個無明確本題用途的歷史通用工具，原因見 `scope-review.json`，過往資料不變。
- 快照增量＝本次總 stars − 前次快照總 stars；相對增幅＝增量 ÷ 前次總 stars。兩者與 Trending 的 stars today 觀測窗口不同，不能相加或互換。首次觀測或無基準時記為未知，不把 0 當成已證實零成長。
- Issue／PR 活動另取每庫最近更新的 5 筆，見 `activity-evidence.json`；這是活動抽樣，不是解決率。open_issues 含 PR，不能當成純 bug 數。README／描述是專案自述，release 缺失可能是沒有發布或端點失敗。
- API rate-limit 狀態：未偵測到 rate-limit 錯誤；使用 --limit 10 完成（詳見 collection-status.json）。

## 優先關注清單

| 專案 | 決策 | stars today | 總 stars | 快照增量 | 相對增幅 |
|---|---|---:|---:|---:|---:|
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | Deep research | 2,707 | 6,738 | +2,491 | +58.65% |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Demo content | 2,173 | 16,409 | +1,967 | +13.62% |
| [scenario-labs/skills](https://github.com/scenario-labs/skills) | Skill candidate | 674 | 2,870 | +651 | +29.34% |
| [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | Demo content | 546 | 11,376 | +502 | +4.62% |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skill candidate | 2,053 | 314,608 | +1,920 | +0.61% |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Watch | 608 | 139,751 | +614 | +0.44% |
| [google/skills](https://github.com/google/skills) | Reference only | 199 | 22,200 | +280 | +1.28% |
| [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | Watch | 181 | 14,027 | +209 | +1.51% |

### 1. NVIDIA/auto-ontology — Deep research

- **用途與 README 判讀：** 建立企業資料的 ontology 與語意 context layer，協助 agent 理解資料位置、定義與查詢方式。
- **與 Adam／metabiz 的關聯：** 直接對應 know metabiz wiki：先拿少量去識別化的 CRM／報價／產品詞彙，檢驗能否降低同名異義與錯誤查詢；可做「RAG 找到文件後，如何正確理解業務」課程。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-11-05T14:45:30Z；release：API 未取得正式 release；不推論為沒有維護；近期 Issue／PR 抽樣最新更新：2026-11-05T14:51:54Z。
- **風險與限制：** 語意建模與維護成本尚未驗證；近期 SQLDatabase 文件參數不一致，以及 RLS／CLS 整合需求仍待處理，不能把 README 的可靠性主張當成實測結果。 [相關討論](https://github.com/NVIDIA/auto-ontology/issues/428)。
- **來源：** [專案與 README](https://github.com/NVIDIA/auto-ontology)、[活動清單](https://github.com/NVIDIA/auto-ontology/issues?q=sort%3Aupdated-desc)。

### 2. vercel-labs/agent-desktop — Demo content

- **用途與 README 判讀：** 透過作業系統 accessibility tree，讓 AI agent 觀察及操作桌面應用。
- **與 Adam／metabiz 的關聯：** 適合 Adam 的 AI 辦公自動化課程：展示桌面表單與文件工作流，量測成功率、重試與人工接手；用沙盒假資料製作跨平台操作示範。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-11-05T06:31:12Z；release：[v1.2.0](https://github.com/vercel-labs/agent-desktop/releases)，發布於 2026-11-05T02:43:54Z；近期 Issue／PR 抽樣最新更新：2026-11-05T14:00:11Z。
- **風險與限制：** Windows 按鍵與 modal 可讀性仍有公開問題，Linux Wayland 支援仍見開發中 PR；須逐平台測試，不可把桌面可操作等同可可靠批次執行。 [相關討論](https://github.com/vercel-labs/agent-desktop/issues/513)。
- **來源：** [專案與 README](https://github.com/vercel-labs/agent-desktop)、[活動清單](https://github.com/vercel-labs/agent-desktop/issues?q=sort%3Aupdated-desc)。

### 3. scenario-labs/skills — Skill candidate

- **用途與 README 判讀：** 以 agent skills 串接 Scenario MCP，提供影像、影音與 3D 內容製作流程。
- **與 Adam／metabiz 的關聯：** 可拆成 Adam 內容製作的「先估價、再生成、保存素材與來源」候選 skill，先用單一課程封面／短影音素材測試品牌一致性與每件成本。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-11-05T15:49:39Z；release：[skills-v0.60.1](https://github.com/scenario-labs/skills/releases)，發布於 2026-10-29T15:25:46Z；近期 Issue／PR 抽樣最新更新：2026-11-05T15:57:36Z。
- **風險與限制：** 依賴外部服務與額度，成本、素材權利與模型輸出品質都須另查；stable branch／plugin 發布方式仍有未合併變更，候選版本需固定。 [相關討論](https://github.com/scenario-labs/skills/pull/314)。
- **來源：** [專案與 README](https://github.com/scenario-labs/skills)、[活動清單](https://github.com/scenario-labs/skills/issues?q=sort%3Aupdated-desc)。

### 4. max-sixty/worktrunk — Demo content

- **用途與 README 判讀：** 管理 Git worktree，支援多個 coding agent 並行工作的 CLI。
- **與 Adam／metabiz 的關聯：** 適合 coding agent 課程：把兩個獨立任務放入不同 worktree，展示差異檢視、驗證與合併，並量測衝突及整合時間；metabiz 開發自動化可先小範圍試作。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-11-05T08:57:29Z；release：[v0.81.0](https://github.com/max-sixty/worktrunk/releases)，發布於 2026-10-20T21:28:34Z；近期 Issue／PR 抽樣最新更新：2026-11-05T15:12:21Z。
- **風險與限制：** worktree 只隔離工作目錄，無法自行避免需求衝突、共用服務或憑證干擾；近期 hook 錯誤傳遞與 GitHub Enterprise host 修正顯示整合仍需驗證。 [相關討論](https://github.com/max-sixty/worktrunk/pull/4689)。
- **來源：** [專案與 README](https://github.com/max-sixty/worktrunk)、[活動清單](https://github.com/max-sixty/worktrunk/issues?q=sort%3Aupdated-desc)。

### 5. mattpocock/skills — Skill candidate

- **用途與 README 判讀：** 提供工程設計、需求釐清、測試與開發流程等可重用 agent skills。
- **與 Adam／metabiz 的關聯：** 用於 Adam 的「從 prompt 到可驗證工作流程」教材；與本地既有 skills 比對更新內容，挑一項需求釐清或 code review 流程做 A/B 任務，不整包覆蓋。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-11-05T10:40:01Z；release：[v1.3.2](https://github.com/mattpocock/skills/releases)，發布於 2026-10-29T10:27:41Z；近期 Issue／PR 抽樣最新更新：2026-11-05T15:43:23Z。
- **風險與限制：** 近期有人回報 skill 自動觸發控制與 Codex PR 截圖進入 repo 等問題；需審核觸發條件、檔案寫入與版本差異，熱門度不能證明符合個人工作方式。 [相關討論](https://github.com/mattpocock/skills/issues/1389)。
- **來源：** [專案與 README](https://github.com/mattpocock/skills)、[活動清單](https://github.com/mattpocock/skills/issues?q=sort%3Aupdated-desc)。

### 6. garrytan/gstack — Watch

- **用途與 README 判讀：** 將產品、設計、工程、QA 與交付等角色包成 coding-agent 工作流程。
- **與 Adam／metabiz 的關聯：** 適合 Adam 做「虛擬工程團隊」流程拆解內容，並為 metabiz 專案選取一段 review→QA 的閉環；把每步的證據與交付條件寫清楚再試跑。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-11-05T16:17:25Z；release：[v1.96.0.0](https://github.com/garrytan/gstack/releases)，發布於 2026-11-05T14:05:48Z；近期 Issue／PR 抽樣最新更新：2026-11-05T16:09:58Z。
- **風險與限制：** 流程規模大，導入可能增加工具與 token 成本；近期測試結果計數修正，以及 Codex 檔案邊界調整仍在變動，驗證證據與操作邊界需自行檢查。 [相關討論](https://github.com/garrytan/gstack/issues/4016)。
- **來源：** [專案與 README](https://github.com/garrytan/gstack)、[活動清單](https://github.com/garrytan/gstack/issues?q=sort%3Aupdated-desc)。

### 7. google/skills — Reference only

- **用途與 README 判讀：** Google 產品與技術的官方 agent skills 集合，包含 Google Cloud 工作流。
- **與 Adam／metabiz 的關聯：** 適合作為課程與企業 skill 編寫的來源參考；metabiz 若有 Google Cloud 資料整合需求再挑相應 skill，不直接推論為 Gmail／Calendar 辦公自動化的完整方案。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-11-05T11:41:06Z；release：API 未取得正式 release；不推論為沒有維護；近期 Issue／PR 抽樣最新更新：2026-11-05T10:04:36Z。
- **風險與限制：** 供應商特定指令、雲端權限與計費需逐項確認；近期 gcloud 列表的 limit/filter 假陰性回報提醒教材需驗證實際命令結果。 [相關討論](https://github.com/google/skills/issues/242)。
- **來源：** [專案與 README](https://github.com/google/skills)、[活動清單](https://github.com/google/skills/issues?q=sort%3Aupdated-desc)。

### 8. ConardLi/garden-skills — Watch

- **用途與 README 判讀：** 提供網站設計、知識擷取、圖片與程式渲染影片等內容製作 skills。
- **與 Adam／metabiz 的關聯：** 適合 Adam 內容產線：從一篇 know metabiz wiki 條目轉成圖文或短影片，對照現有短影音流程的可編輯性、繁體中文呈現及製作時間。
- **維護與動能證據：** stars 指標見上表；相較基準日 2026-11-04。最近 push：2026-10-25T13:45:33Z；release：[motion-showreel-v0.1.0](https://github.com/ConardLi/garden-skills/releases)，發布於 2026-10-11T02:28:11Z；近期 Issue／PR 抽樣最新更新：2026-10-31T01:32:40Z。
- **風險與限制：** 相較其他熱門候選，近期程式更新與討論較慢；直式影片與擷取整合仍見待處理 PR／建議，不能視為正式可用能力，需先測依賴與輸出。 [相關討論](https://github.com/ConardLi/garden-skills/pull/37)。
- **來源：** [專案與 README](https://github.com/ConardLi/garden-skills)、[活動清單](https://github.com/ConardLi/garden-skills/issues?q=sort%3Aupdated-desc)。

## 判讀與明日觀察清單

排序刻意把小基數且相對增長較高的知識語意層、影音 Skills 與 worktree 工作流放進前排；總 stars 很高的 gstack 與 mattpocock/skills 仍值得看，但用途匹配與可驗證變更比名氣更重要。

1. **auto-ontology：** 追蹤 RLS／CLS、文件參數問題及正式 release，設計一個可量測的 know metabiz wiki 詞彙歧義測試；先確認語意建模成本。
2. **agent-desktop／agent-browser：** 看 Windows modal／鍵盤與 MCP session 隔離修正是否合併；選相同假資料任務，分別量測桌面與瀏覽器自動化的成功率及接手點。
3. **scenario-labs/skills：** 觀察 stable branch 與下一次正式發布，先做一張封面的報價／生成／重現流程；未合併的 release PR 不當作已發布。
4. **worktrunk：** 觀察 hook 錯誤傳遞修正，規劃兩 agent、兩 worktree 的課程示範，記錄整合與清理時間。
5. **mattpocock/skills／gstack：** 查看自動觸發與驗證證據相關 Issue／PR 的後續，只比較與既有 skills 有關的變更，避免重複導入。
6. **garden-skills／google/skills：** 前者看直式影片 PR 與知識擷取整合是否落地；後者待有具體 Google Cloud 任務再挑選，維持參考優先。

明日重新取得快照後，檢查增量與相對成長是否持續；若 Trending 已消退但 release／Issue 解決仍前進，仍可保留研究價值。

## 收集查詢

- `mcp server ai`
- `model context protocol`
- `agent skills coding agent`
- `claude code template`
- `codex skills`
- `coding agent llm`
- `rag knowledge base`
- `ai wiki knowledge management`
- `llm orchestration agent`
- `developer automation ai`
