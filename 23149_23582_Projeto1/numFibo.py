class Fibonacci:     
    def __init__(self, n):
        self._n = n     #atributo privado que armazena o número de dígitos desejados na sequência de Fibonacci recebino pelo parâmetro

    def fibo(self) -> list[int]:
        sequencia = [0] * self._n   #inicializa a lista de inteiros com o valor do atributo como tamanho
        sequencia[0] = 1    #inicializa o primeiro elemento da sequência com 1
        
        if self._n > 1:          # caso a sequência desejada pelo usuário tenha mais de um dígito
            sequencia[1] = 1     #inicializa o segundo elemento da sequência com 1

        for i in range(2,len(sequencia), 1):        #a partir do terceiro elemento da sequência faz a repetição até acabar a lista
            anterior1 = sequencia[i - 1]            #armazena o valor do elemento anterior
            anterior2 = sequencia[i - 2]            #armazena o valor do elemento dois lugares antes

            sequencia[i] = anterior1 + anterior2    #calcula o valor do elemento atual como a soma dos dois anteriores
    
        return sequencia    #retorna a sequência de Fibonacci gerada