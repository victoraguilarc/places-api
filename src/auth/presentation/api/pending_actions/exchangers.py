# -*- coding: utf-8 -*-

from rest_framework.response import Response

from src.auth.application.pending_actions.responses import PendingActionResponse
from src.auth.application.pending_actions.use_cases.action_exchanger import PendingActionExchanger
from src.auth.presentation.validators.pending_action import PendingActionTokenValidator
from src.common.presentation.api.domain_api import DomainAPIView


class ExchangePendingActionView(DomainAPIView):
    def post(self, request):
        validator = PendingActionTokenValidator(data=request.data)
        validator.is_valid(raise_exception=True)

        pending_action = PendingActionExchanger(
            token=validator.validated_data.get('token'),
            action_repository=self.domain_context.pending_action_repository,
        ).execute()

        response = PendingActionResponse(pending_action)
        return Response(response.render(self.locale_context))
