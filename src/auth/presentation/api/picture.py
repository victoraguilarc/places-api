# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.auth.application.pictures.use_cases.deleter import PictureDeleter
from src.common.domain.value_objects import PictureId
from src.common.presentation.api.domain_api import DomainAPIView


class PictureView(DomainAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, **kwargs):
        app_service = PictureDeleter(
            picture_id=PictureId(kwargs.get('picture_id')),
            picture_repository=self.domain_context.picture_repository,
        )
        response = app_service.execute()
        return Response(
            response.render(self.locale_context),
            status=status.HTTP_204_NO_CONTENT,
        )
