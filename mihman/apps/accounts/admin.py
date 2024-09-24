from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser

class MyUserAdmin(BaseUserAdmin):
 # The forms to add and change user instances
 model = MyUser
 list_display = ('mobile', 'full_name', 'is_active', 'is_admin')
 list_filter = ('is_admin', 'is_active')
 fieldsets = (
     (None, {'fields': ('mobile', 'full_name', 'password')}),
     ('Permissions', {'fields': ('is_admin', 'is_active')}),
 )
 add_fieldsets = (
     (None, {
         'classes': ('wide',),
         'fields': ('mobile', 'full_name', 'password1', 'password2', 'is_admin', 'is_active')}
     ),
 )
 search_fields = ('mobile', 'full_name')
 ordering = ('mobile',)
 filter_horizontal = ()

admin.site.register(MyUser, MyUserAdmin) 