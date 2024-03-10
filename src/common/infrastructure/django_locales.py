from datetime import datetime
from typing import Optional

from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from src.common.domain.enums.locales import Language
from src.common.domain.interfaces.locales import LocaleService

locales = {
    'MONDAY': _('Monday'),
    'TUESDAY': _('Tuesday'),
    'WEDNESDAY': _('Wednesday'),
    'THURSDAY': _('Thursday'),
    'FRIDAY': _('Friday'),
    'SATURDAY': _('Saturday'),
    'SUNDAY': _('Sunday'),
    'ADMIN': _('Administrator'),
    'PAYMENT_REMINDER': _('Payment Reminder'),
}


class DjangoLocaleService(LocaleService):
    def get(self, label: str, language: Language = None):
        language = language or Language.ES
        current_lang = translation.get_language()
        try:
            translation.activate(language.value)
            transladted_value = locales.get(label)
        finally:
            translation.activate(current_lang)
        return transladted_value

    def to_natural_time(self, date_time: datetime, time_zone: Optional[str] = None) -> str:
        return naturaltime(date_time)
