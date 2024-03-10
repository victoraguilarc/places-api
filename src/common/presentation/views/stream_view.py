from typing import Optional

from django.http import HttpRequest, JsonResponse
from django.utils import translation
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from src.common.domain.context.domain import DomainContext
from src.common.domain.context.locale import LocaleContext
from src.common.domain.enums.locales import Language, TimeZone
from src.common.domain.exceptions.common import DomainException
from src.common.infrastructure.context_builder import AppContextBuilder
from src.common.infrastructure.django_locales import DjangoLocaleService
from src.common.presentation.api.exceptions.collection import get_error_code
from src.common.presentation.constants import HTTP_CLIENT_HEADER
from src.common.presentation.parsers import ConsumerClient


class StreamView(View):
    domain_context: DomainContext
    locale_context: Optional[LocaleContext] = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        try:
            self._setup_contexts(request)
            return super().dispatch(request, *args, **kwargs)
        except (Exception, DomainException) as exc:
            parsed_exception = get_error_code(exc.__class__)
            return JsonResponse(
                {'errors': [parsed_exception.to_dict], 'validation': None},
                status=parsed_exception.status_code,
            )

    def _setup_contexts(self, http_request: HttpRequest):
        app_context = AppContextBuilder.from_env()
        self.domain_context = app_context.domain
        self.locale_context = LocaleContext(
            client=ConsumerClient.build(http_request.headers.get(HTTP_CLIENT_HEADER, '')),
            time_zone=TimeZone.UTC,
            language=Language.from_value(translation.get_language()),
            locale_service=DjangoLocaleService(),
        )

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
