# -*- coding: utf-8 -*-

import factory

from src.common.database.models import PhoneNumberORM
from src.common.presentation.utils.testing.faker import instance_faker

faker = instance_faker()


class PhoneNumberORMFactory(factory.django.DjangoModelFactory):
    iso_code = 'MX'
    dial_code = '+52'
    phone_number = factory.LazyFunction(faker.msisdn)
    is_verified = True

    class Meta:
        model = PhoneNumberORM
