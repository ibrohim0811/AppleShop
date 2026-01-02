from django.contrib import admin
from .models import Category, Products, Users

admin.site.register(Category)
admin.site.register(Products)
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_superuser', 'id')
    search_fields = ('username', 'first_name', 'last_name')
