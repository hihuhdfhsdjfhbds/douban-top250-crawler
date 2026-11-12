"""存储层：把结构化数据写进 CSV。后续可扩展 SQLite。"""

import logging
from pathlib import Path
from typing import Iterable

import pandas as pd

from scraper.parser import BookItem

logger = logging.getLogger(__name__)


def save_to_csv(items: Iterable[BookItem], path: str) -> None:
    df = pd.DataFrame(list(items))
    if df.empty:
        logger.warning("没有数据可保存")
        return
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    logger.info("已保存 %s 条记录到 %s", len(df), path)