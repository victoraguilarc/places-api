# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.application.pictures.responses import PictureResponse
from src.auth.domain.exceptions import PictureNotFound
from src.common.domain.interfaces.responses import ApiResponse
from src.common.domain.interfaces.services import ApiService
from src.common.domain.respositories.picture import PictureRepository
from src.common.domain.value_objects import PictureId


@dataclass
class PictureDeleter(ApiService):
    picture_id: PictureId
    picture_repository: PictureRepository

    def execute(self) -> ApiResponse:
        picture = self.picture_repository.find(self.picture_id)
        if not picture:
            raise PictureNotFound
        self.picture_repository.delete(self.picture_id)
        # TODO Publish stream_events
        return PictureResponse()
