from src.common.application.commands.users import (
    PersistEmailAddressCommand,
    PersistPhoneNumberCommand,
)
from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.messaging.commands import CommandBus


class VerificationsMixin(object):
    command_bus: CommandBus

    def _check_validations(self, pending_action: PendingAction):
        if 'email_address' in pending_action.metadata:
            self._check_email_address(
                email_address=EmailAddress.from_dict(
                    data=pending_action.metadata['email_address'],
                )
            )

        if 'phone_number' in pending_action.metadata:
            self._check_phone_number(
                phone_number=PhoneNumber.from_dict(
                    verified_data=pending_action.metadata['phone_number'],
                ),
            )

    def _check_email_address(self, email_address: EmailAddress):
        if email_address.is_verified:
            return
        email_address.is_verified = True
        self.command_bus.dispatch(command=PersistEmailAddressCommand(email_address))

    def _check_phone_number(self, phone_number: PhoneNumber):
        if phone_number.is_verified:
            return
        phone_number.is_verified = True
        self.command_bus.dispatch(command=PersistPhoneNumberCommand(phone_number))
