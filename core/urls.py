from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, EmpresaViewSet, PostulanteViewSet, OfertaEmpleoViewSet, AplicacionViewSet, ReporteViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'postulantes', PostulanteViewSet)
router.register(r'ofertas', OfertaEmpleoViewSet)
router.register(r'aplicaciones', AplicacionViewSet)
router.register(r'reportes', ReporteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
