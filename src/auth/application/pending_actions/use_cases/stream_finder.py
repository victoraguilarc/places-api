# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.domain.exceptions import PendingActionNotFound
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.interfaces.services import Service


@dataclass
class PendingActionStreamFinder(Service):
    stream_token: str
    repository: PendingActionRepository

    def execute(self) -> PendingAction:
        pending_action = self.repository.find_by_tracking_code(
            tracking_code=self.stream_token,
        )
        if not pending_action:
            raise PendingActionNotFound

        return pending_action
