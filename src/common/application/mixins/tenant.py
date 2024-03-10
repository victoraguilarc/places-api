from dataclasses import dataclass
from typing import Optional

from src.common.application.queries.tenants import GetTenantByIdQuery
from src.common.domain.entities.tenant import Tenant
from src.common.domain.messaging.queries import QueryBus
from src.common.domain.value_objects import TenantId
from src.tenants.domain.exceptions import TenantNotFound


@dataclass
class GetTenantFromQueryMixin(object):
    tenant_id: TenantId
    query_bus: QueryBus

    def get_tenant(self) -> Optional[Tenant]:
        tenant: Optional[Tenant] = self.query_bus.ask(
            query=GetTenantByIdQuery(tenant_id=self.tenant_id),
        )
        if not tenant:
            raise TenantNotFound
        return tenant
