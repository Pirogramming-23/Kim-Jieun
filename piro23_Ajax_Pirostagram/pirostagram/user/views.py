from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# 첫 화면(로그인 화면)
def hello_index(request):
    if request.user.is_authenticated:
        return redirect('home') # 로그인 된 상태: 홈화면으로 이동
    
    if request.method == 'POST':
        account = request.POST.get('account')
        
        if account == 'login':
            userid = request.POST.get('userid')
            password = request.POST.get('password')
            
            userObject = authenticate(username = userid, password = password)
            
            if userObject is not None:
                login(request, userObject)
        
            else:
                # 로그인 실패 관련 문구 출력
                pass
        else:
            # 로그인 정보가 없으니 회원 가입을 진행해달라는 문구 출력
            pass
    else:
        pass
    
    return render(request, 'hello.html', {'form': form})