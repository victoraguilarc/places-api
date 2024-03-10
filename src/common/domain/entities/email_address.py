import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.common.domain.interfaces.entities import AggregateRoot
from src.common.domain.value_objects import EmailAddressId


@dataclass
class EmailAddress(AggregateRoot):
    id: EmailAddressId
    email: str
    is_verified: Optional[bool] = False
    created_at: Optional[datetime] = None

    @property
    def to_persist_dict(self):
        return {
            'is_verified': self.is_verified,
        }

    @property
    def to_minimal_dict(self):
        return {
            'email': self.email,
            'is_verified': self.is_verified,
        }

    @property
    def to_dict(self):
        return {
            'id': str(self.id),
            **self.to_minimal_dict,
        }

    @property
    def verification_metadata(self) -> dict:
        if self.is_verified:
            return {}
        return {'email_address': self.to_dict}

    @classmethod
    def from_dict(cls, data: dict) -> 'EmailAddress':
        return cls(
            id=EmailAddressId(data.get('id', uuid.uuid4())),
            email=data.get('email'),
            is_verified=bool(data.get('is_verified', False)),
        )
