from dataclasses import dataclass

from django.conf import settings

from src.common.domain.context.bus import BusContext
from src.common.domain.context.domain import DomainContext
from src.common.domain.enums.config import AppConfigEnv


@dataclass
class AppContext(object):
    domain: DomainContext
    bus: BusContext
    scheduler: None = None


class AppContextBuilder(object):
    @classmethod
    def from_env(cls, env: str = settings.ENV) -> AppContext:
        environment = AppConfigEnv.from_value(env)
        if environment.is_production or environment.is_development:
            from src.common.infrastructure.context.bus_singleton import BusSingleton
            from src.common.infrastructure.context.domain_singleton import DomainSingleton

            return AppContext(
                domain=DomainSingleton.instance,
                bus=BusSingleton.instance,
            )
        elif environment.is_testing:
            from src.common.infrastructure.context.mock_bus_singleton import MockBusSingleton
            from src.common.infrastructure.context.mock_domain_singleton import MockDomainSingleton

            return AppContext(
                domain=MockDomainSingleton.instance,
                bus=MockBusSingleton.instance,
            )
        else:
            raise NotImplementedError('Invalid environment: {}'.format(env))
