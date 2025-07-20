from django.urls import reverse
from rest_framework.test import APITestCase
from back_teste_wittel.models import Cliente
from datetime import date
from django.utils import timezone


class EstatisticasViewTest(APITestCase):
    def setUp(self):
        hoje = timezone.now().date()

        # Classe A, menor de 18
        Cliente.objects.create(
            nome='Menor Classe A',
            cpf='48457123009',
            data_nascimento=date(2010, 1, 1),
            renda_familiar=900.00,
            data_cadastro=hoje
        )
        # Classe B, maior de 18
        Cliente.objects.create(
            nome='Adulto Classe B',
            cpf='12345678901',
            data_nascimento=date(1995, 1, 1),
            renda_familiar=2000.00,
            data_cadastro=hoje
        )
        # Classe C, maior de 18
        Cliente.objects.create(
            nome='Adulto Classe C',
            cpf='16219314042',
            data_nascimento=date(1990, 1, 1),
            renda_familiar=3000.00,
            data_cadastro=hoje
        )


    def test_hoje_view(self):
        url = reverse('clientes-hoje')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.data

        # Testa se todos os campos estão presentes
        self.assertIn('classe_a', data)
        self.assertIn('classe_b', data)
        self.assertIn('classe_c', data)
        self.assertIn('maiores_18_acima_media', data)
        self.assertIn('total_clientes', data)

        # Testa a contagem das classes
        self.assertEqual(data['classe_a'], 1)
        self.assertEqual(data['classe_b'], 1)
        self.assertEqual(data['classe_c'], 1)
        self.assertEqual(data['total_clientes'], 3)

        # Testa maiores de 18 com renda acima da média
        # Média: (3000 + 900 + 2000) / 3 = 1966.67
        # Maiores de 18: Adulto Classe B (2000 <= 1966.67), Adulto Classe C (3000 > 1966.67)
        self.assertEqual(data['maiores_18_acima_media'], 2)
