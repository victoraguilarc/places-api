from dataclasses import dataclass

from src.auth.application.pending_actions.use_cases.generators.phone_number_verification import (
    PhoneNumberVerificationGenerator,
)
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.auth.domain.repositories.session import SessionRepository
from src.common.application.queries.auth import GetPhoneVerificationQuery
from src.common.domain.entities.pending_action import PendingActionContext
from src.common.domain.messaging.queries import QueryHandler


@dataclass
class GetPhoneNumberVerificationHandler(QueryHandler):
    action_repository: PendingActionRepository
    sesion_repository: SessionRepository

    def execute(
        self,
        query: GetPhoneVerificationQuery,
    ) -> PendingActionContext:
        return PhoneNumberVerificationGenerator(
            user=query.user,
            action_repository=self.action_repository,
            callback_url=query.callback_url,
            metadata=query.metadata,
        ).execute()
