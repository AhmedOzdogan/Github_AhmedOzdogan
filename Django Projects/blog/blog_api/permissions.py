from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors of a blog post to edit it.
    Read-only permissions are allowed for any request.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the blog post.
        return obj.author == request.user
    
class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    Read-only permissions are allowed for any request.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users.
        return request.user and request.user.is_staff
class AuthenticatedReadOnly(BasePermission):
    """
    Custom permission to allow only authenticated users to have read-only access.
    """

    def has_permission(self, request, view):
        # Allow read-only methods, but only if user is authenticated
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Deny all write permissions
        return False