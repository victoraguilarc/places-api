import json

import pytest
from expects import be_a, be_empty, equal, expect, raise_error
from requests_mock import Mocker

from src.places.domain.entities.place import Place
from src.places.domain.enums import PlaceType
from src.places.domain.exceptions import FetchPlacesError
from src.places.domain.services.place import PlaceService
from src.places.infrastructure.services.http_place import HttpPlaceService

TEST_BASE_URL = 'http://places.server'
TESTS_SEARCH_TERM = 'cdmx'
TEST_GET_PLACES_ENDPOINT = f'{TEST_BASE_URL}/places?q={TESTS_SEARCH_TERM}'


@pytest.fixture(scope='function')
def use_case():
    return HttpPlaceService(base_url=TEST_BASE_URL)


@pytest.fixture(scope='function')
def place():
    return Place(
        id='place_id',
        slug='place_slug',
        city_name='place_city_name',
        state='place_state',
        country='place_country',
        lat=0.0,
        lng=0.0,
        result_type=PlaceType.city,
    )


@pytest.fixture(scope='function')
def place_data() -> dict:
    return {
        'id': 1,
        'slug': 'monterrey',
        'city_slug': 'monterrey',
        'display': 'Monterrey',
        'ascii_display': 'monterrey',
        'city_name': 'Monterrey',
        'city_ascii_name': 'monterrey',
        'state': 'Nuevo León',
        'country': 'México',
        'lat': '25.6866142',
        'long': '-100.3161126',
        'result_type': 'city',
        'popularity': '0.365111433802639',
        'sort_criteria': '0.32604458067361297',
    }


def test_get_places_error(
    use_case: PlaceService,
    requests_mock: Mocker,
):
    requests_mock.get(TEST_GET_PLACES_ENDPOINT, text='', status_code=404)

    expect(lambda: use_case.get_places(search_term=TESTS_SEARCH_TERM)).to(
        raise_error(FetchPlacesError)
    )


def test_get_places_empty(
    use_case: PlaceService,
    requests_mock: Mocker,
):
    requests_mock.get(TEST_GET_PLACES_ENDPOINT, text='[]')

    places = use_case.get_places(search_term=TESTS_SEARCH_TERM)

    expect(places).to(be_a(list))
    expect(places).to(be_empty)


def test_get_places(
    place: Place,
    use_case: PlaceService,
    requests_mock: Mocker,
    place_data: dict,
):
    places_sample = [place_data]
    requests_mock.get(TEST_GET_PLACES_ENDPOINT, text=json.dumps(places_sample))

    places = use_case.get_places(search_term=TESTS_SEARCH_TERM)

    expect(places).to(be_a(list))
    expect(len(places)).to(equal(len(places_sample)))
    expect(places[0]).to(be_a(Place))
