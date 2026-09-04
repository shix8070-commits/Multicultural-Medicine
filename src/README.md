# src/ — 本期开发主目录

入口：`app/index.html`。脚本加载顺序见该文件注释，不要改乱。

```
src/
├── shared/          【张鸣守接口】三人只调用，不擅自改形状
│   ├── contracts.js
│   ├── storage.js
│   └── state.js
├── literature/      【张璨】来源、分类、查找
│   ├── data/shelves.js
│   ├── data/entries.js      ★ 先补演示题条目
│   ├── js/search.js
│   ├── js/pages.js          ★ 速查 / 详情 / 空态
│   └── css/search.css
├── agents/          【何权】临床助手 + 科研助手
│   ├── shared/parse.js · refuse.js · signals.js
│   ├── clinic/prompt.js · agent.js
│   ├── research/prompt.js · agent.js
│   ├── js/pages.js          ★ 两助手页面
│   └── css/agents.css
├── forum/           【张鸣】论坛（禁止写入 ENTRIES，禁止给 Agent 当出处）
│   ├── data/seed-posts.js
│   ├── js/store.js · pages.js
│   └── css/forum.css
└── app/             【张鸣】外壳、顶栏、路由
    ├── index.html
    ├── css/app.css
    ├── js/app.js
    └── assets/
```

| 人 | 开工先打开 |
| --- | --- |
| 张璨 | `literature/README.md` → 改 `data/entries.js` 和 `js/pages.js` |
| 何权 | `agents/README.md` → 改 `clinic/`、`research/`、`js/pages.js` |
| 张鸣 | `app/`、`forum/`、`shared/`、仓库根目录 `deploy/` |

挂到 `window.MM` 上的函数，名字以 `src/shared/contracts.js` 为准。
