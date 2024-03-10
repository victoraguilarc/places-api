# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.common.domain.messaging.commands import CommandBus
from src.common.domain.messaging.events import EventBus
from src.common.domain.messaging.queries import QueryBus


@dataclass
class BusContext(object):
    command_bus: CommandBus
    query_bus: QueryBus
    event_bus: EventBus
