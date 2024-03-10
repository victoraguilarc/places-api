# -*- coding: utf-8 -*-

from django.db import models

from src.common.database.models.mixins.common import UUIDTimestampMixin
from src.common.domain.enums.locales import CountryIsoCode


class PhoneNumberORM(UUIDTimestampMixin):
    iso_code = models.CharField(
        choices=CountryIsoCode.choices(),
        verbose_name='Iso Code',
        max_length=3,
        blank=True,
        null=True,
    )
    dial_code = models.SmallIntegerField(
        verbose_name='Dial Code',
        db_index=True,
    )
    phone_number = models.CharField(
        verbose_name='Phone Number',
        max_length=255,
        db_index=True,
    )
    prefix = models.CharField(
        verbose_name='Prefix',
        help_text=(
            'This is to solve numbers inconsistency, ' 'specially for Mexican and Brazilian numbers'
        ),
        max_length=2,
        blank=True,
        null=True,
    )
    is_verified = models.BooleanField(
        verbose_name='Is Verified?',
        default=False,
    )

    @property
    def display_phone_number(self):
        return f'+{self.dial_code}{self.phone_number}'

    def __str__(self):
        return self.display_phone_number

    def save(self, **kwargs):
        super().save(**kwargs)

    class Meta:
        db_table = 'phone_numbers'
        unique_together = ('dial_code', 'phone_number')
        verbose_name = 'Phone Number'
        verbose_name_plural = 'Phone Numbers'
