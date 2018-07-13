from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    url(r'^$',views.images,name='Photos'),
    url(r'^location/',views.location,name='location'),
    url(r'^image/(?P<image_id>\d+)/$',views.display_details,name='details'),
    url(r'^category/',views.category,name='category'),
    url(r'^search/',views.search_image,name='search'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)