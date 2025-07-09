from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'), 
    #views.post_list를 보여주도록 함. name은 URL에 붙인 이름
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # url이 post 문자를 포함해야 함/int 형으로 기대되는 pk 변수를 뷰로 전송
]