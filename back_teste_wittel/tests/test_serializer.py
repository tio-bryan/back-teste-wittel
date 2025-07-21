from django.test import TestCase
from back_teste_wittel.serializers import ClienteSerializer
from django.utils import timezone


class ClienteSerializerTest(TestCase):
    def test_serializer_valido(self):
        serializer = ClienteSerializer(data={
            'nome': 'Teste',
            'cpf': '56712691052',
            'data_nascimento': '2000-01-01',
            'renda_familiar': 1000.00
        })

        self.assertTrue(serializer.is_valid())


    def test_serializer_invalido_nome_vazio(self):
        serializer = ClienteSerializer(data={
            'nome': '',
            'cpf': '56712691052',
            'data_nascimento': '2000-01-01',
            'renda_familiar': 1000.00
        })

        self.assertFalse(serializer.is_valid())
        self.assertIn('nome', serializer.errors)


    def test_serializer_invalido_cpf(self):
        cpfs_invalidos = [
            '',             # CPF vazio
            '11111111111',  # CPF com todos os dígitos iguais
            '12345678901',  # CPF inválido (dígito verificador errado))
            '12345',        # CPF muito curto
            '123456789012', # CPF muito longo
            'abcdefghijk',  # CPF com letras
        ]

        for cpf in cpfs_invalidos:
            serializer = ClienteSerializer(data={
                'nome': 'Teste',
                'cpf': cpf,
                'data_nascimento': '2000-01-01',
                'renda_familiar': 1000.00
            })

            self.assertFalse(serializer.is_valid())
            self.assertIn('cpf', serializer.errors)


    def test_serializer_invalido_data_nascimento(self):
        # Data de nascimento vazia
        serializer = ClienteSerializer(data={
            'nome': 'Teste',
            'cpf': '56712691052',
            'data_nascimento': '',
            'renda_familiar': 1000.00
        })

        self.assertFalse(serializer.is_valid())
        self.assertIn('data_nascimento', serializer.errors)

        # Data de nascimento no futuro
        data_futura = timezone.now().date() + timezone.timedelta(days=1)

        serializer = ClienteSerializer(data={
            'nome': 'Teste',
            'cpf': '56712691052',
            'data_nascimento': data_futura,
            'renda_familiar': 1000.00
        })

        self.assertFalse(serializer.is_valid())
        self.assertIn('data_nascimento', serializer.errors)


    def test_serializer_invalido_renda_familiar(self):
        # Renda familiar vazia
        serializer = ClienteSerializer(data={
            'nome': 'Teste',
            'cpf': '56712691052',
            'data_nascimento': '2000-01-01',
            'renda_familiar': ''
        })

        self.assertFalse(serializer.is_valid())
        self.assertIn('renda_familiar', serializer.errors)

        # Renda familiar negativa
        serializer = ClienteSerializer(data={
            'nome': 'Teste',
            'cpf': '56712691052',
            'data_nascimento': '2000-01-01',
            'renda_familiar': -1000.00
        })

        self.assertFalse(serializer.is_valid())
        self.assertIn('renda_familiar', serializer.errors)