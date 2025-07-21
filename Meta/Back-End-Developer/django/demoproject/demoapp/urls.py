from django.urls import path
from . import views

app_name = 'demoapp'

urlpatterns = [
    path('', views.demo_home, name='demo_home'),
    path('login123/', views.login, name='login'),
    path('user/<int:user_id>/', views.user_home, name='user_home'),
    path('user/<str:user_name>/<int:user_id>/', views.user_profile, name='user_profile'),
    path('user_query/', views.qryview, name='qryview'),
]
