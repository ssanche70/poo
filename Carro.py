from Vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, placa, color):
        super().__init__(4, placa, color)

    def mover(self, distancia):
        if self.encendido:
            return f'Moviendose {distancia}'
        else:
            raise Exception('El carro no esta prendido')

    def reversa(self, distancia):
        if self.encendido:
            return f'Dando Reversa {distancia}'
        else:
            raise Exception('El carro no esta prendido')

    def encender(self):
        return super().encender()

    def frenar(self):
        super().frenar()