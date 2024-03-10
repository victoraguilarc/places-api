# -*- coding: utf-8 -*-

from typing import Optional

from src.auth.domain.repositories.session import SessionRepository
from src.common.database.models import UserORM, EmailAddressORM, PhoneNumberORM
from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.entities.user import User
from src.common.domain.value_objects import UserId, EmailAddressId, PhoneNumberId
from src.common.infrastructure.builders.email_address import build_email_address
from src.common.infrastructure.builders.phone_number import build_phone_number
from src.common.infrastructure.builders.user import build_user


class ORMSessionRepository(SessionRepository):

    def find_by_email(
        self,
        email: str,
    ) -> Optional[User]:
        user_orm = self._find_by_email(email)
        if not user_orm:
            return None
        return build_user(user_orm)

    def find(
        self,
        user_id: UserId,
    ) -> Optional[User]:
        return self._get_from_user_by_id(user_id)

    def find_email_address(
        self,
        email_address_id: EmailAddressId,
    ) -> Optional[EmailAddress]:
        try:
            orm_instance = EmailAddressORM.objects.get(uuid=email_address_id)
            return build_email_address(orm_instance=orm_instance)
        except EmailAddressORM.DoesNotExist:
            return None

    def find_phone_number(
        self,
        phone_number_id: PhoneNumberId,
    ) -> Optional[PhoneNumber]:
        try:
            orm_instance = PhoneNumberORM.objects.get(uuid=phone_number_id)
            return build_phone_number(orm_instance=orm_instance)
        except PhoneNumberORM.DoesNotExist:
            return None

    def has_valid_password(
        self,
        user: User,
        password: str,
    ) -> bool:
        user_orm = self._find(user.id)
        return user_orm.check_password(password)

    @classmethod
    def _find(cls, user_id: UserId) -> Optional[UserORM]:
        try:
            return UserORM.objects.select_related('phone_number').get(uuid=user_id)
        except UserORM.DoesNotExist:
            return None

    @classmethod
    def _find_by_email(cls, email: str) -> Optional[UserORM]:
        try:
            return (
                UserORM.objects
                .select_related('phone_number', 'email_address')
                .get(email_address__email=email)
            )
        except UserORM.DoesNotExist:
            return None

    @classmethod
    def _get_from_user_by_email(cls, email: str) -> Optional[User]:
        user_orm = UserORM.objects.select_related('phone_number').filter(email=email).first()
        if not user_orm:
            return None
        return build_user(user_orm)

    @classmethod
    def _get_from_user_by_id(cls, user_id: UserId) -> Optional[User]:
        user_orm = UserORM.objects.select_related('phone_number').filter(uuid=user_id).first()
        if not user_orm:
            return None
        return build_user(orm_instance=user_orm)
