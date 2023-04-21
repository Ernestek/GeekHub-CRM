from rest_framework.permissions import BasePermission


class TemporaryPasswordChanged(BasePermission):
    """
    Allows access only to users who changed temporary password.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.password_changed)


class IsStaffOrAssigned(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE', 'PUT', 'PATCH'] and \
                (request.user.is_staff or obj.user_assigned == request.user):
            return True
        return False


class IsStaff(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
