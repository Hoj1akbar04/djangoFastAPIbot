from django.contrib import admin
from .models import Product, Comment, Team, Blog, ProductsProducts, ProductsUsers
from import_export.admin import ImportExportModelAdmin


@admin.register(ProductsUsers)
class ProductUserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'full_name', 'username', 'telegram_id', 'create_date')
    list_display_links = ('id', 'full_name', 'username', 'telegram_id', 'create_date')
    search_fields = ('username','full_name',)
    ordering = ('id',)


@admin.register(ProductsProducts)
class ProductProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'category_code', 'category_name', 'subcategory_code', 'subcategory_name')
    list_display_links = ('id', 'name', 'price', 'description', 'category_code', 'category_name', 'subcategory_code', 'subcategory_name')
    search_fields = ('name', 'price')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'count')
    list_display_links = ('id', 'name', 'price', 'description', 'count')
    search_fields = ('name', 'price')
    ordering = ('id',)


@admin.register(Comment)
class ClientCommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'comment', 'product')
    list_display_links = ('id', 'name', 'comment', 'product')
    search_fields = ('name', 'comment', 'product')
    ordering = ('id',)


@admin.register(Team)
class TeamSaysAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    search_fields = ('name', )
    ordering = ('id', )