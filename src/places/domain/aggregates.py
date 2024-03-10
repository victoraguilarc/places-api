from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import List

from src.common.domain import BaseEnum


class PlaceType(BaseEnum):
    city = 'city'
    terminal = 'terminal'
    airport = 'airport'


@dataclass
class DayForecast(object):
    day: date
    max: Decimal
    min: Decimal
    weather: str


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
