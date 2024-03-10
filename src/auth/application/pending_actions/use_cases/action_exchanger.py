from dataclasses import dataclass

from src.auth.domain.exceptions import PendingActionNotFound
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.interfaces.services import Service


@dataclass
class PendingActionExchanger(Service):
    token: str
    action_repository: PendingActionRepository

    def execute(self) -> PendingAction:
        pending_action = self.action_repository.find(token=self.token)
        if not pending_action:
            raise PendingActionNotFound
        return pending_action
