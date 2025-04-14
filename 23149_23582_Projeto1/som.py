import raizQuad


class Somatoria:
    def __init__(self): 
        self._soma = 0.0
        self._soma_valor_com_peso = 0.0
        self._soma_pesos = 0.0                  
        self._quantos_valores_somados = 0   
        self._quantos_valores_com_pesos_somados = 0    
        self._maior = float('-inf')
        self._menor = float('inf')
        
    @property
    def valor(self):
        return self._soma
    
    @property
    def quantos(self):
        return self._quantos_valores_somados
    
    @property
    def raiz_media_quadratica(self):
        if self._quantos_valores_somados == 0:
            raise Exception("Não é possível calcular a média de 0 valores.")
            
        raiz = raizQuad.RaizQuadrada((self._soma / self._quantos_valores_somados))
        return raiz.raiz_quadrada()
    
    @property
    def media_ponderada(self):
        if self._soma_pesos == 0:
            raise Exception("Não se pode calcular a média ponderada. Soma de pesos = 0.")
        return self._soma_valor_com_peso / self._soma_pesos

    def somar(self, valor_a_somar):
        self._soma += valor_a_somar        
        self._quantos_valores_somados += 1 

    def somar_com_peso(self, valorX, peso):
        self._soma_valor_com_peso += valorX * peso 
        self._soma_pesos = self._soma_pesos + peso 
        self._quantos_valores_com_pesos_somados += 1

    
    def media_aritmetica(self):
        if self._quantos_valores_somados == 0:
            raise Exception("Não é possível calcular a média de 0 valores.")
        
        return self._soma / self._quantos_valores_somados
    
    def somar_inversos(self):
        pass

    def media_harmonica_dos_inversos(self):
        pass