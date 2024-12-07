import uuid as _uuid
from stdimage import StdImageField
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

# Create your models here.
class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\d+$', message=_('Ingrese solo números.'))

    # Campos adicionales para el usuario
    ADMIN = 'Administrador'
    GUEST = 'Guest'
    REGULAR = 'Regular'
    PREMIUM = 'Premium'
    ARTIST = 'Artist'
    MODERATOR = 'Moderator'

    TYPE = (
        (ADMIN, _('Administrador')),
        (GUEST, _('Guest User')),
        (REGULAR, _('Regular User')),
        (PREMIUM, _('Premium User')),
        (ARTIST, _('Artist')),
        (MODERATOR, _('Moderator')),
    )


    uuid = models.UUIDField(default=_uuid.uuid4, editable=False, db_index=True, unique=True)
    avatar = StdImageField(_('Avatar'), upload_to='images/users/%Y/%m/', default='images/users/avatar.png',
                           variations={
                               'perfil': {'width': 240, 'height': 240, 'crop': True},
                               'thumbnail': {'width': 45, 'height': 45, 'crop': True}
                           })
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(_("Dirección"), blank=True)
    phone_number = models.CharField(_("Teléfono Celular"), max_length=250, blank=True,
                                    validators=[phone_regex])
    postal_code = models.CharField(_('Código postal'), max_length=50, blank=True)
    billing_address = models.TextField(_('Dirección de facturación'), max_length=100, blank=True)
    billing_email = models.EmailField(_('Email de facturación'), blank=True)
    district = models.CharField(_('Localidad/Barrio/Departamento'), max_length=50, blank=True)
    city = models.CharField(_('Ciudad/Municipio'), max_length=50, blank=True)
    license = models.CharField(_('Licencia DNI/C.I./C.C.'), max_length=35, blank=True)
    tipo_usuario = models.ForeignKey("TipoUsuario", on_delete=models.SET_NULL, null=True, blank=True)
    client_status = models.ForeignKey("ClientStatus", on_delete=models.SET_NULL, null=True, blank=True)
    empresa = models.ForeignKey("Empresa", on_delete=models.SET_NULL, null=True, blank=True)
    plan = models.ForeignKey("PlanEmpresa", on_delete=models.SET_NULL, null=True, blank=True)

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
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.estado


class Empresa(models.Model):
    uuid = models.UUIDField(verbose_name=_('Identificador de empresa'), editable=False, default=_uuid.uuid4,
                            db_index=True, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_contratacion = models.DateTimeField(blank=True, null=True)
    fecha_suspension = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Suspension")

    def __str__(self):
        return self.nombre


class PlanEmpresa(models.Model):
    uuid = models.UUIDField(default=_uuid.uuid4, editable=False, db_index=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_meses = models.PositiveIntegerField()  # Duración en meses
    descripcion = models.TextField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='planes')
    pais = CountryField(null=True)

    def __str__(self):
        return f"{self.nombre} - {self.empresa.nombre}"
