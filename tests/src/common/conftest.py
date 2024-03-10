# -*- coding: utf-8 -*-

import secrets

import pytest

from src.common.domain.enums.users import PendingActionCategory


@pytest.fixture
def test_pending_action_category():
    return secrets.choice(
        [PendingActionCategory.VERIFY_EMAIL, PendingActionCategory.RESET_PASSWORD]
    )
