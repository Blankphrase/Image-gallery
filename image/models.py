from django.db import models

# Create your models here.


class Location(models.Model):
    
    name = models.CharField(max_length=255)

    def __str__(self):
  	    
        return self.name

    def save_location(self):

        self.save() 


class Categorie(models.Model):
    
    name = models.CharField(max_length=255)

    def __str__(self):
  	    
        return self.name

    def save_category(self):

        self.save() 


class Gallerie(models.Model):
    
    title = models.CharField(max_length = 255)
    
    description = models.TextField()
    
    Location = models.ForeignKey("Location",null=True)
    
    path = models.ImageField(upload_to = 'gallery/')
    
    Categorie = models.ForeignKey("Categorie",null=True)
    
    pub_date = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
  	    
        return self.title

    def save_gallerie(self):

        self.save() 

                                                                                                                                                                                                                                                                                                                                                                                                                           
    @classmethod
    def get_gallerie_by_id(cls,id):

        gallerie = cls.objects.filter(id=id).all()

        return gallerie
        
    @classmethod
    def get_gallerie_by_category(cls,category):
        
        gallerie = cls.objects.filter(Categorie__name__icontains=category).all()
        
        return gallerie

    @classmethod
    def get_gallerie_by_location(cls,location):
        
        gallerie = cls.objects.filter(Location__name__icontains=location).all()
        
        return gallerie


