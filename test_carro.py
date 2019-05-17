from unittest import TestCase
from Carro import Carro


class TestCarro(TestCase):
    def test_mover(self):
        mi_carro = Carro('ABC-123', 'Gris')
        print(f'--Inicia la prueba de conduccion {mi_carro}')
        espero = 'Moviendose 10'
        mi_carro.encender()
        resultado = mi_carro.mover(10)
        self.assertEqual(espero, resultado)

    def test_reversa(self):
        self.fail()

    def test_encender(self):
        self.fail()

    def test_frenar(self):
        self.fail()
