# -*- coding: utf-8 -*-
from datetime import date
from decimal import Decimal

import pytest
from expects import be_a, equal, expect, have_keys

from src.places.domain.entities.day_forecast import DayForecast


@pytest.fixture
def instance() -> DayForecast:
    return DayForecast(
        day=date(2024, 6, 1),
        weather='sunny',
        max=Decimal(30),
        min=Decimal(20),
    )


def test_to_dict(
    instance: DayForecast,
):
    result = instance.to_dict

    expect(result).to(be_a(dict))
    expect(result).to(
        have_keys(
            {
                'day': '2024-06-01',
                'max': '30',
                'min': '20',
                'weather': 'sunny',
            }
        )
    )


def test_from_dict(
    instance: DayForecast,
):
    instance_dict = instance.to_dict

    result_instance = DayForecast.from_dict(instance_dict)

    expect(result_instance).to(be_a(DayForecast))
    expect(result_instance).to(equal(instance))
