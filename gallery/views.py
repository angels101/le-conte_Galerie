from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Image, Location
import datetime as dt 

# Create your views here.
def main_flikr(request):
    images= Image.all_images()
    location = Location.objects.all()
    return render(request,'index.html',{"images":images,"locations":location})

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    return render(request, 'location.html', {"location":selected_location,"locations":locations,"images":images})


def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        return render(request,'search.html',{"images":searched_images,"category":search_term})

