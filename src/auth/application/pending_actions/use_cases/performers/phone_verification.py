# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.domain.exceptions import InvalidPendingToken, CorruptedPendingAction
from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.common.application.commands.users import PersistPhoneNumberCommand
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.enums.users import PendingActionCategory, PendingActionStatus
from src.common.domain.interfaces.services import Service
from src.common.domain.messaging.commands import CommandBus


@dataclass
class PhoneVerificationPerformer(Service):
    token: str
    action_repository: PendingActionRepository
    command_bus: CommandBus

    def execute(self):
        pending_action = self._get_pending_action()
        self._persist_verification(pending_action)
        self._process_status(pending_action)

    def _process_status(self, pending_action: PendingAction):
        pending_action.increment_usage()
        if pending_action.is_usage_limit_reached:
            self.action_repository.complete(pending_action)
        self.action_repository.persist(pending_action)

    def _get_pending_action(self) -> PendingAction:
        pending_action: PendingAction = self.action_repository.find(
            token=self.token,
            category=PendingActionCategory.VERIFY_PHONE_NUMBER,
            status=PendingActionStatus.PENDING,
        )
        if not pending_action:
            raise InvalidPendingToken

        if not pending_action.has_metadata('phone_number'):
            raise CorruptedPendingAction

        return pending_action

    def _persist_verification(self, pending_action):
        phone_number = PhoneNumber.from_dict(pending_action.metadata['phone_number'])
        if phone_number.is_verified:
            return
        phone_number.is_verified = True
        self.command_bus.dispatch(command=PersistPhoneNumberCommand(phone_number))
