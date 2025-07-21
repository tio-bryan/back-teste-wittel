from django.core.exceptions import ValidationError
import datetime
from django.utils.translation import gettext_lazy as _


def validate_cpf(cpf):
    numeros = [int(digito) for digito in cpf if digito.isdigit()]

    if len(numeros) == 11 and len(set(numeros)) == 1:
        raise ValidationError(f"O CPF {cpf} não é válido. Não pode conter todos os dígitos iguais.")
    
    quant_digitos = False
    validacao1 = False
    validacao2 = False

    if len(numeros) == 11:
        quant_digitos = True

        soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
        digito_esperado = (soma_produtos * 10 % 11) % 10
        if numeros[9] == digito_esperado:
            validacao1 = True

        soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
        digito_esperado1 = (soma_produtos1 *10 % 11) % 10
        if numeros[10] == digito_esperado1:
            validacao2 = True

        if quant_digitos and validacao1 and validacao2:
            return
        else:
            raise ValidationError(f"O CPF {cpf} não é válido.")
    else:
        raise ValidationError(f"O CPF {cpf} não é válido. Deve conter 11 dígitos.")


def date_not_future(value):
    if value > datetime.date.today():
        raise ValidationError(
            _("%(value)s está no futuro!"),
            params={"value": value.strftime("%d/%m/%Y") },
        )