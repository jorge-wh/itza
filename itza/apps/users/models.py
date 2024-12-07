from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # Campos adicionales para el usuario
    tipo_usuario = models.ForeignKey("TipoUsuario", on_delete=models.SET_NULL, null=True, blank=True)
    client_status = models.ForeignKey("ClientStatus", on_delete=models.SET_NULL, null=True, blank=True)
    empresa = models.ForeignKey("Empresa", on_delete=models.SET_NULL, null=True, blank=True)
    plan = models.ForeignKey("PlanEmpresa", on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario.nombre})"


class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class ClientStatus(models.Model):
    estado = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.estado


class Empresa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class PlanEmpresa(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_meses = models.PositiveIntegerField()  # Duración en meses
    descripcion = models.TextField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='planes')

    def __str__(self):
        return f"{self.nombre} - {self.empresa.nombre}"
