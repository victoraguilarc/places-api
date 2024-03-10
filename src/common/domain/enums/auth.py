from src.common.domain import BaseEnum


class AuthenticationMethod(BaseEnum):
    EMAIL = 'EMAIL'
    WHATSAPP = 'WHATSAPP'
    SMS = 'SMS'

    @property
    def is_email(self) -> bool:
        return self == self.EMAIL

    @property
    def is_whatsapp(self) -> bool:
        return self == self.WHATSAPP

    @property
    def is_sms(self) -> bool:
        return self == self.SMS


class PendingActionNamespace(BaseEnum):
    TENANTS = 'TENANTS'
    TENANT_USERS = 'TENANT_USERS'
    TENANT_CUSTOMERS = 'TENANT_CUSTOMERS'
