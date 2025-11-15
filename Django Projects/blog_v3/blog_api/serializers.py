from rest_framework import serializers
from .models import User, Category, Post, Comment
from blog_api.models import User, Category, Post, Comment

# --------------------------
# User Serializer
# --------------------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'blocked'] 
        
        
        
# --------------------------
# Category Serializer
# --------------------------

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']
        
# --------------------------
# Comment Serializer
# --------------------------


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        source='post',
        write_only=True
    )

    class Meta:
        model = Comment
        fields = [
            'id',
            'post_id',
            'content',
            'created_by',
            'approved',
            'created_at'
        ]

# --------------------------
# Post Serializer
# --------------------------


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'book_author',      
            'created_by',
            'category',
            'category_id',
            'created_at',
            'updated_at',
            'comments'
        ]
        