import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from core import models
from django.views.generic import TemplateView, ListView
from core import filters
from core import serializers
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filterset_class = filters.Tag

class ItemViewSet(ReadOnlyModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.Item
    filterset_class = filters.Item

# class Tags(ListAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.Tag
#     filterset_class = filters.Tag
#
#     def list(self, request, *args, **kwargs):
#         serializer = serializers.TagSearch(data=request.query_params)
#         serializer.is_valid(raise_exception=True)
#
#         return super().list(request, *args, **kwargs)
#
# class Tag(RetrieveAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.Tag

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

# def tags(request):
#     search_serializer = serializers.TagSearch(data=request.GET)
#     if not search_serializer.is_valid():
#         return JsonResponse(search_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     f = filters.Tag(request.GET, queryset=models.Tag.objects.all())
#     serializer = serializers.Tag(instance=f.qs, many=True)
#     return JsonResponse({'result': serializer.data})