from django.contrib import admin
from .models import Category, Products, Users, ProductImage

admin.site.register(Category)

admin.site.register(Products)

admin.site.register(Users)

@admin.register(ProductImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'id', 'image']
    search_fields = ['id']


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_superuser', 'id')
    search_fields = ('username', 'first_name', 'last_name')
