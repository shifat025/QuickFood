from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsOwner(BasePermission):
    """
    Custom permission to allow only owners to add, get, or delete restaurants.
    """

    def has_permission(self, request, view):
        # Allow access only to owners (users with is_superuser=True)
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to access the specific restaurant (obj).
        """
        # Only allow owners to access their own restaurants
        if request.user.is_superuser and obj.owner == request.user:
            return True
        raise PermissionDenied("You do not have permission to perform this action.")
