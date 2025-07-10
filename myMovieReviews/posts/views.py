from django.shortcuts import render
from .models import Review

# Create your views here.
def reviews_list(request):
    reviews = Review.objects.all()
    context = {"reviews" : reviews}
    return render(request, "reviews_list.html", context)

def reviews_read(request, pk):
    review = Review.objects.get(id=pk)
    context = {"review" : review}
    return render(request, "reviews_read.html", context)

def reviews_create(request):
    if request.method == "POST":
        Review.objects.create(
            title=request.POST["title"],
            release_year=request.POST["release_year"],
            rating=request.POST["rating"],
            runningTime=request.POST["runningTime"],
            content=request.POST["content"],
            director=request.POST["director"],
            actor=request.POST["actor"],
        )
        return redirect("/posts/")
    return render(request, "reviews_create.html")