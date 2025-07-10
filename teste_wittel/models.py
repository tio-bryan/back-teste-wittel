from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    # renda_familiar = 

    def __str__(self):
        return self.nome