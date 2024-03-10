# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CallbackData(ABC):
    hostname: str

    @abstractmethod
    def apply_token(self, token: str) -> str:
        raise NotImplementedError
