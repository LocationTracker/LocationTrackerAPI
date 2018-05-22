from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from core.views import FamiliaViewSet, UsuarioViewSet, ListUsers
from location.views import LocalizacaoViewSet

router = routers.DefaultRouter()
# router.register('familias', FamiliaViewSet)
router.register('usuarios', UsuarioViewSet)
# router.register('localizacoes', LocalizacaoViewSet)
# router.register('user', ListUsers.as_view())

schema_view = get_swagger_view(title='LocationTracker API')

urlpatterns = [
    path('', schema_view),
    path('router/', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]
