# -*- coding: utf-8 -*-
"""三条闭环。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#1d2430"
MUTED = "#5c6573"
BLUE = "#dbeafe"
BLUE_E = "#3b82c4"
PURPLE = "#ede9fe"
PURPLE_E = "#6b6ad6"
TEAL = "#e8f4f2"
TEAL_E = "#2f6f6a"
SLATE = "#e8eef4"
SLATE_E = "#64748b"


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.3)
    plt.close(fig)
    print("ok", name)


def rbox(ax, x, y, w, h, title, sub=None, fc="white", ec="#334155", lw=1.65, tfs=12.5):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.07",
        facecolor=fc, edgecolor=ec, linewidth=lw, clip_on=False, zorder=3,
    ))
    if sub:
        ax.text(x + w / 2, y + h * 0.64, title, ha="center", va="center",
                fontsize=tfs, fontweight="bold", color=INK, zorder=4)
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center",
                fontsize=10.2, color=MUTED, zorder=4)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center",
                fontsize=tfs, fontweight="bold", color=INK, zorder=4)


def arr_h(ax, x1, x2, y):
    ax.add_patch(FancyArrowPatch(
        (x1, y), (x2, y), arrowstyle="-|>", mutation_scale=12,
        linewidth=1.55, color="#334155", clip_on=False, zorder=2,
    ))


def return_arc(ax, x_left, x_right, y, label):
    ax.annotate(
        "",
        xy=(x_left, y),
        xytext=(x_right, y),
        arrowprops=dict(
            arrowstyle="-|>",
            color="#334155",
            lw=1.55,
            mutation_scale=12,
            connectionstyle="arc3,rad=0.28",
        ),
        zorder=2,
    )
    ax.text((x_left + x_right) / 2, y - 0.72, label,
            ha="center", va="center", fontsize=11, color=INK, fontweight="bold")


def lane(ax, y, h, label, fc):
    ax.add_patch(Rectangle((0.28, y), 17.64, h, facecolor=fc, edgecolor="#d0d7e2",
                           linewidth=1.0, zorder=0, clip_on=False))
    ax.text(0.48, y + h - 0.34, label, fontsize=13, fontweight="bold", color=INK, zorder=1)


def draw_loop(ax, y_lane, h_lane, lane_label, lane_fc, y_box, boxes, ret_label):
    lane(ax, y_lane, h_lane, lane_label, lane_fc)
    w, h, gap = 3.35, 1.38, 0.42
    x0 = 1.55
    xs = []
    for i, (title, sub, fc, ec) in enumerate(boxes):
        x = x0 + i * (w + gap)
        xs.append(x)
        rbox(ax, x, y_box, w, h, title, sub, fc, ec)
        if i < len(boxes) - 1:
            arr_h(ax, x + w, x + w + gap, y_box + h / 2)
    left_c = xs[0] + w * 0.35
    right_c = xs[-1] + w * 0.65
    return_arc(ax, left_c, right_c, y_box, ret_label)


def draw():
    fig, ax = plt.subplots(figsize=(18.2, 11.4), facecolor="white")
    ax.set_xlim(0, 18.2)
    ax.set_ylim(0.05, 11.4)
    ax.axis("off")

    ax.text(9.1, 11.05, "三条闭环", ha="center", fontsize=22, fontweight="bold", color=INK)
    ax.text(9.1, 10.58, "闭环 1、2 共用文献库 · 闭环 3 走论坛",
            ha="center", fontsize=12.5, color=MUTED)

    draw_loop(
        ax, 7.22, 3.12, "闭环 1 · 医生查证", "#f4f9fc", 8.05,
        [
            ("医生提问", "民族 + 病 / 药", BLUE, BLUE_E),
            ("临床助手", "辅助判断 · 前沿研究", BLUE, BLUE_E),
            ("文献库 / 速查", "MES · PICOS · 出处", TEAL, TEAL_E),
            ("带走判断", "结论 + 来源可点", BLUE, BLUE_E),
        ],
        "下次再问 · 或去速查核对",
    )

    draw_loop(
        ax, 3.82, 3.12, "闭环 2 · 科研查证", "#f6f4fc", 4.65,
        [
            ("科研提问", "这题做不做", PURPLE, PURPLE_E),
            ("科研助手", "开题 · 做不做 · 证据", PURPLE, PURPLE_E),
            ("文献 + 现场", "双源对照", TEAL, TEAL_E),
            ("三选一结论", "跟 / 不跟 / 再等等", PURPLE, PURPLE_E),
        ],
        "研判记录 · 换题再问",
    )

    draw_loop(
        ax, 0.22, 3.32, "闭环 3 · 论坛交流", "#f4f5f7", 1.18,
        [
            ("医生发帖", "现场问题", SLATE, SLATE_E),
            ("我的论坛", "发现 · 发布 · 聊天", SLATE, SLATE_E),
            ("科研看帖", "了解现场", SLATE, SLATE_E),
            ("继续交流", "跟帖 · 回复", SLATE, SLATE_E),
        ],
        "现场信息持续流通",
    )

    save(fig, "12-closed-loop.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
