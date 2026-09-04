# -*- coding: utf-8 -*-
"""Demo 本地服务：托管 dual-agent 页面，并把对话转发到 DeepSeek（默认 deepseek-v4-flash）。

用法（仓库根目录）：
  py -3 demo/server.py
然后打开 http://127.0.0.1:8767/

Key 放在仓库根目录 .env，不要写进 HTML。
"""

from __future__ import annotations

import json
import mimetypes
import os
import sys
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEMO_DIR = Path(__file__).resolve().parent / "dual-agent"
# 本地默认 8767；Render 会注入 PORT，必须监听 0.0.0.0
HOST = os.getenv("HOST") or "0.0.0.0"
PORT = int(os.getenv("PORT") or os.getenv("DEMO_PORT") or "8767")


def _load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv(ROOT / ".env")


def _settings() -> dict:
    api_key = (
        os.getenv("LLM_API_KEY")
        or os.getenv("DEEPSEEK_API_KEY")
        or os.getenv("GROQ_API_KEY")
        or ""
    ).strip()
    mock_env = (os.getenv("LLM_MOCK") or "").strip().lower()
    mock = mock_env in {"1", "true", "yes", "on"} or not api_key
    return {
        "api_key": api_key,
        "model": (os.getenv("LLM_MODEL") or "deepseek-v4-flash").strip(),
        "base_url": (os.getenv("LLM_BASE_URL") or "https://api.deepseek.com").rstrip("/"),
        "timeout": float(os.getenv("LLM_TIMEOUT") or "60"),
        "mock": mock,
    }


def _chat_url(base: str) -> str:
    base = base.rstrip("/")
    if base.endswith("/v1"):
        return base + "/chat/completions"
    return base + "/v1/chat/completions"


def _mock_reply(messages: list) -> str:
    last = ""
    for item in reversed(messages):
        if item.get("role") == "user":
            last = (item.get("content") or "").strip()
            break
    snippet = (last[:80] + "…") if len(last) > 80 else (last or "（空）")
    return f"已收到：{snippet}。当前为本地 mock，请在 .env 填写 LLM_API_KEY 后重启。"


def _http_chat(cfg, messages, temperature, max_tokens):
    payload = {
        "model": cfg["model"],
        "messages": messages,
        "temperature": temperature,
    }
    if max_tokens is not None:
        payload["max_tokens"] = max_tokens
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        _chat_url(cfg["base_url"]),
        data=body,
        headers={
            "Authorization": "Bearer " + cfg["api_key"],
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=cfg["timeout"]) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"模型接口错误 HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"模型网络错误: {exc.reason}") from exc
    except TimeoutError as exc:
        raise RuntimeError(f"模型超时（>{cfg['timeout']}s）") from exc

    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("模型响应格式异常") from exc
    if content is None:
        raise RuntimeError("模型返回空 content")
    text = str(content).strip()
    if not text:
        raise RuntimeError("模型只返回了思考过程，没有正文。请增大 max_tokens 后重试。")
    return text


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        sys.stderr.write("[demo] " + (fmt % args) + "\n")
        sys.stderr.flush()

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except Exception:
            traceback.print_exc()
            try:
                self.close_connection = True
            except Exception:
                pass

    def do_OPTIONS(self):
        self._send(204, b"", "text/plain; charset=utf-8")

    def do_GET(self):
        path = urlparse(self.path).path
        if path in {"/api/health", "/health"}:
            cfg = _settings()
            return self._json(200, {"ok": True, "model": cfg["model"], "mock": cfg["mock"]})
        if path in {"/", "/index.html"}:
            path = "/index.html"
        rel = unquote(path.lstrip("/")) or "index.html"
        target = (DEMO_DIR / rel).resolve()
        if DEMO_DIR.resolve() not in target.parents and target != DEMO_DIR.resolve():
            return self._send(403, b"forbidden", "text/plain; charset=utf-8")
        if not target.is_file():
            return self._send(404, b"not found", "text/plain; charset=utf-8")
        data = target.read_bytes()
        mime = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
        if target.suffix == ".html":
            mime = "text/html; charset=utf-8"
        self._send(200, data, mime)

    def do_POST(self):
        path = urlparse(self.path).path
        if path != "/api/chat":
            return self._json(404, {"error": "not found"})
        length = int(self.headers.get("Content-Length") or "0")
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return self._json(400, {"error": "请求不是合法 JSON"})

        messages = payload.get("messages")
        if not isinstance(messages, list) or not messages:
            return self._json(400, {"error": "messages 不能为空"})
        cleaned = []
        for item in messages:
            if not isinstance(item, dict):
                return self._json(400, {"error": "message 格式错误"})
            role = str(item.get("role") or "").strip()
            content = item.get("content")
            if role not in {"system", "user", "assistant"}:
                return self._json(400, {"error": f"不支持的 role: {role}"})
            if content is None:
                return self._json(400, {"error": "message.content 不能为空"})
            cleaned.append({"role": role, "content": str(content)})

        temperature = payload.get("temperature", 0.3)
        try:
            temperature = float(temperature)
        except (TypeError, ValueError):
            temperature = 0.3
        max_tokens = payload.get("max_tokens", 4096)
        try:
            max_tokens = int(max_tokens) if max_tokens is not None else None
        except (TypeError, ValueError):
            max_tokens = 800

        cfg = _settings()
        try:
            if cfg["mock"]:
                text = _mock_reply(cleaned)
            else:
                text = _http_chat(cfg, cleaned, temperature, max_tokens)
        except Exception as exc:  # noqa: BLE001
            return self._json(502, {"error": str(exc), "model": cfg["model"], "mock": cfg["mock"]})
        return self._json(200, {"content": text, "model": cfg["model"], "mock": cfg["mock"]})

    def _json(self, code, data):
        blob = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self._send(code, blob, "application/json; charset=utf-8")

    def _send(self, code, body, content_type):
        if not isinstance(body, (bytes, bytearray)):
            body = str(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(body)
        self.close_connection = True


def main() -> None:
    print("starting demo server…", flush=True)
    if not DEMO_DIR.is_dir():
        raise SystemExit("找不到 demo/dual-agent/")
    cfg = _settings()
    try:
        httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    except OSError as exc:
        raise SystemExit(f"端口 {PORT} 无法绑定: {exc}") from exc
    print(f"Demo  http://{HOST}:{PORT}/", flush=True)
    print(f"模型  {cfg['model']}  mock={cfg['mock']}", flush=True)
    if cfg["mock"]:
        print("未读到 LLM_API_KEY，对话会走本地 mock。把 Key 写入仓库根目录 .env 后重启。", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止", flush=True)


if __name__ == "__main__":
    main()
