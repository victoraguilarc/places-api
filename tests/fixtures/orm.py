from datetime import datetime

import pytest

from src.common.database.models.factories.user import UserORMFactory

TEST_PASSWORD = 'test_password'


@pytest.fixture
@pytest.mark.django_db
def user_orm():
    user = UserORMFactory()
    user.set_password(TEST_PASSWORD)
    user.save()
    return user


@pytest.fixture(scope='function')
@pytest.mark.django_db
def ocurrence() -> datetime:
    return datetime(year=2024, month=1, day=1)
