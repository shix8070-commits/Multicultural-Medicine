# -*- coding: utf-8 -*-
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False
BLACK = "#111111"


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.3)
    plt.close(fig)
    print("ok", name)


def box(ax, x, y, w, h, title, sub=None, fc="white", ec=BLACK, lw=2.6, fs=18, sub_fs=12):
    p = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor=fc, edgecolor=ec, linewidth=lw, clip_on=False,
    )
    ax.add_patch(p)
    if sub:
        ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center",
                fontsize=fs, fontweight="bold", color=BLACK)
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center",
                fontsize=sub_fs, color="#444")
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center",
                fontsize=fs, fontweight="bold", color=BLACK)


def h_arrow(ax, x1, y, x2):
    ax.add_patch(FancyArrowPatch(
        (x1, y), (x2, y), arrowstyle="-|>", mutation_scale=20,
        linewidth=2.8, color=BLACK, clip_on=False,
    ))


def v_arrow(ax, x, y1, y2):
    ax.add_patch(FancyArrowPatch(
        (x, y1), (x, y2), arrowstyle="-|>", mutation_scale=18,
        linewidth=2.4, color=BLACK, clip_on=False,
    ))


def main():
    fig, ax = plt.subplots(figsize=(16.5, 8.2))
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 8.2)
    ax.axis("off")
    ax.text(8.25, 7.85, "技术架构图", ha="center", fontsize=28, fontweight="bold")

    # 表现层
    ax.text(0.35, 6.95, "表现层", fontsize=14, color="#555")
    box(ax, 1.2, 6.05, 6.4, 1.05, "临床助手", "病例对话 · 历史记录 · 文献速查", fc="#dcfce7", fs=20)
    box(ax, 8.9, 6.05, 6.4, 1.05, "科研助手", "现场发现 · 研判记录 · 文献速查", fc="#ede9fe", fs=20)

    v_arrow(ax, 4.4, 6.05, 5.35)
    v_arrow(ax, 12.1, 6.05, 5.35)

    # Agent 层
    ax.text(0.35, 5.15, "Agent 层", fontsize=14, color="#555")
    box(ax, 1.2, 4.15, 6.4, 1.15, "临床助手 Agent", "前沿研究  |  辅助判断", fc="#bbf7d0", fs=20)
    box(ax, 8.9, 4.15, 6.4, 1.15, "科研助手 Agent", "开题对照 | 上传了啥 | 做不做研究", fc="#ddd6fe", fs=18)

    v_arrow(ax, 8.25, 4.15, 3.45)

    # 服务层
    ax.text(0.35, 3.25, "服务层", fontsize=14, color="#555")
    box(ax, 0.6, 2.2, 3.5, 1.15, "检索服务", "四维分类 · 关键词映射", fc="#dbeafe", fs=18, sub_fs=12)
    box(ax, 4.5, 2.2, 3.5, 1.15, "会话服务", "病例 / 研判对话归档", fc="#dbeafe", fs=18, sub_fs=12)
    box(ax, 8.4, 2.2, 3.5, 1.15, "信号服务", "脱敏校验 · 条数统计", fc="#dbeafe", fs=18, sub_fs=12)
    box(ax, 12.3, 2.2, 3.5, 1.15, "研判服务", "文献×信号对照规则", fc="#dbeafe", fs=18, sub_fs=12)

    v_arrow(ax, 2.35, 2.2, 1.5)
    v_arrow(ax, 6.25, 2.2, 1.5)
    v_arrow(ax, 10.15, 2.2, 1.5)
    v_arrow(ax, 14.05, 2.2, 1.5)

    # 数据层
    ax.text(0.35, 1.3, "数据层", fontsize=14, color="#555")
    box(ax, 0.6, 0.25, 4.9, 1.15, "文献库", "公开条目 · 与信号隔离", fc="#e7f1f1", ec="#2a7a7a", lw=3.2, fs=20)
    box(ax, 5.85, 0.25, 4.9, 1.15, "信号库", "脱敏观察 · 只计条数", fc="white", fs=20)
    box(ax, 11.1, 0.25, 4.7, 1.15, "记录库", "对话 / 研判 / 收藏", fc="white", fs=20)

    save(fig, "06-tech-architecture.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    main()
