from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from words.models import Tag, Word
from words.serializers import TagSerializer, WordSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class WordViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
