from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOnly(BasePermission):
    """Allows access only to admin users."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
        )


class AuthorOrAdminOnly(BasePermission):
    """Allows access to authors or admins."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ['author', 'admin']
        )


class AuthorOnly(BasePermission):
    """Allows only authors."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'author'
        )


class IsAuthorOrReadOnly(BasePermission):
    """
    Read: anyone.
    Write: only the user who created the post.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user  


class IsCommentAuthorOrReadOnly(BasePermission):
    """
    Read: anyone.
    Write: only the user who created the comment.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user  
