# -*- coding: utf-8 -*-

from django.conf import settings
from rest_framework.response import Response

from src.auth.application.pending_actions.responses import PendingActionResponse
from src.auth.application.sessions.use_cases.user_register import UserRegister
from src.auth.presentation.helpers import get_token_path_builder
from src.auth.presentation.validators.session_user import CreateUserValidator
from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.entities.user import User
from src.common.presentation.api.domain_api import DomainAPIView


class RegisterView(DomainAPIView):
    def post(self, request):
        validator = CreateUserValidator(data=request.data)
        validator.is_valid(raise_exception=True)

        pending_action = UserRegister(
            user_instance=User.from_payload(
                verified_data=validator.validated_data,
                email_address=EmailAddress.from_dict(validator.validated_data),
            ),
            raw_password=validator.validated_data.get('password'),
            session_user_repository=self.domain_context.session_user_repository,
            action_repository=self.domain_context.pending_action_repository,
            command_bus=self.bus_context.command_bus,
            token_path=get_token_path_builder(view_name='auth:verify-email'),
            send_from_email=settings.DEFAULT_FROM_EMAIL,
            send_async_emails=not settings.DEBUG,
        ).execute()

        response = PendingActionResponse(instance=pending_action)
        return Response(
            response.render(self.locale_context),
        )
