from django.contrib import admin
from .models import Person

# Register your models here.
# admin.site.register(Person)
@admin.register(Person)
class Persons(admin.ModelAdmin):
    list_display = ('name', 'phone')