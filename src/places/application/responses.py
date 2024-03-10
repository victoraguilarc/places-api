# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List

from src.common.domain.context.locale import LocaleContext
from src.common.domain.interfaces.responses import ApiResponse
from src.places.application.presenters import PlaceContainerPresenter
from src.places.domain.entities.place import PlaceContainer


@dataclass
class PlaceContainersResponse(ApiResponse):
    instances: List[PlaceContainer]

    def render(self, locale_context: LocaleContext) -> List[dict]:
        return [
            PlaceContainerPresenter(container, locale_context).to_dict
            for container in self.instances
        ]
