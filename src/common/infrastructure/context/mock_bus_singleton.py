# -*- coding: utf-8 -*-

from unittest.mock import MagicMock

from src.common.domain.context.bus import BusContext
from src.common.helpers.singlenton import SingletonMeta


class MockBusSingleton(metaclass=SingletonMeta):
    instance: BusContext = MagicMock()
