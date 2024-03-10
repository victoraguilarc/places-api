# -*- coding: utf-8 -*-

from django.shortcuts import render


def error400(request, *args, **kwargs):
    """Renders default template for bad request errors."""
    return render(request, 'errors/400.html', {})


def error403(request, *args, **kwargs):
    """Renders default template for forbidden errors."""
    return render(request, 'errors/403.html', {})


def error404(request, *args, **kwargs):
    """Renders default template for not found errors."""
    return render(request, 'errors/404.html', {})


def error500(request, *args, **kwargs):
    """Renders default template for server errors."""
    return render(request, 'errors/500.html', {})
