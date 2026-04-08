from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # список полей
    list_filter = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # список полей
    list_filter = ('category',)  # фильтрация
    search_fields = ('name', 'description')  # поиск по выбранным полям

