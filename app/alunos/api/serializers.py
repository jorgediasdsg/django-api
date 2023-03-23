from rest_framework import serializers
from alunos.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        # fields = ('nome', 'sobrenome', 'ano_nasc', 'email', 'ativo')
        fields = '__all__'