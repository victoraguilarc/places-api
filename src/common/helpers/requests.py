from typing import Optional

from rest_framework.request import Request

from src.common.database.models import UserORM
from src.common.domain.entities.user import User
from src.common.infrastructure.builders.user import build_user
from src.common.presentation.api.exceptions.collection import USER_NOT_FOUND


def get_user_from_request(
    request: Request,
    raise_exception: bool = False,
) -> Optional[User]:
    if not request.user.is_authenticated:
        return None

    try:
        orm_instance = UserORM.objects.get(uuid=request.user.uuid)
        return build_user(orm_instance)
    except UserORM.DoesNotExist:
        if raise_exception:
            raise USER_NOT_FOUND
        return None
