from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow read-only access for everyone
        return request.user and request.user.is_staff  # Only allow admin and staff to create, update, delete
