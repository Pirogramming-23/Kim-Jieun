from django.shortcuts import render, redirect
from .models import Review, GENRES

# Create your views here.
def reviews_list(request):
    reviews = Review.objects.all()
    context = {"reviews" : reviews}
    return render(request, "reviews_list.html", context)

def reviews_read(request, pk):
    review = Review.objects.get(id=pk)
    hours = review.runningTime // 60
    minutes = review.runningTime % 60
    running_time = f"{hours}시간 {minutes}분"
    context = {"review" : review,
               "running_time": running_time}
    return render(request, "reviews_read.html", context)

def reviews_create(request):
    if request.method == "POST":
        Review.objects.create(
            title=request.POST["title"],
            release=request.POST["release"],
            rating=request.POST["rating"],
            runningTime=request.POST["runningTime"],
            content=request.POST["content"],
            director=request.POST["director"],
            actor=request.POST["actor"],
        )
        return redirect("/posts/")
    return render(request, "reviews_create.html", {'genres': GENRES})

def reviews_update(request, pk):
    review = Review.objects.get(id=pk)
    
    if request.method == "POST":
        review.title=request.POST["title"]
        review.release=request.POST["release"]
        review.genre=request.POST["genre"]
        review.rating=request.POST["rating"]
        review.runningTime=request.POST["runningTime"]
        review.content=request.POST["content"]
        review.director=request.POST["director"]
        review.actor=request.POST["actor"]
        review.save()
        return redirect(f"/posts/{pk}/")
    
    context = {"review": review,
               'genres': GENRES}
    return render(request, "reviews_update.html", context)

def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/posts/")