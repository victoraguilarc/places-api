from dataclasses import dataclass

from src.auth.application.pending_actions.use_cases.generators.email_address_verification import (
    EmailVerificationGenerator,
)
from src.auth.domain.repositories import PendingActionRepository, SessionRepository
from src.common.application.queries.auth import GetEmailVerificationQuery
from src.common.domain.entities.pending_action import PendingActionContext
from src.common.domain.messaging.queries import QueryHandler


@dataclass
class GetEmailVerificationHandler(QueryHandler):
    action_repository: PendingActionRepository
    sesion_repository: SessionRepository

    def execute(
        self,
        query: GetEmailVerificationQuery,
    ) -> PendingActionContext:
        return EmailVerificationGenerator(
            user=query.user,
            email_address_id=query.email_address_id,
            action_repository=self.action_repository,
            session_repository=self.sesion_repository,
            callback_url=query.callback_url,
        ).execute()
