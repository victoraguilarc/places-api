from abc import ABC, abstractmethod

from src.auth.domain.value_objects import SessionToken
from src.common.domain.entities.user import User


class SessionTokenBuilder(ABC):
    @abstractmethod
    def make_token(self, user: User) -> SessionToken:
        raise NotImplementedError
