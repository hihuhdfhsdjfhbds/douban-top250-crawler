"""解析层：输入 HTML，输出结构化数据。不发起网络请求，方便单测。"""

import logging
from typing import TypedDict

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class BookItem(TypedDict):
    rank: str
    title: str
    author: str
    rating: str
    quote: str


def parse_books(html: str) -> list[BookItem]:
    """从一页 Top250 的 HTML 中解析书籍列表。"""
    soup = BeautifulSoup(html, "html.parser")
    items: list[BookItem] = []

    for row in soup.select("tr.item"):
        title_tag = row.select_one("div.pl2 a")
        rating_tag = row.select_one("span.rating_nums")
        quote_tag = row.select_one("span.inq")
        rank_tag = row.select_one("div.pic em")
        info_tag = row.select_one("p.pl")

        if not title_tag or not rating_tag:
            logger.debug("跳过一条结构不完整的记录")
            continue

        items.append(
            {
                "rank": rank_tag.get_text(strip=True) if rank_tag else "",
                "title": title_tag.get_text(strip=True),
                "author": info_tag.get_text(strip=True).split("/")[0] if info_tag else "",
                "rating": rating_tag.get_text(strip=True),
                "quote": quote_tag.get_text(strip=True) if quote_tag else "",
            }
        )

    logger.info("本页解析出 %s 条记录", len(items))
    return items