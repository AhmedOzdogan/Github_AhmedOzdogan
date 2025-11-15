from django.urls import path
from blog_api import views

urlpatterns = [
    # -------------------- USERS --------------------
    path('register/', views.register_user, name='register_user'),
    
    # -------------------- POSTS --------------------
    path('posts/', views.posts, name='posts_list'),
    path('posts/<int:post_id>/', views.posts, name='post_detail'),

    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/modify/', views.modify_post, name='modify_post'),

    # ------------------- COMMENTS -------------------
    path('posts/<int:post_id>/comments/', views.comments, name='post_comments'),
    path('posts/<int:post_id>/comments/<int:comment_id>/modify/', views.modify_comment, name='modify_comment'),

    # Approve / Disapprove
    path('posts/<int:post_id>/comments/<int:comment_id>/approve/', views.approve_comment, name='approve_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/disapprove/', views.disapprove_comment, name='disapprove_comment'),
]
