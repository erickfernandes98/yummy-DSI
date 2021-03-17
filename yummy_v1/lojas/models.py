from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return self.nome
