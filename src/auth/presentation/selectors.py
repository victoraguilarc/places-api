# -*- coding: utf-8 -*-

from typing import Optional

from src.common.database.models import UserORM
from src.common.domain.value_objects import UserId


class UserSelector(object):
    @classmethod
    def find(cls, user_id: UserId) -> Optional[UserORM]:
        return UserORM.objects.filter(uuid=user_id).first()
