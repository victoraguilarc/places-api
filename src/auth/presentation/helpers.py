# -*- coding: utf-8 -*-

from typing import Optional

from config.settings.components.common import BACKEND_HOSTNAME
from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.auth.infrastructure.builders.callback_url import (
    DjangoCallbackData,
    SimpleCallbackData,
)


def get_token_path_builder(
    hostname: Optional[str] = None,
    view_name: Optional[str] = None,
) -> CallbackData:
    if hostname and not view_name:
        return SimpleCallbackData(hostname=hostname)
    if view_name:
        return DjangoCallbackData(BACKEND_HOSTNAME, view_name)
    return SimpleCallbackData('/')
