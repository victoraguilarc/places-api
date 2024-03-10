# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

from src.common.presentation.views.errors import error400, error403, error404, error500

admin.site.site_header = 'Destinations'
admin.site.site_title = 'Destinations Admin'
admin.site.index_title = 'Destinations Admin'

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(route='', view=TemplateView.as_view(template_name='home.html'), name='home'),
    path(
        route='robots.txt',
        view=TemplateView.as_view(template_name="robots.txt", content_type='text/plain'),
        name='robots',
    ),
    re_path(
        route=r'^favicon\.ico$',
        view=RedirectView.as_view(url=settings.FAVICON_PATH, permanent=True),
        name='favicon',
    ),
    # API
    path('', include('src.urls', namespace='api')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('', include('config.debug_urls', namespace='debug')),
        path('__reload__/', include('django_browser_reload.urls')),
    ]

    # Developer tools
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        if settings.DEBUG:
            import debug_toolbar  # noqa: WPS433
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
else:
    handler400 = error400
    handler403 = error403
    handler404 = error404
    handler500 = error500
