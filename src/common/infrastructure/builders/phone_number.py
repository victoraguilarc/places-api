from src.common.database.models import PhoneNumberORM
from src.common.domain.entities.phone_number import PhoneNumber
from src.common.domain.enums.locales import CountryIsoCode


def build_phone_number(orm_instance: PhoneNumberORM) -> PhoneNumber:
    return PhoneNumber(
        id=orm_instance.uuid,
        iso_code=CountryIsoCode.from_value(orm_instance.iso_code),
        dial_code=orm_instance.dial_code,
        phone_number=orm_instance.phone_number,
        is_verified=orm_instance.is_verified,
        prefix=orm_instance.prefix,
    )
