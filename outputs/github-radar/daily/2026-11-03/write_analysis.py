import json
from pathlib import Path
out=Path(__file__).resolve().parent
root=out.parents[3]
e=json.loads((out/'review-evidence.json').read_text())
records={r['full_name']:r for r in e['repos']}
if (out/'repos.json').exists():
    records.update({r['full_name']:r for r in json.loads((out/'repos.json').read_text())['repos']})
previous={r['full_name']:r for r in json.loads((out.parent/'2026-11-02/repos.json').read_text())['repos']}
trending=json.loads((out/'trending-daily.json').read_text())['repos']
notes=[
('vercel-labs/agent-desktop','Deep research','透過作業系統 accessibility tree 讀取與操作桌面應用的 CLI。','可拍攝 AI 辦公室跨應用操作示範；先以測試資料比較可重複性，再評估 metabiz 行政流程。','近期 issue #374 回報視窗列舉與截圖失敗，#487 指出參數不一致；桌面寫入操作需逐步驗證。'),
('max-sixty/worktrunk','Demo content','管理 Git worktree，支援多個 coding agent 平行開發。','適合 Adam 的 coding agent 課程，以隔離分支、合併與驗證流程示範團隊協作。','issue #4142 指出 hook 失敗提示可能建議略過 gate；README 標示雙授權，但 API 為 NOASSERTION，商用前讀取授權原文。'),
('mattpocock/skills','Skill candidate','將日常工程決策與工作流整理成 agent skills。','挑選適用的研究、需求與驗收流程，轉為 Adam 課程練習與 metabiz 開發 SOP。','issue #1380 指出研究產物命名與落點不一致，#1379 涉及變更未重新驗證；先審查個別 skill 再採用。'),
('thedotmack/claude-mem','Deep research','擷取、壓縮並跨 session 注入 agent 工作記憶。','適合「短期上下文、長期記憶、know metabiz wiki」比較教材；評估辦公流程交接的記憶品質。','近期 PR #5342 涉及 OAuth token 遮蔽，尚為開啟狀態；記憶蒐集範圍、刪除與敏感資料遮蔽須實測。'),
('D4Vinci/Scrapling','Demo content','從單頁請求到爬取流程的網頁擷取框架，README 有 MCP 標記。','適合資料蒐集到 AI 摘要的內容示範，以及 know metabiz wiki 的公開來源匯入前處理。','開啟中的 PR #542 涉及 URL scheme 與本機檔案洩漏防護；issue #540 涉及 cookie 解析。示範先限定公開資料與受控 URL。'),
('spotify/portal-ai-plugins','Watch','將 Portal 軟體目錄、技術文件搜尋、診斷與動作整合進 coding agents。','可研究「企業知識目錄＋agent」介面，作為 know metabiz wiki 的服務所有權與文件搜尋設計參考。','issue #26 回報 hook schema 驗證失敗，#25 回報登入 token 被拒；需 Portal 環境，不能直接視為通用辦公工具。'),
('Donchitos/Claude-Code-Game-Studios','Demo content','以多角色 agents、skills 與協調流程模擬遊戲工作室。','適合 Adam 多 agent 內容企劃：示範角色分工、交接與驗收，再抽象為辦公室工作流。','README 與 description 的 skills 數量不同；issue #172 仍有 bug 回報，PR #170 涉及 worktree 設定。角色數量不等於品質，需衡量成本與產物。'),
('nashsu/llm_wiki','Watch','將文件增量整理成持久且互連的桌面 wiki。','與 know metabiz wiki 高度相關，可作為傳統 RAG 與持久知識頁的對照實驗。','issue #837 回報重匯入縮短來源頁且產生重複；API 授權為 NOASSERTION。先用去識別樣本測試來源追溯、重匯入與還原。'),
('SamurAIGPT/llm-wiki-agent','Skill candidate','讓 coding agent 從來源建立及維護 Markdown wiki 的 skill。','適合 know metabiz wiki 小型驗證，以及 Adam 的「資料變成可維護知識」課程；雖低動能仍保留。','issue #83 與開啟中的 PR #84 涉及轉檔覆寫既有 Markdown；沒有 release 資料，近期 issue 更新較少，先在副本驗證。'),
]
lines=['# GitHub AI 趨勢雷達｜2026-11-03','','## 觀測範圍與判讀','','- 歸檔目標：Asia/Taipei 前一日 2026-11-03；本次為執行時即時擷取，不是 11 月 3 日收盤還原。實際 UTC 觀測時間記於 `review-evidence.json` 與 `trending-daily.json`。','- 來源：[GitHub Trending daily](https://github.com/trending?since=daily)、十組指定 GitHub 搜尋、專案 README、最新 release、最近更新的 5 筆 issue／PR；詳見 `repos.json`、`report.md` 與 `review-evidence.json`。','- 排序綜合 Trending stars today、相對前一資料夾快照差值／成長率、最近 push、release 與 issue／PR，並加入 Adam 課程、內容與辦公應用價值。搜尋本身依總星數排序，仍有大型專案偏差。','- stars today 是 Trending 的滾動口徑；快照差值是兩次觀測差，兩者不可相加。新收錄不代表新成立；缺少基準不以零成長解讀。issue 數量不等於品質或處理速度，開啟 PR 不代表修正已發布。','','## 今日重點','','優先深研桌面操作與 agent 記憶；以 worktree、工程 skills 和網頁資料流程製作可驗證示範。企業目錄插件保持觀察；wiki 專案即使星數動能較低，也因 know metabiz 的實際需求保留。','','| 專案 | 總 stars | Trending today | 快照 Δ | 相對成長 | 分類 |','| --- | ---: | ---: | ---: | ---: | --- |']
for name,cat,*_ in notes:
 r=records[name];old=previous.get(name);delta=r['stars']-old['stars'] if old else None
 growth=f'{delta/old["stars"]*100:.2f}%' if old and old['stars'] else '無基準'
 today=trending.get(name,{}).get('trending_stars_today','未上榜')
 lines.append(f'| [{name}]({r["html_url"]}) | {r["stars"]:,} | {today} | {delta if delta is not None else "無基準"} | {growth} | {cat} |')
for name,cat,purpose,relevance,risk in notes:
 r=records[name];release=r['latest_release'];ev=next(x for x in e['repos'] if x['full_name']==name)
 lines+=['',f'### [{name}]({r["html_url"]})｜{cat}','',f'- 用途：{purpose}',f'- 動能與維護：表列 stars／成長；最近 push `{r["pushed_at"]}`；最新 release `{release.get("tag_name") or "未取得"}`（{release.get("published_at") or "無發布時間"}）。最近 issue／PR 樣本最後更新 `{ev["recent_issues_and_prs"][0]["updated_at"]}`。',f'- Adam／metabiz 關聯：{relevance}',f'- 風險與下一步：{risk}',f'- 驗證來源：[README]({r["html_url"]}#readme)、[releases]({r["html_url"]}/releases)、[issue／PR 活動]({r["html_url"]}/issues?q=sort%3Aupdated-desc)。']
lines+=['','## 明日觀察清單','','1. agent-desktop：觀察高相對成長是否持續、v1.1.0 後視窗定位與截圖問題處理，設計一個可重播的行政任務。','2. worktrunk／mattpocock skills：追蹤 hook gate、研究檔案命名與驗收問題，挑一條最小 workflow 作課堂示範。','3. claude-mem／Scrapling：確認敏感資料遮蔽及 URL 防護 PR 是否合併並發布，才安排企業資料 PoC。','4. Spotify Portal：檢查 hook 與認證問題進展，評估目錄查詢介面能否映射到 know metabiz wiki。','5. 兩個 wiki 專案：重匯入相同文件，比較重複頁、覆寫、引用保留與變更回復；記錄成本與人工作業節省量。','6. 再取相同搜尋與 Trending，分開比較即時日增星與相鄰快照差；特別檢查新入榜是否有可用 README、release 與修復活動。','','## 執行與資料品質','','- 搜尋參數：十組指定查詢、`--limit 10 --include-trending-daily --include-readme`，以 `--snapshot-date 2026-11-03` 歸檔。','- 限流與擷取異常：見 `run-status.json`（完成後更新）；歷史專案若 API 失敗，收集器可能沿用上次資料，相關項目列於 `collector.log`，不可當成本次新鮮觀測。','']
(out/'analysis.md').write_text('\n'.join(lines),encoding='utf-8')
print('analysis written: 9 repos')
