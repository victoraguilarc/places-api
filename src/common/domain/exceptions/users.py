from src.common.domain.exceptions.common import NotFound, Forbidden


class UserNotFound(NotFound):
    pass


class NotEnoughTenantPermissions(Forbidden):
    pass
