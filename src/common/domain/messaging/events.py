# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Type
from uuid import UUID


@dataclass
class DomainEvent(ABC):
    id: UUID
    timestamp: datetime
    args: Optional[tuple] = None


class DomainEventHandler(ABC):
    @abstractmethod
    def execute(self, event: DomainEvent):
        raise NotImplementedError


class EventBus(ABC):
    @abstractmethod
    def subscribe(self, event: Type[DomainEvent], handler: DomainEventHandler):
        raise NotImplementedError

    @abstractmethod
    def publish_batch(self, event: List[DomainEvent]):
        raise NotImplementedError

    @abstractmethod
    def publish(self, events: List[DomainEvent]):
        raise NotImplementedError
