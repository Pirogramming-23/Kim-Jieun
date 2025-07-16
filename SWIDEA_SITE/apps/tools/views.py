from django.shortcuts import render, redirect
from .models import Tool
from .forms import ToolForm

# Create your views here.

def main(request):
    tools = Tool.objects.all()
    
    context = {
        'tools': tools,
    }
    return render(request, 'tools/toolList.html', context=context)

def create(request):
    if request.method == 'GET':
        form = ToolForm()
        context = { 'form': form }
        return render(request, 'tools/toolPosts.html', context=context)
    else:
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('tools:main')

def detail(request, pk):
    target_tool = Tool.objects.get(id = pk)
    context = { 'tool': target_tool }
    return render(request, 'tools/toolDetail.html', context=context)

def delete(request, pk):
    item = Tool.objects.get(id=pk)
    item.delete()
    return redirect('tools:main')

def update(request, pk):
    item = Tool.objects.get(id=pk)
    if request.method == 'GET':
        form = ToolForm(instance=item)
        context = {
            'form': form, 
            'pk': pk,
            'tool': item,
        }
        return render(request, 'tools/toolUpdate.html', context=context)
    else:
        form = ToolForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
        return redirect('tools:detail', pk=pk)
