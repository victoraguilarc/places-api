# -*- coding: utf-8 -*-
from django.conf import settings

from src.auth.infrastructure.repositories import (
    ORMPendingActionRepository,
    ORMSessionRepository,
    ORMSessionUserRepository,
)
from src.common.domain.context.domain import DomainContext
from src.common.helpers.singlenton import SingletonMeta
from src.places.infrastructure.http_services import HttpPlaceService, HttpForecastService


class DomainSingleton(metaclass=SingletonMeta):
    instance: DomainContext = DomainContext(
        session_repository=ORMSessionRepository(),
        session_user_repository=ORMSessionUserRepository(),
        pending_action_repository=ORMPendingActionRepository(),
        place_service=HttpPlaceService(
            base_url=settings.RESERVAMOS_BASE_URL,
        ),
        forecast_service=HttpForecastService(
            base_url=settings.OPEN_WEATHER_BASE_URL,
            api_key=settings.OPEN_WEATHER_API_KEY,
        ),
    )
