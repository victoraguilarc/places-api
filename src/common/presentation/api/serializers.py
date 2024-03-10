from dataclasses import dataclass
from datetime import datetime

from src.common.helpers.time import TimeUtils


@dataclass
class SplitDatetimeDisplayer(object):
    date_time: datetime
    time_zone: str = None

    @property
    def data(self):
        return {
            'date': TimeUtils.extract_humanized_date(
                date_time=self.date_time,
                time_zone=self.time_zone,
            ),
            'time': TimeUtils.extract_simple_time(self.date_time),
        }
