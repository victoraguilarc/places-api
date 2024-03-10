from abc import ABC, abstractmethod
from typing import Optional


class CacheStore(ABC):

    @abstractmethod
    def save(self, key: str, value: str):
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        raise NotImplementedError
