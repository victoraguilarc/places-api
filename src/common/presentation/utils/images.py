# -*- coding: utf-8 -*-

import tempfile
from io import BytesIO
from urllib.parse import urlparse

from django.core import files

import requests


class DownloadedImage(object):
    file_name: str = None
    image: files.File = None

    def __init__(self, file_name: str, image: files.File):
        self.file_name = file_name
        self.image = image


def clean_path_params(dirty_url: str):
    url = urlparse(dirty_url)
    return f'{url.scheme}://{url.netloc}{url.path}'


def download_image(image_url: str) -> DownloadedImage or None:
    response = requests.get(image_url)

    if response.status_code != requests.codes.ok:
        return

    file_bytes = BytesIO()
    file_bytes.write(response.content)
    file_name = image_url.split('/')[-1]

    image_file = files.File(file_bytes, name=file_name)

    return DownloadedImage(file_name, image_file)
