from dataclasses import dataclass

from src.common.domain.context.locale import LocaleContext
from src.common.domain.interfaces.responses import JSONPresenter
from src.places.domain.entities.place import DayForecast, Place, PlaceContainer


@dataclass
class DayForecastPresenter(JSONPresenter):
    instance: DayForecast
    locale_context: LocaleContext

    @property
    def to_dict(self) -> dict:
        return {
            'day': self.instance.day.isoformat(),
            'max': str(self.instance.max),
            'min': str(self.instance.max),
            'weather': self.instance.weather,
        }


@dataclass
class PlacePresenter(JSONPresenter):
    instance: Place
    locale_context: LocaleContext

    @property
    def to_dict(self) -> dict:
        return {
            'id': self.instance.id,
            'slug': self.instance.slug,
            'city_name': self.instance.city_name,
            'state': self.instance.state,
            'country': self.instance.country,
            'lat': self.instance.lat,
            'long': self.instance.lng,
            'result_type': str(self.instance.result_type),
        }


@dataclass
class PlaceContainerPresenter(JSONPresenter):
    instance = PlaceContainer
    locale_context: LocaleContext

    @property
    def to_dict(self) -> dict:
        return {
            **PlacePresenter(self.instance.place, self.locale_context).to_dict,
            'forecasts': [
                DayForecastPresenter(forecast, self.locale_context).to_dict
                for forecast in self.instance.forecasts
            ],
        }
