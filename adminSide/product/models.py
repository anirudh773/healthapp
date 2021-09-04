from django.db import models

# Create your models here.
class Product (models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_name_hindi = models.CharField(max_length=255,default = ' ',verbose_name='नाम')
    product_brand = models.CharField(max_length=255, blank=True, null=True)
    product_brand_hindi = models.CharField(max_length=255, blank=True, null=True,default = ' ',verbose_name='ब्रांड')
    product_company = models.CharField(max_length=255, blank=True, null=True)
    product_company_hindi = models.CharField(max_length=255, blank=True, null=True,default = ' ',verbose_name='कंपनी')
    product_image = models.ImageField(upload_to='', blank=True, null=True)
    description = models.TextField()
    description_hindi = models.TextField(default = ' ',verbose_name='विवरण')
    cgst_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    sgst_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    class Meta:
        db_table= 'product'
    
    def __str__(self):
        return '%s: %s-%s' % (self.product_name ,self.product_brand, self.product_company)
