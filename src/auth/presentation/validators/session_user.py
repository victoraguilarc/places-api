# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import Serializer

from src.common.presentation.api.rest_fields import Base64ImageField


class CreateUserValidator(Serializer):
    """Serialier to request and validate user basic info."""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    paternal_surname = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    maternal_surname = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    photo = Base64ImageField(required=False, allow_null=False)
