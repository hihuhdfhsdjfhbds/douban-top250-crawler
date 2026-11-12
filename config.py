"""项目配置：所有可调参数集中在此，避免散落在代码里。"""

BASE_URL = "https://book.douban.com/top250?start={start}"
PAGE_SIZE = 25
MAX_PAGES = 10          # Top250 共 10 页
REQUEST_DELAY = 2.0     # 每次请求间隔（秒），尊重目标站点
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3

CSV_PATH = "data/douban_top250.csv"
CHART_PATH = "docs/rating_distribution.png"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)