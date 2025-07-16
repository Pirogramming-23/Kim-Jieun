from django.urls import path
from . import views
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    
    path('star_status/', views.star_status, name='star_status'),
    path('star/<int:pk>/', views.star, name='star'),
    path('interest/<int:pk>/', views.update_interest, name='update_interest'),
]