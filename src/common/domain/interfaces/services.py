# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from src.common.domain.interfaces.responses import ApiResponse


class Service(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError


class ApiService(Service):
    @abstractmethod
    def execute(self, *args, **kwargs) -> ApiResponse:
        raise NotImplementedError
