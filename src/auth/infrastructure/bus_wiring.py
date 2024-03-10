from src.auth.application.pending_actions.handlers.get_email_verification import GetEmailVerificationHandler
from src.auth.application.pending_actions.handlers.get_phone_verification import GetPhoneNumberVerificationHandler
from src.common.application.queries.auth import (
    GetPhoneVerificationQuery,
    GetEmailVerificationQuery,
)
from src.common.infrastructure.context_builder import AppContextBuilder


def wire_handlers():
    app_context = AppContextBuilder.from_env()
    domain_context, bus = app_context.domain, app_context.bus

    #  Q U E R I E S
    bus.query_bus.subscribe(
        query=GetEmailVerificationQuery,
        handler=GetEmailVerificationHandler(
            action_repository=domain_context.pending_action_repository,
            sesion_repository=domain_context.session_repository,
        ),
    )
    bus.query_bus.subscribe(
        query=GetPhoneVerificationQuery,
        handler=GetPhoneNumberVerificationHandler(
            action_repository=domain_context.pending_action_repository,
            sesion_repository=domain_context.session_repository,
        ),
    )
