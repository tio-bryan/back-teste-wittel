from django.test import TestCase
from back_teste_wittel.models import Cliente
from datetime import date


class ClienteModelTest(TestCase):
    def test_criacao_cliente(self):
        cliente = Cliente.objects.create(
            nome='Teste',
            cpf='55574225018',
            data_nascimento=date(2000, 1, 1),
            renda_familiar=1500.00
        )

        self.assertEqual(cliente.nome, 'Teste')
        self.assertEqual(cliente.cpf, '55574225018')
        self.assertEqual(cliente.data_nascimento, date(2000, 1, 1))
        self.assertEqual(cliente.renda_familiar, 1500.00)
