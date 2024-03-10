from dataclasses import dataclass
from datetime import datetime

from src.common.domain.enums.locales import TimeZone
from src.common.domain.interfaces.locales import LocaleService, TimeFormatter
from src.common.helpers.time import TimeUtils


@dataclass
class RawTimeFormatter(TimeFormatter):
    time_zone: TimeZone
    locale_service: LocaleService

    DAYS_IN_YEAR = 365
    DAYS_IN_MONTH = 30
    SECS_IN_DAY = 86400
    SECS_IN_HOUR = 3600

    def to_natural_time(self, input_datetime: datetime) -> str:
        local_now = TimeUtils.local_now(
            time_zone=str(self.time_zone),
        )
        date_time = TimeUtils.localize_datetime(
            date_time=input_datetime,
            time_zone=str(self.time_zone),
        )
        if type(date_time) is int:
            diff = local_now - datetime.fromtimestamp(date_time)
        elif isinstance(date_time, datetime):
            diff = local_now - date_time
        else:
            diff = local_now - local_now

        second_diff = diff.seconds
        day_diff = diff.days

        if day_diff < 0:
            return ''

        if day_diff == 0:
            if second_diff < 10:
                return "just now"
            if second_diff < 60:
                return str(second_diff) + " seconds ago"
            if second_diff < 120:
                return "a minute ago"
            if second_diff < 3600:
                return str(second_diff // 60) + " minutes ago"
            if second_diff < 7200:
                return "an hour ago"
            if second_diff < 86400:
                return str(second_diff // 3600) + " hours ago"
        if day_diff == 1:
            return "Yesterday"
        if day_diff < 7:
            return str(day_diff) + " days ago"
        if day_diff < 31:
            return str(day_diff // 7) + " weeks ago"
        if day_diff < 365:
            return str(day_diff // 30) + " months ago"
        return str(day_diff // 365) + " years ago"
