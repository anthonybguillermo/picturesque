from django.contrib import admin
from .models import Poster, Category

# Register your models here.

class PosterAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Poster, PosterAdmin)
admin.site.register(Category, CategoryAdmin)
