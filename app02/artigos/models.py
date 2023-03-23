from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    site = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return self.nome
    
class Artigo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    publicado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    texto = models.TextField()    

    def __str__(self):
        return self.titulo