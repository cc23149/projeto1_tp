import math

class RaizQuadrada:
    def __init__(self):
        self._numeroReal = 0.0

    @property
    def valor(self):
        return self._numeroReal
    
    def raiz_quadrada(self):
        y = self._numeroReal
        g = y

        x = (g + y/ g) / 2
        while math.abs((g / x) - 1) > 0.0001:
            g = x
        else:
            return x
