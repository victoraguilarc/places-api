from src.common.database.models import PendingActionORM
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.enums.users import PendingActionCategory, PendingActionStatus
from src.common.infrastructure.builders.user import build_user


def build_pending_action(orm_instance: PendingActionORM) -> PendingAction:
    return PendingAction(
        user=build_user(orm_instance.user),
        category=PendingActionCategory.from_value(orm_instance.category),
        status=PendingActionStatus.from_value(orm_instance.status),
        tracking_code=orm_instance.tracking_code,
        token=orm_instance.token,
        expires_at=orm_instance.expires_at,
        metadata=orm_instance.metadata,
        usage=orm_instance.usage,
        usage_limit=orm_instance.usage_limit,
    )
