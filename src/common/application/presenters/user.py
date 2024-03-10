# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.common.domain.context.locale import LocaleContext
from src.common.domain.entities.user import User
from src.common.helpers.time import TimeUtils


@dataclass
class UserPresenter(object):
    instance: User
    locale_context: LocaleContext

    @property
    def to_dict(self) -> dict:
        return {
            'id': str(self.instance.id),
            'email_address': (
                self.instance.email_address.to_minimal_dict
                if self.instance.email_address else None
            ),
            'phone_number': (
                self.instance.phone_number.to_minimal_dict
                if self.instance.phone_number else None
            ),
            'created_at': (
                TimeUtils.localize_isoformat(
                    date_time=self.instance.created_at,
                    time_zone=str(self.locale_context.time_zone),
                )
                if self.instance.created_at else None
            ),
        }
