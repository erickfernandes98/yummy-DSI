from django.db import models
from datetime import datetime

class Sobremesa(models.Model):
    nome_loja = models.CharField(max_length=200, default="Loja")
    nome_sobremesa = models.CharField(max_length=200)
    ingredientes = models.TextField()
    valor = models.FloatField()
    tempo_entrega = models.IntegerField()
    categoria = models.CharField(max_length=100)
    date_sobremesa = models.DateTimeField(default=datetime.now, blank=True)
