# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.common.domain.interfaces.entities import AggregateRoot
from src.common.domain.value_objects import PictureId


@dataclass
class SessionTenantLogo(AggregateRoot):
    id: PictureId
    image_url: str
