# -*- coding: utf-8 -*-

from rest_framework import serializers


class LoginValidator(serializers.Serializer):
    """Serializer to extends some validation to UsernameOrEmailSerializer."""

    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
