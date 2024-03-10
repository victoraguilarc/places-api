from dataclasses import dataclass
from typing import List, Optional, Type, Union
from uuid import UUID

from django.http import QueryDict

from src.common.domain import BaseEnum


def camelize_string(value: str) -> str:
    if not value:
        return value
    value = ''.join(word.title() for word in value.split('_'))
    return value[:1].lower() + value[1:]


@dataclass
class QueryParams(object):
    params: QueryDict

    def get(self, key, default=None):
        return self.params.get(key, default) or self.params.get(camelize_string(key), default)

    def get_str(self, key, default=None):
        try:
            return self._get_or_none(key, str, default)
        except (ValueError, TypeError):
            return None

    def get_int(self, key, default=None):
        try:
            return self._get_or_none(key, int, default)
        except (ValueError, TypeError):
            return None

    def get_float(self, key, default=None):
        try:
            return self._get_or_none(key, float, default)
        except (ValueError, TypeError):
            return None

    def get_bool(self, key, default=False):
        try:
            value = self.get(key, default)
            if isinstance(value, bool):
                return value
            elif isinstance(value, str):
                return value in ['true', 'True', 'TRUE', '1', 'active']
            elif value is None:
                return None
            return False
        except (ValueError, TypeError):
            return None

    def get_uuid(self, key, default=None):
        try:
            return self._get_or_none(key, UUID, default)
        except (ValueError, TypeError):
            return None

    def get_list(self, key, default=None):
        default = default or []
        try:
            return self.params.getlist(key) or self.params.getlist(camelize_string(key)) or default
        except (ValueError, TypeError):
            return None

    def get_enum(
        self,
        key: str,
        enum_class: Type[BaseEnum],
        default: BaseEnum = None,
    ) -> Optional[BaseEnum]:
        try:
            str_value = self.get_str(key) or default
            return enum_class.from_value(str_value) if str_value else None
        except (ValueError, TypeError):
            return None

    def get_enum_list(
        self,
        key: str,
        enum_class: Type[BaseEnum],
        default: BaseEnum = None,
    ) -> List:
        str_value = self.get_str(key) or default
        if not str_value:
            return []
        converted_enum_list = []
        str_enum_items = str_value.split(',')
        for str_enum_item in str_enum_items:
            enum_value = enum_class.from_value(value=str_enum_item)
            if not enum_value:
                continue
            converted_enum_list.append(enum_value)
        return converted_enum_list

    def _get_or_none(
        self,
        key: str,
        cast_type: Type[Union[str, int, float, bool, UUID]],
        default=None,
    ) -> Optional[Union[str, int, float, bool, UUID]]:
        item_value = self.get(key, default)
        return cast_type(item_value) if item_value else default
