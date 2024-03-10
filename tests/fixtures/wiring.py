from unittest.mock import create_autospec

import pytest

from src.common.domain.messaging.commands import CommandBus
from src.common.domain.messaging.queries import QueryBus


@pytest.fixture
def query_bus_mock() -> QueryBus:
    return create_autospec(spec=QueryBus)


@pytest.fixture
def command_bus_mock() -> CommandBus:
    return create_autospec(spec=CommandBus)
