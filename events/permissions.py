from rest_framework.permissions import BasePermission


class CreateOnly(BasePermission):
    """
    Create-only request.
    """
    SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        return bool(
            request.method in self.SAFE_METHODS
        )


class ReadOnly(BasePermission):
    """
    Read-only request.
    """
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        return bool(
            request.method in self.SAFE_METHODS
        )
