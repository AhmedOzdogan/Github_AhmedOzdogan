from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_by', 'created_at']
