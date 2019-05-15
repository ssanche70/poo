class Casa:



    def __init__(self, direccion):
        self.banos = 0
        self.ambientes = 0
        self.direccion = direccion

    def __repr__(self):
        return f'Casa ubicada en {self.direccion}'