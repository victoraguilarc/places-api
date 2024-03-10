# -*- coding: utf-8 -*-

from rest_framework.response import Response

from config.settings.components.common import BACKEND_HOSTNAME
from src.auth.application.reset_password.use_cases.performer import ResetPasswordPerformer
from src.auth.application.reset_password.use_cases.requester import ResetPasswordRequester
from src.auth.infrastructure.builders.callback_url import (
    DjangoCallbackData,
    QueryParamsCallbackData,
)
from src.auth.presentation.validators.reset_password import (
    ResetPasswordPerformValidator,
    ResetPasswordRequestValidator,
)
from src.common.presentation.api.domain_api import DomainAPIView


class ResetPasswordRequestView(DomainAPIView):
    def post(self, request):
        """Request a password reset."""

        validator = ResetPasswordRequestValidator(data=request.data)
        validator.is_valid(raise_exception=True)

        app_service = ResetPasswordRequester(
            user_email=validator.validated_data.get('email'),
            session_user_repository=self.domain_context.session_user_repository,
            action_repository=self.domain_context.pending_action_repository,
            command_bus=self.bus_context.command_bus,
            token_path_finder=(
                QueryParamsCallbackData(hostname=validator.validated_data.get('next'))
                if validator.validated_data.get('next')
                else DjangoCallbackData(BACKEND_HOSTNAME, 'auth:reset-password')
            ),
        )

        response = app_service.execute()
        return Response(response.render(self.locale_context))


class ResetPasswordPerformView(DomainAPIView):
    def post(self, request):
        """Request a password reset."""

        validator = ResetPasswordPerformValidator(data=request.data)
        validator.is_valid(raise_exception=True)

        app_service = ResetPasswordPerformer(
            token=validator.validated_data.get('token'),
            raw_password=validator.validated_data.get('password'),
            sesson_user_repository=self.domain_context.session_user_repository,
            action_repository=self.domain_context.pending_action_repository,
        )
        response = app_service.execute()
        return Response(response.render(self.locale_context))
