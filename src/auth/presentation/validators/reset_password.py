# -*- coding: utf-8 -*-

from rest_framework import serializers


class ResetPasswordRequestValidator(serializers.Serializer):
    email = serializers.EmailField()
    next = serializers.CharField(required=False)


class ResetPasswordPerformValidator(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()
