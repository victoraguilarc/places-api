# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional

from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.entities.user import User
from src.common.domain.value_objects import RawPhoneNumber, UserId


class SessionUserRepository(ABC):
    @abstractmethod
    def find_by_email(
        self,
        email: str,
    ) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_phone_number(
        self,
        raw_phone_number: RawPhoneNumber,
    ) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find(self, user_id: UserId) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def register(
        self,
        user: User,
        raw_password: Optional[str] = None,
    ) -> User:
        raise NotImplementedError

    @abstractmethod
    def persist_email_address(self, email_address: EmailAddress) -> EmailAddress:
        raise NotImplementedError

    @abstractmethod
    def set_verified_email(
        self,
        user_id: UserId,
        user_email: str,
    ) -> User:
        raise NotImplementedError

    @abstractmethod
    def set_verified_phone_number(
        self,
        user_id: UserId,
        phone_number: PhoneNumber,
    ) -> User:
        raise NotImplementedError

    @abstractmethod
    def persist(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def set_password(
        self,
        user_id: UserId,
        user_password: str,
    ) -> User:
        raise NotImplementedError
