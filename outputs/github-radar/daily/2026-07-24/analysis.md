# GitHub AI Trend Radar｜2026-07-24（台灣）

## 結論先講

今天最值得投入研究的不是又一個「skills 清單」，而是三條可直接接到 Adam 工作流的路線：

1. **可查證的程式與文件上下文**：Graphify、Headroom，可用於 coding agent、RAG 與知識庫的成本/可追溯性設計。
2. **可版本化的 agent 工作方法**：Superpowers、agent-skills，適合作為課程或內部技能規範的參考來源，而不是直接整包安裝。
3. **Markdown-first 長期記憶**：Obsidian Mind 的相對成長最高，和 know metabiz wiki 的方向最接近，值得先做隔離 PoC。

本輪 API 搜尋取得 **89** 個去重 repo，與上一輪資料全數重疊；因此下列 `star delta` 為 2026-07-24 00:12 至 2026-07-25 00:12（台灣時間附近）的跨快照差異，而不是 GitHub 歷史日榜。GitHub Trending 沒有歷史回放能力，文末的 `stars today` 是 7/25 收集當下的即時頁面訊號，**不可混同為 7/24 的數字**。

## 今日優先清單

| 分類 | Repo | 動能 | 為什麼現在看 | 風險 / 採取方式 |
| --- | --- | --- | --- | --- |
| Deep research | [earendil-works/pi](https://github.com/earendil-works/pi) | +772；76,947 stars；1.00% | 統一 LLM API、agent loop、TUI 與 coding-agent CLI；7/24 有 push 與 release，是目前最強的 agent toolkit 動能。 | MIT；先比較其 loop/tool contract 與現有 Codex 流程，勿因人氣改換既有身份或 token 邊界。 |
| Deep research | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +658；95,065；0.69% | 把 code、文件、SQL、設定、PDF 轉成可解釋知識圖，且明列 Claude Code/Cursor/Codex；特別符合「先取證、再回答」。 | Apache-2.0；635 open issues 代表評估面要看。先以小型 metabiz mirror 做只讀 PoC，驗證敏感資料與索引成本。 |
| Deep research | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +607；62,142；0.98% | 壓縮 tool output、log、檔案與 RAG chunk，提供 library/proxy/MCP server，直接命中 agent context 成本問題。 | Apache-2.0；525 open issues。其「same answers」是主張，應以 mVoice/Metabiz 真實任務量測品質、延遲與 token，而非照單全收。 |
| Skill candidate | [obra/superpowers](https://github.com/obra/superpowers) | +528；260,470；0.20% | 可組合 skills 加上 SDLC 方法；7/24 push 與 release，適合拆成內部可審核的工作步驟。 | MIT；不要整套覆蓋既有 skill。抽取一項可驗證流程（例如 spec-to-test）做試行。 |
| Skill candidate | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +160；80,180；0.20% | 明確定位為 coding agent 的工程品質閘門，且含 Codex/Cursor/Claude Code 關聯 topics。 | MIT；可讀性佳但仍是外部指令來源。逐 skill 審核 shell 權限、資料外送與專案契約。 |
| Deep research | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +151；3,923；**3.85%** | 自組織 Obsidian vault，供 Claude Code、Codex CLI、Gemini CLI 保存持久記憶；相對成長是本輪最高。 | MIT；只 4 個 open issues 不等於成熟。先在非機密 vault 驗證 backlink、衝突處理、可逆性，再評估 know metabiz wiki。 |
| Watch | [MODSetter/SurfSense](https://github.com/MODSetter/SurfSense) | +127；15,427；0.82% | 開源 NotebookLM 替代品，能經平台/API/MCP 進行網路研究；可作「研究自動化」內容示範。 | **NOASSERTION license**；外網擷取、帳號/資料來源權限風險高。僅做公開資料 demo，不接企業資料。 |
| Watch | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +118；65,794；0.18% | 多 agent swarm、協調 workflow、memory/RAG 與多 CLI 整合，題材上很適合 agent coordination 課程。 | MIT，但 827 open issues、功能面很廣。先研究 orchestration 模型，不把它當成生產底座。 |
| Reference only | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +637；69,882；0.91% | skills 生態的高熱度索引，且在即時 Trending 仍有 +662 stars today。 | **未標示 license、1,086 open issues**；只用作發現來源，不能把清單中的 scripts 視為可信供應鏈。 |

## 即時 Trending（7/25 收集時，與 7/24 快照分開）

- [mattpocock/skills](https://github.com/mattpocock/skills)：**+2,224 stars today**。工程師 skills 的內容選題訊號很強；先比較授權與實際工作流，再決定是否引用。
- [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)：**+1,843 stars today**。多模型 gateway、Claude Code/Codex/Cursor 與 MCP/A2A 整合，適合做「成本、fallback、供應商鎖定」解說；先審查金鑰流向與服務依賴。
- [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)：**+884 stars today**。共享登入 browser state 的 agent web automation，適合安全課案例；這正是高權限資產，禁止直接接入真實工作帳號。
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)：**+662 stars today**，與 API delta 方向一致，但仍只當索引。

## 對 Adam 的行動轉譯

### 課程與內容選題

- 做一篇「AI coding agent 不是靠長 prompt：Graphify 的可追溯 context、Headroom 的壓縮、skills 的品質閘門」；可用小 repo 的 code-to-answer 做 demo。
- 做一支「Obsidian vault 如何成為 agent 的可版本化記憶」：先講 Markdown、Git、敏感資料隔離，再展示 Obsidian Mind 的思路；不要宣稱可直接解決知識治理。
- 用 Ruflo 對比單 agent，講清 coordination 的收益、觀測性與失控成本；用架構解讀而不是承諾採用。

### AI 辦公室自動化

- 優先試驗 Headroom 在 log、API JSON 與 RAG chunks 的壓縮，建立 `品質 / token / latency` 三欄實測表。
- 要自動化外部研究時，SurfSense 和 ego-lite 都屬高權限設計：以公開資料、最小權限與短效憑證為前提；不得把登入瀏覽器狀態或企業資料交給未審核服務。
- Skills 清單可以變成「候選庫」，但每個 candidate 要有來源、授權、權限、測試證據與撤回方式。

### know metabiz wiki

- **先做**：Obsidian Mind 的隔離 sandbox，輸入可公開/可刪除的 Markdown 複本，驗證記憶產物是否仍是可 review 的檔案。
- **再做**：以 Graphify 對一小段 code + schema + 文件建立只讀索引，檢查回答可否回鏈到來源。
- **不做**：在未驗證資料流與授權前，將完整 vault、客戶資料或憑證丟進任何 agent memory / RAG / MCP server。

## 明日持續追蹤

1. `earendil-works/pi`：release 後的持續增長與 CLI/tool contract。
2. `Graphify-Labs/graphify`：release 後 issue 增量、文件與小型 PoC 的可重現性。
3. `headroomlabs-ai/headroom`：壓縮效果的獨立測試與 MCP proxy 邊界。
4. `breferrari/obsidian-mind`：README、issue/PR 活性與 Markdown 可逆性。
5. `obra/superpowers`、`addyosmani/agent-skills`：挑可抽取、可測試、可撤回的一項 skill，而非追星數。
6. `MODSetter/SurfSense`、`ruvnet/ruflo`：授權、資料權限與維護負載；若沒有改善，維持 Watch。

## 收集與限制

- API collector：10 組指定 query、每組 limit 10、附 README excerpt；GitHub CLI authentication 已使用，未 rate limited，沒有降為 limit 5。
- 產物：`repos.json` 是本輪完整快照；`report.md` 是 collector 原始列表；`snapshots/repos-2026-07-25.json` 為本次實際收集日期快照。
- `stars today` 只出自 7/25 00:xx 的 live Trending HTML；`star delta` 是兩次 API snapshot 的差，兩者量測方法不同。
