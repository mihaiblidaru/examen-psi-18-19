# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aplicacion.models import Prenda, Vendedor, Venta


class PrendaAdmin(admin.ModelAdmin):
    list_display = ('nombreP',)

class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nombreV',)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'prenda','fechaDeVenta')
    exclude = ('fechaDeVenta',)


admin.site.register(Prenda, PrendaAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Venta, VentaAdmin)
