from django.urls import path
from . import views

# urlpatterns = [
    #path('products', views.products, name='products'),
    # path('products', views.ProductDetailView.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #     }
    # )),
    # path('products/<int:pk>',views.ProductDetailView.as_view(
    #     {
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'patch': 'partial_update',
    #         'delete': 'destroy',
    #     }
    # ))
    
# ],

"""
After this mapping, you can access the  http://127.0.0.1:8000/api/products  
endpoint with GET and POST methods. While you can access the http://127.0.0.1:8000/api/products/1  
endpoint with GET, PUT, PATCH and DELETE.
This allows you to manage products using the Django REST Framework's viewsets, which simplifies the process of creating APIs.
"""

from rest_framework.routers import SimpleRouter
router = SimpleRouter(trailing_slash=False)
router.register('products', views.ProductDetailView, basename='products')
urlpatterns = router.urls



"""After mapping, you can access the api/products and api/products/1 endpoints with the same methods as in the previous example.

Did you notice that the argument trailing_slash=False was passed, instantiating the SimpleRouter object? Without this argument, your API endpoints will have a trailing slash. 
And, since you don’t want a trailing slash at the end of your API endpoints, you have to pass this argument."""


urlpatterns += [
    path('secret/', views.secret, name='secret'),
]

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # This endpoint allows users to obtain an authentication token
    path('manager/', views.managerView, name='manager'),
    path('throttlecheck/', views.throttlecheck, name='throttlecheck'),
    path('userthrottlecheck/', views.userthrottlecheck, name='userthrottlecheck'),
]