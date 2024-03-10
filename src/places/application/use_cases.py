from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from dataclasses import dataclass
from typing import List

from loguru import logger

from src.common.domain.interfaces.services import Service
from src.places.domain.entities.place import PlaceContainer, Place
from src.places.domain.services.forecast import ForecastService
from src.places.domain.services.place import PlaceService


@dataclass
class PlaceContainersFilterer(Service):
    search_term: str
    place_service: PlaceService
    forecast_service: ForecastService

    def execute(self) -> List[PlaceContainer]:
        containers = []
        places = self.place_service.get_places(search_term=self.search_term)

        num_tasks = len(places)

        with ThreadPoolExecutor(num_tasks) as executor:
            futures = [executor.submit(self._fetch_forecasts, place) for place in places]
            wait(futures)
            for future in futures:
                containers.append(future.result())

        return containers

    def _fetch_forecasts(self, place: Place):
        logger.info(f'Fetching forecasts for: {place.slug}')
        return PlaceContainer(
            place=place,
            forecasts=self.forecast_service.get_forecasts(lat=place.lat, lng=place.lng),
        )
