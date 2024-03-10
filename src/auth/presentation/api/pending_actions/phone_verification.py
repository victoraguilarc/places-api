# -*- coding: utf-8 -*-

from rest_framework.response import Response

from src.auth.application.pending_actions.use_cases.performers.phone_verification import (
    PhoneVerificationPerformer,
)
from src.auth.presentation.validators.pending_action import PendingActionTokenValidator
from src.common.application.responses.generics import ResultResponse
from src.common.presentation.api.domain_api import DomainAPIView


class PerformPhoneVerificationView(DomainAPIView):
    def post(self, request):
        validator = PendingActionTokenValidator(data=request.data)
        validator.is_valid(raise_exception=True)

        PhoneVerificationPerformer(
            token=validator.validated_data.get('token'),
            action_repository=self.domain_context.pending_action_repository,
            stream_events_publisher=self.domain_context.stream_events_publisher,
            command_bus=self.bus_context.command_bus,
        ).execute()

        response = ResultResponse()
        return Response(response.render(self.locale_context))
