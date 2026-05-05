from rest_framework import permissions


class IsPublic(permissions.BasePermission):
    """
    Permite acceso público (sin autenticación)
    """
    def has_permission(self, request, view):
        return True


class IsPublicOrAdmin(permissions.BasePermission):
    """
    Permite acceso público para lectura, solo admin para escritura
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff