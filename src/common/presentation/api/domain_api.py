# -*- coding: utf-8 -*-

from typing import Optional

from django.utils import translation

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request

from src.common.domain.context.bus import BusContext
from src.common.domain.context.domain import DomainContext
from src.common.domain.context.locale import LocaleContext
from src.common.domain.entities.user import User
from src.common.domain.enums.locales import Language, TimeZone
from src.common.helpers.requests import get_user_from_request
from src.common.infrastructure.context_builder import AppContextBuilder
from src.common.infrastructure.django_locales import DjangoLocaleService
from src.common.presentation.api.pagination import StandarPagination
from src.common.presentation.api.renderers import StandarJSONRenderer
from src.common.presentation.constants import HTTP_CLIENT_HEADER
from src.common.presentation.parsers import ConsumerClient


class DomainAPIView(GenericAPIView):
    domain_context: DomainContext = None
    bus_context: BusContext = None
    locale_context: Optional[LocaleContext] = None

    user: Optional[User] = None

    format_kwarg = None

    pagination_class = StandarPagination
    renderer_classes = (StandarJSONRenderer,)

    def initial(self, request, *args, **kwargs):
        self.format_kwarg = self.get_format_suffix(**kwargs)

        # Perform content negotiation and store the accepted info on the request
        neg = self.perform_content_negotiation(request)
        request.accepted_renderer, request.accepted_media_type = neg

        # Determine the API version, if versioning is in use.
        version, scheme = self.determine_version(request, *args, **kwargs)
        request.version, request.versioning_scheme = version, scheme

        # Ensure that the incoming request is permitted
        self.perform_authentication(request)
        self.setup_user(request)
        self.check_authentication(request)
        self.check_permissions(request)
        self.check_throttles(request)
        self.setup_contexts(request)

    def check_authentication(self, request):
        return

    def render_paginated_response(self, request, items, displayer_class):
        report_items = self.paginator.paginate_queryset(items, request)
        return self.paginator.get_paginated_response(
            displayer_class(report_items, many=True).data,
        )

    def setup_contexts(
        self,
        request: Request,
    ):
        app_context = AppContextBuilder.from_env()

        self.domain_context = app_context.domain
        self.bus_context = app_context.bus
        self.locale_context = LocaleContext(
            client=ConsumerClient.build(request.META.get(HTTP_CLIENT_HEADER, '')),
            time_zone=TimeZone.UTC,
            language=Language.from_value(translation.get_language()),
            locale_service=DjangoLocaleService(),
        )

    def setup_user(self, request):
        self.user = get_user_from_request(request)

    def initialize_request(self, request, *args, **kwargs):
        request: Request = super().initialize_request(request, *args, **kwargs)
        # Add some loggers here
        return request
