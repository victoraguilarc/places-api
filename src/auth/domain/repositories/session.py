# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional

from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.entities.user import User
from src.common.domain.value_objects import UserId, EmailAddressId, PhoneNumberId


class SessionRepository(ABC):
    @abstractmethod
    def find_by_email(
        self,
        email: str,
    ) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find(
        self,
        user_id: UserId,
    ) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_email_address(
        self,
        email_address_id: EmailAddressId,
    ) -> Optional[EmailAddress]:
        raise NotImplementedError

    @abstractmethod
    def find_phone_number(
        self,
        phone_number_id: PhoneNumberId,
    ) -> Optional[PhoneNumber]:
        raise NotImplementedError

    @abstractmethod
    def has_valid_password(
        self,
        user: User,
        password: str,
    ) -> bool:
        raise NotImplementedError
