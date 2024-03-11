from unittest.mock import Mock, call

import pytest
from expects import be_a, equal, expect

from src.places.application.use_cases.places_filterer import PlaceContainersFilterer
from src.places.domain.entities.place import Place, PlaceContainer
from src.places.domain.enums import PlaceType
from src.places.domain.services.forecast import ForecastService
from src.places.domain.services.place import PlaceService

TEST_SEARCH_TERM = 'cdmx'


@pytest.fixture(scope='function')
def place():
    return Place(
        id='place_id',
        slug='place_slug',
        city_name='place_city_name',
        state='place_state',
        country='place_country',
        lat=100.0,
        lng=50.0,
        result_type=PlaceType.city,
    )


@pytest.fixture(scope='function')
def place_service_mock() -> PlaceService:
    return Mock(spec=PlaceService)


@pytest.fixture(scope='function')
def forecast_service_mock() -> ForecastService:
    return Mock(spec=ForecastService)


@pytest.fixture
def use_case(
    place_service_mock: PlaceService,
    forecast_service_mock: ForecastService,
) -> PlaceContainersFilterer:
    return PlaceContainersFilterer(
        search_term=TEST_SEARCH_TERM,
        place_service=place_service_mock,
        forecast_service=forecast_service_mock,
    )


def test_execute(
    use_case: PlaceContainersFilterer,
    place_service_mock: Mock,
    forecast_service_mock: Mock,
    place: Place,
):
    places_sample = [place]
    place_service_mock.get_places.return_value = places_sample
    forecast_service_mock.get_forecasts.return_value = []

    containers = use_case.execute()

    expect(containers).to(be_a(list))
    expect(len(containers)).to(equal(len(places_sample)))
    expect(containers[0]).to(be_a(PlaceContainer))
    expect(containers[0].place).to(equal(place))
    expect(place_service_mock.get_places.call_args).to(
        equal(
            call(search_term=TEST_SEARCH_TERM),
        )
    )
    expect(forecast_service_mock.get_forecasts.call_args).to(
        equal(
            call(lat=place.lat, lng=place.lng),
        )
    )
    expect(forecast_service_mock.get_forecasts.call_count).to(equal(len(places_sample)))
