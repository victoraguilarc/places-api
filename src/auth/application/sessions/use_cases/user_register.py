# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.auth.domain.repositories.session_user import SessionUserRepository
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.entities.user import User
from src.common.domain.exceptions.common import EmailIsAlreadyUsed
from src.common.domain.interfaces.services import ApiService
from src.common.domain.messaging.commands import CommandBus


@dataclass
class UserRegister(ApiService):
    user_instance: User
    raw_password: str
    session_user_repository: SessionUserRepository
    action_repository: PendingActionRepository
    command_bus: CommandBus
    token_path: CallbackData
    send_from_email: str
    send_async_emails: bool

    def execute(
        self,
    ) -> PendingAction:
        existent_user = self.session_user_repository.find_by_email(
            email=self.user_instance.email,
        )
        if existent_user:
            raise EmailIsAlreadyUsed

        new_user = self.session_user_repository.register(
            user=self.user_instance,
            raw_password=self.raw_password,
        )
        pending_action = self.action_repository.persist(
            pending_action=PendingAction.email_verification(
                user=new_user,
                metadata={},
            ),
        )
        return pending_action
