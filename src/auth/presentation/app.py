# -*- coding: utf-8 -*-

from django.apps import AppConfig


class AuthConfig(AppConfig):
    """Configuration for auth and registering."""

    name = 'src.auth'
    label = 'authentication'
    verbose_name = 'Auth'
    verbose_name_plural = 'Auth'

    def ready(self):
        from src.auth.infrastructure.bus_wiring import wire_handlers

        wire_handlers()
