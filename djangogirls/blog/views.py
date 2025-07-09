from django.shortcuts import render
from django.utils import timezone
from .models import Post

# view : app의 로직을 넣는 곳
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})