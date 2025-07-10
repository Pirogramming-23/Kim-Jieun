from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", reviews_list),
    path("posts/<int:pk>/", reviews_read),
]