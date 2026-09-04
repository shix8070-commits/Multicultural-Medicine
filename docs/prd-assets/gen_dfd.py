# -*- coding: utf-8 -*-
"""数据流图：外部实体 / 处理 / 数据存储，对齐 PRD 模板。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#1d2430"
MUTED = "#5c6573"
PINK = "#f7d0d4"
PINK_EC = "#c97a82"
BLUE = "#cfe6f6"
BLUE_EC = "#3a7ca5"
RED = "#b42318"
PAGE = "white"


def wrap(text, n=6):
    lines = []
    for para in str(text).split("\n"):
        s = para
        while len(s) > n:
            lines.append(s[:n])
            s = s[n:]
        if s:
            lines.append(s)
    return "\n".join(lines)


def entity(ax, x, y, w, h, text):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor=PINK, edgecolor=PINK_EC, linewidth=1.5, zorder=3, clip_on=False,
    ))
    ax.text(x + w / 2, y + h / 2, wrap(text, 7), ha="center", va="center",
            fontsize=12, color=INK, zorder=4, linespacing=1.25)
    return x + w / 2, y + h / 2, x, y, w, h


def process(ax, cx, cy, r, text):
    ax.add_patch(Circle((cx, cy), r, facecolor=BLUE, edgecolor=BLUE_EC,
                        linewidth=1.7, zorder=3, clip_on=False))
    ax.text(cx, cy, wrap(text, 5), ha="center", va="center",
            fontsize=12, color=INK, zorder=4, linespacing=1.2)
    return cx, cy


def store(ax, x, y, w, text):
    h = 0.62
    ax.plot([x, x + w], [y + h / 2, y + h / 2], color=INK, lw=1.7, zorder=3, clip_on=False)
    ax.plot([x, x + w], [y - h / 2, y - h / 2], color=INK, lw=1.7, zorder=3, clip_on=False)
    ax.text(x + w / 2, y, text, ha="center", va="center", fontsize=12, color=INK, zorder=4)
    return x + w / 2, y, x, y, w, h


def flow(ax, p1, p2, label, dashed=False, color="#334155", ox=0, oy=0.22):
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="-|>", mutation_scale=12,
        linewidth=1.35, color=color,
        linestyle=(0, (5, 3)) if dashed else "solid",
        clip_on=False, zorder=2,
    ))
    if label:
        ax.text((p1[0] + p2[0]) / 2 + ox, (p1[1] + p2[1]) / 2 + oy, label,
                ha="center", va="center", fontsize=10, color=color, zorder=5,
                bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.95))


def edge(cx, cy, r, side):
    d = {"left": (-r, 0), "right": (r, 0), "top": (0, r), "bottom": (0, -r),
         "tl": (-r * 0.7, r * 0.7), "tr": (r * 0.7, r * 0.7),
         "bl": (-r * 0.7, -r * 0.7), "br": (r * 0.7, -r * 0.7)}[side]
    return cx + d[0], cy + d[1]


def draw():
    W, H = 21.2, 15.2
    fig, ax = plt.subplots(figsize=(W, H), facecolor=PAGE)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_facecolor(PAGE)
    ax.axis("off")

    ax.text(W / 2, H - 0.38, "多民族健康证据服务 · 数据流图",
            ha="center", va="center", fontsize=22, fontweight="bold", color=INK)
    ax.text(W / 2, H - 0.82,
            "文献库供助手与速查只读检索 · 论坛独立存储",
            ha="center", va="center", fontsize=12, color=MUTED)

    # legend
    ax.add_patch(FancyBboxPatch((0.45, H - 1.55), 1.35, 0.42,
                                boxstyle="round,pad=0.01,rounding_size=0.08",
                                facecolor=PINK, edgecolor=PINK_EC, lw=1.2, zorder=3))
    ax.text(1.95, H - 1.34, "外部实体", ha="left", va="center", fontsize=10.5, color=INK)
    ax.add_patch(Circle((4.55, H - 1.34), 0.2, facecolor=BLUE, edgecolor=BLUE_EC, lw=1.2, zorder=3))
    ax.text(4.9, H - 1.34, "处理过程", ha="left", va="center", fontsize=10.5, color=INK)
    ax.plot([7.15, 8.45], [H - 1.22, H - 1.22], color=INK, lw=1.5)
    ax.plot([7.15, 8.45], [H - 1.46, H - 1.46], color=INK, lw=1.5)
    ax.text(8.6, H - 1.34, "数据存储", ha="left", va="center", fontsize=10.5, color=INK)
    ax.plot([10.7, 12.0], [H - 1.34, H - 1.34], color=RED, lw=1.4, linestyle=(0, (4, 2)))
    ax.annotate("", xy=(12.0, H - 1.34), xytext=(11.85, H - 1.34),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2))
    ax.text(12.2, H - 1.34, "分库存储", ha="left", va="center", fontsize=10.5, color=RED)

    ew, eh, R = 2.7, 1.18, 1.22

    inst = entity(ax, 0.4, 11.85, ew, eh, "权威机构\n公开文献")
    adm = entity(ax, 18.1, 11.85, ew, eh, "管理员")
    doc = entity(ax, 0.4, 6.55, ew, eh, "基层医生")
    sci = entity(ax, 18.1, 6.55, ew, eh, "科研人员")

    litm = process(ax, 10.55, 12.45, R, "文献入库\n管理")
    ask = process(ax, 10.55, 7.15, R, "助手问答")
    search = process(ax, 5.15, 2.85, R, "文献速查")
    forum = process(ax, 13.2, 2.85, R, "论坛交互")

    lit = store(ax, 9.05, 9.75, 3.05, "文献库")
    fav = store(ax, 3.75, 0.72, 2.85, "收藏")
    posts = store(ax, 14.55, 0.72, 3.05, "论坛帖与聊天")

    # 入库
    flow(ax, (inst[0] + ew / 2, inst[1]), edge(*litm, R, "left"), "核验后的条目", oy=0.28)
    flow(ax, (adm[0] - ew / 2, adm[1]), edge(*litm, R, "right"), "维护 / 上下架", oy=0.28)
    flow(ax, edge(*litm, R, "bottom"), (lit[0], lit[1] + 0.31), "写入文献", oy=0)
    flow(ax, (lit[0], lit[1] - 0.31), edge(*ask, R, "top"), "只读检索", oy=0)

    # 提问
    flow(ax, (doc[0] + ew / 2, doc[1] + 0.15), edge(*ask, R, "left"), "提问", oy=0.26)
    flow(ax, (sci[0] - ew / 2, sci[1] + 0.15), edge(*ask, R, "right"), "提问", oy=0.26)

    # 禁止
    flow(ax, (posts[0], posts[1] + 0.31), edge(*ask, R, "br"), "论坛独立",
         dashed=True, color=RED, ox=1.15, oy=0.05)

    # 速查
    flow(ax, (doc[0] + 0.2, doc[1] - eh / 2), edge(*search, R, "tl"), "检索请求", ox=-0.55, oy=0)
    flow(ax, (lit[0] - 1.2, lit[1] - 0.15), edge(*search, R, "top"), "文献数据", ox=-0.7, oy=0)
    flow(ax, edge(*search, R, "bottom"), (fav[0] + 0.4, fav[1] + 0.31), "收藏条目", oy=0)

    # 论坛
    flow(ax, (sci[0] - ew / 2, sci[1] - eh / 2), edge(*forum, R, "top"), "看帖 / 回复",
         ox=0.55, oy=0.22)
    flow(ax, (doc[0] + ew / 2, doc[1] - 0.45),
         (forum[0] - R, forum[1] + 0.35),
         "发帖 / 聊天", ox=1.8, oy=-1.05)
    flow(ax, edge(*forum, R, "bottom"), (posts[0], posts[1] + 0.31), "帖子数据", oy=0)

    fig.savefig(OUT / "09-data-flow.png", dpi=200, bbox_inches="tight",
                facecolor=PAGE, pad_inches=0.3)
    plt.close(fig)
    print("ok 09-data-flow.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
