# -*- coding: utf-8 -*-
import uuid
from dataclasses import dataclass

from src.common.domain.value_objects import PhoneNumberId, RawPhoneNumber


@dataclass
class PhoneNumber(RawPhoneNumber):
    id: PhoneNumberId
    is_verified: bool

    @property
    def to_raw_phone_number(self) -> RawPhoneNumber:
        return RawPhoneNumber(
            iso_code=self.iso_code,
            dial_code=self.dial_code,
            phone_number=self.phone_number,
            prefix=self.prefix,
        )

    @property
    def display_phone(self) -> str:
        return super().display_phone

    @property
    def international_number(self) -> str:
        return super().international_number

    @property
    def to_minimal_dict(self) -> dict:
        return {
            'dial_code': self.dial_code,
            'phone_number': self.phone_number,
            'prefix': self.prefix,
            'is_verified': self.is_verified,
        }

    @property
    def to_dict(self) -> dict:
        return {
            **super().to_dict,
            'is_verified': self.is_verified,
        }

    @property
    def to_raw_persist_dict(self) -> dict:
        return {
            'iso_code': str(self.iso_code),
            'prefix': self.prefix,
        }

    @property
    def to_persist_dict(self) -> dict:
        return {
            'iso_code': str(self.iso_code),
            'is_verified': self.is_verified,
            'prefix': self.prefix,
        }

    @property
    def verification_metadata(self) -> dict:
        if self.is_verified:
            return {}
        return {'phone_number': self.to_dict}

    def load_raw_phone_number(self, raw_phone_number: RawPhoneNumber):
        self.iso_code = raw_phone_number.iso_code
        self.dial_code = raw_phone_number.dial_code
        self.phone_number = raw_phone_number.phone_number
        self.prefix = raw_phone_number.prefix

    @classmethod
    def from_dict(cls, verified_data: dict) -> 'PhoneNumber':

        return cls(
            id=PhoneNumberId(verified_data.get('id', uuid.uuid4())),
            iso_code=verified_data['iso_code'],
            dial_code=verified_data['dial_code'],
            phone_number=verified_data.get('phone_number'),
            is_verified=verified_data.get('is_verified', False),
            prefix=verified_data.get('prefix'),
        )
