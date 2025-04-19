from math import pow
class Produtorio:
    def __init__(self):
        self._produto = 1.0                         # totalizador de valores multiplicados
        self._quantos_valores_multiplicados = 0     # contador de valores multiplicados
        self._maior = float('-inf')
        self._menor = float('inf')
        
    def multiplicar(self, valor_a_multiplicar):
        self._produto *= valor_a_multiplicar        # acumula o valor passado pela aplicação
        self._quantos_valores_multiplicados += 1    # conta mais um valor multiplicado
        if valor_a_multiplicar > self._maior:
            self._maior = valor_a_multiplicar
        if valor_a_multiplicar < self._menor:
            self._menor = valor_a_multiplicar
            
    @property
    def valor(self):                         # método que retorna o valor do produto dos valores multiplicados
        return self._produto
    
    @property
    def quantos(self):                       # método que retorna a quantidade de valores multiplicados
        return self._quantos_valores_multiplicados
    
    def media_geometrica(self):              #método que calcula a média geométrica dos valores multiplicados
        try:
            return pow(self._produto, 1/self._quantos_valores_multiplicados) #retorna o valor da média geométrica dos valores multiplicados
        except Exception as erro:
            raise Exception(f"Erro ao calcular a média geométrica: {erro}") 