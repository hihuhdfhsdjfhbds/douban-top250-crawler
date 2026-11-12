"""统一日志配置：同时输出到控制台和文件。"""

import logging
import sys
from pathlib import Path


def setup_logging(level: int = logging.INFO) -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)

    file_handler = logging.FileHandler(log_dir / "crawler.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()
    root.addHandler(console)
    root.addHandler(file_handler)