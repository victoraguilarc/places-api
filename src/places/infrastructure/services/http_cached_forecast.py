import json
from dataclasses import dataclass
from typing import List

from loguru import logger

from src.common.domain.interfaces.cache_store import CacheStore
from src.places.domain.entities.place import DayForecast
from src.places.infrastructure.services.http_forecast import HttpForecastService


@dataclass
class HttpCachedForecastService(HttpForecastService):
    cache_store: CacheStore

    def get_forecasts(self, lat: float, lng: float) -> List[DayForecast]:
        raw_lat, raw_lng = round(lat, 4), round(lng, 4)
        cache_key = self.get_cache_key(lat=raw_lat, lng=raw_lng)

        cached_value: str = self.cache_store.get(cache_key)
        if cached_value:
            logger.info(f'Hitting cache: {cache_key}')
            instances = json.loads(cached_value)
            return [DayForecast.from_dict(instance_dict) for instance_dict in instances]

        forecasts = super().get_forecasts(lat=lat, lng=lng)
        self.cache_store.save(
            key=cache_key,
            value=json.dumps([forecast.to_dict for forecast in forecasts]),
        )
        return forecasts

    @classmethod
    def get_cache_key(cls, lat: float, lng: float) -> str:
        raw_lat, raw_lng = round(lat, 4), round(lng, 4)
        return f'{raw_lat}|{raw_lng}'
