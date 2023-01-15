from typing import Any

from bs4 import BeautifulSoup


class XMLConfig(BeautifulSoup):
    def get(self, key: str, default: Any = None) -> Any | None:
        value = self.find(key)
        return value.get_text() if value else default
