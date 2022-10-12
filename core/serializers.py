from rest_framework import  serializers
from core import models

class Tag(serializers.ModelSerializer):
    display = serializers.SerializerMethodField()
    class Meta:
        model = models.Tag
        fields = '__all__'

    def get_display(self, obj: models.Tag) -> str:
        return f'{obj.id}. {obj.name}'

class Item(serializers.ModelSerializer):
    display = serializers.SerializerMethodField()
    class Meta:
        model = models.Item
        fields = '__all__'

    def get_display(self, obj: models.Tag) -> str:
        return f'{obj.id}. {obj.name}'

class TagSearch(serializers.Serializer):
    name = serializers.CharField(label='Название', required=True)

    def validate_name(self, value):
        if not models.Tag.objects.filter(name_incontains=value):
            raise serializers.ValidationError(f'Нет меток, содержащих название "{value}"')
        return value

    def validate(self, attrs):
        return attrs


class Item(serializers.ModelSerializer):
    tags = Tag(many=True)

    class Meta:
        model = models.Item
        exclude = ('user', )