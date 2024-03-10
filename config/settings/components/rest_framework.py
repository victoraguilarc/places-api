# -*- coding: utf-8 -*-
# See: https://www.django-rest-framework.org/api-guide/settings/
from datetime import timedelta

from corsheaders.defaults import default_headers

from config.settings.components import env

CORS_ORIGIN_ALLOW_ALL = True
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'src.common.presentation.api.exceptions.handler.formatted_error_handler',
    'NON_FIELD_ERRORS_KEY': 'errors',
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_RENDERER_CLASSES': (
        'src.common.presentation.renderers.CamelizedFormattedJSONRenderer',
        'rest_framework.renderers.MultiPartRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FileUploadParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'src.common.presentation.auth_backends.TenantJWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'src.common.presentation.renderers.CamelizedFormattedJSONRenderer',
        'rest_framework.renderers.MultiPartRenderer',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%SZ',  # noqa: WPS323
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
}

API_KEY_CUSTOM_HEADER = 'HTTP_X_API_KEY'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'content-disposition',
    'cache-control',
    'referer',
    'connection',
    'x-tenant',
    'x-client',
]
APPEND_SLASH = True

# Simple Django JWT
# https://github.com/davesque/django-rest-framework-simplejwt

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=8),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': env('DJANGO_SECRET_KEY', default='default_secret_key'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'uuid',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
