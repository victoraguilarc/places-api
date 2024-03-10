from src.common.domain import BaseEnum


class StudentEnrollmentProcessStatus(BaseEnum):
    CREATED = 'CREATED'
    PENDING_PAYMENT = 'PENDING_PAYMENT'
    EXCEMPTED = 'EXCEMPTED'
    EXPIRED = 'EXPIRED'
    CANCELLED = 'CANCELLED'
    COMPLETED = 'COMPLETED'
