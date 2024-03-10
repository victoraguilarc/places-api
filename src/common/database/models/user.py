# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models

from src.common.database.models.mixins.common import UUIDTimestampMixin
from src.common.database.models.mixins.users import AbstractUser, AuthMixin
from src.common.helpers.string import alias_generator

REQUIRED_FIELDS = getattr(settings, 'PROFILE_REQUIRED_FIELDS', ['email'])


def user_photos_folder(instance, filename):
    return '/'.join(['users', filename])


class UserORM(UUIDTimestampMixin, AuthMixin, AbstractUser):
    """Represents the user of the platform."""

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = alias_generator()
        super().save(*args, **kwargs)

    def change_password(self, new_password):
        self.set_password(new_password)
        self.save()

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        constraints = (
            models.UniqueConstraint(
                fields=('email_address',),
                name='unique_user_email_address',
            ),
            models.UniqueConstraint(
                fields=('phone_number',),
                name='unique_user_phone_number',
            ),
        )
