"""请求层：负责发 HTTP 请求、重试、异常处理，不关心页面结构。"""

import logging
import time
from typing import Optional

import requests

from config import MAX_RETRIES, REQUEST_DELAY, REQUEST_TIMEOUT, USER_AGENT

logger = logging.getLogger(__name__)


def fetch(url: str) -> Optional[str]:
    """抓取页面 HTML。成功返回文本，失败返回 None（不抛异常给上层）。"""
    headers = {"User-Agent": USER_AGENT}
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            resp.encoding = resp.apparent_encoding
            logger.info("请求成功 [%s/%s] %s", attempt, MAX_RETRIES, url)
            return resp.text
        except requests.RequestException as exc:
            logger.warning(
                "请求失败 [%s/%s] %s | 原因: %s", attempt, MAX_RETRIES, url, exc
            )
            if attempt == MAX_RETRIES:
                logger.error("达到最大重试次数，放弃: %s", url)
                return None
            time.sleep(REQUEST_DELAY * attempt)
    return None