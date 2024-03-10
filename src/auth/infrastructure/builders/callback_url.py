# -*- coding: utf-8 -*-

from dataclasses import dataclass

from django.urls import reverse

from src.auth.domain.interfaces.token_path_finder import CallbackData


@dataclass
class DjangoCallbackData(CallbackData):
    name: str

    def apply_token(self, token: str) -> str:
        return '{hostname}{path}'.format(
            hostname=self.hostname,
            path=reverse(self.name, kwargs={'token': token}),
        )


@dataclass
class SimpleCallbackData(CallbackData):
    hostname: str

    def apply_token(self, token: str) -> str:
        return f'{self.hostname}/{token}'


@dataclass
class QueryParamsCallbackData(CallbackData):
    hostname: str

    def apply_token(self, token: str) -> str:
        return f'{self.hostname}?token={token}'
