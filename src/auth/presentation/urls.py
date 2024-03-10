# -*- coding: utf-8 -*-

from django.urls import path

from src.auth.presentation.api.login import LoginView
from src.auth.presentation.api.pending_actions.email_verification import (
    PerformEmailVerificationView,
)
from src.auth.presentation.api.pending_actions.exchangers import ExchangePendingActionView
from src.auth.presentation.api.pending_actions.phone_verification import (
    PerformPhoneVerificationView,
)
from src.auth.presentation.api.register import RegisterView
from src.auth.presentation.api.reset_password import (
    ResetPasswordPerformView,
    ResetPasswordRequestView,
)
from src.auth.presentation.streams.pending_action import PendingActionStream

app_name = 'auth'
urlpatterns = [
    path(
        'auth/login/',
        view=LoginView.as_view(),
        name='login',
    ),
    path(
        'auth/register/',
        view=RegisterView.as_view(),
        name='register',
    ),
    path(
        'auth/reset-password/',
        ResetPasswordRequestView.as_view(),
        name='reset-password',
    ),
    path(
        'auth/reset-password/perform/',
        ResetPasswordPerformView.as_view(),
        name='reset-password-perform',
    ),
    path(
        'auth/actions/email-verification/',
        PerformEmailVerificationView.as_view(),
        name='email-verification',
    ),
    path(
        'auth/actions/phone-verification/',
        PerformPhoneVerificationView.as_view(),
        name='phone-verification',
    ),
    path(
        'auth/actions/state/',
        ExchangePendingActionView.as_view(),
        name='state',
    ),
    # ~ STREAMS
    path(
        'streams/pending-actions/<str:stream_token>/',
        view=PendingActionStream.as_view(),
        name='pending-actions-stream',
    ),
]
