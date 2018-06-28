from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as TokenView
from rest_framework_swagger.views import get_swagger_view
from core.views import UsuarioViewSet

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet)

schema_view = get_swagger_view(title='LocationTracker API')

urlpatterns = [
    path('', schema_view),
    path('router/', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
    # path('router/auth/', TokenView.obtain_auth_token)
]
