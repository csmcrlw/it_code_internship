from core import models
from core import filters
from core import serializers
from rest_framework.viewsets import ReadOnlyModelViewSet

class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filterset_class = filters.Tag
