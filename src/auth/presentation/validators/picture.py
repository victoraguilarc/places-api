# -*- coding: utf-8 -*-

from rest_framework import serializers


class CreatePictureValidator(serializers.Serializer):
    image = serializers.ImageField(required=True, allow_null=False)
