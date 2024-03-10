# -*- coding: utf-8 -*-
# ruff: noqa: S324
import hashlib
import secrets
import string
import uuid

from django.conf import settings

from src.common.presentation.utils.dates import ago, now


def compute_md5_hash(input_value):
    """Gets md5 digest from a string."""
    md5_hash = hashlib.md5()  # noqa: S303, W291
    md5_hash.update(input_value.encode('utf-8'))
    return md5_hash.hexdigest()


def get_random_token():
    """Gets a limited uuid."""
    instance = uuid.uuid4()
    return instance.hex


def get_expiration_lapse():
    """Returns a range of dates."""
    now_date = now()
    days = 7
    if settings.TOKEN_EXPIRATION_DAYS:
        days = settings.TOKEN_EXPIRATION_DAYS
    end_date = ago(days=days)

    return now_date, end_date


def get_hostname(request=None):
    """Calculates the server hostname."""
    hostname = ''
    if request:
        hostname = '127.0.0.1'
        if 'HTTP_HOST' in request.META:
            hostname = request.META.get('HTTP_HOST')

        try:
            has_settings = settings.USE_HTTPS
        except AttributeError:
            has_settings = False

        protocol = 'https' if has_settings else 'http'
        hostname = '{protocol}://{hostname}'.format(
            protocol=protocol,
            hostname=hostname,
        )
    return hostname


def get_random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(secrets.choice(letters) for i in range(length))


def is_valid_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False
