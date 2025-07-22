from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('home/', home, name='home'),
    path('create/', create_post, name='create_post'),
    path('detail/<int:pk>/', post_detail, name='post_detail'),
    path('like_ajax/', like_ajax, name="like_ajax"),
    path('comment_ajax/', comment_ajax, name="comment_ajax"),
    path('add_comment/', add_comment, name="add_comment"),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('delete_comment/<int:pk>/', delete_comment, name='delete_comment'),
]
