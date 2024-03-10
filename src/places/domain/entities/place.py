from dataclasses import dataclass
from typing import List

from src.places.domain.entities.day_forecast import DayForecast
from src.places.domain.enums import PlaceType


@dataclass
class Place(object):
    id: str
    slug: str
    city_name: str
    state: str
    country: str
    lat: float
    lng: float
    result_type: PlaceType


@dataclass
class PlaceContainer(object):
    place: Place
    forecasts: List[DayForecast]
