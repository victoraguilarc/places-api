from src.common.domain.exceptions.common import Forbidden, NotFound


class UserNotFound(NotFound):
    pass


class NotEnoughTenantPermissions(Forbidden):
    pass
