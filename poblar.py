import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proyecto.settings')

import django

django.setup()

from aplicacion.models import Vendedor, Venta, Prenda


def populate():
    add_vendedor(1001, 'vendedor1')
    add_vendedor(1002, 'vendedor2')
    add_vendedor(1003, 'vendedor3')

    add_prenda(1001, 'prenda1')
    add_prenda(1002, 'prenda2')
    add_prenda(1003, 'prenda3')
    add_prenda(1004, None)

    add_venta(1001, 1001, 1001)
    add_venta(1002, 1001, 1003)
    add_venta(1003, 1003, 1003)
    add_venta(1004, 1003, 1001)
    add_venta(1005, 1002, 1002)

def add_vendedor(id, nombre):
    Vendedor.objects.get_or_create(id=id, nombreV=nombre)


def add_prenda(id, nombre):
    Prenda.objects.get_or_create(id=id, nombreP=nombre)

def add_venta(id, vendedor, prenda):
    v = Vendedor.objects.get(id=vendedor)
    p = Prenda.objects.get(id=prenda)
    Venta.objects.get_or_create(id=id, vendedor=v, prenda=p)

if __name__ == '__main__':
    print("Starting aplicacion population script...")
    populate()
