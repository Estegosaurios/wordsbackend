from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from words.models import Word
from words.serializers import WordSerializer


class WordViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
