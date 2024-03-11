# -*- coding: utf-8 -*-
from django.conf import settings

from cachetools import TTLCache

from src.auth.infrastructure.repositories.orm_pending_action import ORMPendingActionRepository
from src.auth.infrastructure.repositories.orm_session import ORMSessionRepository
from src.auth.infrastructure.repositories.orm_session_user import ORMSessionUserRepository
from src.common.domain.context.domain import DomainContext
from src.common.helpers.singlenton import SingletonMeta
from src.common.infrastructure.mem_cache_store import MemCacheStore
from src.places.infrastructure.services.http_cached_forecast import HttpCachedForecastService
from src.places.infrastructure.services.http_place import HttpPlaceService


class DomainSingleton(metaclass=SingletonMeta):
    instance: DomainContext = DomainContext(
        session_repository=ORMSessionRepository(),
        session_user_repository=ORMSessionUserRepository(),
        pending_action_repository=ORMPendingActionRepository(),
        place_service=HttpPlaceService(
            base_url=settings.RESERVAMOS_BASE_URL,
        ),
        forecast_service=HttpCachedForecastService(
            base_url=settings.OPEN_WEATHER_BASE_URL,
            api_key=settings.OPEN_WEATHER_API_KEY,
            cache_store=MemCacheStore(
                instance=TTLCache(maxsize=1000, ttl=3600),
            ),
        ),
    )
