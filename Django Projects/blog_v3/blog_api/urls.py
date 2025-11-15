from django.urls import path
from blog_api import views

urlpatterns = [

    # -----------------------------------
    #               USERS
    # -----------------------------------
    path('users/register/', views.register_user, name='user-register'),

    # -----------------------------------
    #               CATEGORIES
    # -----------------------------------
    
    path('categories/', views.categories, name='category-list'),
    
    # -----------------------------------
    #               POSTS
    # -----------------------------------
    # List all posts OR create post
    path('posts/', views.posts, name='post-list'),
    path('posts/<int:post_id>/detail/', views.posts_with_comments, name='post-detail'),
    path('posts/create/', views.create_post, name='post-create'),

    # Retrieve / Update / Delete a single post
    path('posts/edit/<int:post_id>/', views.update_delete_post, name='post-edit'),

    # -----------------------------------
    #             COMMENTS
    # -----------------------------------
    # List or create comments for a post
    path('posts/<int:post_id>/comments/', views.see_or_create_comments, name='comment-list-create'),

    # Modify a specific comment
    path('comments/<int:comment_id>/', views.modify_comment, name='comment-detail'),
]
