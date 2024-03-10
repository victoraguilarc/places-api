from abc import ABC, abstractmethod
from typing import List

from src.places.domain.entities.place import Place


class PlaceService(ABC):
    @abstractmethod
    def get_places(self, search_term: str) -> List[Place]:
        raise NotImplementedError
