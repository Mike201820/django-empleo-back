from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Rol(models.TextChoices):
    EMPRESA = 'Empresa', 'Empresa'
    POSTULANTE = 'Postulante', 'Postulante'

class TipoTrabajo(models.TextChoices):
    PROFESOR = 'Profesor', 'Profesor'
    DOCTOR = 'Doctor', 'Doctor'
    ARTESANO = 'Artesano', 'Artesano'
    OTROS = 'Otros', 'Otros'

class EstadoAplicacion(models.TextChoices):
    PENDIENTE = 'Pendiente', 'Pendiente'
    ACEPTADA = 'Aceptada', 'Aceptada'
    RECHAZADA = 'Rechazada', 'Rechazada'

class Usuario(AbstractUser):
    rol = models.CharField(max_length=20, choices=Rol.choices)
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Empresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombreEmpresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def publicarOferta(self):
        pass

    def editarOferta(self):
        pass

    def eliminarOferta(self):
        pass

class Postulante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    curriculumVitae = models.TextField()
    experienciaLaboral = models.TextField()

    def buscarEmpleo(self):
        pass

    def aplicarOferta(self):
        pass

    def verHistorialAplicaciones(self):
        pass

class OfertaEmpleo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipoTrabajo = models.CharField(max_length=20, choices=TipoTrabajo.choices)
    fechaPublicacion = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='ofertas')

    def publicar(self):
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass

class Aplicacion(models.Model):
    fechaAplicacion = models.DateField()
    estado = models.CharField(max_length=20, choices=EstadoAplicacion.choices)
    oferta = models.ForeignKey(OfertaEmpleo, on_delete=models.CASCADE, related_name='aplicaciones')
    postulante = models.ForeignKey(Postulante, on_delete=models.CASCADE, related_name='aplicaciones')

    def actualizarEstado(self):
        pass

class TipoReporte(models.TextChoices):
    ACTIVIDADES = 'Actividades', 'Actividades'
    ESTADISTICAS = 'Estadísticas', 'Estadísticas'

class Reporte(models.Model):
    tipoReporte = models.CharField(max_length=20, choices=TipoReporte.choices)
    fechaGeneracion = models.DateField()
    datos = models.TextField()

    def generarReporte(self):
        pass
