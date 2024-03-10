# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.domain.repositories import (
    PendingActionRepository,
    SessionRepository,
    SessionUserRepository,
)
from src.places.domain.services.forecast import ForecastService
from src.places.domain.services.place import PlaceService


@dataclass
class DomainContext(object):
    session_repository: SessionRepository
    session_user_repository: SessionUserRepository
    pending_action_repository: PendingActionRepository
    place_service: PlaceService
    forecast_service: ForecastService
