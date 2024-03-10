# -*- coding: utf-8 -*-
import logging

from django.core.management.base import BaseCommand

from src.common.database.models import UserORM


class Command(BaseCommand):
    """Creates a superuser."""

    help = 'Touch a superuser!'  # noqa: WPS125

    def handle(self, *args, **options):
        """Creates a superuser admin."""
        user_orm, created = UserORM.objects.get_or_create(
            username='admin',
            defaults={
                'is_superuser': True,
                'is_staff': True,
            },
        )
        if not created:
            return

        user_orm.set_password('12345678x')
        user_orm.save()

        logging.info('Superuser created!')
