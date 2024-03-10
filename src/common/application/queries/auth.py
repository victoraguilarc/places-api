from dataclasses import dataclass
from typing import Optional

from src.auth.domain.interfaces.token_path_finder import CallbackData
from src.common.domain.entities.user import User
from src.common.domain.messaging.queries import Query
from src.common.domain.value_objects import EmailAddressId


@dataclass
class GetEmailVerificationQuery(Query):
    user: User
    email_address_id: EmailAddressId
    callback_url: CallbackData


@dataclass
class GetPhoneVerificationQuery(Query):
    user: User
    callback_url: CallbackData
    metadata: Optional[dict] = None
