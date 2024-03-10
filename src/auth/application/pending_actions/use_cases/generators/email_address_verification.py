# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.auth.domain.repositories.session import SessionRepository
from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.pending_action import PendingAction, PendingActionContext
from src.common.domain.entities.user import User
from src.common.domain.enums.users import PendingActionCategory
from src.common.domain.exceptions.auth import EmailAddressNotFound
from src.common.domain.interfaces.services import Service
from src.common.domain.value_objects import EmailAddressId


@dataclass
class EmailVerificationGenerator(Service):
    user: User
    email_address_id: EmailAddressId
    action_repository: PendingActionRepository
    session_repository: SessionRepository
    callback_url: CallbackData

    def execute(self) -> PendingActionContext:
        email_address = self._get_email_address(self.email_address_id)
        self.action_repository.expire_past_similars(
            user_id=self.user.id,
            category=PendingActionCategory.VERIFY_EMAIL,
        )
        pending_action = self.action_repository.persist(
            pending_action=PendingAction.email_verification(
                user=self.user,
                metadata={
                    'email_address': email_address.to_dict,
                },
            ),
        )
        return PendingActionContext(
            pending_action=pending_action,
            callback_url=self.callback_url.apply_token(token=pending_action.token),
        )

    def _get_email_address(self, email_address_id: EmailAddressId) -> EmailAddress:
        email_address = self.session_repository.find_email_address(email_address_id)
        if not email_address:
            raise EmailAddressNotFound
        return email_address
