from django.db import models
from user import utils

# Create your models here.
class AppUser(models.Model):
    user_id = models.AutoField(primary_key= True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    password = models.CharField(max_length=255,null=True,blank=True)
    mobile_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=255 )
    midddle_name = models.CharField(max_length=255,  blank=True, null=True )
    last_name = models.CharField(max_length=255, blank=True, null=True)
    aadhar_number = models.CharField(max_length=250, blank=True, null=True )
    education = models.CharField(max_length=250, choices= utils.EDUCATION, blank=True, null=True )
    category = models.CharField(max_length=250, choices= utils.CATEGORY, blank=True, null=True )
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    latitude = models.CharField(max_length= 255)
    longitude = models.CharField(max_length= 255)
    referral_key = models.CharField(max_length=70,blank=True, null= True, unique = True)
    refer_count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table= 'app_user'
    
class UserReferralBridge(models.Model):
    referral_bridge_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('AppUser', on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 255, null=False)

    class Meta:
        db_table = 'user_referral_bridge'
    
    def __str__(self):
        return str(self.referral_bridge_id)
    