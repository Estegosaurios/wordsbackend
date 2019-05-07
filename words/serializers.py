from rest_framework.serializers import ModelSerializer
from words.models import Tag, Word


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )

class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = (
            'id',
            'name',
            'description',
            'tags',
        )
