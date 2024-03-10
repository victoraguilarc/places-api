# -*- encoding: utf-8 -*-

from config.settings.components import env

OPEN_WEATHER_BASE_URL = env.str('OPEN_WEATHER_BASE_URL')
RESERVAMOS_BASE_URL = env.str('RESERVAMOS_BASE_URL')

OPEN_WEATHER_API_KEY = env.str('OPEN_WEATHER_API_KEY')
