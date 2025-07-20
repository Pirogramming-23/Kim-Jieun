from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('home/', home, name='home'),
    path('create/', create_post, name='create_post')
]
