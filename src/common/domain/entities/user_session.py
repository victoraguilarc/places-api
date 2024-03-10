from dataclasses import dataclass

from src.auth.domain import SessionToken
from src.common.domain.entities.user import User
from src.common.domain.interfaces.entities import AggregateRoot


@dataclass
class UserSession(AggregateRoot):
    profile: User
    token: SessionToken
