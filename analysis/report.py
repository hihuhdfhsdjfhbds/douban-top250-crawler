"""分析层：用 pandas + matplotlib 出评分分布图，体现数据闭环。"""

import logging
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # 无图形界面环境也能出图
import matplotlib.pyplot as plt
import pandas as pd

logger = logging.getLogger(__name__)


def plot_rating_distribution(csv_path: str, chart_path: str) -> None:
    df = pd.read_csv(csv_path)
    if df.empty or "rating" not in df.columns:
        logger.warning("CSV 无评分数据，跳过分图")
        return

    ratings = pd.to_numeric(df["rating"], errors="coerce").dropna()

    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(ratings, bins=15, color="#4C72B0", edgecolor="white")
    ax.set_title("豆瓣读书 Top250 评分分布")
    ax.set_xlabel("评分")
    ax.set_ylabel("书籍数量")
    ax.grid(axis="y", alpha=0.3)

    Path(chart_path).parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(chart_path, dpi=150)
    plt.close(fig)
    logger.info("评分分布图已保存到 %s", chart_path)

    logger.info("平均评分: %.2f，最高: %.1f，最低: %.1f",
                ratings.mean(), ratings.max(), ratings.min())