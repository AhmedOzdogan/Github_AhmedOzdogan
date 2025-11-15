

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User

from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly, AuthenticatedReadOnly

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=201)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly, AuthenticatedReadOnly])
def post_list(request, author=None):
    if request.method == 'GET':
        posts = Post.objects.filter(author__username=author).order_by('-created_at') if author else Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAuthorOrReadOnly | IsAdminOrReadOnly])
def is_admin(user):
    return user and user.is_staff


    