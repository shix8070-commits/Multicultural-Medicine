# agents/  【负责人：何权】

临床助手 Agent 与科研助手 Agent。只检索 `MM.ENTRIES` / `MM.searchLiterature`。**禁止读取** `mm-posts-v1`。

## 你改

```
agents/
├── README.md
├── shared/
│   ├── parse.js       parseAsk、抽民族/病药/现象
│   └── refuse.js      拒答诊疗、拒引用论坛
├── clinic/
│   ├── prompt.js      临床助手提示词
│   └── agent.js       answerClinic
├── research/
│   ├── prompt.js      科研助手提示词
│   └── agent.js       answerResearch
├── js/
│   └── pages.js       临床首页、科研首页、对话区渲染
└── css/
    └── agents.css
```

## 你不改

`src/literature/data/`（条目内容问张璨改）、`src/forum/`、`deploy/`

## 完成标准

华法林对照能出出处或「不足」；做不做只对照文献条数；问怎么治、按帖子回答都拒绝。现场问题走论坛，助手里不做上传观察。
