# -*- coding: utf-8 -*-

from datetime import date, datetime, time, timedelta
from typing import Optional

import pytz
from dateutil.relativedelta import relativedelta


class TimeUtils(object):
    """Reflects all reading and transformation queries over timestamps."""

    UTC_DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    LOCAL_DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S %z'
    ONLY_DATE_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    CORE_TIMESTAMP_FORMAT: str = '%Y-%m-%dT%H:%M:%S.%f%z'
    RRULE_TIMESTAMP_FORMAT: str = '%Y%m%dT%H%M%S'
    ONE_MINUTE = 60
    ONE_HOUR = 60 * ONE_MINUTE
    ONE_DAY = 24 * ONE_HOUR
    ONE_YEAR = 365 * ONE_DAY

    @classmethod
    def get_local_tz(cls, time_zone: Optional[str] = None):
        return pytz.timezone(time_zone) if time_zone else pytz.utc

    @classmethod
    def localize_datetime(cls, date_time: datetime, time_zone: Optional[str] = None):
        local_tz = cls.get_local_tz(time_zone)
        local_time = pytz.utc.localize(date_time) if not date_time.tzinfo else date_time
        return local_time.astimezone(local_tz)

    @classmethod
    def localize_and_format(cls, date_time: datetime, time_zone: Optional[str] = None) -> str:
        return cls.datetime_to_string(cls.localize_datetime(date_time, time_zone))

    @classmethod
    def localize_isoformat(cls, date_time: datetime, time_zone: Optional[str] = None) -> str:
        return cls.localize_datetime(date_time, time_zone).isoformat()

    @classmethod
    def local_datetime(
        cls,
        year: int,
        month: int,
        day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
        microsecond: int = 0,
        time_zone: Optional[str] = None,
    ) -> datetime:
        local_now = cls.localize_datetime(cls.utc_now(), time_zone)
        return local_now.replace(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
        )

    @classmethod
    def replace_timezone(cls, date_time: datetime, time_zone: str):
        local_date_time = cls.localize_datetime(date_time, time_zone)
        return local_date_time.replace(
            year=date_time.year,
            month=date_time.month,
            day=date_time.day,
            hour=date_time.hour,
            minute=date_time.minute,
            second=date_time.second,
            microsecond=date_time.microsecond,
        )

    @classmethod
    def replace_timezone_and_time(cls, date_time: datetime, time_zone: str, new_time: time):
        local_date_time = cls.localize_datetime(date_time, time_zone)
        return local_date_time.replace(
            year=date_time.year,
            month=date_time.month,
            day=date_time.day,
            hour=new_time.hour,
            minute=new_time.minute,
            second=new_time.second,
            microsecond=new_time.microsecond,
        )

    @classmethod
    def replace_time(cls, date_time: datetime, new_time: time):
        return date_time.replace(
            hour=new_time.hour,
            minute=new_time.minute,
            second=new_time.second,
            microsecond=new_time.microsecond,
        )

    @classmethod
    def replace_date(cls, date_time: datetime, new_date: date):
        return date_time.replace(
            year=new_date.year,
            month=new_date.month,
            day=new_date.day,
        )

    @classmethod
    def strftime_with_core_format(cls, date_time):
        """Returns a datetime with the core server format."""
        return date_time.strftime(cls.CORE_TIMESTAMP_FORMAT)

    @classmethod
    def strftime_with_rrule_format(cls, date_time):
        """Returns a datetime with the core server format."""
        return date_time.strftime(cls.RRULE_TIMESTAMP_FORMAT)

    @classmethod
    def switch_datetime_str_format(cls, date_time_str, old_format=None, new_format=None) -> str:
        """Transforms a datetime format from the core format to the bases format."""
        old_format = old_format or cls.CORE_TIMESTAMP_FORMAT
        new_format = new_format or cls.LOCAL_DATETIME_FORMAT
        _datetime = datetime.strptime(date_time_str, old_format)
        return _datetime.strftime(new_format)

    @classmethod
    def datetime_to_string(cls, date_time):
        return date_time.strftime(cls.LOCAL_DATETIME_FORMAT)

    @classmethod
    def pluralize(cls, n, word):
        if n == 1:
            return '%d %s' % (n, word)
        return '%d %ss' % (n, word)

    @classmethod
    def format_duration(cls, seconds):
        if seconds == 0:
            return 'now'

        units = (
            (cls.ONE_YEAR, 'year'),
            (cls.ONE_DAY, 'day'),
            (cls.ONE_HOUR, 'h'),
            (cls.ONE_MINUTE, 'min'),
            # (1, _('s')),
        )

        r = []
        for unit in units:
            time_period, word = unit
            if seconds >= time_period:
                n = int(seconds / time_period)
                r.append(f'{n}{word}')
                seconds -= n * time_period

        return ','.join(', '.join(r).rsplit(',', 1))

    @classmethod
    def extract_simple_date(cls, date_time: datetime, time_zone: Optional[str] = None):
        return cls.localize_datetime(date_time, time_zone).strftime('%Y-%m-%d')

    @classmethod
    def extract_humanized_date(
        cls,
        date_time: datetime,
        time_zone: Optional[str] = None,
    ):
        return cls.localize_datetime(date_time, time_zone).strftime('%d %b %Y')

    @classmethod
    def extract_simple_time(
        cls,
        date_time: datetime,
        time_zone: Optional[str] = None,
    ):
        return cls.localize_datetime(date_time, time_zone).strftime('%H:%M')

    @classmethod
    def format_simple_date(cls, input_date: datetime.date):
        return input_date.strftime('%Y-%m-%d')

    @classmethod
    def format_humanized_date(cls, input_date: datetime.date):
        return input_date.strftime('%d %b %Y')

    @classmethod
    def format_simple_time(cls, input_time: datetime.time) -> str:
        return input_time.strftime('%H:%M')

    @classmethod
    def utc_now(cls) -> datetime:
        return datetime.now().astimezone(pytz.utc)

    @classmethod
    def local_now(cls, time_zone: Optional[str] = None):
        return cls.localize_datetime(cls.utc_now(), time_zone)

    @classmethod
    def date_time_plus_days(
        cls,
        date_time: Optional[datetime] = None,
        time_zone: Optional[str] = None,
        days: Optional[int] = 0,
        return_on_last: Optional[bool] = False,
    ) -> datetime:
        date_time = date_time or cls.utc_now()

        date_time = TimeUtils.localize_datetime(date_time, time_zone) if time_zone else date_time
        date_time_plus_days = date_time + timedelta(days=days)

        if not return_on_last:
            return date_time_plus_days

        return date_time_plus_days.replace(hour=23, minute=59, second=59, microsecond=0)

    @classmethod
    def date_time_plus_months(
        cls,
        date_time: Optional[datetime] = None,
        time_zone: Optional[str] = None,
        months: Optional[int] = 0,
        return_on_last: Optional[bool] = False,
    ) -> datetime:
        date_time = date_time or cls.utc_now()

        date_time = TimeUtils.localize_datetime(date_time, time_zone) if time_zone else date_time
        date_time_plus_months = date_time + relativedelta(months=months)

        if not return_on_last:
            return date_time_plus_months

        return date_time_plus_months.replace(hour=23, minute=59, second=59, microsecond=0)

    @classmethod
    def localize_and_split(cls, date_time: datetime, time_zone: str):
        local_date_time = cls.replace_timezone(date_time=date_time, time_zone=str(time_zone))
        return (
            cls.extract_humanized_date(local_date_time),
            cls.extract_simple_time(local_date_time),
        )

    @classmethod
    def instance_datetime_from_string(
        cls,
        date_time_str: str,
        time_zone: Optional[str] = None,
    ) -> datetime:
        date_time = datetime.strptime(date_time_str, cls.UTC_DATETIME_FORMAT)
        return cls.replace_timezone(date_time, time_zone)

    @classmethod
    def instance_date_from_string(cls, date_str: str) -> date:
        datetime_instance = datetime.strptime(date_str, cls.ONLY_DATE_FORMAT)
        return datetime_instance.date()
