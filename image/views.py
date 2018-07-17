from django.shortcuts import render,render_to_response,redirect
from django.template.loader import render_to_string
from .models import Gallerie,Location,Categorie
import json

# Create your views here.

def images(request):
    images = Gallerie.objects.all()
    categories = Categorie.objects.all()
    location = Location.objects.all()

    return render(request,'images/index.html',{'images':images,'categories':categories,'location':location})


def image_by_location(request):
    name = Location.name
    location = Location.objects.all()
    category = Categorie.objects.all()
    if 'location' in request.GET and request.GET['location']:
        search_category = request.GET.get('location')
        images_location = Gallerie.get_gallerie_by_location(search_category)
        print(images_location)
        message = f'{search_category}'

        return render(request,'images/location.html',{'images_location':images_location,'message':message, 'name':name, 'category':category,'location':location})
    else:
        return render(request, 'images/location.html')


def search_results(request):
    category = Categorie.objects.all()
    location = Location.objects.all()
    if 'image' in request.GET and request.GET['image']:
        search_category = request.GET.get('image')
        images_result = Gallerie.get_gallerie_by_category(search_category)
        print(images_result)
        message = f'{search_category}'

        return render(request,'images/search.html',{'images_result':images_result,'message':message,'category':category,'location':location})

    else:

        return render(request,'images/search.html')

def display_details(request,id):
    category = Categorie.objects.all()
    location = Location.objects.all()
    images = Gallerie.get_gallerie_by_id(id)

    return render(request,'images/SingleImage.html',{'images':images,'category':category,'location':location})
