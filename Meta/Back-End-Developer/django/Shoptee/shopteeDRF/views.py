from urllib import request
from django.shortcuts import render
from django.http import JsonResponse 
from .models import Product 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.decorators import api_view 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from django.core.paginator import Paginator, EmptyPage

@csrf_exempt
def products(request):
    
    if request.method == 'GET':
        products = Product.objects.all()
        return JsonResponse({
            'products': list(products.values())
        })
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        picture = request.FILES.get('picture')
        stock = request.POST.get('stock')
        
        product = Product.objects.create(
            name=name,
            brand=brand,
            category=category,
            description=description,
            price=price,
            picture=picture,
            stock=stock
        )   
        
        try:
            product.save()
            return JsonResponse({
                'message': 'Product created successfully',
                'product': {
                    'name': product.name,
                    'brand': product.brand,
                    'category': product.category,
                    'description': product.description,
                    'price': product.price,
                    'picture': product.picture.url if product.picture else None,
                    'stock': product.stock
                }
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'message': 'Error creating product',
                'error': str(e)
            }, status=400)
            
    return JsonResponse({'message': 'Method not allowed'}, status=405)

class ProductDetailView(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        category_names = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        perpage = int(request.query_params.get('perpage', 2))
        page = int(request.query_params.get('page', 1))

        if category_names:
            products = products.filter(category__in=category_names.split(','))

        if to_price:
            try:
                to_price = float(to_price)
                products = products.filter(price__lte=to_price)
            except ValueError:
                return Response({"error": "Invalid price value"}, status=400)
        if search:
            products = products.filter(name__icontains=search)
            # contains is case-insensitive, while icontains is case-sensitive
        if ordering:
            products = products.order_by(ordering)
            # price asc, -price desc, name asc, -name desc

        paginator = Paginator(products, perpage)
        try:
            products = paginator.page(page)
        except EmptyPage:
            products = []  # Return an empty list if the page is out of range

        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data}, status.HTTP_200_OK)

    def create(self, request):
        product = ProductSerializer(data=request.data)
        product.is_valid(raise_exception=True)
        product.save()
        return Response(product.data, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a product"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a product"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a product"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        return Response({"message":"Deleting a product"}, status.HTTP_200_OK)
    
    
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer  # Assuming you have a serializer defined for Product #type: ignore
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete']  # Specify allowed methods

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,throttle_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "This is a secret view"}, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def managerView(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "You are a manager"}, status=200)
    return Response({"message": "You are not a manager"}, status=403)

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
 
@api_view()
@throttle_classes([AnonRateThrottle])  # Apply throttling to this view
def throttlecheck(request):
    return Response({"message": "This is a throttle check view"}, status=200)


from .throttles import TenCallsPerMinute
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])  # Apply user throttling to this view
def userthrottlecheck(request):
    if request.user.is_authenticated:
        return Response({"message": "This is a user throttle check view"}, status=200)
    return Response({"message": "You are not authenticated"}, status=403)


# Service

# Anonymous

# Authenticated

# Facebook graph API

# X

# 200/hour

# Instagram API

# X

# 200/hour

# Instagram messenger API

# X

# 100/second

# WhatsApp messaging API

# X

# 80/second