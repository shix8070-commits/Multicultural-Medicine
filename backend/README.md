# backend/  【正式服务，张鸣拼装】

同域托管 `src/` 小程序画面，并提供 `/api/*`。选型见 `docs/技术架构文档.md`。

```bash
uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

打开 `http://127.0.0.1:8000/` 即前端。部署到 Render 后发给老师的是同一个链接。

| 人 | 目录 |
| --- | --- |
| 张璨 | `api/literature.py`、`db/` 种子文献 |
| 何权 | `agents/`、`rules/`、`api/session.py` `chat.py` `signal.py` `judge.py`、`llm/`、`prompts/` |
| 张鸣 | `app.py`、`api/deps.py` `user.py` `forum.py` `literature_admin.py`、Docker / Render |
