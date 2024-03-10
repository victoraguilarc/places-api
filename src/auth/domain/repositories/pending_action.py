# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional, List

from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.enums.users import PendingActionCategory, PendingActionStatus
from src.common.domain.value_objects import UserId


class PendingActionRepository(ABC):
    @abstractmethod
    def find(
        self,
        token: str,
        category: Optional[PendingActionCategory] = None,
        status: Optional[PendingActionStatus] = None,
    ) -> Optional[PendingAction]:
        raise NotImplementedError

    @abstractmethod
    def find_with_categories(
        self,
        token: str,
        categories: List[PendingActionCategory],
    ) -> Optional[PendingAction]:
        raise NotImplementedError

    @abstractmethod
    def find_by_tracking_code(
        self,
        tracking_code: str,
    ) -> Optional[PendingAction]:
        raise NotImplementedError

    @abstractmethod
    def persist(
        self,
        pending_action: PendingAction,
    ) -> PendingAction:
        raise NotImplementedError

    @abstractmethod
    def expire_past_similars(
        self,
        user_id: UserId,
        category: PendingActionCategory,
    ):
        raise NotImplementedError

    @abstractmethod
    def delete(
        self,
        pending_action: PendingAction,
    ):
        raise NotImplementedError

    @abstractmethod
    def cancel(
        self,
        pending_action: PendingAction,
    ):
        raise NotImplementedError

    @abstractmethod
    def complete(
        self,
        pending_action: PendingAction,
    ):
        raise NotImplementedError

    @abstractmethod
    def clean_expired(
        self,
        user_id: UserId,
    ):
        raise NotImplementedError
