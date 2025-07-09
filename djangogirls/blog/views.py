from django.shortcuts import render

# view : app의 로직을 넣는 곳
def post_list(request):
    return render(request, 'blog/post_list.html', {})