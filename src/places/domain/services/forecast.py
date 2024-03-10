from abc import ABC, abstractmethod
from typing import List

from src.places.domain.entities.place import DayForecast


class ForecastService(ABC):
    @abstractmethod
    def get_forecasts(self, lat: float, lng: float) -> List[DayForecast]:
        raise NotImplementedError
