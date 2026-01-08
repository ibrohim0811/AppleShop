from django.contrib import admin
from .models import Category, Products, Users, ProductImage, Comment, BannerImage

admin.site.register(Category)

admin.site.register(Products)

# admin.site.register(Users)

@admin.register(ProductImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'id', 'image']
    search_fields = ['id']

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_superuser', 'id')
    search_fields = ('username', 'first_name', 'last_name')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'id']
    

@admin.register(BannerImage)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

