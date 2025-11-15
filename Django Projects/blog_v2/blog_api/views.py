from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Post, Comment, User
from .serializers import PostSerializer, CommentSerializer
from .permissions import (
    IsAuthorOrReadOnly,
    IsCommentAuthorOrReadOnly,
    AuthorOnly,
    AdminOnly,
    AuthorOrAdminOnly  # Make sure name matches your permission class
)

# --------------------------------------------------
#                   USER REGISTRATION
# --------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role', 'reader')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        role=role
    )
    return Response({'message': 'User created successfully'}, status=201)


# --------------------------------------------------
#                   POST VIEWS
# --------------------------------------------------

@api_view(['GET'])
@permission_classes([AllowAny])
def posts(request, post_id=None):
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AuthorOrAdminOnly])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthorOrReadOnly])
def modify_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        post.delete()
        return Response(status=204)


# --------------------------------------------------
#                   COMMENT VIEWS
# --------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comments(request, post_id):

    if request.method == 'GET':
        queryset = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=401)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user, post_id=post_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsCommentAuthorOrReadOnly])
def modify_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        comment.delete()
        return Response(status=204)


@api_view(['PATCH'])
@permission_classes([AdminOnly])
def approve_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    comment.approved = True
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([AdminOnly])
def disapprove_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    comment.approved = False
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
