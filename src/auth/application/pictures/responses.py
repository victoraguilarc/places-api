# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from src.auth.application.pictures.presenters import PicturePresenter
from src.common.constants import INSTANCE_DELETED_RESPONSE
from src.common.domain.context.locale import LocaleContext
from src.common.domain.entities.picture import Picture
from src.common.domain.interfaces.responses import ApiResponse


@dataclass
class PictureResponse(ApiResponse):
    instance: Optional[Picture] = None

    def render(self, locale_context: LocaleContext) -> Union[Dict, str]:
        if not self.instance:
            return INSTANCE_DELETED_RESPONSE
        return PicturePresenter(self.instance).to_dict


@dataclass
class PicturesResponse(ApiResponse):
    instances: List[Picture]

    def render(self, locale_context: LocaleContext) -> list:
        return [PicturePresenter(instance).to_dict for instance in self.instances]
