from abc import ABC, abstractmethod
from typing import List

from src.places.domain.aggregates import Place, DayForecast


class PlaceService(ABC):
    @abstractmethod
    def get_places(self, search_term: str) -> List[Place]:
        raise NotImplementedError


class ForecastService(ABC):
    @abstractmethod
    def get_forecasts(self, lat: float, lng: float) -> List[DayForecast]:
        raise NotImplementedError
