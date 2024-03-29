# -*- coding: utf-8 -*-

"""Production settings.

This file contains all the settings used in production.
This file is required and if development.py is present these
values are overridden.
https://docs.djangoproject.com/en/2.2/howto/deployment/
"""
import logging
from socket import gethostbyname_ex, gethostname

from django.core.exceptions import DisallowedHost

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration, ignore_logger
from sentry_sdk.integrations.redis import RedisIntegration

from config.settings.components import env
from config.settings.components.common import TEMPLATES

DEBUG = False

LOCAL_HOSTNAMES = [gethostname()]
LOCAL_HOSTNAMES += list(set(gethostbyname_ex(gethostname())[2]))

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS') + LOCAL_HOSTNAMES
SECRET_KEY = env('DJANGO_SECRET_KEY')

#
# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa: F405
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
    ),
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'  # noqa: S105
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.MinimumLengthValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.CommonPasswordValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.NumericPasswordValidator'.format(_PASS),
    },
]

# Security
# https://docs.djangoproject.com/en/2.2/topics/security/
SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://places.codemia.dev']  # Change this to your domain

EMAIL_SUBJECT_PREFIX = env(
    'DJANGO_EMAIL_SUBJECT_PREFIX',
    default='[noreply]',
)
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
ANYMAIL = {
    'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': env('MAILGUN_DOMAIN'),
    'MAILGUN_API_URL': env('MAILGUN_API_URL', default='https://api.mailgun.net/v3'),
}

#
#  E R R O R  L O G G I N G
#
DJANGO_STAGE = env('DJANGO_STAGE', default='dev')
SENTRY_DSN = env('SENTRY_DSN')
SENTRY_LOG_LEVEL = env.int('DJANGO_SENTRY_LOG_LEVEL', logging.INFO)

sentry_logging = LoggingIntegration(
    level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as stream_events
)
ignore_logger('django.security.DisallowedHost')


def before_send(event, hint):
    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, (DisallowedHost,)):
            return None
    return event


integrations = [sentry_logging, DjangoIntegration(), RedisIntegration()]
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=integrations,
    environment=DJANGO_STAGE,
    traces_sample_rate=env.float('SENTRY_TRACES_SAMPLE_RATE', default=1.0),
    send_default_pii=True,
    before_send=before_send,
)
