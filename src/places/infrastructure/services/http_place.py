from dataclasses import dataclass
from typing import List

import requests

from src.common.constants import DEFAULT_REQUEST_TIMEOUT
from src.places.domain.entities.place import Place, PlaceType
from src.places.domain.services.place import PlaceService


@dataclass
class HttpPlaceService(PlaceService):
    base_url: str

    def get_places(self, search_term: str) -> List[Place]:
        endpoint = f'{self.base_url}/places?q={search_term}'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(endpoint, headers=headers, timeout=DEFAULT_REQUEST_TIMEOUT)
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
            for place in response_json
            if place.get('lat') and place.get('long')
        ]
