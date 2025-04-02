class Somatoria:
    def __init__(self):
        self._soma = 0.0                        # totalizador de valores somados
        self._quantos_valores_somados = 0       # contador de valores somados
        self._maior = float('-inf')
        self._menor = float('inf')
        
    @property
    def valor(self):
        return self._soma
    
    @property
    def quantos(self):
        return self._quantos_valores_somados
    
    def somar(self, valor_a_somar):
        self._soma += valor_a_somar         # acumula o valor passado pela aplicação
        self._quantos_valores_somados += 1  # conta mais um valor somado
        
    def media_aritmetica(self):
        if self._quantos_valores_somados == 0:
            raise Exception("Não é possível calcular a média de 0 valores.")
        
        return self._soma / self._quantos_valores_somados