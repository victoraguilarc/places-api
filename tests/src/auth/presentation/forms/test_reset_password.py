# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _

from src.auth.presentation.forms import ResetPasswordForm


class ResetPasswordFormTests:
    @staticmethod
    def test_valid_data():
        data = {'password1': 'anything', 'password2': 'anything'}
        form = ResetPasswordForm(data=data)
        assert form.is_valid()

    @staticmethod
    def test_invalid_data():
        data = {'password1': 'anything', 'password2': 'another_thing'}
        form = ResetPasswordForm(data=data)
        assert not form.is_valid()
        assert form.errors == {'password2': [_('Passwords Mismatch')]}

    @staticmethod
    def test_blank_data():
        form = ResetPasswordForm(data={})
        assert not form.is_valid()
        assert form.errors == {
            'password1': [_('This field is required.')],
            'password2': [_('This field is required.')],
        }
