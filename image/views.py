from django.shortcuts import render,render_to_response,redirect
from django.template.loader import render_to_string
from .models import Gallery,Location,Category
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def images(request):
    images = Gallery.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()

    return render(request,'index.html',{'images':images,'categories':categories,'location':location})

# def image_by_location(request):
#     if request.method == "GET" and 'location_name' in request.GET and request.is_ajax():
#         location = request.GET['location_name']
#         images_loc = Image.get_image_by_location(location)

#         return render_to_response('gallery/location.html',{'images_loc':images_loc})

#     return redirect(all_images)

# def image_by_category(request):

#     if request.method == "GET" and 'category_name' in request.GET and request.is_ajax():
#         category = request.GET['category_name']
#         images_cat = Image.get_image_by_cat(category)

#         return render_to_response('gallery/category.html',{'images_cat':images_cat})

#     return redirect(all_images)


# def search_image(request):
#     categories = Category.objects.all()
#     location = Location.objects.all()
#     if 'image-search' in request.GET and request.GET['image-search']:
#         search_cat = request.GET.get('image-search')
#         images_result = Image.get_image_by_cat(search_cat)
#         message = f'{search_cat}'

#         return render(request,'gallery/search.html',{'images_result':images_result,'message':message,'categories':categories,'locations':location})

#     else:

#         return render(request,'gallery/search.html')

# def display_details(request,image_id):
#     categories = Category.objects.all()
#     location = Location.objects.all()
#     this_image = Image.get_image_by_id(image_id)

#     return render(request,'gallery/image.html',{'this_image':this_image,'categories':categories,'locations':location})
