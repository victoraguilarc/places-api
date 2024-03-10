# -*- coding: utf-8 -*-

from faker import Factory
from faker.providers import credit_card, internet, lorem, misc, person, phone_number, profile


def instance_faker():
    faker = Factory.create()
    faker.add_provider(person)
    faker.add_provider(profile)
    faker.add_provider(lorem)
    faker.add_provider(misc)
    faker.add_provider(internet)
    faker.add_provider(credit_card)
    faker.add_provider(phone_number)

    return faker
