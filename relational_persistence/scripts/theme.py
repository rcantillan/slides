"""Shared house theme for all manuscript figures (matches make_fis_figure.py)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE = "#2878B5"
ORANGE = "#E87522"
DARK = "#252525"
GREY = "#777777"
LIGHT_GREY = "#D4D4D4"

TITLE_KW = dict(loc="left", fontsize=15.5, fontweight="bold", pad=12)
SUPTITLE_KW = dict(fontsize=16.5, fontweight="bold", y=0.99)


def apply_theme():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 14,
        "axes.edgecolor": DARK,
        "axes.labelcolor": DARK,
        "text.color": DARK,
        "xtick.color": DARK,
        "ytick.color": DARK,
        "xtick.labelsize": 13,
        "ytick.labelsize": 13,
        "axes.labelsize": 14,
    })


def style_axes(ax, spines_off=("top", "right"), grid_axis="y"):
    ax.tick_params(axis="both", length=0)
    for s in spines_off:
        ax.spines[s].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color=LIGHT_GREY, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
