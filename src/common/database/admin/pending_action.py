# -*- coding: utf-8 -*-

from django.contrib import admin

from src.common.database.models import PendingActionORM


@admin.register(PendingActionORM)
class PendingActiondmin(admin.ModelAdmin):
    """Defines the pending action admin behaviour."""

    search_fields = (
        'token',
        'uuid',
        'user__email',
        'user__uuid',
        'tracking_code',
    )
    list_display = (
        'token',
        'user',
        'category',
        'status',
        'tracking_code',
        'created_at',
        'expires_at',
        'metadata',
    )
    list_filter = (
        'category',
        'status',
    )
    raw_id_fields = ('user',)
