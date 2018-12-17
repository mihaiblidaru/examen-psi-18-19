# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from aplicacion.models import Prenda, Vendedor, Venta
from django.core.exceptions import ObjectDoesNotExist

def prenda(request):
    prenda = None
    nombreP = None
    error = None
    vendedores = []
    
    try:
        prenda = Prenda.objects.get(id=1003)
        nombreP = prenda.nombreP
        
        ventas = Venta.objects.filter(prenda=prenda)
        if(len(ventas) < 1):
            error = 'Esta prenda no tiene vendedores'
        id_vendedores = []
        for venta in ventas:
            if not venta.vendedor.id in id_vendedores:
                vendedores.append(venta.vendedor)
                id_vendedores.append(venta.vendedor.id)
    except ObjectDoesNotExist:
        error = 'Prenda con id 1003 no encontrada'

    _dict = {
        'error':error,
        'nombreP':nombreP,
        'vendedores':vendedores
    }

    return render(request, 'aplicacion/prenda.html', context=_dict)

