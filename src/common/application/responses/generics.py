# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.common.domain.context.locale import LocaleContext
from src.common.domain.interfaces.responses import ApiResponse
from src.common.helpers.time import TimeUtils


@dataclass
class ResultResponse(ApiResponse):
    def render(self, locale_context: LocaleContext) -> dict:
        return {
            'status': str(GenericActionStatus.SUCCESS),
            'completed_at': TimeUtils.local_now(str(locale_context.time_zone)).isoformat(),
        }
