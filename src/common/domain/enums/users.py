from src.common.domain import BaseEnum


class PendingActionCategory(BaseEnum):
    """Action options for User actions."""

    VERIFY_EMAIL = 'VERIFY_EMAIL'
    VERIFY_PHONE_NUMBER = 'VERIFY_PHONE_NUMBER'  # noqa: S105
    RESET_PASSWORD = 'RESET_PASSWORD'  # noqa: S105
    REDEEM_SESSION = 'REDEEM_SESSION'  # noqa: S105

    @classmethod
    def get_verifications(cls):
        return [
            cls.VERIFY_EMAIL,
            cls.VERIFY_PHONE_NUMBER,
        ]


class PendingActionStatus(BaseEnum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    EXPIRED = 'EXPIRED'


class VerificationType(BaseEnum):
    EMAIL = 'EMAIL'
    PHONE_NUMBER = 'PHONE_NUMBER'
    WHATSAPP = 'WHATSAPP'

    @property
    def is_email(self):
        return self == self.EMAIL

    @property
    def is_phone_number(self):
        return self == self.PHONE_NUMBER

    @property
    def is_whatsapp(self):
        return self == self.WHATSAPP
