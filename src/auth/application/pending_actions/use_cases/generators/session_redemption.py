# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.auth.domain.repositories import PendingActionRepository
from src.common.constants import DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES
from src.common.domain.entities.pending_action import PendingAction, PendingActionContext
from src.common.domain.entities.user import User
from src.common.domain.enums.users import PendingActionCategory
from src.common.domain.interfaces.services import ApiService


@dataclass
class SessionRedemptionGenerator(ApiService):
    user: User
    action_repository: PendingActionRepository
    callback_url: CallbackData
    metadata: Optional[dict] = None
    expiration_in_mins: int = DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES

    def execute(self, *args, **kwargs) -> PendingActionContext:
        self.action_repository.expire_past_similars(
            user_id=self.user.id,
            category=PendingActionCategory.REDEEM_SESSION,
        )

        pending_action = self.action_repository.persist(
            pending_action=PendingAction.session_redemption(
                user=self.user,
                metadata=self.metadata or {},
            ),
        )
        return PendingActionContext(
            pending_action=pending_action,
            callback_url=self.callback_url.apply_token(pending_action.token),
        )
