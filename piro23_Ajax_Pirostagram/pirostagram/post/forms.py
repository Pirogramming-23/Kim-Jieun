from django import forms
from .models import Post, PostImgContent

class PostForm(forms.Form):
    txtContent = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': '내용을 입력하세요'}),
        label='내용'
    )
