# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from datetime import datetime

from src.common.domain.enums.locales import Language


class LocaleService(ABC):
    @abstractmethod
    def get(self, label: str, language: Language) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_natural_time(self, date_time: datetime) -> str:
        raise NotImplementedError


class TimeFormatter(ABC):
    @abstractmethod
    def to_natural_time(self, input_datetime: datetime) -> str:
        raise NotImplementedError
