# -*- coding: utf-8 -*-

from rest_framework.request import Request
from rest_framework.response import Response

from src.common.presentation.api.domain_api import DomainAPIView
from src.places.application.responses import PlaceContainersResponse
from src.places.application.use_cases import PlaceContainersFilterer


class PlacesView(DomainAPIView):
    def get(self, request: Request):
        search_term = request.query_params.get('search', '')

        place_containers = PlaceContainersFilterer(
            search_term=search_term,
            place_service=self.domain_context.place_service,
            forecast_service=self.domain_context.forecast_service,
        ).execute()

        response = PlaceContainersResponse(place_containers)
        return Response(response.render(self.locale_context))
