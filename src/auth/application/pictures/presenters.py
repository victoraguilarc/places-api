# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.common.domain.entities.picture import Picture


@dataclass
class PicturePresenter(object):
    instance: Picture

    @property
    def to_dict(self) -> dict:
        return {
            'id': str(self.instance.id),
            'image_url': str(self.instance.image_url),
        }
