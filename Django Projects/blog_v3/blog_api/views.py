from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import User, Category, Post, Comment
from .serializers import (
    UserSerializer,
    CategorySerializer,
    PostSerializer,
    CommentSerializer
)

from .permissions import (
    IsNotBlocked,
    CanCreatePost,
    IsOwnerOrAdmin,
    IsAdminForApproval
)

# ------------------------------------------------------------
#                 USER REGISTRATION
# ------------------------------------------------------------

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({'error': 'Username, password, and email required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        role='reader'    # default role
    )
    return Response({'message': 'User created successfully'}, status=201)


# ------------------------------------------------------------
#                         POSTS
# ------------------------------------------------------------

@api_view(['GET'])
@permission_classes([AllowAny])
def posts(request, post_id=None):
    """ List posts or retrieve a single post """
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def posts_with_comments(request, post_id):
    """ Retrieve a single post with its comments """
    post = get_object_or_404(Post, id=post_id)
    post_serializer = PostSerializer(post)
    comments = Comment.objects.filter(post=post)
    comment_serializer = CommentSerializer(comments, many=True)

    data = post_serializer.data
    data['comments'] = comment_serializer.data #type: ignore

    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsNotBlocked, CanCreatePost])
def create_post(request):
    """ Editor or admin can create a post """
    serializer = PostSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsNotBlocked])
def update_delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    owner_perm = IsOwnerOrAdmin()

    if not owner_perm.has_object_permission(request, None, post):
        return Response({"error": "Not allowed"}, status=403)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': 'Post deleted successfully'}, status=204)


# ------------------------------------------------------------
#                        COMMENTS
# ------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes([IsNotBlocked])
def see_or_create_comments(request, post_id):
    """ Anyone can see comments, only authenticated can create """
    if request.method == 'GET':
        comments = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error': 'Login required'}, status=401)

        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(created_by=request.user, post=post)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated, IsNotBlocked, IsAdminForApproval])
def modify_comment(request, comment_id):
    """ Owner or admin can edit/delete. Admin can approve. """
    comment = get_object_or_404(Comment, id=comment_id)
    owner_perm = IsOwnerOrAdmin()

    if not owner_perm.has_object_permission(request, None, comment):
        return Response({'error': 'Not allowed'}, status=403)

    # UPDATE
    if request.method in ['PUT', 'PATCH']:
        serializer = CommentSerializer(
            comment,
            data=request.data,
            partial=(request.method == 'PATCH')
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message': 'Comment deleted successfully'}, status=204)

# ------------------------------------------------------------
#                        Categories
# ------------------------------------------------------------

@api_view(['GET'])
@permission_classes([AllowAny])
def categories(request):
    """ List all categories """
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)