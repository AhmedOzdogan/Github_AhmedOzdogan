from rest_framework import generics
from .models import MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, CartSerializer, OrderSerializer
from .permissions import ReadOnlyOrManager, IsManager, IsCustomer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Order, OrderItem, Cart
from .serializers import OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager, IsCustomer
from rest_framework.response import Response
from rest_framework import serializers


class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrManager]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['price', 'inventory']
    ordering_fields = ['price', 'title']
    search_fields = ['title']

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrManager]
    
# Utility function
def get_group(name):
    return Group.objects.get(name=name)

# Base view for group management
class GroupUserList(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    group_name = None  # to be overridden

    def get(self, request):
        group = get_group(self.group_name)
        users = group.user_set.all()
        data = [{"id": u.id, "username": u.username, "email": u.email} for u in users] #type: ignore
        return Response(data)

    def post(self, request):
        user_id = request.data.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            group = get_group(self.group_name)
            group.user_set.add(user)
            return Response({"message": f"User {user.username} added to {self.group_name}"}, status=201)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

class GroupUserDetail(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    group_name = None  # to be overridden

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            group = get_group(self.group_name)
            group.user_set.remove(user)
            return Response({"message": f"User {user.username} removed from {self.group_name}"})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        
class ManagerGroupUsers(GroupUserList):
    group_name = 'Manager'

class ManagerGroupUserDetail(GroupUserDetail):
    group_name = 'Manager'

class DeliveryCrewGroupUsers(GroupUserList):
    group_name = 'Delivery_Crew'

class DeliveryCrewGroupUserDetail(GroupUserDetail):
    group_name = 'Delivery_Crew'
    
    
class CartMenuItemView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartMenuItemDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def delete(self, request, *args, **kwargs):
        Cart.objects.filter(user=request.user).delete()
        return Response({"message": "Cart cleared."}, status=204)


# Create & list orders
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'date']
    ordering_fields = ['date', 'total']

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return Order.objects.all()
        elif user.groups.filter(name='delivery_crew').exists():
            return Order.objects.filter(delivery_crew=user)
        else:
            return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        cart_items = Cart.objects.filter(user=user)
        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty")

        order = serializer.save(user=user, total=0)
        total = 0
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                menuitem=item.menuitem,
                quantity=item.quantity,
                unit_price=item.unitprice,
                price=item.price
            )
            total += item.price
        order.total = total
        order.save()
        cart_items.delete()

# Retrieve, update, delete single order
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return obj
        elif user.groups.filter(name='delivery_crew').exists():
            if obj.delivery_crew != user:
                self.permission_denied(self.request, message="Not your order")
            return obj
        elif obj.user == user:
            return obj
        self.permission_denied(self.request, message="You do not have access")

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        user = request.user

        if user.groups.filter(name='manager').exists():
            # Allow assigning delivery crew and setting status
            data = request.data
            if "delivery_crew" in data:
                try:
                    crew = User.objects.get(id=data["delivery_crew"])
                    if not crew.groups.filter(name='delivery_crew').exists():
                        return Response({"error": "User is not in delivery crew"}, status=400)
                    order.delivery_crew = crew
                except User.DoesNotExist:
                    return Response({"error": "User not found"}, status=404)
            if "status" in data:
                order.status = bool(data["status"])
            order.save()
            return Response(OrderSerializer(order).data)
        elif user.groups.filter(name='delivery_crew').exists():
            # Can only change status
            if "status" in request.data:
                order.status = bool(request.data["status"])
                order.save()
                return Response(OrderSerializer(order).data)
            return Response({"error": "You can only update status"}, status=403)
        return Response({"error": "Not allowed"}, status=403)