from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserForm(UserCreationForm):
    username = forms.CharField(label="사용자 아이디", max_length=30)
    nickname = forms.CharField(label="닉네임", max_length=20, required=False)
    email = forms.EmailField(label="이메일 주소")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'nickname',)
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if CustomUser.objects.filter(username=username).exclude(pk=self.instance.pk if self.instance else None).exists():
                raise forms.ValidationError("사용 불가능한 아이디 입니다.")
        return username

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="사용자 이름")
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)