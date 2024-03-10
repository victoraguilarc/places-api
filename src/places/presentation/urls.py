# -*- coding: utf-8 -*-

from django.urls import path

from src.places.presentation.api.places import PlacesView

app_name = 'places'
urlpatterns = [
    path(
        'places',
        view=PlacesView.as_view(),
        name='places',
    ),
]
