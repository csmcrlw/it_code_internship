import django_filters
from core import models

class Tag(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    name = django_filters.CharFilter(field_name='id', lookup_expr='icontains')

    class Meta:
        model = models.Tag
        fields = '__all__'

class Item(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    name = django_filters.CharFilter(field_name='id', lookup_expr='icontains')

    class Meta:
        model = models.Item
        fields = '__all__'