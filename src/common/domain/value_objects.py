# -*- coding: utf-8 -*-

import tempfile
from dataclasses import dataclass
from typing import NewType, Union, Optional
from uuid import UUID

from src.common.domain.enums.locales import CountryIsoCode


@dataclass
class RawPhoneNumber:
    iso_code: CountryIsoCode
    dial_code: int
    phone_number: str
    prefix: Optional[str]

    @property
    def display_phone(self) -> str:
        return f'+{self.dial_code}{self.phone_number}'

    @property
    def international_number(self) -> str:
        if self.prefix:
            return f'{self.dial_code}{self.prefix}{self.phone_number}'
        return f'{self.dial_code}{self.phone_number}'

    @property
    def to_dict(self):
        return {
            'iso_code': str(self.iso_code),
            'dial_code': self.dial_code,
            'phone_number': self.phone_number,
            'prefix': self.prefix,
        }

    @classmethod
    def from_dict(cls, instance_data: dict) -> 'RawPhoneNumber':
        return RawPhoneNumber(
            iso_code=CountryIsoCode.from_value(instance_data.get('iso_code')),
            dial_code=int(instance_data.get('dial_code')),
            phone_number=str(instance_data.get('phone_number')),
            prefix=instance_data.get('prefix'),
        )


class Slug(str):
    def validate(self):
        raise NotImplemented


UserId = NewType('UserId', Union[UUID, str])
EmailAddressId = NewType('EmailAddressId', Union[UUID, str])
PhoneNumberId = NewType('PhoneNumberId', Union[UUID, int])
SessionToken = NewType('SessionToken', dict)


class TenantSlug(Slug):
    pass


@dataclass
class RawPicture(object):
    image: tempfile
