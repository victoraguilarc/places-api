from typing import Callable

import pytest
from pytest_django.lazy_django import skip_if_no_django
from rest_framework_simplejwt.tokens import RefreshToken, Token

from rest_framework.test import APIClient

from src.common.database.models import UserORM


@pytest.fixture()
def api_client() -> APIClient:
    skip_if_no_django()
    return APIClient()


@pytest.fixture()
def api_client_factory(
    api_client: APIClient,
    user_orm: UserORM,
) -> Callable:
    def _api_client_factory(
        authenticated: bool = False,
    ) -> APIClient:
        refresh_token: Token = RefreshToken.for_user(user_orm)
        access_token = 'Bearer {0}'.format(str(refresh_token.access_token))

        if authenticated:
            api_client.credentials(HTTP_AUTHORIZATION=access_token)

        return api_client

    return _api_client_factory


@pytest.fixture()
def auth_api_client(api_client_factory) -> APIClient:
    return api_client_factory(authenticated=True)


@pytest.fixture()
def tenant_api_client(api_client_factory) -> APIClient:
    return api_client_factory(
        authenticated=True,
        has_tenant=True,
    )


@pytest.fixture()
def owner_api_client(api_client_factory) -> APIClient:
    return api_client_factory(
        authenticated=True,
        has_tenant=True,
        is_owner=True,
    )


@pytest.fixture()
def unauthorized_api_client(
    api_client_factory: Callable,
) -> APIClient:
    return api_client_factory(
        authenticated=True,
        has_tenant=True,
    )


@pytest.fixture()
def external_api_client(
    api_client_factory: Callable,
) -> APIClient:
    return api_client_factory(
        authenticated=True,
        has_tenant=True,
    )
