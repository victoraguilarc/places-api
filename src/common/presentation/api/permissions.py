# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwner(BasePermission):
    """Checks if the object's owner is a certain user."""

    def has_object_permission(self, request, view, obj):
        """Checks the object permissions."""
        return obj.user == request.user


class IsSuperUser(IsAuthenticated):
    """Checks if the user has permissions as superuser."""

    def has_permission(self, request, view, obj=None):
        """Checks if the user has permissions."""
        return request.user and request.user.is_authenticated and request.user.is_superuser


class IsTenantAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        has_authenticated_user = bool(request.user and request.user.is_authenticated)
        tenant_customer_exists = view.membership is not None
        return has_authenticated_user and tenant_customer_exists


class IsTenantCustomerActive(IsTenantAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        has_authenticated_user = super().has_permission(request, view)
        return has_authenticated_user and view.membership.is_active


class IsTenantOwnerOfStaff(IsTenantAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        has_authenticated_user = super().has_permission(request, view)
        return (
            has_authenticated_user
            and view.tenant
            and (
                (view.membership.uuid == request.user.uuid)
                or (view.membership and view.membership.is_staff)
            )
        )
