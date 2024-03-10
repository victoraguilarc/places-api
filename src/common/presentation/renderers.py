# -*- coding: utf-8 -*-

from django.utils import timezone

from djangorestframework_camel_case.render import CamelCaseJSONRenderer

from rest_framework.renderers import JSONRenderer
from rest_framework.utils.encoders import JSONEncoder
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


class SafeJSONEncoder(JSONEncoder):
    """Process the object encode/decode to JSON safely."""

    def encode(self, instance):
        """Override JSONEncoder.encode method.

        It because it has hacks for performance that make things more complicated.
        """
        chunks = self.iterencode(instance, True)  # noqa: WPS425
        return ''.join(chunks)

    def iterencode(self, instance, _one_shot=False):  # noqa: D102
        chunks = super().iterencode(instance, _one_shot)
        for chunk in chunks:
            chunk = chunk.replace('&', '\\u0026')
            chunk = chunk.replace('<', '\\u003c')
            chunk = chunk.replace('>', '\\u003e')
            yield chunk


class SafeJSONRenderer(JSONRenderer):  # noqa: D101
    encoder_class = SafeJSONEncoder


class CamelizedFormattedJSONRenderer(CamelCaseJSONRenderer):
    """Force response body to new body"""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        response = renderer_context.get('response')

        extra_data = dict()

        # For a paginated response
        if 'results' in data and isinstance(data['results'], list):
            results = data.pop('results')
            extra_data = data
            data = results

        # For a regular response
        has_allowed_response_type = type(data) in (str, list, dict, ReturnList, ReturnDict)
        if response and response.exception is False and has_allowed_response_type:
            cleaned_data = None if isinstance(data, str) and len(data) == 0 else data
            data = {**extra_data, 'data': cleaned_data, 'datetime': timezone.now()}
        return super().render(data, accepted_media_type, renderer_context)
