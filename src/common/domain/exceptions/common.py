class DomainException(Exception):
    pass


class NotFound(DomainException):
    pass


class BadRequest(DomainException):
    pass


class Forbidden(DomainException):
    pass


class UnAuthenticated(DomainException):
    pass


class EmailIsAlreadyUsed(BadRequest):
    pass


class DomainEmptyPage(BadRequest):
    pass
