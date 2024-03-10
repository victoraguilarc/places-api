# -*- coding: utf-8 -*-

from django.db import models

from src.common.database.models.mixins.common import UUIDTimestampMixin


class EmailAddressORM(UUIDTimestampMixin):
    email = models.EmailField(
        verbose_name='Email',
        db_index=True,
        unique=True,
    )
    is_verified = models.BooleanField(
        verbose_name='Verified',
        default=False,
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'email_addresses'
        verbose_name = 'Email Address'
        verbose_name_plural = 'Email Addresses'
