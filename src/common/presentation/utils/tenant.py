# -*- coding: utf-8 -*-

from rest_framework.request import Request


def hostname_from_request(request: Request):
    # split on `:` to remove port
    return request.META.get('HTTP_HOST')
