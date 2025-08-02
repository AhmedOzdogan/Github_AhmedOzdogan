from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})" # type: ignore
    
    class Meta:
        permissions = (
            ("can_view_menu", "Can view menu items"),
            ("can_edit_menu", "Can edit menu items"),
            ("can_delete_menu", "Can delete menu items"),
        )