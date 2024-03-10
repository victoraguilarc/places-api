from src.common.database.models import EmailAddressORM
from src.common.domain.entities.email_address import EmailAddress
from src.common.domain.value_objects import EmailAddressId


def build_email_address(orm_instance: EmailAddressORM) -> EmailAddress:
    return EmailAddress(
        id=EmailAddressId(orm_instance.uuid),
        email=orm_instance.email,
        is_verified=orm_instance.is_verified,
        created_at=orm_instance.created_at,
    )
