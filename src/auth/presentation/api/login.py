# -*- coding: utf-8 -*-

from django.conf import settings

from rest_framework.request import Request
from rest_framework.response import Response

from src.auth.application.sessions.responses import UserSessionResponse
from src.auth.application.sessions.use_cases.session_builder import LoginSessionBuilder
from src.auth.infrastructure.jwt_token_builder import JWTSessionTokenBuilder
from src.auth.presentation.validators.login import LoginValidator
from src.common.presentation.api.domain_api import DomainAPIView


class LoginView(DomainAPIView):
    def post(self, request: Request):
        validator = LoginValidator(
            data=request.data,
            context={'request': request},
        )
        validator.is_valid(raise_exception=True)

        session = LoginSessionBuilder(
            email=validator.validated_data.get('email'),
            password=validator.validated_data.get('password'),
            session_repository=self.domain_context.session_repository,
            token_builder=JWTSessionTokenBuilder(),
            query_bus=self.bus_context.query_bus,
            path_hostname=settings.FRONTEND_HOSTNAME,
        ).execute()

        response = UserSessionResponse(session)
        return Response(
            response.render(self.locale_context),
        )
