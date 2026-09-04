# -*- coding: utf-8 -*-
"""正式整体技术栈：浏览器小程序画面 → FastAPI → SQLite。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#1d2430"
MUTED = "#5c6573"


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.28)
    plt.close(fig)
    print("ok", name)


def box(ax, x, y, w, h, lines, fc="#e8eef4", ec="#334155", lw=1.6):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.07",
        facecolor=fc, edgecolor=ec, linewidth=lw, clip_on=False,
    ))
    n = len(lines)
    for i, t in enumerate(lines):
        ax.text(
            x + w / 2,
            y + h - (i + 0.7) * (h / (n + 0.35)),
            t, ha="center", va="center",
            fontsize=14 if i == 0 else 12,
            fontweight="bold" if i == 0 else "normal",
            color=INK if i == 0 else MUTED,
        )


def arrow(ax, y1, y2):
    ax.add_patch(FancyArrowPatch(
        (6.2, y1), (6.2, y2), arrowstyle="-|>", mutation_scale=14,
        linewidth=1.6, color="#334155", clip_on=False,
    ))


def draw():
    fig, ax = plt.subplots(figsize=(12.6, 11.6), facecolor="white")
    ax.set_xlim(0, 12.6)
    ax.set_ylim(0, 11.6)
    ax.axis("off")

    ax.text(6.3, 11.15, "多民族健康证据服务 · 正式技术架构",
            ha="center", fontsize=20, fontweight="bold", color=INK)
    ax.text(6.3, 10.7, "浏览器打开链接（小程序画面）  →  FastAPI 同域托管  →  SQLite 四库",
            ha="center", fontsize=11, color=MUTED)

    box(ax, 1.4, 8.85, 9.8, 1.55, [
        "浏览器    src/app/index.html",
        "临床助手     科研助手     文献速查     我的论坛",
        "fetch /api/*     同域     Bearer token",
    ], fc="#dbeafe")

    arrow(ax, 8.85, 8.22)

    box(ax, 1.4, 5.45, 9.8, 2.65, [
        "FastAPI    backend/app.py    同域托管 src/",
        "api/     用户 · 文献 · 会话 · 信号 · 研判 · 论坛 · 收藏 · 入库",
        "agents/  临床助手 · 科研助手",
        "rules/   过滤 · 拒答 · 研判阈值 · 脱敏 · 论坛隔离",
        "llm/ + prompts/     db/  peewee Models + 种子灌库",
    ], fc="#ede9fe")

    arrow(ax, 5.45, 4.82)

    box(ax, 1.4, 2.85, 9.8, 1.85, [
        "SQLite    data/app.db",
        "文献库          信号库          记录库          论坛库",
        "Agent 只读已入库    只计条数         会话/消息/研判     禁止进入 Agent",
    ], fc="#e8f4f2", ec="#2f6f6a", lw=2.2)

    ax.text(6.3, 2.2, "规则与 AI 分离。用户消息先落库再调模型。cite_ids 只能是文献 ID。",
            ha="center", fontsize=11, color=INK)
    ax.text(6.3, 1.65, "createPost 不得写入 literature。文献缺出处或边界不得被引用。",
            ha="center", fontsize=11, color="#9a3412")
    ax.text(6.3, 1.1, "张璨 · 文献库与检索     何权 · 两 Agent / 会话 / 信号 / 研判     张鸣 · 外壳、论坛、后端拼装与部署",
            ha="center", fontsize=11, color=MUTED)

    save(fig, "11-tech-stack.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
