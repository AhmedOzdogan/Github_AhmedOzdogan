from rest_framework import serializers
from .models import MenuItem, Cart, OrderItem, Order

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']
        read_only_fields = ['unit_price', 'price']

    def create(self, validated_data):
        user = self.context['request'].user
        menuitem = validated_data['menuitem']
        quantity = validated_data['quantity']
        unit_price = menuitem.price
        total_price = unit_price * quantity

        return Cart.objects.create(
            user=user,
            menuitem=menuitem,
            quantity=quantity,
            unit_price=unit_price,
            price=total_price
        )
        
class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = ['menuitem', 'quantity', 'unit_price', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'items']
        read_only_fields = ['user', 'total']