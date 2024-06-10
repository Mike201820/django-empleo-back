from rest_framework import serializers
from .models import Usuario, Empresa, Postulante, OfertaEmpleo, Aplicacion, Reporte

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol']  # Añade o elimina campos según sea necesario

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nombreEmpresa', 'direccion', 'telefono', 'usuario']

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = ['id', 'curriculumVitae', 'experienciaLaboral', 'usuario']

class OfertaEmpleoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaEmpleo
        fields = ['id', 'titulo', 'descripcion', 'tipoTrabajo', 'fechaPublicacion', 'empresa']

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicacion
        fields = ['id', 'fechaAplicacion', 'estado', 'oferta', 'postulante']

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ['id', 'tipoReporte', 'fechaGeneracion', 'datos']
