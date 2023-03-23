from rest_framework import viewsets, permissions
from alunos.models import Aluno
from .serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().filter(ativo=True)
    serializer_class = AlunoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
