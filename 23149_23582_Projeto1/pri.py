class Primo:

    def __init__(self):
        self._numero = 0
    
    def ehPrimo(self, numero) -> bool:
    
        quantos_divisores  = 0
        metade = numero  // 2

        for possivel_divisor in range(3, metade +1, 2): #Para cada possivel divisor a partir de 3 e até metade de num inical
            if numero % possivel_divisor == 0:
                quantos_divisores += 1

        if quantos_divisores != 0:
            return False
        else:
            return True