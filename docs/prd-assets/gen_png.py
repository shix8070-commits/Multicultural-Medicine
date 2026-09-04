# -*- coding: utf-8 -*-
"""生成 PRD 流程图 PNG：横向标准流程图，大字、粗线。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

TEAL = "#2a7a7a"
TEAL_BG = "#e7f1f1"
BLACK = "#111111"


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.3)
    plt.close(fig)
    print("ok", name)


def box(ax, x, y, w, h, title, sub=None, fc="white", ec=BLACK, lw=2.8, fs=22, sub_fs=13):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
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


def h_arrow(ax, x1, y, x2, lw=3.2):
    ax.add_patch(FancyArrowPatch(
        (x1, y), (x2, y),
        arrowstyle="-|>", mutation_scale=24,
        linewidth=lw, color=BLACK, clip_on=False,
    ))


def d_arrow(ax, p1, p2, dashed=False, lw=2.6):
    ax.add_patch(FancyArrowPatch(
        p1, p2,
        arrowstyle="-|>", mutation_scale=22,
        linewidth=lw, color=BLACK,
        linestyle=(0, (5, 4)) if dashed else "solid",
        clip_on=False,
    ))


def arch():
    fig, ax = plt.subplots(figsize=(16.5, 6.4))
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    ax.text(8.25, 6.0, "产品架构图", ha="center", fontsize=30, fontweight="bold")

    y, w, h = 3.35, 3.9, 1.35
    box(ax, 0.45, y, w, h, "科研助手", "② 查资料  ·  研判记录", fs=26, sub_fs=14)
    box(ax, 6.3, y, w, h, "文献库", "底座 · 数据 · 更新 · 反馈",
        fc=TEAL_BG, ec=TEAL, lw=4.2, fs=28, sub_fs=14)
    box(ax, 12.15, y, w, h, "临床助手", "① 查文献  ·  病例对话", fs=26, sub_fs=14)

    h_arrow(ax, 0.45 + w, y + h / 2, 6.3, lw=3.4)
    h_arrow(ax, 6.3 + w, y + h / 2, 12.15, lw=3.4)

    ax.annotate(
        "", xy=(0.45 + w * 0.55, y), xytext=(6.3 + w * 0.15, y),
        arrowprops=dict(arrowstyle="-|>", lw=2.2, color=BLACK, linestyle=(0, (5, 4))),
    )
    ax.text(4.15, 3.08, "研判记录", ha="center", fontsize=13, color="#555")

    ax.annotate(
        "", xy=(6.3 + w * 0.85, y), xytext=(12.15 + w * 0.45, y),
        arrowprops=dict(arrowstyle="-|>", lw=2.2, color=BLACK, linestyle=(0, (5, 4))),
    )
    ax.text(12.05, 3.08, "反馈现场信号（脱敏观察）", ha="center", fontsize=13, color="#555")

    y2, bw, bh = 0.95, 3.5, 0.95
    xs = [0.7, 6.5, 12.3]
    labels = ["文献库小闭环", "科研小闭环", "临床小闭环"]
    for i, (x, lb) in enumerate(zip(xs, labels)):
        box(ax, x, y2, bw, bh, lb, fs=20)
        if i < 2:
            h_arrow(ax, x + bw, y2 + bh / 2, xs[i + 1], lw=3)

    ax.add_patch(Arc((8.25, 0.55), 14.4, 1.55, angle=0, theta1=200, theta2=-20,
                     linewidth=3.0, color=BLACK))
    ax.annotate("", xy=(1.05, 0.95), xytext=(0.85, 0.62),
                arrowprops=dict(arrowstyle="-|>", lw=3.0, color=BLACK))
    ax.text(8.25, 0.18, "大闭环", ha="center", fontsize=20, fontweight="bold")

    save(fig, "01-architecture.png")


def main_loop():
    fig, ax = plt.subplots(figsize=(16.5, 4.8))
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 4.8)
    ax.axis("off")

    ax.text(8.25, 4.35, "主业务闭环", ha="center", fontsize=28, fontweight="bold")

    steps = [
        ("病例对话", "临床端", TEAL_BG),
        ("标红上传", "临床端", "#d4ede8"),
        ("现场发现", "科研端", "#ede9fe"),
        ("研判记录", "科研端", "#ddd6fe"),
        ("文献速查", "共用", "#dbeafe"),
    ]
    x0, w, h, gap, y = 0.35, 2.75, 1.15, 0.48, 1.85
    for i, (t, tag, c) in enumerate(steps):
        x = x0 + i * (w + gap)
        box(ax, x, y, w, h, t, fc=c, fs=22)
        ax.text(x + w / 2, y - 0.38, tag, ha="center", fontsize=15, fontweight="bold", color="#555")
        if i < len(steps) - 1:
            h_arrow(ax, x + w, y + h / 2, x + w + gap, lw=3.4)

    ax.text(8.25, 0.45, "临床查证  →  上传现场信号  →  科研汇总研判  →  再次查阅文献",
            ha="center", fontsize=16, color="#333")
    save(fig, "02-main-loop.png")


def lit_flow():
    fig, ax = plt.subplots(figsize=(17.2, 4.6))
    ax.set_xlim(0, 17.2)
    ax.set_ylim(0, 4.6)
    ax.axis("off")

    ax.text(8.6, 4.15, "文献速查 · 分步引导检索", ha="center", fontsize=28, fontweight="bold")

    steps = [
        ("① 点「文献」", "下拉选四类主题", "#e8f4f4"),
        ("② 输入关键词", "民族 / 病药 / 基因", "#dbeafe"),
        ("③ 筛选条件", "文献类型 · 证据等级", "#cfe8e8"),
        ("④ 搜索结果", "MES 编号 · 等级 · 摘要", "#bfdbfe"),
        ("⑤ 文献详情", "PICOS · 出处 · 边界", TEAL_BG),
    ]
    x0, w, h, gap, y = 0.28, 2.95, 1.45, 0.4, 1.55
    for i, (t, s, c) in enumerate(steps):
        x = x0 + i * (w + gap)
        box(ax, x, y, w, h, t, s, fc=c, fs=20, sub_fs=12)
        if i < len(steps) - 1:
            h_arrow(ax, x + w, y + h / 2, x + w + gap, lw=3.4)

    ax.text(8.6, 0.42, "顶栏搜索框 · 选项按步骤出现",
            ha="center", fontsize=14, color="#555")
    for name in ("14-lit-search.png", "03-lit-flow.png"):
        fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.3)
        print("ok", name)
    plt.close(fig)


def clinic_agent():
    fig, ax = plt.subplots(figsize=(17.2, 4.6))
    ax.set_xlim(0, 17.2)
    ax.set_ylim(0, 4.6)
    ax.axis("off")

    ax.text(8.6, 4.15, "临床助手 · 对话式对照", ha="center", fontsize=28, fontweight="bold")

    steps = [
        ("① 用户提问", "民族 + 病 / 药", "white"),
        ("② 检索文献库", "后台拆问句", "#dbeafe"),
        ("③ 选技能", "辅助判断 · 前沿研究", "#dcfce7"),
        ("④ 判断摘要", "够 / 不够 / 偏少", "#cfe8e8"),
        ("⑤ 参考来源", "[1] MES 可点详情", TEAL_BG),
    ]
    x0, w, h, gap, y = 0.28, 2.95, 1.45, 0.4, 1.55
    for i, (t, s, c) in enumerate(steps):
        x = x0 + i * (w + gap)
        box(ax, x, y, w, h, t, s, fc=c, fs=19, sub_fs=12)
        if i < len(steps) - 1:
            h_arrow(ax, x + w, y + h / 2, x + w + gap, lw=3.4)

    save(fig, "04-clinic-agent.png")


def research_agent():
    fig, ax = plt.subplots(figsize=(17.2, 4.6))
    ax.set_xlim(0, 17.2)
    ax.set_ylim(0, 4.6)
    ax.axis("off")

    ax.text(8.6, 4.15, "科研助手 · 文献 + 现场对照", ha="center", fontsize=28, fontweight="bold")

    steps = [
        ("① 用户提问", "民族 + 病 / 药", "white"),
        ("② 双源对照", "文献库 + 现场信号", "#ede9fe"),
        ("③ 选技能", "开题 · 做不做 · 证据", "#ddd6fe"),
        ("④ 判断摘要", "三选一 / 缺口分析", "#e9d5ff"),
        ("⑤ 证据 + 来源", "等级条 · MES 可点", TEAL_BG),
    ]
    x0, w, h, gap, y = 0.28, 2.95, 1.45, 0.4, 1.55
    for i, (t, s, c) in enumerate(steps):
        x = x0 + i * (w + gap)
        box(ax, x, y, w, h, t, s, fc=c, fs=17, sub_fs=11)
        if i < len(steps) - 1:
            h_arrow(ax, x + w, y + h / 2, x + w + gap, lw=3.4)

    save(fig, "05-research-agent.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    arch()
    main_loop()
    lit_flow()
    clinic_agent()
    research_agent()
