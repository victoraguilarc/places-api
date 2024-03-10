# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Union, Any

from src.common.domain.context.locale import LocaleContext


class ApiResponse(ABC):
    @abstractmethod
    def render(self, locale_context: LocaleContext) -> Union[Dict, List, str]:
        raise NotImplementedError


@dataclass
class JSONPresenter(ABC):
    instance: Any

    @property
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError
