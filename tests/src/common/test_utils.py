# -*- coding: utf-8 -*-

from datetime import datetime
from io import BytesIO

from django.core.files import File
from django.http import HttpRequest
from django.test.utils import override_settings
from django.utils import timezone

from src.common.domain import BaseEnum
from src.common.presentation.utils import dates, files
from src.common.presentation.utils.strings import compute_md5_hash, get_hostname, get_random_token


class UtilsTests:
    @staticmethod
    def test_generate_image():
        photo = files.generate_image()
        assert photo is not None
        assert isinstance(photo, BytesIO)

    @staticmethod
    def test_generate_image_file():
        photo_file = files.generate_image_file()
        assert photo_file is not None
        assert isinstance(photo_file, File)

    @staticmethod
    def test_now():
        timestamp = dates.now()
        assert isinstance(timestamp, datetime)

    @staticmethod
    def test_ago():
        timestamp = dates.ago(days=1)
        assert isinstance(timestamp, datetime)

    @staticmethod
    def test_after():
        timestamp = dates.after(days=1)
        assert isinstance(timestamp, datetime)

    @staticmethod
    def test_local_datetime():
        timestamp = dates.local_datetime()
        assert isinstance(timestamp, datetime)

    @staticmethod
    def test_get_timeslug():
        str_datetime_slug = dates.get_timeslug()
        assert isinstance(str_datetime_slug, str)

    @staticmethod
    def test_compute_md5_hash():
        test_hash = compute_md5_hash("anything")
        assert isinstance(test_hash, str)

    @staticmethod
    def test_get_random_token():
        test_hash = get_random_token()
        assert isinstance(test_hash, str)

    @staticmethod
    def test_get_hostname():
        hostname = get_hostname()
        assert isinstance(hostname, str)

    @staticmethod
    def test_get_hostname_with_request():
        request = HttpRequest()
        request.method = 'GET'
        request.META['HTTP_HOST'] = 'localhost:8000'

        with override_settings(USE_HTTPS=True):
            hostname = get_hostname(request=request)
            assert isinstance(hostname, str)

        with override_settings(USE_HTTPS=False):
            hostname = get_hostname(request=request)
            assert isinstance(hostname, str)

    @staticmethod
    def test_choices_from_base_enum():
        choices = BaseEnum.choices()
        assert isinstance(choices, list)
