# -*- coding: utf-8 -*-

from typing import Optional

from src.auth.domain.repositories.session_user import SessionUserRepository
from src.common.database.models import EmailAddressORM, PhoneNumberORM, UserORM
from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.entities.user import User
from src.common.domain.value_objects import RawPhoneNumber, UserId
from src.common.infrastructure.builders.email_address import build_email_address
from src.common.infrastructure.builders.user import build_user


class ORMSessionUserRepository(SessionUserRepository):
    def find_by_email(
        self,
        email: str,
    ) -> Optional[User]:
        try:
            orm_instance = UserORM.objects.get(email_address__email=email)
            return build_user(orm_instance)
        except UserORM.DoesNotExist:
            return None

    def find_by_phone_number(
        self,
        raw_phone_number: RawPhoneNumber,
    ) -> Optional[User]:
        try:
            orm_instance = UserORM.objects.get(
                phone_number__phone_number=raw_phone_number.phone_number,
                phone_number__dial_code=raw_phone_number.dial_code,
            )
            return build_user(orm_instance)
        except UserORM.DoesNotExist:
            return None

    def find(self, user_id: UserId) -> Optional[User]:
        orm_instance = self._find(user_id)
        if not orm_instance:
            return None
        return build_user(orm_instance)

    def register(
        self,
        user: User,
        raw_password: Optional[str] = None,
    ) -> User:
        user.email_address = self.persist_email_address(user.email_address)

        orm_instance, _ = UserORM.objects.get_or_create(
            email_address_id=user.email_address.id,
            defaults=user.to_persist_dict,
        )
        if raw_password:
            orm_instance.set_password(raw_password)
            orm_instance.save()

        return build_user(orm_instance)

    def persist_email_address(self, email_address: EmailAddress) -> EmailAddress:
        email_address_orm, _ = EmailAddressORM.objects.update_or_create(
            email=email_address.email,
            defaults=email_address.to_persist_dict,
        )
        return build_email_address(email_address_orm)

    def set_verified_email(
        self,
        user_id: UserId,
        user_email: str,
    ) -> User:
        orm_instance = self._find(user_id)
        orm_instance.email_address = user_email
        orm_instance.save(update_fields=['email', 'email_verified'])
        return build_user(orm_instance)

    def set_verified_phone_number(
        self,
        user_id: UserId,
        phone_number: PhoneNumber,
    ) -> User:
        phone_number_orm: PhoneNumberORM = PhoneNumberORM.objects.get_or_create(
            phone_number=phone_number.phone_number,
            dial_code=phone_number.dial_code,
            defaults=phone_number.to_persist_dict,
        )
        phone_number_orm.is_verified = True
        phone_number_orm.save(update_fields=['is_verified'])

        orm_instance = self._find(user_id)
        orm_instance.phone_number = phone_number_orm
        orm_instance.save(update_fields=['phone_number'])

        return build_user(orm_instance)

    def persist(self, user: User) -> User:
        self._persist_phone_number(user)
        orm_instance, _ = UserORM.objects.update_or_create(
            uuid=user.id,
            defaults=user.to_persist_dict,
        )
        return build_user(orm_instance)

    @classmethod
    def _persist_user(cls, user: User) -> UserORM:
        filter_criteria = {'uuid': user.id} if user.created_at else {'email': user.email}
        user_instance, _ = UserORM.objects.update_or_create(
            **filter_criteria, defaults={'email': user.email}
        )
        return user_instance

    @classmethod
    def _persist_phone_number(cls, user: User) -> Optional[PhoneNumberORM]:
        if not user.phone_number:
            return None
        phone_number, _ = PhoneNumberORM.objects.get_or_create(
            phone_number=user.phone_number.phone_number,
            defaults={
                'iso_code': str(user.phone_number.iso_code),
                'dial_code': str(user.phone_number.dial_code),
            },
        )
        return phone_number

    def set_password(
        self,
        user_id: UserId,
        user_password: str,
    ) -> User:
        orm_instance = self._find(user_id)
        orm_instance.set_password(user_password)
        orm_instance.save()
        return build_user(orm_instance)

    @classmethod
    def _find(cls, user_id: UserId) -> Optional[UserORM]:
        try:
            return UserORM.objects.get(uuid=user_id)
        except UserORM.DoesNotExist:
            return None
