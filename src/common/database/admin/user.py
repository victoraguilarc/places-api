# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as UserChangeFormBase
from django.contrib.auth.forms import UserCreationForm as UserCreationFormBase
from django.utils.translation import gettext_lazy as _

from src.common.database.models import UserORM


class UserChangeForm(UserChangeFormBase):
    """Overrides the user update form."""

    class Meta(UserChangeFormBase.Meta):
        model = UserORM


class UserCreationForm(UserCreationFormBase):
    """Overrides the user creation form."""

    email = forms.EmailField(label=_('Email'), required=False)

    error_message = UserCreationFormBase.error_messages.update(
        {
            'duplicate_username': 'This username has already been taken.',
        }
    )

    def clean_username(self):
        """Validates the username of a user."""
        username = self.cleaned_data.get('username')
        if UserORM.objects.filter(username=username).exists():
            raise forms.ValidationError(self.error_messages['duplicate_username'])
        return username

    def clean_email(self):
        return self.cleaned_data['email'] or None

    class Meta(UserCreationFormBase.Meta):
        model = UserORM


@admin.register(UserORM)
class UserAdmin(AuthUserAdmin):
    """Defines the user admin behaviour."""

    form = UserChangeForm
    add_form = UserCreationForm
    search_fields = (
        'uuid',
        'username',
        'email_address__email',
        'phone_number__phone_number',
        'phone_number__uuid',
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            _('Personal Information'),
            {
                'fields': (
                    'email_address',
                    'phone_number',
                )
            },
        ),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide', 'full'),
                'fields': (
                    'username',
                    'password1',
                    'password2',
                    'email_address',
                    'phone_number',
                ),
            },
        ),
    )
    list_display = (
        'username',
        'user_email',
        'user_phone_number',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    raw_id_fields = ('phone_number', 'email_address')

    def user_email(self, instance: UserORM):
        if not instance.email_address:
            return '---'
        verification_icon = '✔' if instance.email_address.is_verified else ''
        return f'{verification_icon} {instance.email_address.email}'

    def user_phone_number(self, instance: UserORM):
        if not instance.phone_number:
            return '---'
        verification_icon = '✔' if instance.phone_number_verified else ''
        return f'{verification_icon}{instance.display_phone_number}'

    user_email.short_description = 'Email'
    user_phone_number.short_description = _('Phone Number')
