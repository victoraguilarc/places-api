# -*- coding: utf-8 -*-

import random

import pytest

from src.common.domain.enums.users import PendingActionCategory


@pytest.fixture
def test_pending_action_category():
    return random.choice([PendingActionCategory.VERIFY_EMAIL, PendingActionCategory.RESET_PASSWORD])
