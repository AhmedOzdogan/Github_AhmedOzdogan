from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class ReadOnlyOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Manager').exists()
    
class IsCustomer(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and
            not user.groups.filter(name__in=['manager', 'delivery_crew']).exists()
        )
        
class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='delivery_crew').exists()
