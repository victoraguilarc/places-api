# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import List, Optional

from src.common.domain.entities.picture import Picture
from src.common.domain.value_objects import PictureId, RawPicture


class PictureRepository(ABC):
    @abstractmethod
    def find(self, picture_id: PictureId) -> Optional[Picture]:
        raise NotImplementedError

    @abstractmethod
    def persist(self, raw_picture: RawPicture) -> Picture:
        raise NotImplementedError

    @abstractmethod
    def delete(self, picture_id: PictureId):
        raise NotImplementedError

    @abstractmethod
    def filter(self) -> List[Picture]:
        raise NotImplementedError
