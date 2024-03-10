# -*- coding: utf-8 -*-

import factory
from factory import fuzzy

from src.common.database.models import PendingActionORM
from src.common.database.models.factories.user import UserORMFactory
from src.common.domain.enums.users import PendingActionCategory
from src.common.presentation.utils import dates
from src.common.presentation.utils.testing.faker import instance_faker

faker = instance_faker()


def now_after_three():
    return dates.ago(days=3)


class PendingActionORMFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserORMFactory)
    category = fuzzy.FuzzyChoice(choices=PendingActionCategory.choices())
    expires_at = factory.LazyFunction(now_after_three)
    token = factory.LazyFunction(faker.uuid4)

    class Meta:
        model = PendingActionORM
