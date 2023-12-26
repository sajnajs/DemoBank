from django.contrib import admin

# Register your models here.

from .models import Registration, Branch, UserInfo,Material

admin.site.register(Material)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


admin.site.register(Registration, RegisterAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', 'wikipedia_link']


admin.site.register(Branch, BranchAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phone_number', 'email_id', 'address', 'district', 'branch',
                    'account_type', 'materials_provided']


    list_editable = ['account_type', 'materials_provided']


    def materials_provided(self, obj):
        return ", ".join([material.name for material in obj.userinfo.materials_provided.all()])

    def update_materials_provided(modeladmin, request, queryset):
        # Your update logic here
        pass

        # Register the custom admin action

    actions = [update_materials_provided]

    list_per_page = 20


admin.site.register(UserInfo, UserAdmin)
from django.contrib import admin

# Register your models here.
