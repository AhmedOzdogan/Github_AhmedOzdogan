from django.urls import path
from . import views
from .views import (
    ManagerGroupUsers,
    ManagerGroupUserDetail,
    DeliveryCrewGroupUsers,
    DeliveryCrewGroupUserDetail,
    CartMenuItemView,
    CartMenuItemDeleteView
)

urlpatterns = [
    path('menu-items/', views.MenuItemList.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.MenuItemDetail.as_view(), name='menu-item-detail'),
    path('groups/manager/users', ManagerGroupUsers.as_view()),
    path('groups/manager/users/<int:user_id>', ManagerGroupUserDetail.as_view()),

    path('groups/delivery-crew/users', DeliveryCrewGroupUsers.as_view()),
    path('groups/delivery-crew/users/<int:user_id>', DeliveryCrewGroupUserDetail.as_view()),
    
    path('cart/menu-items', CartMenuItemView.as_view(), name='cart-view'),
    path('cart/menu-items/delete', CartMenuItemDeleteView.as_view(), name='cart-delete'),
]
