# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.application.pictures.responses import PictureResponse
from src.common.domain.interfaces.responses import ApiResponse
from src.common.domain.interfaces.services import ApiService
from src.common.domain.respositories.picture import PictureRepository
from src.common.domain.value_objects import RawPicture


@dataclass
class PictureCreator(ApiService):
    raw_picture: RawPicture
    picture_repository: PictureRepository

    def execute(self) -> ApiResponse:
        picture = self.picture_repository.persist(self.raw_picture)
        return PictureResponse(picture)
