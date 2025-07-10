from django.db import models
from django.core.validators import RegexValidator

class Cliente(models.Model):
    nome = models.CharField(max_length=150, help_text='Até 150 caracteres.')
    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        help_text='11 dígitos.',
        validators=[
            RegexValidator(
                regex='([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})',
                message='Por favor, inserir um CPF válido.',
            ),
        ])
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    renda_familiar = models.DecimalField(max_digits=65, decimal_places=2, help_text='Até 150 caracteres.')

    def __str__(self):
        return self.nome