from dataclasses import dataclass
from typing import List

import requests

from src.common.application.helpers.time import epoch_to_date
from src.common.constants import DEFAULT_REQUEST_TIMEOUT
from src.places.domain.entities.place import DayForecast
from src.places.domain.exceptions import FetchForecastsError
from src.places.domain.services.forecast import ForecastService


@dataclass
class HttpForecastService(ForecastService):
    base_url: str
    api_key: str

    @classmethod
    def build_forecast_endpoint(
        cls,
        base_url: str,
        lat: float,
        lng: float,
        api_key: str,
    ) -> str:
        fixed_params = f'exclude=current,minutely,hourly&units=metric&lang=es&appid={api_key}'
        return f'{base_url}/onecall?lat={lat}&lon={lng}&{fixed_params}'

    def get_forecasts(self, lat: float, lng: float) -> List[DayForecast]:
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(
            self.build_forecast_endpoint(self.base_url, lat, lng, self.api_key),
            headers=headers,
            timeout=DEFAULT_REQUEST_TIMEOUT,
        )
        if response.status_code not in [200, 201]:
            raise FetchForecastsError
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
