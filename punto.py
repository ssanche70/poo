class Elpunto:

    def __init__(self,corx,cory):
        self.corx = corx
        self.cory = cory

    def __repr__(self):
        return f'El punto esta en {self.corx} , {self.cory}'

    def __eq__(self, other):
        return self.corx == other.corx and self.cory == other.cory

    def desplazarx(self,corx):
        return Elpunto(self.corx + corx, self.cory)

    def desplazary(self,cory):
        return Elpunto(self.corx, self.cory + cory,)

    def hallarpendiente(self,other):
        return (other.corx - self.corx) / (other.cory - self.cory)