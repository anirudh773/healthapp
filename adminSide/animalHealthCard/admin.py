from animalHealthCard.models import AnimalVaccine, DiseaseType
from django.contrib import admin

# Register your models here.
@admin.register(DiseaseType)
class DiseaseTypeAdmin(admin.ModelAdmin):
    menu_title = "Pet Disease"
    menu_group = "Disease"
    search_fields = ['disease_name']
    list_filter = ['disease_name', 'pet_type']
    list_display = ['id', 'disease_name', 'pet_type']

@admin.register(AnimalVaccine)
class ProductAdmin(admin.ModelAdmin):
    menu_title = "Pet Vaccine"
    menu_group = "Vaccine"
    search_fields = ['disease_name']
    list_filter = ['vaccine_name', 'pet_type']
    list_display = ['id', 'vaccine_name', 'pet_type']