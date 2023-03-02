from django.contrib import admin

from account.form import modificaUtenteForm, RegistrazioneForm
from account.models import CustomUser
#admin.site.register(CustomUser)






from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from account.models import CustomUser



"""
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = modificaUtenteForm
    add_form = RegistrazioneForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("username",'email',"nome","cognome", 'is_admin')
    list_filter = ('is_admin',)
  
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
   
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
    
"""
admin.site.register(CustomUser)