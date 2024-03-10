# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.common.domain.entities.pending_action import PendingAction, PendingActionContext
from src.common.domain.entities.user import User
from src.common.domain.enums.users import PendingActionCategory
from src.common.domain.interfaces.services import Service


@dataclass
class PhoneNumberVerificationGenerator(Service):
    user: User
    action_repository: PendingActionRepository
    callback_url: CallbackData
    metadata: dict = None

    def execute(self) -> PendingActionContext:
        self.action_repository.expire_past_similars(
            user_id=self.user.id,
            category=PendingActionCategory.VERIFY_PHONE_NUMBER,
        )
        pending_action = self.action_repository.persist(
            pending_action=PendingAction.phone_verification(
                user=self.user,
                metadata=self.metadata or {},
            ),
        )
        return PendingActionContext(
            pending_action=pending_action,
            callback_url=self.callback_url.apply_token(token=pending_action.token),
        )
