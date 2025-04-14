import math 

class RaizQuadrada:
    def __init__(self,numeroReal):
        self._numeroReal = numeroReal
        
    @property
    def valor(self):
        return self._numeroReal
    
    def raiz_quadrada(self):
        y = self._numeroReal
        g = y

        x = (g + y/ g) / 2
        while abs((g / x) - 1) > 0.0001:
            g = x
            x = (g + y/ g) / 2
        else:
            return x
