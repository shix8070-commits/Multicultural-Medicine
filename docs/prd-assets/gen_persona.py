# -*- coding: utf-8 -*-
"""用户画像图：基层医生 / 科研人员，三列结构。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#1d2430"
MUTED = "#5c6573"
LINE = "#d7deea"
BLUE = "#3b82c4"
PURPLE = "#6b6ad6"
BLUE_SOFT = "#e8f2fc"
PURPLE_SOFT = "#eeebfb"
BLUE_HEAD = "#d4e8fa"
PURPLE_HEAD = "#ddd6f8"
PAGE = "#f4f7fb"


def wrap(text, n=11):
    lines = []
    for para in text.split("\n"):
        s = para
        while len(s) > n:
            lines.append(s[:n])
            s = s[n:]
        if s:
            lines.append(s)
    return "\n".join(lines)


def rbox(ax, x, y, w, h, fc="white", ec=LINE, lw=1.4, rs=0.12):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.01,rounding_size={rs}",
        facecolor=fc, edgecolor=ec, linewidth=lw, clip_on=False,
    )
    ax.add_patch(p)
    return p


def col(ax, x, y, w, h, title, bullets, accent, head_fc):
    rbox(ax, x, y, w, h, fc="white", ec=LINE, lw=1.2, rs=0.1)
    rbox(ax, x, y + h - 0.72, w, 0.72, fc=head_fc, ec=accent, lw=1.2, rs=0.08)
    ax.text(x + w / 2, y + h - 0.36, title, ha="center", va="center",
            fontsize=15, fontweight="bold", color=accent)
    ty = y + h - 1.05
    for b in bullets:
        ax.text(x + 0.18, ty, "·  " + wrap(b, 12), ha="left", va="top",
                fontsize=11.5, color=INK, linespacing=1.35)
        ty -= 0.18 + 0.34 * ((len(b) - 1) // 12 + 1)


def persona_card(ax, x, y, w, h, role, one_liner, accent, head, soft, cols):
    rbox(ax, x, y, w, h, fc="white", ec=accent, lw=2.2, rs=0.14)
    rbox(ax, x, y + h - 1.55, w, 1.55, fc=head, ec=accent, lw=0, rs=0.14)
    # cover bottom rounding of header
    ax.add_patch(plt.Rectangle((x, y + h - 0.4), w, 0.4, facecolor=head, edgecolor="none"))

    ax.add_patch(Circle((x + 0.85, y + h - 0.78), 0.42, facecolor=accent, edgecolor="none"))
    ax.text(x + 0.85, y + h - 0.78, role[0], ha="center", va="center",
            fontsize=18, fontweight="bold", color="white")
    ax.text(x + 1.5, y + h - 0.55, role, ha="left", va="center",
            fontsize=20, fontweight="bold", color=INK)
    ax.text(x + 1.5, y + h - 1.08, one_liner, ha="left", va="center",
            fontsize=12, color=MUTED)

    cw = (w - 0.7) / 3
    gap = 0.12
    cy, ch = y + 0.28, h - 2.0
    for i, (title, bullets) in enumerate(cols):
        cx = x + 0.22 + i * (cw + gap)
        col(ax, cx, cy, cw, ch, title, bullets, accent, soft)


def draw():
    fig, ax = plt.subplots(figsize=(18.5, 11.2), facecolor=PAGE)
    ax.set_xlim(0, 18.5)
    ax.set_ylim(0, 11.2)
    ax.set_facecolor(PAGE)
    ax.axis("off")

    ax.text(9.25, 10.72, "多民族健康证据服务 · 用户画像",
            ha="center", va="center", fontsize=26, fontweight="bold", color=INK)
    ax.text(9.25, 10.22, "先分析人，再定功能。本期只做基层医生与科研人员，大众健康问答不做。",
            ha="center", va="center", fontsize=13, color=MUTED)

    persona_card(
        ax, 0.35, 2.15, 8.8, 7.7,
        "基层医生",
        "来确认「现在知道多少」，不是让系统看病",
        BLUE, BLUE_HEAD, BLUE_SOFT,
        [
            ("人群特征", [
                "民族地区或综合医院一线",
                "既要看病，也要跟课题",
                "对「这民族能不能用这药」敏感，但很少有整套药基组数据",
            ]),
            ("工作行为", [
                "接诊窗口短，先问有没有材料可对照",
                "指南多按全国或汉族写，心里没底",
                "要对照和边界，不要系统下诊断",
            ]),
            ("使用习惯", [
                "碎片时间：接诊间隙、晚上补材料",
                "先问临床助手，再去文献速查",
                "对不上才去论坛发问",
            ]),
        ],
    )

    persona_card(
        ax, 9.35, 2.15, 8.8, 7.7,
        "科研人员",
        "来减少重复翻检，并看见医生端遇到了什么",
        PURPLE, PURPLE_HEAD, PURPLE_SOFT,
        [
            ("人群特征", [
                "高校、医院科研科、课题组",
                "做流病、遗传或药物基因组",
                "少数民族样本难求，单中心病例更少",
            ]),
            ("工作行为", [
                "开题要证明有没有人做过、值不值得做",
                "现在靠跨库检索、手工制表",
                "要出处和边界，不要一句「有研究」",
            ]),
            ("使用习惯", [
                "开题、写标书、组会前集中使用",
                "先科研助手对照，再按民族/病/药横比",
                "会看论坛，但不把帖子当立项依据",
            ]),
        ],
    )

    rbox(ax, 0.35, 0.28, 17.8, 1.62, fc="white", ec=LINE, lw=1.6, rs=0.12)
    ax.text(9.25, 1.55, "两人怎么接上", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK)

    bh, by = 0.78, 0.48
    items = [
        (0.55, 3.15, "医生说出\n现场问题", BLUE_SOFT, BLUE),
        (4.0, 3.15, "论坛\n交流，不当证据", "#f3f0ff", PURPLE),
        (7.45, 3.15, "文献库\n助手只引用这里", "#eef6ff", BLUE),
        (10.9, 3.15, "科研对照\n决定跟 / 不跟", PURPLE_SOFT, PURPLE),
        (14.35, 3.15, "新证据回库\n医生下次能查到", BLUE_SOFT, BLUE),
    ]
    for x, w, label, fc, ec in items:
        rbox(ax, x, by, w, bh, fc=fc, ec=ec, lw=1.5, rs=0.08)
        ax.text(x + w / 2, by + bh / 2, label, ha="center", va="center",
                fontsize=11, color=INK, linespacing=1.25)
    for i in range(len(items) - 1):
        x1 = items[i][0] + items[i][1]
        x2 = items[i + 1][0]
        ax.add_patch(FancyArrowPatch(
            (x1 + 0.04, by + bh / 2), (x2 - 0.04, by + bh / 2),
            arrowstyle="-|>", mutation_scale=14, linewidth=1.8, color="#8a93a3",
            clip_on=False,
        ))

    fig.savefig(OUT / "06-user-persona.png", dpi=200, bbox_inches="tight",
                facecolor=PAGE, pad_inches=0.25)
    plt.close(fig)
    print("ok 06-user-persona.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
