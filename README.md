# 通勤新手指南

給第一次搭臺北捷運的人、通勤新手與外國旅客的靜態知識網站。

- [瀏覽網站](https://sooonggg.github.io/commute-guide/)
- [開發規則 AGENTS.md](AGENTS.md)
- [文章範本](templates/guide-template.html)

## 專案要做什麼？
將官方乘車資訊整理為簡短指南，讓使用者快速找到重點、操作步驟與英文求助句。首頁可以搜尋文章，也可以勾選出發前清單。這是依照 AGENTS.md 製作的網站，沒有線上 AI、即時查車或路線規劃功能。

## 目前內容
1. [單程票，隔天還能用嗎？](guides/single-ticket.html)
2. [到了月臺，怎麼安心上車？](guides/platform-safety.html)

兩篇採用相同結構及共用 CSS，展示規則可以重複使用。

## 檔案結構
```text
AGENTS.md                    給 AI 的開發規則
index.html                   首頁與搜尋
assets/styles.css            共用外觀
assets/main.js               搜尋、清單計數
 guides/single-ticket.html   票券指南
 guides/platform-safety.html 候車指南
templates/guide-template.html 新文章範本
scripts/check_site.py         本機檢查
.nojekyll                    GitHub Pages 靜態發布
```

## 如何新增內容？
先讓 AI 閱讀 AGENTS.md，再提供主題與官方資料。AI 應複製範本、查核來源、填寫五個固定章節、加入首頁卡片、補相關文章連結，最後檢查。

可使用這段指令：
> 請先閱讀 AGENTS.md，依照既有格式新增「轉乘前的小準備」指南。先查閱官方來源，未確認的規定不要猜測。沿用共用樣式，更新首頁與相關文章，並回報實際執行的檢查。

此主題尚未實作，僅為下一篇擴充示例。規則讓 AI 知道檔案放哪裡、文章寫什麼、外觀怎麼統一，以及完成前要檢查哪些項目。

## 本機預覽與檢查
不需要 API 金鑰或安裝套件。用 Python 3：
```sh
python3 scripts/check_site.py
python3 -m http.server 8765 --bind 127.0.0.1
```
瀏覽 http://127.0.0.1:8765/ 。亦可直接開啟 index.html。
檢查腳本會檢查正式頁面的必要結構、本機檔案與錨點連結、來源及日期、占位文字。它不會替代人工查核官方規定，也不會檢查遠端連結是否失效。
手動檢查：搜尋「單程票」、不存在關鍵字、清除搜尋、勾選清單、進入兩篇文章並返回首頁，查看手機與桌面版面。

## GitHub Pages
Repository Settings → Pages → Deploy from a branch → main → /(root)。不需要 Colab 或後端主機。

## 官方來源
於 2026-11-16 閱讀並摘要；內容以官方最新公告為準。
- [臺北捷運：單程票](https://www.metro.taipei/cp.aspx?n=CEF54168B23F73B4&s=AD70DC4F6A708EA7)
- [臺北捷運：月臺文字說明](https://www.metro.taipei/cp.aspx?n=1CA42956BE125ECD&s=B367BE618D11B56C)

本站為非官方學習專案。英文求助句是本站整理翻譯，非官方譯文；不提供即時交通資訊。

## AI 協作說明
本專案使用 Codex 協助草擬 AGENTS.md、HTML/CSS/JavaScript、文章範本、檢查腳本與說明文字，並協助查閱官方資料及測試介面。先建立規則，再依規則製作首頁及兩篇指南。網站執行時不呼叫 AI。

理解重點：AGENTS.md 是給開發 AI 閱讀的工作規則，不是使用者聊天的 system prompt。共用 CSS 統一外觀；範本固定文章結構；新增頁面時還要更新首頁入口，使用者才找得到。

繳交時應保留實際 AI 協作對話與成果截圖，閱讀後再用自己的話說明理解及修改內容，不把 AI 產出的程式宣稱為全部獨立撰寫。
