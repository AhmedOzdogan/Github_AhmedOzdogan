from django.db import models
from django.contrib.auth.models import AbstractUser


# --------------------------
# Custom User
# --------------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('reader', 'Reader'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


# --------------------------
# Category Model
# --------------------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# --------------------------
# Post Model
# --------------------------
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # This is the *real book author*, not a user
    book_author = models.CharField(max_length=200, default='Unknown Author')

    # This is the user who created the post
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts_created'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# --------------------------
# Comment Model
# --------------------------
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    content = models.TextField()

    # This is the user who wrote the comment
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments_written'
    )

    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
