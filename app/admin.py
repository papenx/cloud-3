from django.contrib import admin
from .models import UserGroup, CustomUser

# Register your models here.
admin.site.register(UserGroup)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
