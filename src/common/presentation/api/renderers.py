# -*- coding: utf-8 -*-

from djangorestframework_camel_case.render import CamelCaseJSONRenderer

from rest_framework import renderers

from src.common.helpers.time import TimeUtils


class StandarJSONRenderer(CamelCaseJSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        if response.exception is False:
            if data is None:
                data = {}
            if isinstance(data, str | list) or data.get('pagination', None) is None:
                data = {'data': data, 'datetime': TimeUtils.utc_now()}
        return super().render(data, accepted_media_type, renderer_context)


class ZipRenderer(renderers.BaseRenderer):
    media_type = 'application/zip'
    format = 'zip'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
