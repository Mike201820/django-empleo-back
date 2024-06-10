from rest_framework import viewsets
from .models import Usuario, Empresa, Postulante, OfertaEmpleo, Aplicacion, Reporte
from .serializers import UsuarioSerializer, EmpresaSerializer, PostulanteSerializer, OfertaEmpleoSerializer, AplicacionSerializer, ReporteSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class PostulanteViewSet(viewsets.ModelViewSet):
    queryset = Postulante.objects.all()
    serializer_class = PostulanteSerializer

class OfertaEmpleoViewSet(viewsets.ModelViewSet):
    queryset = OfertaEmpleo.objects.all()
    serializer_class = OfertaEmpleoSerializer

class AplicacionViewSet(viewsets.ModelViewSet):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

