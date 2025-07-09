from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'), 
    #views.post_list를 보여주도록 함. name은 URL에 붙인 이름
]