# demo/  可运行原型

`dual-agent/index.html` 是当前给老师看的单页 Demo。对话已接 DeepSeek（默认 `deepseek-v4-flash`），Key 只放在仓库根目录 `.env`，不写进页面。

## 启动

在仓库根目录：

```bash
copy .env.example .env
# 把 DeepSeek Key 填进 .env 的 LLM_API_KEY=
py -3 demo/server.py
```

打开 http://127.0.0.1:8767/

直接双击打开 HTML **不会**走到模型；没有 Key 或服务没开时，助手仍用原来的本地对照模板。

## 部署到 Render

1. 打开 https://dashboard.render.com ，用 GitHub 登录。
2. **New → Blueprint**，选仓库 `Multicultural-Medicine`（会读根目录 `render.yaml`）。
   或 **New → Web Service**，连同一个仓库，Runtime 选 **Python**，Start Command 填 `python demo/server.py`。
3. Environment 填写（**不要写进 GitHub**）：

| 变量 | 值 |
| --- | --- |
| `LLM_API_KEY` | 你的 DeepSeek Key |
| `LLM_BASE_URL` | `https://api.deepseek.com` |
| `LLM_MODEL` | `deepseek-v4-flash` |

4. 部署完成后打开 `https://你的服务名.onrender.com/`。

免费实例大约 15 分钟没人访问会休眠，下次打开要等几十秒冷启动。没有 Key 时页面能开，对话走本地对照。

| 变量 | 说明 |
| --- | --- |
| `LLM_API_KEY` | DeepSeek Key；空则 mock |
| `LLM_BASE_URL` | 默认 `https://api.deepseek.com` |
| `LLM_MODEL` | 默认 `deepseek-v4-flash` |
| `LLM_MOCK=1` | 强制本地 mock |

新功能请写到 `src/` 对应目录。迁代码时：

- 文献 `ENTRIES` / `SHELVES` → `src/literature/data/`
- `CLINIC_PROMPT` / `RESEARCH_PROMPT` 与问答 → `src/agents/`
- 论坛 UI → `src/forum/`
- 顶栏与路由 → `src/app/`
