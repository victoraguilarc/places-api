# -*- coding: utf-8 -*-

from src.common.database.models import UserORM
from src.common.domain.entities.user import User
from src.common.infrastructure.builders.email_address import build_email_address
from src.common.infrastructure.builders.phone_number import build_phone_number


def build_user(orm_instance: UserORM) -> User:
    return User(
        id=orm_instance.uuid,
        email_address=(
            build_email_address(orm_instance.email_address) if orm_instance.email_address else None
        ),
        phone_number=(
            build_phone_number(orm_instance.phone_number) if orm_instance.phone_number else None
        ),
        is_active=orm_instance.is_active,
        created_at=orm_instance.created_at,
    )
