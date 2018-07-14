from django.test import TestCase
from .models import Gallerie, Location, Categorie

# Create your tests here.

class LocationTestClass(TestCase):
     
    def setUp(self):

        self.Deutchstland=Location( name = "Deutchstland")

    def test_instance(self):

        self.assertTrue(isinstance(self.Deutchstland,Location))

    def test_save(self):

        self.Deutchstland.save_location()

        Deutchstland=Location.objects.all()

        self.assertTrue(len(Deutchstland)>0)  


class CategorieTestClass(TestCase):
     
    def setUp(self):

        self.Cars=Categorie( name = "Cars")

    def test_instance(self):

        self.assertTrue(isinstance(self.Cars,Categorie))

    def test_save(self):

        self.Cars.save_category()

        Cars=Categorie.objects.all()

        self.assertTrue(len(Cars)>0)  



class GallerieTestClass(TestCase):
     
    def setUp(self):
        self.Deutchstland=Location( name = "Deutchstland")
        self.Deutchstland.save()

        self.Cars=Categorie( name = "Cars")
        self.Cars.save()

        self.Mercedes=Gallerie( title = "Mercedes", description = "Mercedes at its finest", path= 'gallery/lista.jpg', Location = self.Deutchstland, Categorie = self.Cars )
        self.Mercedes.save()

    def test_instance(self):

        self.assertTrue(isinstance(self.Mercedes,Gallerie))

    def test_save(self):
        self.Mercedes.save_gallerie()


        Mercedes=Gallerie.objects.all()

        self.assertTrue(len(Mercedes)>0)   

    def test_get_gallerie_by_title(self):

        title = "Mercedes"
        search_gallerie = self.Mercedes.get_gallerie_by_title(title)
        
        gallerie = Gallerie.objects.filter(title=self.Mercedes.title)
        
        self.assertTrue(search_gallerie,gallerie)

    def test_get_gallerie_by_category(self):
        
        category=Categorie( name = "Cars")        
        search_gallerie = self.Mercedes.get_gallerie_by_category(category)
        
        self.assertTrue(len(search_gallerie)>0)

    def test_get_gallerie_by_location(self):
        
        location = Location( name = "Deutchstland")
        search_gallerie = self.Mercedes.get_gallerie_by_location(location)
        
        self.assertTrue(len(search_gallerie)>0)




  