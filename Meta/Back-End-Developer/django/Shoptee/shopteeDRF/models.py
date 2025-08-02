from django.db import models # type: ignore
class Product(models.Model):

    CATEGORY_CHOICES = [
        ("Electronics", "Electronics"),
        ("Clothing", "Clothing"),
        ("Books", "Books"),
        ("Home Appliances", "Home Appliances"),
    ]

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    
    


    def __str__(self):
        return f"{self.name} | {self.brand} | {self.category} | ${self.price} | Stock: {self.stock}"
