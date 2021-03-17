from django.db import models
from datetime import datetime
from lojas.models import Loja

class Sobremesa(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome_sobremesa = models.CharField(max_length=200)
    ingredientes = models.TextField()
    valor = models.FloatField()
    tempo_entrega = models.IntegerField()
    categoria = models.CharField(max_length=100)
    date_sobremesa = models.DateTimeField(default=datetime.now, blank=True)
    foto_sobremesa = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_sobremesa
