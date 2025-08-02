from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Custom field names can be defined here
    # For example, if you want to change the field names in the serialized output
    name_changed = serializers.CharField(source='name')
    brand_new = serializers.CharField(source='brand')
    #you can change the fields to include more attributes if needed
    price_new = serializers.SerializerMethodField(method_name='price_vnd',read_only=True)
    
    class Meta:   
        model = Product
        fields = ['id', 'name_changed', 'brand_new', 'price', 'price_new']
        extra_kwargs = {
            'price': {'min_value': 0, 'max_value': 10000},
            'stock': {'min_value': 0,}
        }
        
    def validate_price(self, value):
        if value < 2:
            raise serializers.ValidationError('Price should not be less than 2.0')
        return value  # Return value if it passes validation

    def validate(self, attrs):
         if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
         if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
         return super().validate(attrs)
     
     # Unique validation
     # make sure that the product name is unique
    # from rest_framework.validators import UniqueValidator
    
    # extra_kwargs = {
    #     'title': {
    #         'validators': [
    #             UniqueValidator(
    #                 queryset=MenuItem.objects.all()
    #             )
    #         ]
    #     }
    # }
    
    # title = serializers.CharField(
    #     max_length=255,
    #     validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    # )
    
    
    # from rest_framework.validators import UniqueTogetherValidator
    # validators = [
    #     UniqueTogetherValidator(
    #         queryset=MenuItem.objects.all(),
    #         fields=['title', 'price']
    #     )
    # ]

    def price_vnd(self, product: Product):
        # Assuming you want to convert price to VND
        conversion_rate = 25000
        return product.price * conversion_rate