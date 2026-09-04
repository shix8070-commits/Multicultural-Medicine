# -*- coding: utf-8 -*-
"""产品功能总览。"""
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


def box(ax, x, y, w, h, title, lines, fc, ec, lw=1.8):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.08",
        facecolor=fc, edgecolor=ec, linewidth=lw, clip_on=False,
    ))
    ax.text(x + w / 2, y + h - 0.42, title, ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)
    ax.text(x + w / 2, y + h / 2 - 0.18, lines, ha="center", va="center",
            fontsize=12, color=MUTED, linespacing=1.45)


def draw():
    fig, ax = plt.subplots(figsize=(16.6, 10.8), facecolor="white")
    ax.set_xlim(0, 16.6)
    ax.set_ylim(0, 10.8)
    ax.axis("off")

    ax.text(8.3, 10.35, "多民族健康证据服务 · 本期功能",
            ha="center", fontsize=22, fontweight="bold", color=INK)
    ax.text(8.3, 9.82, "一套文献库 · 两个 Agent · 一层论坛",
            ha="center", fontsize=12, color=MUTED)

    box(ax, 0.5, 7.35, 15.6, 2.05,
        "文献库 + 文献速查",
        "四类主题：流病·患病率 / 危险因素 / 遗传·变异 / 药物基因组\n"
        "点「文献」→ 选主题 → 关键词 → 筛选 → 结果 / 详情\n"
        "MES 编号 · 证据等级 · PICOS · 出处 · 边界",
        "#e8f4f2", "#2f6f6a", lw=2.2)

    ax.add_patch(FancyArrowPatch(
        (8.3, 7.35), (8.3, 6.85), arrowstyle="-|>", mutation_scale=14,
        linewidth=1.6, color="#334155", clip_on=False,
    ))
    ax.text(9.55, 7.05, "两个 Agent 共用", fontsize=11, color="#334155")

    box(ax, 0.5, 4.55, 7.4, 2.2,
        "临床助手",
        "用户：基层医生\n"
        "技能：辅助判断 · 前沿研究\n"
        "先给结论 → 参考来源 [MES] 可点",
        "#dbeafe", "#3b82c4")

    box(ax, 8.7, 4.55, 7.4, 2.2,
        "科研助手",
        "用户：科研人员\n"
        "技能：开题对照 · 做不做 · 证据\n"
        "文献 + 现场信号 → 三选一结论",
        "#ede9fe", "#6b6ad6")

    ax.add_patch(FancyArrowPatch(
        (8.3, 4.55), (8.3, 4.05), arrowstyle="-|>", mutation_scale=14,
        linewidth=1.6, color="#334155", clip_on=False,
    ))
    ax.text(9.8, 4.22, "材料少 → 论坛交流", fontsize=11, color="#334155")

    box(ax, 0.5, 1.55, 15.6, 2.4,
        "我的论坛",
        "医生发现场问题 · 科研看帖回复\n"
        "发现 / 发布 / 聊天 / 圈子",
        "#e8eef4", "#64748b", lw=2.0)

    ax.text(8.3, 0.85, "顶栏：临床助手  |  科研助手  |  我的论坛",
            ha="center", fontsize=12, color=INK)
    ax.text(8.3, 0.38, "演示：维吾尔族 × 华法林 × 出血风险",
            ha="center", fontsize=11, color=MUTED)

    save(fig, "13-product-features.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
