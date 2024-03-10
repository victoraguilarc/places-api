# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.application.sessions.use_cases.mixins import SessionBuilderMixin
from src.auth.domain import SessionTokenBuilder
from src.auth.domain.exceptions import InvalidCredentials
from src.auth.domain.repositories.session import SessionRepository
from src.common.domain.entities.user import User
from src.common.domain.entities.user_session import UserSession
from src.common.domain.interfaces.services import Service
from src.common.domain.messaging.queries import QueryBus


@dataclass
class LoginSessionBuilder(SessionBuilderMixin, Service):
    email: str
    password: str
    session_repository: SessionRepository
    token_builder: SessionTokenBuilder
    query_bus: QueryBus
    path_hostname: str

    def execute(self, *args, **kwargs) -> UserSession:
        user = self._fin_user_by_email()

        has_valid_password = self.session_repository.has_valid_password(
            user=user,
            password=self.password,
        )

        if not has_valid_password:
            raise InvalidCredentials

        return UserSession(
            profile=user,
            token=self.token_builder.make_token(user),
        )

    def _fin_user_by_email(self) -> User:
        user = self.session_repository.find_by_email(self.email)
        if not user:
            raise InvalidCredentials
        return user
    
