from rest_framework.permissions import BasePermission


class TemporaryPasswordChanged(BasePermission):
    """
    Allows access only to users who changed temporary password.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.password_changed)
