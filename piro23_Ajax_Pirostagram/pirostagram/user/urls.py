from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('hello/', hello_index, name="hello_index"),
    #path('join/', join_index, name="join_index"),
]
