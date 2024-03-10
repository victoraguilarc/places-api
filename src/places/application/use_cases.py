from dataclasses import dataclass
from typing import List

from src.common.domain.interfaces.services import Service
from src.places.domain.aggregates import PlaceContainer
from src.places.domain.services import PlaceService, ForecastService


@dataclass
class PlaceContainersFilterer(Service):
    search_term: str
    place_service: PlaceService
    forecast_service: ForecastService

    def execute(self) -> List[PlaceContainer]:
        containers = []
        places = self.place_service.get_places(search_term=self.search_term)
        for place in places:
            containers.append(
                PlaceContainer(
                    place=place,
                    forecasts=self.forecast_service.get_forecasts(lat=place.lat, lng=place.lng),
                )
            )
        return containers
