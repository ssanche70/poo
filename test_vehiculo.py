from unittest import TestCase
from Vehiculo import Vehiculo

class TestVehiculo(TestCase):

    def test_encender(self):

        dado = Vehiculo(4, 'RPG-998', 'Plata')
        espero = False
        recibo = dado.encendido
        self.assertEqual(espero, recibo)

        espero = True
        recibo = dado.encender()
        self.assertEqual(espero, recibo)

        espero = False
        recibo = dado.encender()
        self.assertEqual(espero, recibo)