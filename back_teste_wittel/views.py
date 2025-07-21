from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detail(request, cpf):
    try:
        cliente = Cliente.objects.get(pk=cpf)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def calcular_estatisticas(hoje, clientes):
    # Média de renda
    rendas = [float(c.renda_familiar) for c in clientes]
    print(rendas)
    media_renda = sum(rendas) / len(rendas) if rendas else 0

    # Maiores de 18 com renda acima da média
    maiores_18_acima_media = 0
    classe_a = classe_b = classe_c = 0

    for c in clientes:
        idade = (hoje - c.data_nascimento).days // 365
        renda = float(c.renda_familiar)
        if idade >= 18 and renda > media_renda:
            maiores_18_acima_media += 1
        if renda <= 980:
            classe_a += 1
        elif renda <= 2500:
            classe_b += 1
        else:
            classe_c += 1

    return {
        'maiores_18_acima_media': maiores_18_acima_media,
        'total_clientes': len(clientes),
        'classe_a': classe_a,
        'classe_b': classe_b,
        'classe_c': classe_c,
    }


@api_view(['GET'])
def hoje(request):
    hoje = timezone.localtime(timezone.now()).date()
    print(hoje)
    clientes = Cliente.objects.filter(data_cadastro__date=hoje)
    stats = calcular_estatisticas(hoje, clientes)
    return Response(stats)


@api_view(['GET'])
def semana(request):
    hoje = timezone.localtime(timezone.now()).date()
    inicio_semana = hoje - timezone.timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timezone.timedelta(days=6)
    clientes = Cliente.objects.filter(data_cadastro__date__range=(inicio_semana, fim_semana))
    stats = calcular_estatisticas(hoje, clientes)
    return Response(stats)


@api_view(['GET'])
def mes(request):
    hoje = timezone.localtime(timezone.now()).date()
    inicio_mes = hoje.replace(day=1)
    fim_mes = inicio_mes + timezone.timedelta(days=31)
    fim_mes = fim_mes.replace(day=1) - timezone.timedelta(days=1)
    clientes = Cliente.objects.filter(data_cadastro__date__range=(inicio_mes, fim_mes))
    stats = calcular_estatisticas(hoje, clientes)
    return Response(stats)
