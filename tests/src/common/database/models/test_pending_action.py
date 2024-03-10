# -*- coding: utf-8 -*-

import pytest

from src.common.database.models import PendingActionORM
from src.common.database.models.factories.pending_action import PendingActionORMFactory


@pytest.mark.django_db
def test_string_representation():
    pending_action = PendingActionORMFactory()
    assert str(pending_action) == pending_action.token


def test_verbose_name():
    assert str(PendingActionORM._meta.verbose_name) == 'Pending Action'


def test_verbose_name_plural():
    assert str(PendingActionORM._meta.verbose_name_plural) == 'Pending Actions'
