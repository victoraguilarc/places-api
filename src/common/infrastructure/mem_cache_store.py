from dataclasses import dataclass
from typing import Optional

from cachetools import TTLCache

from src.common.domain.interfaces.cache_store import CacheStore


@dataclass
class MemCacheStore(CacheStore):
    cache: TTLCache

    def save(self, key: str, value: str):
        self.cache[key] = value

    def get(self, key: str) -> Optional[str]:
        return self.cache.get(key)
