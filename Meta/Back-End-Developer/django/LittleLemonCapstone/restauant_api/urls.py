from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, MenuItemsView, SingleMenuItemView, BookingViewSet, msg
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = router.urls

urlpatterns += [
    path('menu-items/', MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('bookings/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('message/', msg, name='protected-message'),
    path('api-token-auth/', obtain_auth_token)
]