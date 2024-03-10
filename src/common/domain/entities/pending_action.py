# -*- coding: utf-8 -*-
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta

from src.common.constants import (
    DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES,
    DEFAULT_PENDING_ACTION_USAGE_LIMIT,
    DEFAULT_PENDING_ACTION_SESSION_USAGE_LIMIT,
)
from src.common.domain.entities.user import User
from src.common.domain.enums.users import PendingActionCategory, PendingActionStatus
from src.common.domain.interfaces.entities import AggregateRoot
from src.common.domain.value_objects import UserId
from src.common.helpers.enconding import encode_base64
from src.common.helpers.time import TimeUtils
from src.common.presentation.utils.dates import now


@dataclass
class PendingAction(AggregateRoot):
    user: User
    category: PendingActionCategory
    status: PendingActionStatus
    token: str
    tracking_code: str
    expires_at: datetime
    metadata: dict = None
    usage_limit: int = DEFAULT_PENDING_ACTION_USAGE_LIMIT
    usage: int = 0

    def __post_init__(self):
        self.metadata = self.metadata or {}

    @property
    def is_usage_limit_reached(self):
        return self.usage >= self.usage_limit

    @property
    def is_email_verification(self):
        return self.category == PendingActionCategory.VERIFY_EMAIL

    @property
    def is_phone_verification(self):
        return self.category == PendingActionCategory.VERIFY_PHONE_NUMBER

    @property
    def user_id(self) -> UserId:
        return self.user.uuid

    @property
    def is_expired(self):
        return now() > self.expires_at

    @property
    def is_completed(self) -> bool:
        return self.status == PendingActionStatus.COMPLETED

    @property
    def is_pending(self) -> bool:
        return self.status == PendingActionStatus.PENDING

    @property
    def to_tracking_dict(self):
        return {
            'tracking_code': str(self.tracking_code),
            'category': str(self.category),
            'status': str(self.status),
        }

    @property
    def to_persist_dict(self):
        return {
            'tracking_code': self.tracking_code,
            'user_id': self.user_id,
            'category': str(self.category),
            'status': str(self.status),
            'token': self.token,
            'expires_at': self.expires_at,
            'metadata': self.metadata,
            'usage': self.usage,
            'usage_limit': self.usage_limit,
        }

    @property
    def channel_id(self):
        return f'PendingAction@{self.tracking_code}'

    def has_metadata(self, key: str) -> bool:
        return key in self.metadata

    def complete(self):
        self.status = PendingActionStatus.COMPLETED

    def cancel(self):
        self.status = PendingActionStatus.EXPIRED

    def increment_usage(self):
        self.usage += 1

    @classmethod
    def email_verification(
        cls,
        user: User,
        metadata: dict,
        expiration_in_mins: int = DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES,
    ) -> 'PendingAction':
        return PendingAction(
            token=encode_base64(uuid.uuid4().hex),
            tracking_code=str(uuid.uuid4().hex),
            user=user,
            category=PendingActionCategory.VERIFY_EMAIL,
            status=PendingActionStatus.PENDING,
            expires_at=(TimeUtils.utc_now() + timedelta(minutes=expiration_in_mins)),
            metadata=metadata,
        )

    @classmethod
    def phone_verification(
        cls,
        user: User,
        metadata: dict,
        expiration_in_mins: int = DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES,
    ) -> 'PendingAction':
        return PendingAction(
            token=encode_base64(uuid.uuid4().hex),
            tracking_code=str(uuid.uuid4().hex),
            user=user,
            category=PendingActionCategory.VERIFY_PHONE_NUMBER,
            status=PendingActionStatus.PENDING,
            expires_at=(TimeUtils.utc_now() + timedelta(minutes=expiration_in_mins)),
            metadata=metadata,
        )

    @classmethod
    def session_redemption(
        cls,
        user: User,
        metadata: dict,
        expiration_in_mins: int = DEFAULT_PENDING_ACTION_EXPIRATION_IN_MINUTES,
    ) -> 'PendingAction':
        return PendingAction(
            token=encode_base64(uuid.uuid4().hex),
            tracking_code=uuid.uuid4().hex,
            user=user,
            category=PendingActionCategory.REDEEM_SESSION,
            status=PendingActionStatus.PENDING,
            expires_at=(TimeUtils.utc_now() + timedelta(minutes=expiration_in_mins)),
            metadata=metadata,
            usage_limit=DEFAULT_PENDING_ACTION_SESSION_USAGE_LIMIT,
        )


@dataclass
class PendingActionContext(object):
    pending_action: PendingAction
    callback_url: str
