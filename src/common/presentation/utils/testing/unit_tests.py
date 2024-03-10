# -*- coding: utf-8 -*-

from django.core import mail

from rest_framework import status


def mail_outbox():
    """It helps to test if any email message was sended."""
    return len(mail.outbox)


def has_same_code(item1, item2):
    """It helps to checl if two responses has the same error code."""
    return (
        isinstance(item1, dict)
        and isinstance(item2, dict)
        and item1.get('code') == item2.get('code')
    )


def has_response_format(response):
    """Checks if a dict has formatted error code."""
    response_json = response.json()
    return list(response_json.keys()) == ['code', 'message']
