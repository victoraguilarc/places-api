# -*- coding: utf-8 -*-
from config.settings.components import env

CONSTANCE_CONFIG = {
    'OTP_VALIDATION_URL': (
        '',
        'It helps to format OTP SMSs',
    ),
}
CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'
CONSTANCE_REDIS_CONNECTION = env('REDIS_CACHE_URL', default='redis://redis:6379/0')
