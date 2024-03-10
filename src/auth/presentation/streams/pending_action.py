# -*- coding: utf-8 -*-

from django.http import HttpResponse, JsonResponse
# from django_grip import set_hold_stream
from djangorestframework_camel_case.util import camelize
from rest_framework import status

from src.auth.application.pending_actions.use_cases.stream_finder import PendingActionStreamFinder
from src.common.presentation.utils.dates import now
from src.common.presentation.views.stream_view import StreamView


class PendingActionStream(StreamView):
    def get(self, request, **kwargs):
        stream_token = kwargs.get('stream_token')

        pending_action = PendingActionStreamFinder(
            stream_token=stream_token,
            repository=self.domain_context.pending_action_repository,
        ).execute()

        if request.grip_proxied:
            # set_hold_stream(request, pending_action.channel_id)
            return HttpResponse(content_type='text/event-stream')

        return JsonResponse(
            data=camelize(
                self._build_response(pending_action.to_tracking_dict),
            ),
        )

    def post(self, request, **kwargs):
        stream_token = kwargs.get('stream_token')

        pending_action = PendingActionStreamFinder(
            stream_token=stream_token,
            repository=self.domain_context.pending_action_repository,
        ).execute()

        return JsonResponse(
            data=camelize(
                self._build_response(pending_action.to_tracking_dict),
            ),
            status=status.HTTP_201_CREATED,
        )

    @classmethod
    def _build_response(cls, data: dict):
        return {
            'data': data,
            'datetime': str(now()),
        }
