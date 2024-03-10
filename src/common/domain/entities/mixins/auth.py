from dataclasses import dataclass
from typing import Optional

from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.phone_number import PhoneNumber


@dataclass
class DomainAuthMixin(object):
    phone_number: Optional[PhoneNumber]
    email_address: Optional[EmailAddress]
