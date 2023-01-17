from django.contrib import admin
# Register your models here.


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# from .forms import creatNewUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 
#                   'first_name', 'last_name', 'NationalityF')
#     add_form = creatNewUser
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2',
#                   'first_name', 'last_name', 'Nationality')}
#         ),
#     )
    
#     def NationalityF(self, obj):
#         return obj.Nationality

