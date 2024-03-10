from django.core.exceptions import DisallowedHost
from django.http import JsonResponse
from django.shortcuts import redirect


class DeactivatedDisallowedHost:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        try:
            request.get_host()
        except DisallowedHost:
            return JsonResponse(
                data={'code': 'common.DisallowedHost', 'message': 'Host is not allowed'},
                status=400,
            )
        return self.get_response(request)
