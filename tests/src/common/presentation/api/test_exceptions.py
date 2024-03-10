# -*- coding: utf-8 -*-

from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken

from rest_framework.exceptions import ValidationError

from src.common.presentation.api.exceptions.base import APINotAuthenticated, APIUnauthorized
from src.common.presentation.api.exceptions.handler import ExceptionNormalizer


def test_invalid_token_format():
    received_exc = InvalidToken()
    exc = ExceptionNormalizer.parse(received_exc)
    assert isinstance(exc, APINotAuthenticated)


def test_authentication_failed_format():
    received_exc = AuthenticationFailed()
    exc = ExceptionNormalizer.parse(received_exc)
    assert isinstance(exc, APIUnauthorized)


def test_another_exception_format():
    received_exc = ValidationError()
    exc = ExceptionNormalizer.parse(received_exc)
    assert type(received_exc) == type(exc)
