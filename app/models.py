from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    p_type = models.CharField()
    brend = models.CharField()
    price = models.IntegerField()
    about = models.TextField()
    sale = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=True)
    count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    @property
    def sale_seller(self):
        return int(self.price - (self.price * self.sale / 100))
    
    class Meta:
        ordering = ['-created_at']        


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return self.product.name
        
        
class Users(AbstractUser):
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='users/', default='media/users/image.png')
    def __str__(self):
        return self.username