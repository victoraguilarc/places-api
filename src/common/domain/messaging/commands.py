# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Type


class Command(ABC):
    @property
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_dict(cls, kwargs: dict) -> 'Command':
        raise NotImplementedError


@dataclass
class CommandHandler(ABC):
    @abstractmethod
    def execute(self, command: Command):
        raise NotImplementedError


@dataclass
class CommandBus(ABC):
    @abstractmethod
    def subscribe(self, command: Type[Command], handler: CommandHandler):
        raise NotImplementedError

    @abstractmethod
    def dispatch_batch(
        self,
        commands: List[Command],
        is_async: bool = False,
    ):
        raise NotImplementedError

    @abstractmethod
    def dispatch(
        self,
        command: Command,
        run_async: bool = False,
    ):
        raise NotImplementedError
