from src.common.domain import BaseEnum


class TimeZone(BaseEnum):
    # Check pytz.all_timezones if you need to add more timezones
    UTC = 'UTC'
    MEXICO_CITY = 'America/Mexico_City'
    MEXICO_BAJA_NORTE = 'Mexico/BajaNorte'
    MEXICO_BAJA_SUR = 'Mexico/BajaSur'
    MEXICO_GENERAL = 'Mexico/General'
    AMERICA_LA_PAZ = 'America/La_Paz'
    AMERICA_LIMA = 'America/Lima'


class Days(BaseEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    @classmethod
    def weekdays(cls):
        return {
            cls.MONDAY: 'MONDAY',
            cls.TUESDAY: 'TUESDAY',
            cls.WEDNESDAY: 'WEDNESDAY',
            cls.THURSDAY: 'THURSDAY',
            cls.FRIDAY: 'FRIDAY',
            cls.SATURDAY: 'SATURDAY',
            cls.SUNDAY: 'SUNDAY',
        }

    @classmethod
    def week(cls):
        return [
            cls.MONDAY,
            cls.TUESDAY,
            cls.WEDNESDAY,
            cls.THURSDAY,
            cls.FRIDAY,
            cls.SATURDAY,
            cls.SUNDAY,
        ]

    @classmethod
    def choices(cls):  # noqa: D102
        return [(weekday.value, day_str) for weekday, day_str in cls.weekdays().items()]

    @classmethod
    def get_weekday_label(cls, day: 'Days'):
        return cls.weekdays().get(day, None)


class Language(BaseEnum):
    ES = 'es'
    EN = 'en'


class CountryIsoCode(BaseEnum):
    MEXICO = 'MX'
    BRAZIL = 'BR'
    BOLIVIA = 'BO'
    ANY = 'XX'

    @property
    def is_mexico(self):
        return self == self.MEXICO

    @property
    def is_brazil(self):
        return self == self.BRAZIL

    @property
    def is_bolivia(self):
        return self == self.BOLIVIA

    @property
    def is_any(self):
        return self == self.ANY


class Platform(BaseEnum):
    ANDROID = 'ANDROID'
    IOS = 'IOS'

    @classmethod
    def choices(cls):  # noqa: D102
        return (
            (cls.ANDROID.value, 'ANDROID'),
            (cls.IOS.value, 'IOS'),
        )
