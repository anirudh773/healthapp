from django.contrib import admin
from .models import SocialMedia, MarketingBanners, MarketingBannersBridge
from import_export.admin import ImportExportMixin
# Register your models here.

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    menu_title = "Social Media"
    menu_group = "Social"
    search_fields = ['medium', 'created_at', 'modified_at', 'title_eng', 'title_hin']
    list_filter = ['medium', 'created_at', 'modified_at']
    list_display = ['social_id', 'title', 'title_hindi', 'link', 'medium', 'visibility_status', 'created_at', 'modified_at']


class MarketingBannersAdminInline(admin.TabularInline):

    model = MarketingBannersBridge
    verbose_name = 'Banners'
    verbose_name_plural = 'Banners List'

    # show one empty instance when creating
    # no empty instance when editing
    def get_extra(self, request, obj=None, **kwargs):
        if obj :
            return 0
        else:
            return 1

    autocomplete_fields = ['banner_id']
    list_select_related = ['banner_id']

@admin.register(MarketingBanners)
class MarketingBannersAdmin(ImportExportMixin, admin.ModelAdmin):
    menu_title = "Marketing Banners"
    menu_group = "Social"
    search_fields = ['banner_title']
    list_filter = ['createdAt',  'updatedAt']
    list_display = ['banner_id','banner_title', 'banner_start_date', 'banner_end_date','createdAt','updatedAt']
    inlines = [MarketingBannersAdminInline]