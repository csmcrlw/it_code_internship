from django.contrib import admin
from core import models

# Register your models here.
# admin.site.register(models.Person)
# @admin.register(models.Person)
# class Persons(admin.ModelAdmin):
#     list_display = ('name', 'phone')

class ItemResultInLine(admin.TabularInline):
    model = models.ItemResult


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    inlines = (ItemResultInLine, )
    list_display = ('name', 'done')
    search_field = ('name', )

@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name', )
    search_field = ('name', )