from typing import List

from pydantic import BaseModel

from src.common.domain.messaging.events import DomainEvent


class Entity(BaseModel):
    pass


class AggregateRoot(object):
    domain_events: List[DomainEvent] = []

    def pull_domain_events(self) -> List[DomainEvent]:
        domain_events = self.domain_events
        self.domain_events = []
        return domain_events

    def record(self, domain_event: DomainEvent) -> None:
        self.domain_events.append(domain_event)
