# -*- coding: utf-8 -*-

from django.urls import include, path

app_name = 'common'
urlpatterns = [
    path('v1/', include('src.auth.presentation.urls', namespace='auth')),
    path('v1/', include('src.places.presentation.urls', namespace='places')),
]
