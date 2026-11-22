# 每日冷知識（Daily Trivia）v2.0

支援電腦與手機安裝、離線閱讀（PWA）的跨領域每日冷知識 App，每天自動更新並附上可點擊查證的繁體中文維基百科連結。

- **線上網址**：`https://kt-bot12.github.io/daily-trivia/`

## 核心特色
- **每日自動切換＋維基百科即時同步**：午夜 00:00 自動換新題，同時串接維基百科公開 API 顯示「歷史上的今天」與無限隨機新知。
- **先猜再看猜題模式**：可隨時切換趣味猜題模式，先思考再翻開解析與來源。
- **一鍵下載 4:5 分享圖卡（PNG）**：內建 `<canvas>` 排版引擎，將今日冷知識轉成適合 LINE／IG／Threads 分享的精美圖卡。
- **中文語音朗讀**：通勤、做家事時一鍵用聽的吸收新知。
- **連續打卡與成就徽章**：追蹤連續探索天數，解鎖 6 項知識成就徽章。
- **完整離線 PWA 與社群縮圖**：獨立 `manifest.json`、Service Worker 離線快取、專屬 App 圖示與 Open Graph 分享預覽圖。

## 專案結構
```text
.
├── index.html              # 主應用程式（響應式 UI、圖卡引擎、語音朗讀、成就系統）
├── facts.json              # 獨立冷知識題庫（8 大領域 38 則，每則皆附維基百科連結）
├── manifest.json           # PWA 應用程式設定檔
├── sw.js                   # Service Worker 離線快取引擎
├── assets/
│   ├── icon-192.png        # PWA / iOS App 圖示（192×192）
│   ├── icon-512.png        # PWA 高解析圖示（512×512）
│   └── og-cover.jpg        # 社群分享預覽封面（1200×630）
├── scripts/
│   └── validate_facts.py   # 題庫格式與來源連結防呆驗證腳本
└── CHANGELOG.md            # 版本更新紀錄
```

## 題庫品質驗證
新增或編輯 `facts.json` 後，可執行以下指令檢查格式、重複 ID 與來源連結：
```bash
python3 scripts/validate_facts.py facts.json
```
