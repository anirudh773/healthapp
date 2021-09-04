from product.models import Product
from django.contrib import admin

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    menu_title = "Our Product"
    menu_group = "Product"
    search_fields = ['product_name']
    list_filter = ['product_brand', 'product_company']
    list_display = ['product_id', 'product_name', 'product_brand', 'product_company', 'selling_price', 'discount_amount']
