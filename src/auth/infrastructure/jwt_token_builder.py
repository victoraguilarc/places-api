# -*- coding: utf-8 -*-

from rest_framework_simplejwt.tokens import RefreshToken

from src.auth.domain import SessionToken, SessionTokenBuilder
from src.common.domain.entities.user import User


class JWTSessionTokenBuilder(SessionTokenBuilder):
    def make_token(self, user: User) -> SessionToken:
        refresh = RefreshToken.for_user(user)
        return SessionToken(
            {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }
        )
