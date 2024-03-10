# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.db.models import JSONField

from src.common.constants import DEFAULT_PENDING_ACTION_USAGE_LIMIT
from src.common.database.models.mixins.common import UUIDTimestampMixin
from src.common.domain.enums.users import PendingActionCategory, PendingActionStatus
from src.common.helpers.enconding import encode_base64


def generate_hex():
    return encode_base64(uuid.uuid4().hex)


class PendingActionORM(UUIDTimestampMixin):
    """Represents a user actions that it must be completed."""

    user = models.ForeignKey(
        'UserORM',
        verbose_name='User',
        related_name='pending_actions',
        on_delete=models.CASCADE,
    )
    category = models.CharField(
        max_length=50,
        choices=PendingActionCategory.choices(),
        db_index=True,
    )
    status = models.CharField(
        max_length=50,
        choices=PendingActionStatus.choices(),
        db_index=True,
        default=str(PendingActionStatus.PENDING),
    )
    token = models.CharField(
        max_length=120,
        db_index=True,
        default=generate_hex,
    )
    tracking_code = models.CharField(
        max_length=120,
        db_index=True,
        default=generate_hex,
    )
    expires_at = models.DateTimeField(blank=True, null=True)
    usage_limit = models.PositiveIntegerField(
        verbose_name='Usage Limit',
        default=DEFAULT_PENDING_ACTION_USAGE_LIMIT,
        help_text='How many times the token can be used',
    )
    usage = models.PositiveIntegerField(
        verbose_name='Usage',
        default=0,
        help_text='How many times the token has been used',
    )
    metadata = JSONField(
        verbose_name='extra',
        help_text='This field changes according to the type of action',
        default=dict,
        blank=True,
    )

    def expire(self):
        self.status = str(PendingActionStatus.EXPIRED)
        self.save(update_fields=['expires_at', 'status'])

    def complete(self):
        self.status = str(PendingActionStatus.COMPLETED)
        self.save(update_fields=['expires_at', 'status'])

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'pending_actions'
        verbose_name = 'Pending Action'
        verbose_name_plural = 'Pending Actions'
