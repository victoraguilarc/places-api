# -*- coding: utf-8 -*-

from dataclasses import asdict, dataclass

from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.entities.user import User
from src.common.domain.messaging.commands import Command




@dataclass
class RegisterUserCommand(Command):
    instance: User
    raw_password: str

    @property
    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, kwargs: dict) -> 'RegisterUserCommand':
        return cls(**kwargs)


@dataclass
class PersistPhoneNumberCommand(Command):
    instance: PhoneNumber

    @property
    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, kwargs: dict) -> 'PersistPhoneNumberCommand':
        return cls(**kwargs)


@dataclass
class PersistEmailAddressCommand(Command):
    instance: EmailAddress

    @property
    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, kwargs: dict) -> 'PersistEmailAddressCommand':
        return cls(**kwargs)
