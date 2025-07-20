from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, PostImgContent

# Create your views here.
def home(request):
    
    return render(request, 'post/home.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            txt = form.cleaned_data['txtContent']
            images = request.FILES.getlist('images')

            post = Post.objects.create(author=request.user, txtContent=txt)

            for img in images:
                PostImgContent.objects.create(post=post, image=img)
            
            return redirect('post:list')
    else:
        form = PostForm()
        
    return render(request, 'post/create.html', {'form':form})