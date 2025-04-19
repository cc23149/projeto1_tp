import math 
class RaizQuadrada:             
    def __init__(self,numeroReal):          
        self._numeroReal = numeroReal       #atributo privado que armazena o número real desejado para calcular a raiz quadrada
        
    @property                           
    def valor(self):                       
        return self._numeroReal              
    
    def raiz_quadrada(self):             
        y = self._numeroReal                #inicializa a variavel y rece o atributo
        g = y                               #inicializa a variável g com o valor de y

        x = (g + y/ g) / 2                  #inicializa a variável x com a média entre g e y/g                                         
        while abs((g / x) - 1) > 0.0001:    #enquanto  continua enquanto a diferença entre g/x e 1 for maior que 0.0001
            g = x                           #atualiza aalor atual de x
            x = (g + y/ g) / 2              #atualiza o valor de x com a média entre g e y/g
        else:
            return x                        #retorna o valor de x, que é a raiz quadrada do número real desejado
