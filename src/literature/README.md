# literature/  【负责人：张璨】

文献底座：来源、四类分类、怎么查找。何权的 Agent、张鸣的外壳都只 **读** 你导出的数据与检索函数。

## 你改

```
literature/
├── README.md          本说明
├── data/
│   ├── shelves.js     四类：prev / risk / geno / pgx
│   └── entries.js     文献条目（演示题至少 6 条，含出处和边界）
├── js/
│   ├── search.js      searchLiterature / getLiterature
│   └── pages.js       速查列表页、详情页、空态
└── css/
    └── search.css     只放速查/详情样式
```

## 你不改

`src/agents/`、`src/forum/`、`src/app/`、`deploy/`

## 完成标准

用「维吾尔族 / 华法林」能查出条目，点开看出处和边界；某一类没有文献时有空态。条目不要写进论坛，也不要在这里写对话回复。

样例字段可参考 `demo/dual-agent/index.html` 里的 `ENTRIES`，但演示题目要补上维吾尔族 × 华法林。
