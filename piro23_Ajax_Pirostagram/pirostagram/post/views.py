from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, PostImgContent, PostComment
from pirostagram.user.models import CustomUser
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    posts = Post.objects.annotate(comment_count=Count('comments'))
    users = CustomUser.objects.all()
    
    context = {
        'posts': posts,
        'users': users,
    }
    
    return render(request, 'post/home.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            txt = form.cleaned_data['txtContent']
            images = request.FILES.getlist('images')

            post = Post.objects.create(author=request.user, txtContent=txt)

            for img in images:
                PostImgContent.objects.create(post=post, image=img)
            
            return redirect('post:home')
    else:
        form = PostForm()
        
    return render(request, 'post/create.html', {'form':form})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    images = PostImgContent.objects.all()
    comments = PostComment.objects.filter(post=post)

    context = {
        'post': post,
        'images': images,
        'comments': comments,
    }
    
    return render(request, 'post/detail.html', context)
    
@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'id': post_id, 'likes': post.likes})

@csrf_exempt
def comment_ajax(request):
    req = json.loads(request.body)
    post_id = req.get('post_id')
    content = req.get('content')
    post = get_object_or_404(Post, id=post_id)
    comment = PostComment.objects.create(
        post=post,
        author=request.user,
        content=content
    )
    return JsonResponse({
        'id': comment.id,
        'post_id': comment.post.id,
        'content': comment.content,
        'author_username': comment.author.username,
    })

@csrf_exempt
def add_comment(request):
    req = json.loads(request.body)
    post_id = req.get('post_id')
    content = req.get('content')
    post = get_object_or_404(Post, id=post_id)
    comment = PostComment.objects.create(
        post=post,
        author=request.user,
        content=content
    )
    return JsonResponse({
        'id': comment.id,
        'post_id': comment.post.id,
        'content': comment.content,
        'author_username': comment.author.username,
    })
    
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post:home')

def delete_comment(request, pk):
    comment = get_object_or_404(PostComment, id=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post:post_detail', pk=post_pk)