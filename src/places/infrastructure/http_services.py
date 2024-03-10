from dataclasses import dataclass
from typing import List

import requests

from src.common.application.helpers.time import epoch_to_date
from src.places.domain.aggregates import Place, DayForecast, PlaceType
from src.places.domain.services import PlaceService, ForecastService


@dataclass
class HttpPlaceService(PlaceService):
    base_url: str

    def get_places(self, search_term: str) -> List[Place]:
        endpoint = f'{self.base_url}/places?q={search_term}'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(endpoint, headers=headers)
        if response.status_code not in [200, 201]:
            raise Exception('Error getting places')
        response_json = response.json()
        return [
            Place(
                id=place.get('id'),
                slug=place.get('slug'),
                city_name=place.get('city_name'),
                state=place.get('state'),
                country=place.get('country'),
                lat=float(place.get('lat')),
                lng=float(place.get('long')),
                result_type=PlaceType.from_value(place.get('result_type')),
            )
            for place in response_json if place.get('lat') and place.get('long')
        ]


@dataclass
class HttpForecastService(ForecastService):
    base_url: str
    api_key: str

    def get_forecasts(self, lat: float, lng: float) -> List[DayForecast]:
        endpoint = f'{self.base_url}/onecall?lat={lat}&lon={lng}&exclude=current,minutely,hourly&appid={self.api_key}&lang=es'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(endpoint, headers=headers)
        if response.status_code not in [200, 201]:
            raise Exception('Error getting forecasts')
        response_json = response.json()
        daily_forecasts = response_json.get('daily', [])
        return [
            DayForecast(
                day=epoch_to_date(forecast.get('dt')),
                max=forecast.get('temp', {}).get('max'),
                min=forecast.get('temp', {}).get('min'),
                weather=forecast.get('weather', [{}])[0].get('main'),
            )
            for forecast in daily_forecasts
        ]
