from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    location = models.ForeignKey('Location', null=True)
    path = models.ImageField(upload_to = 'gallery/')
    category = models.ForeignKey('Category', null = True)
    pub_date = models.DateTimeField(auto_now_add=True)



class Location(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)