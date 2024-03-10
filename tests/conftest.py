import pytest

from src.common.presentation.utils.testing.faker import instance_faker


@pytest.fixture()
def faker():
    return instance_faker()
