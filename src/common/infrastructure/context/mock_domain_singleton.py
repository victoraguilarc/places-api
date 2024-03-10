# -*- coding: utf-8 -*-

from unittest.mock import MagicMock

from src.common.domain.context.domain import DomainContext
from src.common.helpers.singlenton import SingletonMeta


class MockDomainSingleton(metaclass=SingletonMeta):
    instance: DomainContext = MagicMock()
