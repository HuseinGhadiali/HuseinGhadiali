"""Profile banner: a constellation of signals, one glowing lane per portfolio project."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from banner import glow_line, glow_scatter, make_banner  # noqa: E402

rng = np.random.default_rng(7)


def art(ax, acc):
    x = np.linspace(0, 10, 400)
    lanes = [
        np.cumsum(rng.normal(0.02, 0.12, 400)) * 0.08,                      # growth curve (SQL / KPIs)
        0.35 * np.sin(x * 1.3) + 0.25 * np.exp(-((x - 7.2) ** 2) * 6),      # seasonality + festive spike (forecasting)
        0.3 * np.exp(-((x - 3) ** 2) * 1.5) - 0.3 * np.exp(-((x - 6.5) ** 2) * 1.5),  # A vs B
        0.25 * np.sign(np.sin(x * 2.2)) * np.exp(-x / 9),                  # cohort decay steps
        0.2 * np.sin(x * 5) * np.exp(-((x - 5) ** 2) / 8),                  # signal (NLP)
    ]
    for i, y in enumerate(lanes):
        glow_line(ax, x, y + i * 0.9, acc[i % len(acc)], lw=1.8, layers=5)
    px, py = rng.uniform(0, 10, 260), rng.uniform(-0.6, 4.4, 260)
    glow_scatter(ax, px, py, "white", s=2, alpha=0.35)
    ax.set_xlim(-0.2, 10.2)
    ax.set_ylim(-0.8, 4.6)


make_banner(Path(__file__).parent / "banner.png", "Husein Ghadiali",
            "Senior Data Analyst · SQL · Python · Power BI · Pune, India",
            ["SQL", "Python", "Power BI", "Forecasting", "A/B testing", "NLP"], art, theme="aurora",
            emoji_free_kicker="Turning raw data into decisions · 8+ years")
