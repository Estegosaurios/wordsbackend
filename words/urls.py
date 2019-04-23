from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from words.views import WordViewSet

router = DefaultRouter()
router.register(r'words', WordViewSet, base_name='words')

urlpatterns = [
    url(r'^', include(router.urls))
]
