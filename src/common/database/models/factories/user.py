# -*- coding: utf-8 -*-

import factory

from src.common.database.models import UserORM
from src.common.database.models.factories.email_address import EmailAddressORMFactory
from src.common.database.models.factories.phone_number import PhoneNumberORMFactory
from src.common.presentation.utils.testing.faker import instance_faker

faker = instance_faker()


def fake_username():
    return faker.simple_profile()['username']


def generate_user_profile():
    user_profile = faker.simple_profile()
    user_password = faker.uuid4()
    full_name = faker.display_name().split(' ')

    return {
        'email': user_profile['mail'],
        'firstName': full_name[0],
        'paternalSurname': full_name[1],
        'password': user_password,
    }


class UserORMFactory(factory.django.DjangoModelFactory):
    username = factory.LazyFunction(fake_username)
    email_address = factory.SubFactory(EmailAddressORMFactory)
    phone_number = factory.SubFactory(PhoneNumberORMFactory)

    class Meta:
        model = UserORM
