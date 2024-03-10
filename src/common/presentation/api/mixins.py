from typing import List

from rest_framework.pagination import BasePagination
from rest_framework.request import Request


class PaginationMixin(object):
    paginator: BasePagination

    def paginated_response(self, request: Request, rendered_items: List):
        paginated_items = self.paginator.paginate_queryset(
            rendered_items,
            request,
        )
        return self.paginator.get_paginated_response(paginated_items)
