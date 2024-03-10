# -*- coding: utf-8 -*-

from rest_framework import status

from src.common.database.models import TenantORM
from src.common.database.models.factories.tenant import TenantORMFactory


class TenantTesCase:
    tenant = None

    def setup_tenant(self, tenant: TenantORM = None):
        self.tenant = tenant or TenantORMFactory(slug='tenant')

    def setup_tenant_exception(self):
        self.tenant = TenantORMFactory(slug='tenant')

    def assert_done_response(self, response, code):
        response_json = response.json()
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]
        assert ['data', 'datetime'] == list(response_json.keys())
        assert ['code', 'message'] == list(response_json['data'])
        assert response_json['data']['code'] == code

    def assert_validation_code(self, response_json, attribute, code):
        """Utility to validate the standar error code."""
        assert 'validation' in response_json
        assert attribute in response_json['validation']
        assert response_json['validation'][attribute]
        assert response_json['validation'][attribute][0]['code'] == code

    def assert_error_code(self, response_json, code):
        """Utility to check any error code inside errors."""
        assert 'errors' in response_json
        assert response_json['errors']
        assert response_json['errors'][0]['code'] == code

    def assert_unauthorized(self, response):
        """Checks if the status code is unauthorized."""
        response_json = response.json()
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        self.assert_error_code(response_json, 'not_authenticated')
