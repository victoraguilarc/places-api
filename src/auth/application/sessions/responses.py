# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.common.application.presenters.user import UserPresenter
from src.common.domain.context.locale import LocaleContext
from src.common.domain.entities.user_session import UserSession
from src.common.domain.interfaces.responses import ApiResponse


@dataclass
class UserSessionResponse(ApiResponse):
    instance: UserSession

    def render(self, locale_context: LocaleContext) -> dict:
        return {
            'session': self.instance.token,
            'profile': UserPresenter(self.instance.profile, locale_context).to_dict,
        }
