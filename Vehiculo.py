class Vehiculo:

    n_ruedas = 0
    placa = ''
    color = ''
    encendido = False
    moviendose = False



    def __init__(self, n_ruedas, placa, color):
        self.n_ruedas = n_ruedas
        self.placa = placa
        self.color = color
        self.encendido =  False

    def mover(self, distancia):
        pass

    def reversa(self):
        pass

    def encender(self):
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True
        return self.encendido


    def frenar(self):
        pass