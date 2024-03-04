from django.db import models
# Create your models here.

class DadosRaspados(models.Model):
    objeto = models.TextField()
    modalidade = models.TextField()
    comprador = models.TextField()
    descricao = models.TextField()
    unidade = models.TextField()
    quantidade = models.TextField()
    valor = models.TextField()