from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    ano_nasc = models.PositiveSmallIntegerField(validators=[MinValueValidator(1950), MaxValueValidator(datetime.now().year)])
    email = models.EmailField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome