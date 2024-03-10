# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.auth.application.pictures.responses import PicturesResponse
from src.common.domain.interfaces.responses import ApiResponse
from src.common.domain.interfaces.services import ApiService
from src.common.domain.respositories.picture import PictureRepository


@dataclass
class PictureLister(ApiService):
    picture_repository: PictureRepository

    def execute(self) -> ApiResponse:
        pictures = self.picture_repository.filter()
        return PicturesResponse(pictures)
