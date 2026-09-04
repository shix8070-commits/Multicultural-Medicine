# -*- coding: utf-8 -*-
"""业务流程图：跨角色泳道，对齐 PRD 模板。"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon, Rectangle

OUT = Path(__file__).parent
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#1d2430"
MUTED = "#5c6573"
BOX_FC = "#e8f3fb"
BOX_EC = "#4f7cac"
DIA_FC = "#fff8e8"
DIA_EC = "#b8922a"
YEL_FC = "#fff3b0"
YEL_EC = "#b8922a"
OK_FC = "#e7f6ee"
OK_EC = "#2f7d55"
NO_FC = "#fdecea"
NO_EC = "#b42318"
HEAD_FC = "#d7e8f7"
HEAD2 = "#e8eef6"
LANE_A = "#f8fbfe"
LANE_B = "#eef3f8"
PAGE = "white"


def wrap(text, n=8):
    lines = []
    for para in str(text).split("\n"):
        s = para
        while len(s) > n:
            lines.append(s[:n])
            s = s[n:]
        if s:
            lines.append(s)
    return "\n".join(lines)


def rbox(ax, x, y, w, h, text, fc=BOX_FC, ec=BOX_EC, fs=11):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012,rounding_size=0.08",
        facecolor=fc, edgecolor=ec, linewidth=1.45, clip_on=False, zorder=3,
    ))
    ax.text(x + w / 2, y + h / 2, wrap(text, 9), ha="center", va="center",
            fontsize=fs, color=INK, zorder=4, linespacing=1.28)
    return x + w / 2, y + h / 2


def diamond(ax, cx, cy, w, h, text):
    xs = [cx, cx + w / 2, cx, cx - w / 2]
    ys = [cy + h / 2, cy, cy - h / 2, cy]
    ax.add_patch(Polygon(list(zip(xs, ys)), closed=True,
                         facecolor=DIA_FC, edgecolor=DIA_EC, linewidth=1.5,
                         clip_on=False, zorder=3))
    ax.text(cx, cy, wrap(text, 6), ha="center", va="center",
            fontsize=10.5, color=INK, zorder=4, linespacing=1.2)
    return cx, cy


def arrow(ax, p1, p2, dashed=False, text=None, dx=0, dy=0.14):
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="-|>", mutation_scale=12,
        linewidth=1.4, color="#334155",
        linestyle=(0, (4, 3)) if dashed else "solid",
        clip_on=False, zorder=2,
    ))
    if text:
        ax.text((p1[0] + p2[0]) / 2 + dx, (p1[1] + p2[1]) / 2 + dy,
                text, ha="center", va="bottom", fontsize=9.5, color="#475569", zorder=5)


def draw():
    W, H = 20.4, 16.8
    fig, ax = plt.subplots(figsize=(W, H), facecolor=PAGE)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_facecolor(PAGE)
    ax.axis("off")

    ax.text(W / 2, H - 0.36, "多民族健康证据服务 · 业务流程图",
            ha="center", va="center", fontsize=22, fontweight="bold", color=INK)
    ax.text(W / 2, H - 0.76, "按角色分道 · 实线为主流程",
            ha="center", va="center", fontsize=11.5, color=MUTED)

    cols = [
        (0.32, "基层医生", "临床端"),
        (4.32, "系统 / 助手", "校验与检索"),
        (8.32, "文献库", "权威材料底座"),
        (12.32, "我的论坛", "交流层"),
        (16.32, "科研人员", "科研端"),
    ]
    cw, top, bot = 3.88, H - 1.02, 0.28
    for i, (x, dept, role) in enumerate(cols):
        ax.add_patch(Rectangle((x, bot), cw, top - bot,
                               facecolor=LANE_A if i % 2 == 0 else LANE_B,
                               edgecolor="#c5d0de", linewidth=1.0, zorder=0))
        ax.add_patch(Rectangle((x, top - 1.02), cw, 1.02,
                               facecolor=HEAD_FC if i % 2 == 0 else HEAD2,
                               edgecolor="#9ab0c7", linewidth=1.1, zorder=1))
        ax.text(x + cw / 2, top - 0.36, dept, ha="center", va="center",
                fontsize=14, fontweight="bold", color=INK, zorder=2)
        ax.text(x + cw / 2, top - 0.76, role, ha="center", va="center",
                fontsize=11, color=MUTED, zorder=2)

    bw, bh = 3.22, 0.95

    def box(col, y, text, fc=BOX_FC, ec=BOX_EC):
        x = cols[col][0] + (cw - bw) / 2
        return rbox(ax, x, y, bw, bh, text, fc=fc, ec=ec)

    def cx(col):
        return cols[col][0] + cw / 2

    # rows (box bottom y)
    y1, y2, y3, y4, y5, y6, y7, y8, y9 = (
        13.55, 12.15, 10.55, 8.85, 7.05, 5.35, 3.75, 2.15, 0.55
    )

    # start
    sx, sy = cx(0), y1 + bh + 0.58
    ax.add_patch(Circle((sx, sy), 0.17, facecolor="#c45c5c", edgecolor="#8a2b2b",
                        linewidth=1.2, zorder=4))
    ax.text(sx, sy - 0.36, "开始", ha="center", va="top", fontsize=10, color=INK, zorder=4)

    b_open = box(0, y1, "打开小程序")
    arrow(ax, (sx, sy - 0.18), (b_open[0], b_open[1] + bh / 2))

    b_lit0 = box(2, y1, "权威材料入库\n管理员核验")

    b_pick = box(0, y2, "选择入口")
    arrow(ax, (b_open[0], b_open[1] - bh / 2), (b_pick[0], b_pick[1] + bh / 2))

    b_ask = box(0, y3, "临床助手提问\n辅助判断 / 前沿研究")
    b_rask = box(4, y3, "科研助手提问\n开题 / 做不做 / 证据")
    b_post = box(3, y3, "论坛发帖 / 聊天")
    arrow(ax, (b_pick[0], b_pick[1] - bh / 2), (b_ask[0], b_ask[1] + bh / 2), text="医生")
    arrow(ax, (b_pick[0] + bw / 2, b_pick[1]), (b_rask[0] - bw / 2, b_rask[1] + 0.08), text="科研")
    arrow(ax, (b_pick[0] + bw / 2, b_pick[1] - 0.15), (b_post[0] - bw / 2, b_post[1] + 0.08), text="论坛")

    d_chk = diamond(ax, cx(1), y3 + bh / 2, 2.62, 1.48, "解析问句")
    arrow(ax, (b_ask[0] + bw / 2, b_ask[1]), (d_chk[0] - 1.31, d_chk[1]))
    arrow(ax, (b_rask[0] - bw / 2, b_rask[1]), (d_chk[0] + 1.31, d_chk[1]), dashed=True)

    b_search = box(1, y4, "检索入库文献\nMES 条目")
    arrow(ax, (d_chk[0], d_chk[1] - 0.74), (b_search[0], b_search[1] + bh / 2))

    b_ret = box(2, y4, "返回条目\n出处 + 边界")
    arrow(ax, (b_lit0[0], b_lit0[1] - bh / 2), (b_ret[0], b_ret[1] + bh / 2), dashed=True)
    arrow(ax, (b_search[0] + bw / 2, b_search[1]), (b_ret[0] - bw / 2, b_ret[1]))

    d_en = diamond(ax, cx(1), y5 + bh / 2 + 0.08, 2.62, 1.42, "有命中?")
    arrow(ax, (b_search[0], b_search[1] - bh / 2), (d_en[0], d_en[1] + 0.71))
    arrow(ax, (b_ret[0], b_ret[1] - bh / 2), (d_en[0] + 0.3, d_en[1] + 0.71), dashed=True)

    b_ok = box(0, y6, "先给结论\n证据条 + MES 来源", fc=OK_FC, ec=OK_EC)
    b_lack = box(1, y6, "材料不足\n提示换词或去论坛", fc=BOX_FC, ec=BOX_EC)
    arrow(ax, (d_en[0] - 1.31, d_en[1]), (b_ok[0] + bw / 2, b_ok[1] + bh / 2), text="有")
    arrow(ax, (d_en[0], d_en[1] - 0.71), (b_lack[0], b_lack[1] + bh / 2), text="无")

    b_sig = box(0, y7, "论坛发帖\n现场问题")
    b_keep = box(3, y6, "论坛展示\n供科研查看", fc=YEL_FC, ec=YEL_EC)
    arrow(ax, (b_lack[0] - bw / 2, b_lack[1]), (b_sig[0] + bw / 2, b_sig[1] + bh / 2))
    arrow(ax, (b_post[0], b_post[1] - bh / 2), (b_keep[0], b_keep[1] + bh / 2), dashed=True)
    arrow(ax, (b_sig[0] + bw / 2, b_sig[1]), (b_keep[0] - bw / 2, b_keep[1]), dashed=True)

    b_see = box(4, y6, "科研看帖\n了解现场")
    arrow(ax, (b_keep[0] + bw / 2, b_keep[1]), (b_see[0] - bw / 2, b_see[1]), dashed=True)

    b_topic = box(4, y7, "科研助手\n三技能对照")
    arrow(ax, (b_see[0], b_see[1] - bh / 2), (b_topic[0], b_topic[1] + bh / 2))
    arrow(ax, (b_rask[0], b_rask[1] - bh / 2), (b_topic[0] + bw / 2, b_topic[1] + bh / 2), dashed=True)

    d_go = diamond(ax, cx(4), y8 + bh / 2 + 0.1, 2.45, 1.28, "跟不跟?")
    arrow(ax, (b_topic[0], b_topic[1] - bh / 2), (d_go[0], d_go[1] + 0.64))

    b_back = box(2, y8, "新研究入库\n更新文献库", fc=OK_FC, ec=OK_EC)
    arrow(ax, (d_go[0] - 1.22, d_go[1]), (b_back[0] + bw / 2, b_back[1] + bh / 2), text="跟进")
    arrow(ax, (b_back[0], b_back[1] + bh / 2), (b_ret[0], b_ret[1] - bh / 2), dashed=True)

    ex, ey = cx(4), y9 + 0.35
    ax.add_patch(Circle((ex, ey), 0.17, facecolor="#64748b", edgecolor="#334155",
                        linewidth=1.2, zorder=4))
    ax.text(ex + 0.42, ey, "结束", ha="left", va="center", fontsize=10, color=INK, zorder=4)
    arrow(ax, (d_go[0], d_go[1] - 0.64), (ex, ey + 0.2), text="不跟 / 再等等", dx=0.7, dy=0)

    fig.savefig(OUT / "08-biz-flow.png", dpi=200, bbox_inches="tight",
                facecolor=PAGE, pad_inches=0.28)
    plt.close(fig)
    print("ok 08-biz-flow.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    draw()
