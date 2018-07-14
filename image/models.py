from django.db import models

# Create your models here.


class Location(models.Model):
    
    name = models.CharField(max_length=255)


class Categorie(models.Model):
    
    name = models.CharField(max_length=255)


class Gallerie(models.Model):
    
    title = models.CharField(max_length = 255)
    
    description = models.TextField()
    
    location = models.ForeignKey(Location, null=True)
    
    path = models.ImageField(upload_to = 'gallery/')
    
    category = models.ForeignKey(Categorie, null = True)
    
    pub_date = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
  	    
        return self.title

    def save_images(self):

        self.save() 

    def delete_images(self):
        
        self.delete()

        

