# -*- coding: utf-8 -*-

from enum import Enum
from typing import Optional, Union


class BaseEnum(Enum):
    """Provides the common functionalties to multiple model choices."""

    @classmethod
    def get_members(cls):
        return [tag for tag in cls if type(tag.value) in [int, str, float]]

    @classmethod
    def choices(cls):
        """Generate choice options for models."""
        return [
            (option.value, option.value)
            for option in cls
            if type(option.value) in [int, str, float]
        ]

    @classmethod
    def values(cls):
        """Returns values from choices."""
        return [option.value for option in cls]

    def __str__(self):  # noqa: D105
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def as_list(cls):
        """Returns properties as a list."""
        return [
            value
            for key, value in cls.__dict__.items()
            if isinstance(value, str) and not key.startswith('__')
        ]

    @classmethod
    def from_value(cls, value: Union[str, int]) -> Optional['BaseEnum']:
        for tag in cls:
            if isinstance(tag.value, str) and str(tag.value).upper() == str(value).upper():
                return tag
            elif not isinstance(tag.value, str) and tag.value == value:
                return tag
        return None
