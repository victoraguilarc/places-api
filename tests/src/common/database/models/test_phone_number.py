# -*- coding: utf-8 -*-

import pytest

from src.common.database.models import PhoneNumberORM
from src.common.database.models.factories.phone_number import PhoneNumberORMFactory


@pytest.mark.django_db
def test_string_representation():
    instance = PhoneNumberORMFactory()
    assert str(instance) == f'+{instance.dial_code}{instance.phone_number}'


def test_verbose_name():
    assert str(PhoneNumberORM._meta.verbose_name) == 'Phone Number'


def test_verbose_name_plural():
    assert str(PhoneNumberORM._meta.verbose_name_plural) == 'Phone Numbers'
