import json
from dataclasses import dataclass
from typing import List

import requests
from loguru import logger

from src.common.application.helpers.time import epoch_to_date
from src.common.domain.interfaces.cache_store import CacheStore
from src.places.domain.entities.place import DayForecast
from src.places.domain.services.forecast import ForecastService


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


@dataclass
class CachedHttpForecastService(HttpForecastService):
    cache_store: CacheStore

    def get_forecasts(self, lat: float, lng: float) -> List[DayForecast]:
        raw_lat, raw_lng = round(lat, 4), round(lng, 4)
        cache_key = f'{raw_lng}|{raw_lng}'

        cached_value: str = self.cache_store.get(cache_key)
        if cached_value:
            logger.info(f'Hitting cache: {cache_key}')
            instances = json.loads(cached_value)
            return [
                DayForecast.from_dict(instance_dict)
                for instance_dict in instances
            ]

        forecasts = super().get_forecasts(lat=lat, lng=lng)
        self.cache_store.save(
            key=cache_key,
            value=json.dumps([forecast.to_dict for forecast in forecasts]),
        )
        return forecasts
