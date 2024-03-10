from abc import ABC, abstractmethod

from src.common.domain.entities.user import User
from src.common.domain.value_objects import SessionToken


class SessionTokenBuilder(ABC):
    @abstractmethod
    def make_token(self, user: User) -> SessionToken:
        raise NotImplementedError
