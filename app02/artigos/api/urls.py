from django.urls import include, path
from rest_framework import routers
from .views import ArtigoViewSet, AutorViewSet

router = routers.DefaultRouter()

router.register('autores', AutorViewSet)
router.register('artigos', ArtigoViewSet)

urlpatterns = [
    path('', include(router.urls))
]