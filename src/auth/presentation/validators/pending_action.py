# -*- coding: utf-8 -*-

from rest_framework import serializers


class PendingActionTokenValidator(serializers.Serializer):
    token = serializers.CharField()
