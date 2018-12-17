# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

class Vendedor(models.Model):
    nombreV = models.CharField(max_length=128, unique=True)

    def __str__(self): 
        return str(self.nombreV)

    def __unicode__(self): 
        return str(self.nombreV)
    
    class Meta:
        verbose_name_plural = "Vendedores"


class Prenda(models.Model):
    nombreP = models.CharField(max_length=128, unique=True, blank=True, null=True)

    def __str__(self): 
        return str(self.nombreP)

    def __unicode__(self): 
        return str(self.nombreP)


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor)
    prenda = models.ForeignKey(Prenda)
    fechaDeVenta = models.DateField(default=timezone.now)

