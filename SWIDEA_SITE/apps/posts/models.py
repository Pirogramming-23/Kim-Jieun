from django.db import models
from django.utils import timezone
from apps.tools.models import Tool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('제목', max_length=30)
    image = models.ImageField("이미지", blank = True, upload_to='posts/%Y%m%d')
    content = models.CharField('내용', max_length=100)
    interest = models.IntegerField('관심도', default = 0)
    devtool = models.ForeignKey(Tool, verbose_name = '개발툴', on_delete = models.CASCADE)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # 수정일 때에만 갱신
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
	    return self.title

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, verbose_name = '아이디어', on_delete=models.CASCADE)
    starred = models.BooleanField('찜', default=False)