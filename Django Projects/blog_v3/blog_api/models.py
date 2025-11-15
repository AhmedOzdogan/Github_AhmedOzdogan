from django.db import models
from django.contrib.auth.models import AbstractUser

# --------------------------
# Custom User
# --------------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('reader', 'Reader'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='reader')
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.username
 
# --------------------------
# Categories
# --------------------------

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, default='')

    def __str__(self):
        return self.name

# --------------------------
# Posts
# --------------------------
   
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    book_author = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_posts')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=['created_at'], name='created_at_idx'),
            models.Index(fields=['category'], name='category_idx'),
        ]



# --------------------------
# Comments
# --------------------------

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.created_by.username} on {self.post.title}'


