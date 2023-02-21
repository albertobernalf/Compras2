from django.contrib import admin
from django import forms

# Register your models here.

from solicitud.models import SedesCompra, Usuarios, TiposCompra, EstadosValidacion, Presentacion, DescripcionCompra, Proveedores, Areas, Solicitudes, SolicitudesDetalle

@admin.register(SedesCompra)
class sedesCompraAdmin(admin.ModelAdmin):
    list_display = ("id", "codreg_sede", "nom_sede", "codreg_ips", "direccion", "telefono", "departamento", "municipio")
    search_fields = (
    "id", "codreg_sede", "nom_sede", "codreg_ips", "direccion", "telefono", "departamento", "municipio")
    # Filtrar

    list_filter = ("id", "codreg_sede", "nom_sede", "codreg_ips", "direccion", "telefono", "departamento", "municipio")

    def get_actions(self, request):
        actions = super(sedesCompraAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Usuarios)
class usuariosAdmin(admin.ModelAdmin):
    list_display =( "num_identificacion" ,"nom_usuario","carg_usuario","sede","estadoreg" )
    search_fields = ( "num_identificacion" ,"nom_usuario","carg_usuario","sede","estadoreg" )

    list_filter = ( "num_identificacion" ,"nom_usuario","carg_usuario","sede","estadoreg" )

@admin.register(TiposCompra)
class tiposCompraAdmin(admin.ModelAdmin):

    list_display = ("nombre", "descripcion", "estadoreg")
    search_fields = ("nombre", "descripcion", "estadoreg")
    list_filter = ("nombre", "descripcion", "estadoreg")


@admin.register(EstadosValidacion)
class estadosValidacionAdmin(admin.ModelAdmin):

    list_display = ("nombre", "estadoreg")
    search_fields = ("nombre", "estadoreg")
    list_filter = ("nombre", "estadoreg")


@admin.register(Presentacion)
class presentacionAdmin(admin.ModelAdmin):

    list_display = ("nombre", "descripcion", "estadoreg")
    search_fields = ("nombre", "descripcion", "estadoreg")
    list_filter = ("nombre",  "descripcion","estadoreg")


@admin.register(DescripcionCompra)
class descripcionCompraAdmin(admin.ModelAdmin):

    list_display = ("nombre", "descripcion", "estadoreg")
    search_fields = ("nombre", "descripcion", "estadoreg")
    list_filter = ("nombre",  "descripcion","estadoreg")

@admin.register(Proveedores)
class proveedoresAdmin(admin.ModelAdmin):

    list_display = ("codreg_proveedor", "proveedor", "correo", "estadoreg")
    search_fields = ("codreg_proveedor", "proveedor", "correo", "estadoreg")
    list_filter = ("codreg_proveedor", "proveedor", "correo", "estadoreg")

@admin.register(Areas)
class areasAdmin(admin.ModelAdmin):

    list_display = ("sede", "area", "estadoreg")
    search_fields = ("sede", "area", "estadoreg")
    list_filter = ("sede", "area", "estadoreg")

@admin.register(Solicitudes)
class solicitudesAdmin(admin.ModelAdmin):

    list_display = ("fecha", "usuarios", "area", "estadoreg")
    search_fields = ("fecha", "usuarios", "area", "estadoreg")
    list_filter = ("fecha", "usuarios", "area", "estadoreg")

@admin.register(SolicitudesDetalle)
class solicitudesDetalleAdmin(admin.ModelAdmin):

    list_display = ("solicitud", "item", "descripcion", "tiposCompra","cantidad","presentacion","producto","justificacion","estadosSolicitud","usuarioResponsableValidacion","especificacionesTecnicas","estadosValidacion","especificacionesCompras")
    search_fields = ("solicitud", "item", "descripcion", "tiposCompra","cantidad","presentacion","producto","justificacion","estadosSolicitud","usuarioResponsableValidacion","especificacionesTecnicas","estadosValidacion","especificacionesCompras")
    list_filter = ("solicitud", "item", "descripcion", "tiposCompra","cantidad","presentacion","producto","justificacion","estadosSolicitud","usuarioResponsableValidacion","especificacionesTecnicas","estadosValidacion","especificacionesCompras")

