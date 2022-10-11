from django.contrib import admin
from core import models


@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name', )
    search_field = ('name', )

@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ('name', 'done')
    search_field = ('name', )

