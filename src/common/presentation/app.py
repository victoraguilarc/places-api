# -*- coding: utf-8 -*-

from django.apps import AppConfig


class CommonConfig(AppConfig):
    """Configuration for project utilities."""

    name = 'src.common'
    verbose_name = 'Common'

    def ready(self):
        pass
