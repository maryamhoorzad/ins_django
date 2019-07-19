from django.contrib import admin

from .models import Product, Category, Brand

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sous_titre', 'description', 'picture', 'create_date', 'brand')
    search_fields = ('name',)
    list_filter = ('category', 'brand')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('english_name', 'persian_name', 'brand_desc', 'picture')
    search_fields = ('english_name', 'persian_name')


