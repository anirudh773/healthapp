from user.models import AppUser
from django.db import models
from ckeditor.fields import RichTextField
from animalHealthCard import utils

# Create your models here.
class AnimalsDetails(models.Model):
    animal_id = models.AutoField(primary_key = True)
    animal_name = models.CharField(max_length = 255 )
    owner_name = models.ForeignKey(AppUser, on_delete = models.CASCADE)
    animal_categories = models.CharField(max_length = 255 )
    breed_of_animal = models.CharField(max_length = 255 )
    age = models.IntegerField(blank=True, null=True)
    current_location =  models.CharField(max_length = 255 )
    animal_photo = models.URLField(max_length = 200,blank = True, null = True,default = ' ',verbose_name='URL')

    class Meta:
        db_table= 'animal_data'

class AnimalsDetailsBridge(models.Model):
    animals_details_bridge_id = models.AutoField(primary_key=True)
    animal_id = models.ForeignKey(AnimalsDetails, on_delete = models.CASCADE)
    link = models.URLField(max_length = 200,blank = True, null = True,default = ' ',verbose_name='URL')

    class Meta:
        db_table = 'animal_details_bridge'
    
    def __str__(self):
        return str(self.animals_details_bridge_id)


class DiseaseType (models.Model):
    id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=255,blank=True)
    disease_name_hindi = models.CharField(max_length=255,default = ' ',verbose_name='बीमारी का नाम')
    symptoms =  models.CharField(max_length=255,blank=True)
    symptoms_hindi = models.CharField(max_length=255,blank=True,default = ' ',verbose_name='लक्षण')
    image  = models.ImageField(upload_to='disease//', blank=True, null=True)
    description = RichTextField(blank = True, null = True)
    description_hindi = RichTextField(blank = True, null = True,default = ' ',verbose_name='विवरण')
    remedies = RichTextField(blank = True, null = True)
    remedies_hindi = RichTextField(blank = True, null = True,default = ' ',verbose_name = 'उपचार')
    pet_type = models.CharField(max_length=255,choices=utils.PET_CHOICES)


    class Meta:
        db_table = 'disease'
    
    def __str__(self):
        return  self.disease_name
    
class AnimalVaccine(models.Model):
    id = models.AutoField(primary_key=True)
    vaccine_name = models.CharField(max_length=255,blank=True)
    vaccine_name_hindi = models.CharField(max_length=255,blank=True)
    pet_type = models.CharField(max_length=255,choices=utils.PET_CHOICES)
    vaccine_schedule = models.CharField(max_length=255,choices=utils.SCHEDULE_CHOICES)
    
    class Meta:
        db_table = 'vaccine'
    
    def __str__(self):
        return  self.vaccine_name
