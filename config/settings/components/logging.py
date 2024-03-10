# -*- coding: utf-8 -*-

import logging.config  # noqa: WPS301
import os

from django.utils.log import DEFAULT_LOGGING

# Logging
# https://docs.djangoproject.com/en/4.1/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'stdout': {
            'format': '%(levelname)s %(asctime)s module=%(pathname)s#%(lineno)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'stdout': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'stdout',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'console-verbose': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'security': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'sentry_sdk': {'level': 'ERROR', 'handlers': ['console'], 'propagate': False},
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'info').upper()
logging.config.dictConfig(
    {
        'version': LOGGING['version'],
        'disable_existing_loggers': LOGGING['disable_existing_loggers'],
        'formatters': LOGGING['formatters'],
        'handlers': {
            # console logs to stderr
            'stdout': LOGGING['handlers']['stdout'],
            'django.server': LOGGING['handlers']['stdout'],
        },
        'loggers': {
            # default for all undefined Python modules
            '': {
                'level': LOG_LEVEL,
                'handlers': ['stdout'],
            },
            # Our application code
            'app': {
                'level': LOG_LEVEL,
                'handlers': ['stdout'],
                # Avoid double logging because of root logger
                'propagate': False,
            },
            # Prevent noisy modules from logging to Sentry
            'noisy_module': {
                'level': 'ERROR',
                'handlers': ['stdout'],
                'propagate': False,
            },
            # Default runserver request logging
            'django.server': DEFAULT_LOGGING['loggers']['django.server'],
        },
    }
)
