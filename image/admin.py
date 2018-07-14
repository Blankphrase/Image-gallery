from django.contrib import admin


from .models import Gallerie,Location,Categorie

# Register your models here.

admin.site.register(Gallerie)
admin.site.register(Location)
admin.site.register(Categorie)