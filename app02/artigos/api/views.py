from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from artigos.models import Autor, Artigo

from .serializers import AutorSerializer, ArtigoSerializer

class AutorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ArtigoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer