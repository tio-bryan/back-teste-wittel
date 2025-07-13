from django.db import models
from back_teste_wittel import validators


class Cliente(models.Model):
    nome = models.CharField(max_length=150, help_text='Até 150 caracteres.')
    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        help_text='11 dígitos (Sem pontuação).',
        validators=[validators.validate_cpf])
    data_nascimento = models.DateField(validators=[validators.date_not_future])
    data_cadastro = models.DateTimeField(auto_now_add=True)
    renda_familiar = models.DecimalField(null=True, max_digits=65, decimal_places=2, help_text='Até 150 caracteres.')

    def __str__(self):
        return self.nome