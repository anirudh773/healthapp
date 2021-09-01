from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import AppUser, UserReferralBridge
# Register your models here.
class UserReferralBridgeAdminInline(admin.TabularInline):

    model = UserReferralBridge
    verbose_name = 'User Referral'
    verbose_name_plural = 'User Referral List'

    # show one empty instance when creating
    # no empty instance when editing
    def get_extra(self, request, obj=None, **kwargs):
        if obj :
            return 0
        else:
            return 1

    # autocomplete_fields = ['referral_bridge_id']
    # list_select_related = ['referral_bridge_id']

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    menu_title = "App user"
    menu_group = "User"
    search_fields = ['mobile_number']
    list_filter = ['category']
    list_display = ['user_id', 'mobile_number']
    inlines = [UserReferralBridgeAdminInline]