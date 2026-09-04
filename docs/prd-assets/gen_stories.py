# -*- coding: utf-8 -*-
"""用户故事图：作为 / 我希望 / 以便。卡片按内容撑开，互不遮挡。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#1d2430"
MUTED = "#5c6573"
LINE = "#d7deea"
BLUE = "#3b82c4"
PURPLE = "#6b6ad6"
SLATE = "#4b5568"
BLUE_SOFT = "#e8f2fc"
PURPLE_SOFT = "#eeebfb"
SLATE_SOFT = "#eef1f6"
BLUE_HEAD = "#d4e8fa"
PURPLE_HEAD = "#ddd6f8"
SLATE_HEAD = "#e4e8f0"
PAGE = "#f4f7fb"


def wrap(text, n):
    lines = []
    s = text
    while len(s) > n:
        cut = n
        for i in range(n, max(n // 2, n - 8), -1):
            if s[i - 1] in "，、。；：/ ":
                cut = i
                break
        lines.append(s[:cut])
        s = s[cut:]
    if s:
        lines.append(s)
    return lines


def rbox(ax, x, y, w, h, fc="white", ec=LINE, lw=1.4, rs=0.1):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.012,rounding_size={rs}",
        facecolor=fc, edgecolor=ec, linewidth=lw, clip_on=False, zorder=2,
    ))


def chip(ax, x, y, text, fc, ec):
    w, h = 1.22, 0.42
    rbox(ax, x, y, w, h, fc=fc, ec=ec, lw=1.1, rs=0.08)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=12, fontweight="bold", color=ec, zorder=3)


def story_card(ax, x, y_top, w, code, role, want, so_that, accent, head, soft, wrap_n=16):
    header_h = 0.82
    pad_x, pad_y = 0.28, 0.28
    row_gap = 0.22
    line_h = 0.42
    chip_h = 0.42
    labels = [("作为", role, soft), ("我希望", want, "#ffffff"), ("以便", so_that, soft)]
    wrapped = [wrap(body, wrap_n) for _, body, _ in labels]
    row_hs = [max(chip_h, len(lines) * line_h) for lines in wrapped]
    body_h = pad_y + sum(row_hs) + row_gap * 2 + pad_y
    h = header_h + body_h
    y = y_top - h

    rbox(ax, x, y, w, h, fc="white", ec=accent, lw=2.0, rs=0.12)
    rbox(ax, x, y + h - header_h, w, header_h, fc=head, ec=accent, lw=0, rs=0.12)
    ax.add_patch(plt.Rectangle((x, y + h - 0.3), w, 0.3, facecolor=head, edgecolor="none", zorder=2.1))

    ax.add_patch(Circle((x + 0.52, y + h - header_h / 2), 0.24, facecolor=accent, edgecolor="none", zorder=3))
    ax.text(x + 0.52, y + h - header_h / 2, code, ha="center", va="center",
            fontsize=11, fontweight="bold", color="white", zorder=4)
    ax.text(x + 0.92, y + h - header_h / 2, f"作为{role}", ha="left", va="center",
            fontsize=16, fontweight="bold", color=INK, zorder=4)

    cursor = y + h - header_h - pad_y
    text_x = x + pad_x + 1.22 + 0.22
    for (label, _, bg), lines, rh in zip(labels, wrapped, row_hs):
        cursor -= rh
        chip(ax, x + pad_x, cursor + (rh - chip_h) / 2, label, bg, accent)
        ax.text(text_x, cursor + rh / 2, "\n".join(lines), ha="left", va="center",
                fontsize=13.5, color=INK, linespacing=1.45, zorder=4)
        cursor -= row_gap
    return h


def draw():
    W, H = 18.6, 16.4
    fig, ax = plt.subplots(figsize=(W, H), facecolor=PAGE)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_facecolor(PAGE)
    ax.axis("off")

    ax.text(W / 2, H - 0.45, "多民族健康证据服务 · 用户故事",
            ha="center", va="center", fontsize=26, fontweight="bold", color=INK)
    ax.text(W / 2, H - 0.95, "作为 [角色]，我希望 [完成某件事]，以便 [获得某个结果]。",
            ha="center", va="center", fontsize=13.5, color=MUTED)

    card_w = 8.7
    left_x, right_x = 0.4, 0.4 + card_w + 0.4
    y_top = H - 1.35
    gap = 0.42

    h1 = story_card(
        ax, left_x, y_top, card_w, "U1", "基层医生",
        "先按民族和病/药对照现有研究",
        "知道这件事现在有多少材料、有多弱，再自己做临床判断",
        BLUE, BLUE_HEAD, BLUE_SOFT,
    )
    h3 = story_card(
        ax, right_x, y_top, card_w, "U3", "科研人员",
        "按民族、病/药对照入库文献",
        "判断这题做、不做、还是再等等",
        PURPLE, PURPLE_HEAD, PURPLE_SOFT,
    )
    y_mid = y_top - max(h1, h3) - gap
    h2 = story_card(
        ax, left_x, y_mid, card_w, "U2", "基层医生",
        "现场遇到文献里几乎没有的现象时，发到论坛",
        "科研和其他医生能看见，而不是只有我自己记得",
        BLUE, BLUE_HEAD, BLUE_SOFT,
    )
    h4 = story_card(
        ax, right_x, y_mid, card_w, "U4", "科研人员",
        "在论坛里看到医生真实在问什么",
        "选题对准现场，而不是只对着已发表论文打转",
        PURPLE, PURPLE_HEAD, PURPLE_SOFT,
    )
    y_bot = y_mid - max(h2, h4) - gap
    story_card(
        ax, 0.4, y_bot, 17.8, "U5", "两类用户",
        "助手只根据入库文献回答，并标明出处和边界",
        "不被论坛里真假混杂的讨论带偏",
        SLATE, SLATE_HEAD, SLATE_SOFT, wrap_n=32,
    )

    fig.savefig(OUT / "07-user-stories.png", dpi=200, bbox_inches="tight",
                facecolor=PAGE, pad_inches=0.28)
    plt.close(fig)
    print("ok 07-user-stories.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
