from django.shortcuts import render, redirect
from .models import Idea, IdeaStar
from .forms import IdeaForm
from django.http import JsonResponse

# Create your views here.

def main(request):
    ideas = Idea.objects.all()
    stars = IdeaStar.objects.all()
    context = {
        'ideas': ideas,
        'stars': stars,
    }
    return render(request, 'posts/ideaList.html', context=context)

def create(request):
    if request.method == 'GET':
        form = IdeaForm()
        context = { 'form': form }
        return render(request, 'posts/ideaPosts.html', context=context)
    else:
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')

def detail(request, pk):
    target_idea = Idea.objects.get(id=pk)
    idea_star, created = IdeaStar.objects.get_or_create(idea=target_idea)
    
    context = { 'idea': target_idea, 'is_starred': idea_star,}
    return render(request, 'posts/ideaDetail.html', context=context)

def delete(request, pk):
    item = Idea.objects.get(id=pk)
    item.delete()
    return redirect('/')

def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        context = {
            'form': form, 
            'pk': pk,
            'idea': idea,
        }
        return render(request, 'posts/ideaUpdate.html', context=context)
    else:
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
        return redirect('posts:detail', pk=pk)
    
def star_status(request):
    ideas = Idea.objects.all()
    status = {}
    for idea in ideas:
        starred_obj = IdeaStar.objects.filter(idea=idea).first()
        status[str(idea.pk)] = starred_obj.starred if starred_obj else False

    return JsonResponse(status)

def star(request, pk):
    idea = Idea.objects.get(id=pk)
    
    idea_star, created = IdeaStar.objects.get_or_create(idea=idea)
    idea_star.starred = not idea_star.starred
    idea_star.save()
    
    return JsonResponse({str(idea.pk): idea_star.starred})


def update_interest(request, pk):
    idea = Idea.objects.get(pk=pk)
    delta = int(request.GET.get('delta', 0))
    print("Before:", idea.interest, "Delta:", delta)
    idea.interest = max(0, idea.interest + delta)
    idea.save()
    print("After:", idea.interest)
    return JsonResponse({'updated_interest': idea.interest})