# -*- coding: utf-8 -*-

from django.contrib.postgres.forms import JSONField
from django.forms import widgets
from django.template.loader import render_to_string
from django.templatetags.static import static


class EditorJsWidget(widgets.TextInput):
    class Media:
        js = (
            static('vendors/jquery/jquery.min.js'),
            'https://cdn.jsdelivr.net/npm/@editorjs/editorjs@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/paragraph@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/header@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/simple-image@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/delimiter@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/list@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/checklist@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/quote@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/code@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/embed@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/table@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/link@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/warning@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/marker@latest',
            'https://cdn.jsdelivr.net/npm/@editorjs/inline-code@latest',
            # static('editor/editor.js'),
            static('editor/editor_field.js'),
            static('editor/codemirror.js'),
        )
        css = {'all': (static('editor/editor.css'),)}

    def __init__(self, *args, **kwargs):
        super(EditorJsWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, **kwargs):
        ctx = {'name': name, 'id': kwargs['attrs']['id'], 'value': value}

        return render_to_string('admin/editor_field.html', ctx)


class EditorJsField(JSONField):
    widget = EditorJsWidget
