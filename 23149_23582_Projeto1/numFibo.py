class Fibonacci:
    def __init__(self, n):
        self._n = n

    def fibo(self) -> list[int]:
        sequencia = [0] * self._n

        sequencia[0] = 1
        # caso a sequência desejada pelo usuário tenha apenas um dígito
        if self._n > 1:
            sequencia[1] = 1

        for i in range(2,len(sequencia), 1):
            anterior1 = sequencia[i - 1]
            anterior2 = sequencia[i - 2]

            sequencia[i] = anterior1 + anterior2
    
        return sequencia