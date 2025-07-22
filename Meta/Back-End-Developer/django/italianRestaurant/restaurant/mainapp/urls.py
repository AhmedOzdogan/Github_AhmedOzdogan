from django.urls import path, re_path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.ContactView.as_view(), name='contact'), 
    re_path(r'^menu/item/(?P<item_id>\d+)/$', views.menu_item_detail, name='menu_item_detail'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('reservations/', views.reservations, name='reservations'),
]
