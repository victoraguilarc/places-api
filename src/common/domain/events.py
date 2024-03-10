from src.common.domain import BaseEnum


class UserEvent(BaseEnum):
    EMAIL_VERIFIED = 'User.EmailVerified'


class TenantCustomerEvent(BaseEnum):
    UPDATED = 'TenantCustomer.Updated'
    MEMBERSHIP_UPDATED = 'TenantCustomer.MembershipUpdated'


class PendingActionEvent(BaseEnum):
    UPDATED = 'PendingAction.Updated'


class PaymentIntentEvent(BaseEnum):
    UPDATED = 'PaymentIntent.Updated'


class StudentEnrollmentProcessEvent(BaseEnum):
    UPDATED = 'StudentEnrollmentProcess.Updated'


class MembershipPurchaseEvent(BaseEnum):
    UPDATED = 'MembershipPurchase.Updated'


class MembershipChangeEvent(BaseEnum):
    UPDATED = 'MembershipChange.Updated'
