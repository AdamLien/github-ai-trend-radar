# GitHub AI 趨勢雷達分析（2026-09-06）

## 今日結論

本日收集到的候選，最強訊號不是單純的累積星數，而是「今日 stars + snapshot star delta + 最近 push/release」同時出現：技能型 agent harness、開源 coding agent、local inference，以及可直接示範的多代理教學產品。這批資料反映開發者注意力，不等同於付費需求或生產環境成熟度；採用前仍要驗證授權、依賴、部署與 issue 品質。

## 值得保留的專案

| Repo | 用途與觀察到的動能 | 總 stars | 風險 | 建議 | 對 Adam／Metabiz 的關聯 |
| --- | --- | ---: | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 工程師日常 agent skills 集合；今日約 +2,206，snapshot +2,136，254,037 stars，最近 push 2026-09-04。技能內容和可複用工作流的訊號非常強。 | 254,037 | MIT，但規模大、issue 467；需逐項審查 skill 的安全邊界與適用模型。 | Skill candidate | 可作為課程的「技能設計與分發」案例，也可對照 Metabiz 自建 skills／AI office automation 的模組化方法。 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 面向 Claude Code、Codex、OpenCode、Cursor 的 agent harness：skills、memory、security、research-first workflow；今日約 +1,486，snapshot +1,377，250,762 stars。 | 250,762 | MIT；issue 164，但涵蓋面很廣，容易把方法論當成即插即用產品。 | Deep research | 適合做「AI 辦公室作業系統／agent governance」深研，連結 Adam 課程、Know Metabiz wiki 的標準流程與品質控管。 |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 把 codebase 或系統描述轉成可驗證、可匯出的互動架構／流程／sequence 圖；snapshot +1,365，50,442 stars，最近 push 2026-09-06，v2.16.0。 | 50,442 | MIT；最近成長快但 issue 120，需測試輸出一致性、中文與複雜系統的可讀性。 | Demo content | 很適合示範「自然語言→知識圖／流程圖」：可用於課程教材、顧問交付物，以及把 Metabiz wiki 的流程視覺化。 |
| [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | 為既有 agent 接上本地模型，主打免費、私有、離線；今日約 +604，snapshot +555，3,537 stars，最近 push 2026-09-06。相對基數小但相對增長高。 | 3,537 | Apache-2.0；生態仍早期，硬體相容性、模型品質與各 agent adapter 是主要不確定性。 | Watch | 可作為 AI office automation 的私有化／成本控制備案；值得在不碰敏感資料的 sandbox 做 demo。 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 開源 coding agent；今日約 +552，snapshot +540，205,053 stars，最近 push 2026-09-06，v1.18.29。高星數仍伴隨近期更新。 | 205,053 | MIT；issue 5,738，規模與變動面大，需留意相容性、供應鏈與企業治理。 | Deep research | 適合比較 Codex／Claude Code／OpenCode 的課程單元，並評估是否能支援 Metabiz 內部開發與自動化。 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 可成長的 agent，涵蓋 Claude、Codex、LLM 與 desktop 入口；今日約 +520，snapshot +511，242,355 stars，最近 push 2026-09-06，v2026.8.31。 | 242,355 | MIT；issue 40,279 是重大維運訊號，需先做權限、資料外洩與長期記憶風險評估。 | Watch | 可研究「個人 agent 如何累積 context」與 Know Metabiz wiki 的知識回饋迴圈，但不宜直接接入公司資料。 |
| [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 一鍵啟動多代理互動課堂；snapshot +483，32,304 stars，最近 push 2026-09-06，並於當日發布 v1.0.1。 | 32,304 | MIT；issue 231；教學品質、agent 幻覺、成本與中文／英文課程可控性仍需實測。 | Demo content | 與 Adam 課程最直接相關：可示範多代理教學、互動教材與課程助教，也可測試轉成 Metabiz 內訓場景。 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Rust CLI proxy，宣稱降低 agent 讀取常見 dev command 輸出的 token 消耗 60–90%；snapshot +314，79,059 stars，最近 push 2026-09-05，v0.48.0。 | 79,059 | Apache-2.0；issue 1,946；輸出壓縮可能隱藏除錯資訊，須建立可回溯與安全例外規則。 | Skill candidate | 已用於本次 dashboard build；可納入 AI office automation 的成本／可觀測性課程，並成為 Metabiz agent 執行規範的一部分。 |

## 編輯與課程方向

1. 「Agent skills 正在變成新的開發者資產」：比較 `mattpocock/skills` 與 ECC 的 skill、memory、security 分層。
2. 「Coding agent 選型實驗」：用相同小專案比較 OpenCode、Codex、Claude Code 的 context、權限、成本與可維護性。
3. 「把 Metabiz wiki 變成可教、可驗證的系統圖」：用 Archify 將 SOP、CRM／報價流程和 agent handoff 視覺化。
4. 「一堂多代理互動課怎麼做」：以 OpenMAIC 做 demo，明確標出幻覺、評量與人工審核的位置。
5. 「私有模型與 token 成本」：以 Magnitude + RTK 做 sandbox，量測延遲、成本、品質和資料邊界，不把 GitHub 宣稱直接當成實測結果。

## 明日 watchlist

- `mattpocock/skills`、`affaan-m/ECC`：追 README／release 是否出現新的 skill 標準、權限或記憶機制。
- `magnitudedev/magnitude`：追 stars delta、硬體／模型支援與安裝成功率。
- `THU-MAIC/OpenMAIC`：驗證 v1.0.1 的課堂流程、中文體驗與多代理成本。
- `anomalyco/opencode`、`NousResearch/hermes-agent`：追 issue 關閉速度、破壞性變更與安全公告。
- `tt-a1i/archify`、`rtk-ai/rtk`：做最小可重現 demo，確認圖表／輸出壓縮不犧牲核查性。

## 判讀限制

本分析使用本次 collector 的 GitHub API metadata、README 摘要、release、issue、push 與 snapshot delta。stars today 是 GitHub Trending 的觀測值；搜尋結果的 snapshot delta 是相對前一份可用 snapshot 的變化。它們都不是使用者留存、營收、穩定性或企業採用的替代指標。
