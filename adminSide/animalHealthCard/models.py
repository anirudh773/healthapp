from user.models import AppUser
from django.db import models

# Create your models here.
class AnimalsDetails(models.Model):
    animal_id = models.AutoField(primary_key = True)
    animal_name = models.CharField(max_length = 255 )
    owner_name = models.ForeignKey(AppUser, on_delete = models.CASCADE)
    animal_categories = models.CharField(max_length = 255 )
    breed_of_animal = models.CharField(max_length = 255 )
    age = models.IntegerField(blank=True, null=True)
    current_location =  models.CharField(max_length = 255 )
    

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