import logging

from analysis.report import plot_rating_distribution
from config import BASE_URL, CHART_PATH, CSV_PATH, MAX_PAGES, PAGE_SIZE, REQUEST_DELAY
from scraper.fetcher import fetch
from scraper.parser import parse_books
from storage.saver import save_to_csv
from utils.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def main() -> None:
    all_books = []

    for page in range(MAX_PAGES):
        start = page * PAGE_SIZE
        url = BASE_URL.format(start=start)
        logger.info("开始抓取第 %s 页: %s", page + 1, url)

        html = fetch(url)
        if html is None:
            logger.warning("跳过第 %s 页", page + 1)
            continue

        all_books.extend(parse_books(html))

        if page < MAX_PAGES - 1:
            import time
            time.sleep(REQUEST_DELAY)

    save_to_csv(all_books, CSV_PATH)
    plot_rating_distribution(CSV_PATH, CHART_PATH)
    logger.info("全部完成，共 %s 条", len(all_books))


if __name__ == "__main__":
    main()