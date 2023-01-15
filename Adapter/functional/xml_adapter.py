from typing import Any

from bs4 import BeautifulSoup


def get_from_bs(bs: BeautifulSoup, key: str, default: Any = None) -> Any | None:
    value = bs.find(key)
    return value.get_text() if value else default
