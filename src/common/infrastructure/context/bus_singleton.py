# -*- coding: utf-8 -*-

from src.common.domain.context.bus import BusContext
from src.common.helpers.singlenton import SingletonMeta
from src.common.infrastructure.messaging import MemoryCommandBus, MemoryEventBus, MemoryQueryBus


class BusSingleton(metaclass=SingletonMeta):
    instance: BusContext = BusContext(
        command_bus=MemoryCommandBus(),
        query_bus=MemoryQueryBus(),
        event_bus=MemoryEventBus(),
    )
