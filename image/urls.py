from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    url(r'^$',views.images,name='Photos'),
    url(r'^location/',views.image_by_location,name='loca'),
    url(r'^image/(?P<id>\d+)',views.display_details,name='details'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)