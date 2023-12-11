from django.contrib import admin

from catalog.models import Product, Category, BlogEntry, Version




# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'number_of_views',)
    list_filter = ('sign_of_publication',)
    search_fields = ('header', 'content',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'is_active')
    list_filter = ('product',)


