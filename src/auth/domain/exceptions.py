# -*- coding: utf-8 -*-

from src.common.domain.exceptions.common import BadRequest, NotFound, UnAuthenticated


class InvalidCredentials(UnAuthenticated):
    pass


class InvalidCredentialsForTenant(UnAuthenticated):
    pass


class PictureNotFound(NotFound):
    pass


class InvalidPendingToken(BadRequest):
    pass


class CorruptedPendingAction(BadRequest):
    pass


class PendingActionNotFound(NotFound):
    pass
