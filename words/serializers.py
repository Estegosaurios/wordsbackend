from rest_framework.serializers import ModelSerializer
from words.models import Word


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = (
            'id',
            'name',
            'description',
            'tags',
        )
