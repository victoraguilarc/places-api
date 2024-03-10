from django.views import View

from src.common.domain.context.domain import DomainContext
from src.common.infrastructure.context_builder import AppContextBuilder


class TransactionView(View):
    domain_context: DomainContext

    def setup(self, request, *args, **kwargs):
        app_context = AppContextBuilder.from_env()
        self.domain_context = app_context.domain
        super().setup(request, *args, **kwargs)
