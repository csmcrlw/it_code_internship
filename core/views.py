import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from core import models
from django.views.generic import TemplateView, ListView


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['person_name'] = 'Masha'
        return c

class Person(ListView):
    model = models.Person

    # def get(self, request, *args, **kwargs):
    #     response = super().get(request, *args, **kwargs)
    #     return response


# def persons(request):
#     '''Данные всех заказчиков'''
#     object_list = []
#     for p in models.Person.objects.all():
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#         })
#     return JsonResponse({'results': object_list})

def person(request, id):
    '''Данные заказчика с его id'''
    if request.method == "GET":
        p = get_object_or_404(models.Person, id=id)
        detail = {
            'id': p.id,
            'name': p.name,
            'phone': p.phone,
        }
    return JsonResponse(detail)