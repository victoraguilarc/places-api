# -*- coding: utf-8 -*-
import logging
from typing import Type

from django.utils.translation import gettext_lazy as _

from src.auth.domain.exceptions import (
    InvalidCredentials,
    InvalidCredentialsForTenant,
    InvalidPendingToken,
    PendingActionNotFound,
    PictureNotFound,
)
from src.common.domain.exceptions.common import (
    DomainEmptyPage,
    DomainException,
    EmailIsAlreadyUsed,
    UnAuthenticated,
)
from src.common.domain.exceptions.users import NotEnoughTenantPermissions, UserNotFound
from src.common.presentation.api.exceptions.base import (
    APIBadRequest,
    APIBaseException,
    APINotAuthenticated,
    APINotFound,
    APINotImplemented,
    APIPermissionDenied,
    APIUnauthorized,
    GenericError,
)

GENERIC_ERROR = GenericError(
    code='server_error',
    detail=_('Server Error'),
)

NOT_AUTHENTICATED = APINotAuthenticated(
    code='not_authenticated',
    detail=_('Authentication credentials were not provided.'),
)
INVALID_TOKEN = APINotAuthenticated(
    code='users.InvalidToken',
    detail=_('Invalid or Expired token'),
)
AUTHENTICATION_FAILED = APIUnauthorized(
    code='users.AuthenticationFailed',
    detail=_('Authentication Fails'),
)
TENANT_NOT_FOUND = APINotImplemented(
    code='common.TenantNotFound',
    detail=_('Tenant Not Found'),
)
TENANT_USER_NOT_FOUND = APINotFound(
    code='common.TenantUserNotFound',
    detail=_('Tenant User Not Found'),
)
TENANT_CUSTOMER_NOT_FOUND = APINotFound(
    code='common.TenantCustomerNotFound',
    detail=_('Tenant Customer Not Found'),
)
USER_NOT_FOUND = APINotFound(
    code='common.UserNotFound',
    detail=_('User Not Found'),
)
TENANT_ACCESS_UNAUTHORIZED = APIUnauthorized(
    code='common.TenantAccessUnauthorized',
    detail=_('Tenant Access Unauthorized'),
)
TENANT_ACTION_FORBIDDEN = APIPermissionDenied(
    code='common.TenantActionForbidden',
    detail=_('Has no enough permissions to perform this action'),
)
EMPTY_PAGE = APIBadRequest(
    code='common.EmptyPage',
    detail=_('There are no more items'),
)

error_codes = {
    UserNotFound: USER_NOT_FOUND,
    NotEnoughTenantPermissions: TENANT_ACTION_FORBIDDEN,
    DomainEmptyPage: EMPTY_PAGE,
    InvalidCredentials: APIUnauthorized(
        code='accounts.InvalidCredentials',
        detail=_('Invalid Credentials'),
    ),
    InvalidCredentialsForTenant: APIUnauthorized(
        code='accounts.InvalidCredentialsForTenant',
        detail=_('Invalid Credentials for Tenant'),
    ),
    PictureNotFound: APINotFound(
        code='common.PictureNotFound',
        detail=_('Picture Not Found'),
    ),
    InvalidPendingToken: APIBadRequest(
        code='accounts.InvalidPendingToken',
        detail=_('the provided token is invalid'),
    ),
    UnAuthenticated: NOT_AUTHENTICATED,
    EmailIsAlreadyUsed: APIBadRequest(
        code='users.EmailIsAlreadyUsed',
        detail=_('This email is already being used'),
    ),
    PendingActionNotFound: APINotFound(
        code='auth.PendingActionNotFound',
        detail=_('Pending Action not found'),
    ),
}


def get_error_code(error_class: Type[DomainException]) -> APIBaseException:
    error_instance = error_codes.get(error_class)
    if not error_instance:
        logging.error(error_class)
    return error_instance or GENERIC_ERROR
