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
    
    try:
        prenda = Prenda.objects.get(id=1003)
        nombreP = prenda.nombreP
    except ObjectDoesNotExist:
        error = 'Prenda con id 1003 no encontrada'

    _dict = {
        'error':error,
        'nombreP':nombreP
    }

    # Render the response and send it back!
    return render(request, 'aplicacion/prenda.html', context=_dict)

