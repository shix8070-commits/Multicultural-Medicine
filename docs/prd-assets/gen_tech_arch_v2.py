# -*- coding: utf-8 -*-
"""技术架构分层图：含论坛与数据隔离。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#1d2430"
MUTED = "#5c6573"
BLUE_FC = "#dbeafe"
PURPLE_FC = "#ede9fe"
SLATE_FC = "#e8eef4"
TEAL_FC = "#e8f4f2"
YEL_FC = "#fff3b0"


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.28)
    plt.close(fig)
    print("ok", name)


def box(ax, x, y, w, h, title, sub=None, fc="white", ec="#334155", lw=1.8, fs=15, sub_fs=11):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.08",
        facecolor=fc, edgecolor=ec, linewidth=lw, clip_on=False,
    ))
    if sub:
        ax.text(x + w / 2, y + h * 0.64, title, ha="center", va="center",
                fontsize=fs, fontweight="bold", color=INK)
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center",
                fontsize=sub_fs, color=MUTED)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center",
                fontsize=fs, fontweight="bold", color=INK)


def v_arrow(ax, x, y1, y2):
    ax.add_patch(FancyArrowPatch(
        (x, y1), (x, y2), arrowstyle="-|>", mutation_scale=14,
        linewidth=1.6, color="#334155", clip_on=False,
    ))


def draw():
    fig, ax = plt.subplots(figsize=(18.2, 10.4), facecolor="white")
    ax.set_xlim(0, 18.2)
    ax.set_ylim(0, 10.4)
    ax.axis("off")
    ax.set_facecolor("white")

    ax.text(9.1, 10.05, "多民族健康证据服务 · 技术架构",
            ha="center", fontsize=22, fontweight="bold", color=INK)
    ax.text(9.1, 9.6, "一套文献、两个助手、一层论坛。论坛库不进入 Agent。",
            ha="center", fontsize=12, color=MUTED)

    ax.text(0.3, 8.95, "表现层", fontsize=13, color=MUTED)
    box(ax, 0.5, 7.85, 5.4, 1.0, "临床助手", "病例对话 · 文献速查 · 历史", fc=BLUE_FC, fs=16)
    box(ax, 6.4, 7.85, 5.4, 1.0, "科研助手", "开题对照 · 研判 · 文献速查", fc=PURPLE_FC, fs=16)
    box(ax, 12.3, 7.85, 5.4, 1.0, "我的论坛", "发现 · 发布 · 聊天", fc=SLATE_FC, fs=16)

    v_arrow(ax, 3.2, 7.85, 7.25)
    v_arrow(ax, 9.1, 7.85, 7.25)

    ax.text(0.3, 7.05, "Agent 层", fontsize=13, color=MUTED)
    box(ax, 0.5, 5.85, 5.4, 1.1, "临床助手 Agent", "对照现有研究 · 拒答诊疗", fc="#bfdbfe", fs=15)
    box(ax, 6.4, 5.85, 5.4, 1.1, "科研助手 Agent", "开题对照 · 做 / 不做 / 再等等", fc="#ddd6fe", fs=15)
    box(ax, 12.3, 5.85, 5.4, 1.1, "论坛无 Agent", "讨论不当证据 · 禁止被引用", fc=YEL_FC, ec="#b8922a", fs=15)

    v_arrow(ax, 3.2, 5.85, 5.25)
    v_arrow(ax, 9.1, 5.85, 5.25)
    v_arrow(ax, 15.0, 5.85, 5.25)

    ax.text(0.3, 5.05, "服务层", fontsize=13, color=MUTED)
    box(ax, 0.4, 3.75, 4.15, 1.15, "检索服务", "四类筛选 · 关键词", fc=BLUE_FC, fs=14)
    box(ax, 4.75, 3.75, 4.15, 1.15, "会话服务", "对话归档 · 抽槽", fc=BLUE_FC, fs=14)
    box(ax, 9.1, 3.75, 4.15, 1.15, "研判服务", "只对照文献条数", fc=PURPLE_FC, fs=14)
    box(ax, 13.45, 3.75, 4.35, 1.15, "论坛服务", "发帖 · 回复 · 隔离", fc=SLATE_FC, fs=14)

    for x in (2.47, 6.82, 11.17, 15.62):
        v_arrow(ax, x, 3.75, 3.15)

    ax.text(0.3, 2.95, "数据层", fontsize=13, color=MUTED)
    box(ax, 0.4, 1.55, 5.5, 1.2, "文献库", "公开条目 · 有出处有边界", fc=TEAL_FC, ec="#2f6f6a", lw=2.4, fs=15)
    box(ax, 6.15, 1.55, 5.5, 1.2, "记录库", "对话 / 研判 / 收藏", fc="white", fs=15)
    box(ax, 11.9, 1.55, 5.9, 1.2, "论坛库", "帖子与聊天 · 不进 Agent", fc=YEL_FC, ec="#b8922a", lw=2.2, fs=15)

    ax.text(9.1, 0.95, "分工：张璨 · 文献库与检索　　何权 · 两 Agent 与会话 / 研判　　张鸣 · 论坛、外壳与试用链接",
            ha="center", fontsize=12, color=INK)
    ax.text(9.1, 0.45, "黄：论坛不得写入文献库，也不得作为助手答据。医生不在临床助手里上传观察。",
            ha="center", fontsize=11, color="#9a3412")

    save(fig, "10-tech-architecture.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
