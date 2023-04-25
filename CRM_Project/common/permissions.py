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
    Allows access only to staff users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE', 'PUT', 'PATCH'] \
                and obj.owner == request.user:
            return True
        return False


class IsOwnerOrInProject(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET'] \
                and obj.owner == request.user:
            return True
        return False


class IsMyNotifications(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
