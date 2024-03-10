# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from src.common.helpers.time import TimeUtils


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5000
    page_size_query_param = 'page_size'
    max_page_size = 20000


class StandarPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data, http_status: int = status.HTTP_200_OK):
        return Response(
            {
                'pagination': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link(),
                    'count': self.page.paginator.count,
                },
                'data': data,
                'datetime': TimeUtils.utc_now(),
            },
            http_status,
        )
