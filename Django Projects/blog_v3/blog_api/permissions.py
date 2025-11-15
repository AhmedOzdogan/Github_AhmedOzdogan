from rest_framework import permissions

# -----------------------------
# Block banned users globally
# -----------------------------

class IsNotBlocked(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return True  # allow unauthenticated GET
        return not request.user.blocked


# -----------------------------------------------------------
# Only admins or editors can create posts (books)
# -----------------------------------------------------------

class CanCreatePost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'POST':
            return True
        return request.user.is_authenticated and request.user.role in ['admin', 'editor']


# -----------------------------------------------------------
# Owners of objects OR admins can edit/delete
# -----------------------------------------------------------

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user or request.user.role == 'admin'


# -----------------------------------------------------------
# Only admin may approve comments
# PATCH and approved in request.data
# -----------------------------------------------------------

class IsAdminForApproval(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PATCH' and 'approved' in request.data:
            return request.user.role == 'admin'
        return True
