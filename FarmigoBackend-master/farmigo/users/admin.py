from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

class BaseUserAdmin(UserAdmin):
    add_form = BaseUserCreationForm
    model = BaseUser
    list_display = ('user_type', 'username', 'email')
    UserAdmin.add_fieldsets += (
        (None, {
            'fields': ('user_type', 'name', 'email', 'mobnumber', 'state', 'district', 'address')
        }),
    )

admin.site.register(BaseUser, BaseUserAdmin)

admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(FarmerProduct)
admin.site.register(Livestock)

admin.site.register(Retailer)
admin.site.register(RetailerProduct)

admin.site.register(Supplier)
admin.site.register(SupplierProduct)
