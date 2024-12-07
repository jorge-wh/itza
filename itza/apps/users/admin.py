from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdmin_

from .models import TipoUsuario, ClientStatus, Empresa, PlanEmpresa

User = get_user_model()


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin_):
    list_display = ['empresa', *UserAdmin_.list_display]
    search_fields = [*UserAdmin_.search_fields]


@admin.register(TipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(ClientStatus)
class EstadoCliente(admin.ModelAdmin):
    list_display = ('estado',)
    search_fields = ('estado',)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa
    list_display = ('nombre',)


@admin.register(PlanEmpresa)
class PlanEmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('id', 'nombre')