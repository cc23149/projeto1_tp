import raizQuad


class Somatoria:
    def __init__(self):                     #construtor da classe Somatoria
        self._soma = 0.0                    #atributo privado que armazena a soma dos valores
        self._soma_valor_com_peso = 0.0     #atributo privado que armazena a soma dos valores com peso
        self._soma_pesos = 0.0              #atributo privado que armazena a soma dos pesos      
        self._quantos_valores_somados = 0   #atributo privado que armazena a quantidade de valores somados   
        self._quantos_valores_com_pesos_somados = 0     #atributo privado que armazena a quantidade de valores com pesos somados    
        self._maior = float('-inf')         #atributo privado que armazena o maior valor somado
        self._menor = float('inf')          #atributo privado que armazena o menor valor somado
        
    @property
    def valor(self):                        #método que retorna o valor da soma dos valores somados
        return self._soma
    
    @property
    def quantos(self):                      #método que retorna a quantidade de valores somados
        return self._quantos_valores_somados
    
    @property
    def raiz_media_quadratica(self):        #método que calcula a raiz média quadrática dos valores somados
        if self._quantos_valores_somados == 0:          #verifica se a quantidade de valores somados é igual a zero
            raise Exception("Não é possível calcular a média de 0 valores.")
            
        raiz = raizQuad.RaizQuadrada((self._soma / self._quantos_valores_somados))  #cria um objeto da classe RaizQuadrada com o valor da média dos valores somados
        return raiz.raiz_quadrada()         #retorna o valor da raiz quadrada da média dos valores somados
    
    @property
    def media_ponderada(self):              #método que calcula a média ponderada dos valores somados
        if self._soma_pesos == 0:           #verifica se a soma dos pesos é igual a zero
            raise Exception("Não se pode calcular a média ponderada. Soma de pesos = 0.")   
        return self._soma_valor_com_peso / self._soma_pesos     #retorna o valor da média ponderada dos valores somados

    def somar(self, valor_a_somar):             #método que soma um valor à soma total
        self._soma += valor_a_somar             #atualiza o valor da soma com o valor a somar
        self._quantos_valores_somados += 1      #atualiza a quantidade de valores somados com 1

    def somar_com_peso(self, valorX, peso):             #método que soma um valor com peso à soma total
        self._soma_valor_com_peso += valorX * peso      #atualiza o valor da soma com o valor a somar multiplicado pelo peso
        self._soma_pesos = self._soma_pesos + peso      #atualiza a soma dos pesos com o peso a somar
        self._quantos_valores_com_pesos_somados += 1    #atualiza a quantidade de valores com pesos somados com 1

    
    def media_aritmetica(self):                #método que calcula a média aritmética dos valores somados
        if self._quantos_valores_somados == 0:        #verifica se a quantidade de valores somados é igual a zero
            raise Exception("Não é possível calcular a média de 0 valores.") 
        
        return self._soma / self._quantos_valores_somados   #retorna o valor da média aritmética dos valores somados
    
    def somar_inversos(self, valor_a_somar):
        if valor_a_somar == 0:                     #verifica se o valor a somar é igual a zero
            raise Exception("Não é possível somar o inverso de zero.")
        self._soma += 1 / valor_a_somar        #atualiza o valor da soma com o inverso do valor a somar
        self._quantos_valores_somados += 1     #atualiza a quantidade de valores somados com 1

    def media_harmonica_dos_inversos(self):
        if self._quantos_valores_somados == 0:       #verifica se a quantidade de valores somados é igual a zero
            raise Exception("Não é possível calcular a média harmônica com 0 valores.") 
        return self._quantos_valores_somados / self._soma   #retorna o valor da média harmônica dos inversos dos valores somados


    