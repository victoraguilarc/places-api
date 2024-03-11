import json

import pytest
from cachetools import TTLCache
from expects import be_a, be_empty, be_false, be_true, equal, expect, raise_error
from requests_mock import Mocker

from src.common.domain.interfaces.cache_store import CacheStore
from src.common.infrastructure.mem_cache_store import MemCacheStore
from src.places.domain.entities.day_forecast import DayForecast
from src.places.domain.exceptions import FetchForecastsError
from src.places.domain.services.forecast import ForecastService
from src.places.infrastructure.services.http_cached_forecast import HttpCachedForecastService
from src.places.infrastructure.services.http_forecast import HttpForecastService

TEST_BASE_URL = 'http://cached-forecast.server'
TEST_LAT = 0.0
TEST_LNG = 0.0
TEST_API_KEY = 'another_api_key'
TEST_ONE_CALL_ENDPOINT = HttpForecastService.build_forecast_endpoint(
    base_url=TEST_BASE_URL,
    lat=TEST_LAT,
    lng=TEST_LNG,
    api_key=TEST_API_KEY,
)


@pytest.fixture(scope='function')
def cache_store() -> CacheStore:
    return MemCacheStore(instance=TTLCache(maxsize=10, ttl=10))


@pytest.fixture(scope='function')
def use_case(cache_store: CacheStore) -> ForecastService:
    return HttpCachedForecastService(
        base_url=TEST_BASE_URL,
        api_key=TEST_API_KEY,
        cache_store=cache_store,
    )


@pytest.fixture(scope='function')
def cache_key() -> str:
    return HttpCachedForecastService.get_cache_key(lat=TEST_LAT, lng=TEST_LNG)


def test_get_forecasts_error(
    use_case: ForecastService,
    requests_mock: Mocker,
):
    requests_mock.get(TEST_ONE_CALL_ENDPOINT, text='', status_code=404)

    expect(lambda: use_case.get_forecasts(lat=TEST_LAT, lng=TEST_LNG)).to(
        raise_error(FetchForecastsError)
    )


def test_get_forecasts_from_remote(
    use_case: ForecastService,
    requests_mock: Mocker,
    forecast_data: dict,
):
    requests_mock.get(TEST_ONE_CALL_ENDPOINT, text=json.dumps(forecast_data))

    forecasts = use_case.get_forecasts(lat=TEST_LAT, lng=TEST_LNG)

    expect(forecasts).to(be_a(list))
    expect(len(forecasts)).to(equal(len(forecast_data['daily'])))
    expect(forecasts[0]).to(be_a(DayForecast))
    expect(requests_mock.called_once).to(be_true)


def test_get_forecasts_from_cache(
    use_case: ForecastService,
    requests_mock: Mocker,
    forecast_data: dict,
    cache_key: str,
    cache_store: CacheStore,
):
    cache_store.save(cache_key, '[]')
    requests_mock.get(TEST_ONE_CALL_ENDPOINT, text=json.dumps(forecast_data))

    forecasts = use_case.get_forecasts(lat=TEST_LAT, lng=TEST_LNG)

    expect(forecasts).to(be_a(list))
    expect(forecasts).to(be_empty)
    expect(requests_mock.called_once).to(be_false)
