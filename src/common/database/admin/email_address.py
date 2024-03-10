# -*- coding: utf-8 -*-

from django.contrib import admin

from src.common.database.models import EmailAddressORM


@admin.register(EmailAddressORM)
class EmailAddressAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'email')
    list_display = (
        'uuid',
        'email',
        'is_verified',
        'created_at',
    )
    list_filter = ('created_at',)
