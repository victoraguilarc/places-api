# -*- coding: utf-8 -*-

from django.contrib import admin

from src.common.database.models import PhoneNumberORM


@admin.register(PhoneNumberORM)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'iso_code',
        'dial_code',
        'phone_number',
        'is_verified',
        'created_at',
    )
    search_fields = ('phone_number', 'uuid')
    list_filter = (
        'iso_code',
        'dial_code',
        'is_verified',
    )
