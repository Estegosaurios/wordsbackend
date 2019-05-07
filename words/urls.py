from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from words.views import TagViewSet, WordViewSet

tags_router = DefaultRouter()
tags_router.register(r'tags', TagViewSet, base_name='tags')

words_router = DefaultRouter()
words_router.register(r'words', WordViewSet, base_name='words')

urlpatterns = [
    url(r'^', include(tags_router.urls)),
    url(r'^', include(words_router.urls))
]
