from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # 이메일 주소, 비밀번호, 닉네임, 사용자아이디
    nickname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(delf):
        return self.username