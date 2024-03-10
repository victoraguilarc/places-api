# -*- coding: utf-8 -*-

import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.mixins.auth import DomainAuthMixin
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.interfaces.entities import AggregateRoot
from src.common.domain.value_objects import UserId


@dataclass
class User(DomainAuthMixin, AggregateRoot):
    id: UserId
    is_active: bool = True
    is_superuser: bool = False
    created_at: Optional[datetime] = None

    @property
    def email(self) -> Optional[str]:
        return self.email_address.email if self.email_address else None

    @property
    def usable_phone_number(self) -> Optional[str]:
        return self.phone_number.international_number if self.phone_number else None

    @property
    def channel_id(self):
        return f'User#{self.id}'

    @property
    def display_phone(self):
        return self.phone_number.display_phone if self.phone_number else '---'

    @property
    def uuid(self):
        # It's `uuid` and not `id` because JWT need it to gen tokens
        return self.id

    @property
    def phone_number_verified(self) -> bool:
        return self.phone_number and self.phone_number.is_verified

    @property
    def is_new(self) -> bool:
        return self.created_at is None

    @property
    def is_email_reachable(self) -> bool:
        return self.email_address and self.email_address.is_verified

    @property
    def is_phone_number_reachable(self) -> bool:
        return self.phone_number and self.phone_number_verified

    @property
    def to_persist_dict(self) -> dict:
        data = {
            'is_active': self.is_active,
        }
        if self.phone_number:
            data['phone_number_id'] = self.phone_number.id
        if self.email_address:
            data['email_address_id'] = self.email_address.id
        return data

    @classmethod
    def from_payload(
        cls,
        verified_data: dict,
        email_address: Optional[EmailAddress] = None,
        phone_number: Optional[PhoneNumber] = None,
    ) -> 'User':
        return cls(
            id=UserId(verified_data.get('id', uuid.uuid4())),
            email_address=email_address,
            phone_number=phone_number,
            is_active=verified_data.get('is_active', True),
            created_at=None,
        )

    @classmethod
    def get_overload_properties(cls) -> List[str]:
        return [
            'email_address',
            'phone_number',
            'current_tenant_id',
        ]

    def overload(
        self,
        new_instance: 'User',
        properties: List[str] = None,
    ):
        instance_properties = properties or self.get_overload_properties()
        for _property in instance_properties:
            if not hasattr(self, _property):
                continue
            property_value = getattr(new_instance, _property)
            setattr(self, _property, property_value)
        return self

    @classmethod
    def empty(cls) -> 'User':
        return cls(
            id=UserId(uuid.uuid4()),
            email_address=None,
            phone_number=None,
            is_active=False,
            created_at=None,
        )
