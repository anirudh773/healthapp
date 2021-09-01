from django.db import models
from ckeditor.fields import RichTextField
from social_links import utils

# Create your models here.
class SocialMedia(models.Model):
    social_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255,default = ' ')
    title_hindi = models.CharField(max_length=255,default = ' ')
    link = models.URLField(max_length = 200,blank = True, null = True,default = ' ',verbose_name='URL')
    medium = models.CharField(max_length=255,default = ' ',choices=utils.MEDIUM_CHOICES)
    description = RichTextField(blank = True, null = True,default = ' ',verbose_name='Description')
    description_hindi = RichTextField(blank = True, null = True,default = ' ',verbose_name='विवरण')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'social_links'
    
    def __str__(self):
        return  self.title

class MarketingBanners(models.Model):
    banner_id = models.AutoField(primary_key= True)
    banner_title = models.CharField(max_length=255, blank=True, null=True)
    banner_title_hindi = models.CharField(max_length=255, blank=True, null=True,default = ' ',verbose_name = 'बैनर शीर्षक')
    banner_description = RichTextField(blank = True, null = True,default = ' ')
    banner_description_hindi = RichTextField(blank = True, null = True,default = ' ',verbose_name='विवरण')
    banner_image = models.ImageField(upload_to='banner_img//', blank=True, null=True,help_text = "16x9 Image Ratio Mandatory")
    banner_start_date = models.DateTimeField(blank=True, null=True)
    banner_end_date = models.DateTimeField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marketing_banners'
    
    def __str__(self):
        return  self.banner_title

class MarketingBannersBridge(models.Model):
    marketing_banner_bridge_id = models.AutoField(primary_key = True)
    banner_id = models.ForeignKey(MarketingBanners, on_delete = models.CASCADE)
    title = models.CharField(max_length=255,default = ' ')
    title_hindi = models.CharField(max_length=255,default = ' ')
    link = models.URLField(max_length = 200,blank = True, null = True,default = ' ',verbose_name='URL')
    description = RichTextField(blank = True, null = True,default = ' ',verbose_name='Description')
    description_hindi = RichTextField(blank = True, null = True,default = ' ',verbose_name='विवरण')

    class Meta:
        db_table = 'marketing_banners_bridge'
    
    def __str__(self):
        return  self.banner_id.banner_title
