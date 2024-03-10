# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from src.common.domain.enums.locales import Language, TimeZone
from src.common.domain.interfaces.locales import LocaleService
from src.common.presentation.parsers import ConsumerClient


@dataclass
class LocaleContext(object):
    time_zone: TimeZone
    language: Language
    locale_service: Optional[LocaleService] = None
    client: Optional[ConsumerClient] = None

