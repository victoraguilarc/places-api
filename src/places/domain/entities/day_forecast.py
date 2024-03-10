from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class DayForecast(object):
    day: date
    max: Decimal
    min: Decimal
    weather: str

    @classmethod
    def from_dict(cls, data: dict) -> 'DayForecast':
        return cls(
            day=date.fromisoformat(data.get('day')),
            max=Decimal(data.get('max')),
            min=Decimal(data.get('min')),
            weather=data.get('weather'),
        )

    @property
    def to_dict(self) -> dict:
        return {
            'day': self.day.isoformat(),
            'max': str(self.max),
            'min': str(self.min),
            'weather': self.weather,
        }

    def __eq__(self, other):
        return self.to_dict == other.to_dict
