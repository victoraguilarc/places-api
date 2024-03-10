# -*- coding: utf-8 -*-

import uuid
from dataclasses import dataclass
from datetime import timedelta

from src.auth.application.pending_actions.responses import PendingActionResponse
from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.auth.domain.repositories.session_user import SessionUserRepository
from src.common.application.commands.common import SendEmailCommand
from src.common.constants import DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.enums.users import PendingActionCategory, PendingActionStatus
from src.common.domain.exceptions.users import UserNotFound
from src.common.domain.interfaces.responses import ApiResponse
from src.common.domain.interfaces.services import ApiService
from src.common.domain.messaging.commands import CommandBus
from src.common.helpers.time import TimeUtils


@dataclass
class ResetPasswordRequester(ApiService):
    user_email: str
    session_user_repository: SessionUserRepository
    action_repository: PendingActionRepository
    command_bus: CommandBus
    token_path_finder: CallbackData
    expiration_in_mins: int = DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES

    def execute(self) -> ApiResponse:
        user = self.session_user_repository.find_by_email(
            email=self.user_email,
        )
        if not user:
            raise UserNotFound

        pending_action = PendingAction(
            token=str(uuid.uuid4().hex),
            tracking_code=uuid.uuid4().hex,
            user=user,
            category=PendingActionCategory.RESET_PASSWORD,
            status=PendingActionStatus.PENDING,
            expires_at=(TimeUtils.utc_now() + timedelta(minutes=self.expiration_in_mins)),
        )

        self.action_repository.persist(pending_action)
        self.command_bus.dispatch(
            SendEmailCommand(
                to_emails=[user.email],
                context={
                    'action_link': self.token_path_finder.apply_token(pending_action.token),
                },
                template_name='auth/reset_password',
            )
        )
        return PendingActionResponse(instance=pending_action)
