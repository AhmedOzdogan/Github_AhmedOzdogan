from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
            ("customer", "Customer"),
            ("manager", "Manager"),
            ("delivery", "Delivery Crew"),
        )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")    
        
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"