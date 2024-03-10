# -*- coding: utf-8 -*-

import logging

from django import forms
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class ResetPasswordForm(forms.Form):
    """Validates the reset password process."""

    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean_password2(self):
        """Validates two passwords."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Passwords Mismatch'))
        return password2


class ActivateAccountForm(ResetPasswordForm):
    pass
