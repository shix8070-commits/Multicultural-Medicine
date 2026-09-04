# forum/  【负责人：张鸣】

医研交流层。数据只进 `mm-posts-v1`。**禁止** 把帖子写入 `MM.ENTRIES`，也禁止给 Agent 当 `citeIds`。

## 你改

```
forum/
├── README.md
├── data/
│   └── seed-posts.js    演示帖（围绕维吾尔族×华法林，标明不是证据）
├── js/
│   ├── store.js         createPost / listPosts
│   └── pages.js         发现、发布、聊天（打通一条即可）
└── css/
    └── forum.css
```

圈子、我的页可后补。整站顶栏和发布链接在 `src/app/` 与 `deploy/`。
