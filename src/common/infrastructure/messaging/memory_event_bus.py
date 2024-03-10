# -*- coding: utf-8 -*-

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Type

from src.common.domain.messaging.events import DomainEvent, DomainEventHandler, EventBus
from src.common.infrastructure.messaging._exceptions import EventHandlerDoesNotExistException


@dataclass
class MemoryEventBus(EventBus):
    def __init__(self):
        self._events: Dict[Type[DomainEvent], List[DomainEventHandler]] = defaultdict(list)

    def subscribe(self, event: Type[DomainEvent], handler: DomainEventHandler):
        self._events[event].append(handler)

    def publish_batch(self, events: List[DomainEvent]):
        for event in events:
            self.publish(event)

    def publish(self, event: DomainEvent):
        if event.__class__ not in self._events:
            raise EventHandlerDoesNotExistException

        for event_handler in self._events[event.__class__]:
            event_handler.execute(event)
