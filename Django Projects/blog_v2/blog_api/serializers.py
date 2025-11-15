from rest_framework import serializers
from blog_api.models import User, Category, Post, Comment


# ---------------- USER ----------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


# ---------------- CATEGORY ----------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


# ---------------- POST ----------------
class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

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
            'updated_at'
        ]
# ---------------- COMMENT ----------------
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
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
            'author',
            'approved',
            'created_at'
        ]
        read_only_fields = ['approved'] 
