# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ConsumerClient(object):
    """
    This class parse the user agent for grow supported clients
    The correct format for user-agent is:
    PLATFORM:(BUNDLE_ID|APPLICATION_ID)/VERSION_NAME:VERSION_CODE
    e.g: android:com.grow.chargers/1.0.0-testing:1
    """

    ANDROID = 'android'
    IOS = 'ios'

    platform: Optional[str] = None
    application_id: Optional[str] = None
    version_name: Optional[str] = None
    version_code: Optional[str] = None

    VERSION_PATTERN = r'(android|ios|web):([a-z]|\.)*\/(\d|\.|-|[a-z])+:(\d|.)+'

    @classmethod
    def is_valid_agent(cls, agent: str):
        matched = re.match(cls.VERSION_PATTERN, agent)
        return bool(matched)

    @classmethod
    def build(cls, agent: str):
        if not cls.is_valid_agent(agent):
            return

        app_info, version_info = agent.split('/')
        platform, application_id = app_info.split(':')
        version_name, version_code = version_info.split(':')

        return ConsumerClient(
            platform=platform,
            application_id=application_id,
            version_name=version_name,
            version_code=version_code,
        )
