# -*- coding: utf-8 -*-
from typing import List, Optional

from src.auth.domain.repositories.pending_action import PendingActionRepository
from src.common.database.models import PendingActionORM
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.enums.users import PendingActionCategory, PendingActionStatus
from src.common.domain.value_objects import UserId
from src.common.helpers.time import TimeUtils
from src.common.infrastructure.builders.pending_action import build_pending_action


class ORMPendingActionRepository(PendingActionRepository):
    def find_by_tracking_code(
        self,
        tracking_code: str,
    ) -> Optional[PendingAction]:
        try:
            return build_pending_action(
                orm_instance=PendingActionORM.objects.get(
                    tracking_code=tracking_code,
                ),
            )
        except PendingActionORM.DoesNotExist:
            return None

    def find(
        self,
        token: str,
        category: Optional[PendingActionCategory] = None,
        status: Optional[PendingActionStatus] = None,
    ) -> Optional[PendingAction]:
        filter_criteria = {'token': token}

        if category:
            filter_criteria['category'] = str(category)
        if status:
            filter_criteria['status'] = str(status)

        try:
            return build_pending_action(
                orm_instance=PendingActionORM.objects.get(**filter_criteria),
            )
        except PendingActionORM.DoesNotExist:
            return None

    def find_with_categories(
        self,
        token: str,
        categories: List[PendingActionCategory],
    ) -> Optional[PendingAction]:
        try:
            return build_pending_action(
                orm_instance=PendingActionORM.objects.get(
                    token=token,
                    category__in=[str(category) for category in categories],
                    status=str(PendingActionStatus.PENDING),
                ),
            )
        except PendingActionORM.DoesNotExist:
            return None

    def persist(self, pending_action: PendingAction) -> PendingAction:
        orm_instance, _ = PendingActionORM.objects.update_or_create(
            token=pending_action.token,
            defaults=pending_action.to_persist_dict,
        )
        return build_pending_action(orm_instance)

    def expire_past_similars(
        self,
        user_id: UserId,
        category: PendingActionCategory,
    ):
        utc_now = TimeUtils.utc_now()
        PendingActionORM.objects.filter(
            user_id=user_id,
            category=str(category),
            status=str(PendingActionStatus.PENDING),
            expires_at__lte=utc_now,
        ).update(
            status=str(PendingActionStatus.EXPIRED),
        )

    def delete(self, pending_action: PendingAction):
        PendingActionORM.objects.filter(token=pending_action.token).delete()

    def cancel(self, pending_action: PendingAction):
        pending_action.cancel()
        self.persist(pending_action)

    def complete(self, pending_action: PendingAction):
        pending_action.complete()
        self.persist(pending_action)

    def clean_expired(self, user_id: UserId):
        PendingActionORM.objects.filter(
            user_id=user_id, status=str(PendingActionStatus.EXPIRED)
        ).delete()
