from dataclasses import dataclass

from src.common.domain.messaging.queries import QueryBus


@dataclass
class SessionBuilderMixin(object):
    query_bus: QueryBus
    path_hostname: str
