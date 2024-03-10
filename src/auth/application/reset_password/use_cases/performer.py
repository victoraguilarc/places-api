# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.application.sessions.responses import UserSessionResponse
from src.auth.domain.exceptions import InvalidPendingToken
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.auth.domain.repositories.session_user import SessionUserRepository
from src.common.domain.enums.users import PendingActionCategory
from src.common.domain.interfaces.services import ApiService
from src.common.domain.value_objects import UserId


@dataclass
class ResetPasswordPerformer(ApiService):
    token: str
    raw_password: str
    sesson_user_repository: SessionUserRepository
    action_repository: PendingActionRepository

    def execute(self) -> UserSessionResponse:
        pending_token = self.action_repository.find(
            token=self.token,
            category=PendingActionCategory.RESET_PASSWORD,
        )

        if not pending_token:
            raise InvalidPendingToken

        session_user = self.sesson_user_repository.set_password(
            user_id=UserId(pending_token.user_id),
            user_password=self.raw_password,
        )
        self.action_repository.delete(pending_token)
        return UserSessionResponse(session_user)
