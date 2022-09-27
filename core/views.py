from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from core import models

# Create your views here.
def index(request):
    person = models.Person.objects.first()
    response = render(request, 'core/index.html', context={'person': person})
    return response