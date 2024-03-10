# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.common.domain.messaging.commands import Command


@dataclass
class TaskScheduler(ABC):
    @abstractmethod
    def enqueue(self, command: Command):
        raise NotImplementedError
