from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', login_view, name="first_view"),
    path('hello/', login_view, name="login_view"),  # 로그인 페이지
    path('join/', join_view, name="join_view"),  # 회원가입 페이지
]
