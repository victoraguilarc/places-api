# -*- coding: utf-8 -*-

import factory

from src.common.database.models import EmailAddressORM
from src.common.presentation.utils.testing.faker import instance_faker

faker = instance_faker()


class EmailAddressORMFactory(factory.django.DjangoModelFactory):
    email = factory.LazyFunction(faker.email)
    is_verified = True

    class Meta:
        model = EmailAddressORM
