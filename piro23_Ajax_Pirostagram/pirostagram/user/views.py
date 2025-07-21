from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm

# Create your views here.

# login - 로그인 부분(기능)
def login_view(request):
    if request.user.is_authenticated:
        return redirect('post:home') # 로그인 된 상태: 홈화면으로 이동
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('post:home')
        else:
            form.add_error(None, "아이디 또는 비밀번호가 올바르지 않습니다.")
            context = {
                'form': form
            }
            return render(request, 'user/hello_index.html', context)
    
    else:
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request, 'user/hello_index.html', context)
    

# join - 회원가입 부분(기능)
def join_view(request):
    if request.method == 'GET':
        form = UserForm()
        context={
            'form': form
        }
        return render(request, 'user/join_index.html', context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login_view')
        else:
            return render(request, 'user/join_index.html', {'form': form})
        
def logout_view(request):
    logout(request)
    return redirect('user:login_view')