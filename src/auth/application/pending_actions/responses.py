# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.application.pending_actions.presenters import PendingActionPresenter
from src.common.domain.context.locale import LocaleContext
from src.common.domain.entities.pending_action import PendingAction
from src.common.domain.interfaces.responses import ApiResponse


@dataclass
class PendingActionResponse(ApiResponse):
    instance: PendingAction

    def render(self, locale_context: LocaleContext) -> dict:
        return PendingActionPresenter(self.instance).to_dict


@dataclass
class KeyValueResponse(ApiResponse):
    key: str
    value: str

    def render(self, locale_context: LocaleContext) -> dict:
        return {
            self.key: self.value,
        }
