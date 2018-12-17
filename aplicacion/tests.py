from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.test import Client
from aplicacion.models import Vendedor, Prenda, Venta

class AplicacionTests(TestCase):
    def setUp(self):
        # The test client is a Python class that acts as a dummy Web browser
    
        self._client   = Client()

    def add_vendedor(self, id, nombre):
        Vendedor.objects.get_or_create(id=id, nombreV=nombre)

    def add_prenda(self, id, nombre):
        Prenda.objects.get_or_create(id=id, nombreP=nombre)

    def add_venta(self, id, vendedor, prenda):
        v = Vendedor.objects.get(id=vendedor)
        p = Prenda.objects.get(id=prenda)
        Venta.objects.get_or_create(id=id, vendedor=v, prenda=p)


    def test_examen(self): 
        print '    Borrando todos los objetos de la base de datos'
        Venta.objects.all().delete()
        Vendedor.objects.all().delete()
        Prenda.objects.all().delete()

        self.assertEqual(len(Venta.objects.all()), 0) 
        self.assertEqual(len(Vendedor.objects.all()), 0) 
        self.assertEqual(len(Prenda.objects.all()), 0) 

        print '    Creando vendedor1'
        self.add_vendedor(1001, 'vendedor1')
        print '    Creando prenda1'
        self.add_prenda(1001, 'prenda1')
        print '    Creando prenda2'
        self.add_prenda(1003, 'prenda2')
        print '    Creando venta vendedor1 prenda2'
        self.add_venta(1001, 1001, 1003)

        vendedores = Vendedor.objects.all()
        self.assertEqual(len(vendedores), 1) 
        self.assertEqual(vendedores[0].id, 1001)
        self.assertEqual(vendedores[0].nombreV, 'vendedor1')
        print '    Vendedor creado correctamente'

        prendas = Prenda.objects.all().order_by('id')
        self.assertEqual(len(prendas), 2) 
        self.assertEqual(prendas[0].id, 1001)
        self.assertEqual(prendas[0].nombreP, 'prenda1')
        self.assertEqual(prendas[1].id, 1003)
        self.assertEqual(prendas[1].nombreP, 'prenda2')
        print '    Prendas creadas correctamente'

        ventas = Venta.objects.all()
        self.assertEqual(len(ventas), 1) 
        self.assertEqual(ventas[0].id, 1001)
        self.assertEqual(ventas[0].vendedor.id, 1001)
        self.assertEqual(ventas[0].prenda.id, 1003)
        print '    Venta creada correctamente'


        response = self._client.post(reverse('prenda'))

        print '    Comprobando resultados devueltos por la vista'
        self.assertIn('prenda2', str(response.content).decode('utf-8'))
        self.assertIn('1001', str(response.content).decode('utf-8'))
        self.assertIn('vendedor1', str(response.content).decode('utf-8'))
        print '    Resultados ok'

