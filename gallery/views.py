from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image, Location
# Create your views here.
def main_flikr(request):
    images= Image.all_images()
    location = Location.objects.all()
    return render(request, 'index.html',)