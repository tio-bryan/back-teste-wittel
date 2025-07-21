from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router.urls)),
    path('api/v1/clientes/hoje', views.hoje, name='clientes-hoje'),
    path('api/v1/clientes/semana', views.semana, name='clientes-semana'),
    path('api/v1/clientes/mes', views.mes, name='clientes-mes'),
    path('api/v1/clientes/<str:cpf>', views.cliente_detail),
]
