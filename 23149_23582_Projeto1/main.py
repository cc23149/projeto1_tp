import som, prod, os, raizQuad, numFibo
from tkinter import filedialog

def seletorDeOpcoes():
    opcao = -1      #a variavel opcao é inicializada com valor -1
    while opcao != 0:       #enquanto a opção digitada não for 0                           
        os.system('cls') or None       #o teminal é limpo e é exibido as funcionalidades disponiveis
        print("Seletor de Opções - Projeto 1")
        print("============= // =============\n")
        print("0 - Terminar Programa")
        print("1 - Primos")
        print("2 - Raiz Quadrada")
        print("3 - Números de Fibonacci")
        print("4 - Processamento de Dados")
        opcao = int(input("\nDigite a opção desejada: "))       #e é pedido ao usúario que digite o número correspondente a opção desejada 
        match opcao:
            case 1:        #caso o número digitado for 1
                os.system('cls') or None        #o terminal é limpo
                fazPrimos()                 #e é chamada a função fazPrimos()
            case 2:        #caso o número digitado for 2
                os.system('cls') or None        #o terminal é limpo
                fazRaizQuadrada()           #e é chamada a função fazRaizQuadrada
            case 3:        #caso o número digitado for 3
                os.system('cls') or None        #o terminal é limpo
                fazNumerosDeFibonacci()     #e é chamada a função fazNumerosDeFibonacci()
            case 4:         #caso o número digitado for 4
                os.system('cls') or None        #o terminal é limpo
                fazProcessamentoDeDados()   #e é chamada a função fazProcessamentoDeDados()

        if opcao != 0:                          #se a opção escolhida não foi encerrar o programa ao final da execulção da execução do médoto 
            input("\nTecle [Enter] para retornar ao seletor de opções: ")       #é avisado para apertar ENTER para poder escolher outra funcionalidade

def fazPrimos():
    print("1. Números primos num intervalo\n")

    valor_inicial = -1                          #inicializa valor_inicial com um número não aceito para que seja pedido um novo valor
    while valor_inicial <= 2:                   #pede ao usuario um valor até que a seja digitado um número maior que 2
        valor_inicial = int(input("Informe o valor inicial do intervalo: "))
        if valor_inicial <= 2:                  #caso não seja despara o erro e volta para a verificação da repetição
            print("\nO valor inicial precisa ser maior que 2!")

    valor_final = int(input("Informe o valor final do intervalo : "))     #pede o valor final do intervalo
    soma = som.Somatoria()                      #instância o objeto da classe Somatoria

    contador_linhas = 0                         #inicializa o contador de números por linha
    print(f"\nOs primos nesse intervalo são: ")
    for numero in range(valor_inicial, valor_final + 1, 1):     #faz a repetição do bloco de código no intervalo determinado entre os valores passados pelo usuario

        qts_divisores = 0                       #inicializa o contador de divisores
        metade = numero // 2                    #metade do número atual para o agilizar o cálculo de divisores
        for possivel_divisor in range(2, metade + 1, 1):   #faz a repetição para verificar se o número é primo
            if numero % possivel_divisor == 0:  #se o número atual for divisível por algum número menor que ele mesmo
                qts_divisores += 1              #a quantidade de divisores é aumentada em 1

            possivel_divisor += 1               #incrementa o divisor para verificar o próximo número

        
        if qts_divisores == 0:                  #se o número não possuir divisores ele é é primo
            contador_linhas += 1                #incrementa o contador de números por linha
              
            if numero < valor_final:            #caso o número atual for menor que o valor final do intervalo
                if contador_linhas >= 10:       #verifica se o contador de números por linha for maior ou igual a 10
                    print(numero,end=", \n") 
                    soma.somar(numero)  
                    contador_linhas = 0         #zera o contador de números por linha para começar a contar novamente
                else:                           #se o contador de números por linha for menor que 10
                    print(numero,end=", ") 
                    soma.somar(numero)
            else:                               #se o número atual for igual ao valor final do intervalo
                print(numero)
                soma.somar(numero)

        numero += 1                             #incrementa o número atual para verificar o próximo número  

    print(f"\n\nA soma desses primos é: {soma.valor}")       #exibe a soma dos números primos encontrados no intervalo
    try:                               
        print(f"A média aritmética dos primos é: {soma.media_aritmetica():.2f}") #exibe a média aritmética dos números primos encontrados no intervalo
    except Exception as erro:                                      #caso não tenha nenhum número exibe o erro
        print(erro) 


def fazRaizQuadrada(): 
    print("2. Raiz Quadrada\n")

    a = -1                          #inicializa a variável a com um número não aceito para que seja pedido um novo valor
    while a < 2:                    #pede ao usuario um valor até que a seja digitado um número maior que 2
        a = float(input("Informe o valor final do intervalo: "))            
        if a < 2:                   #caso não seja desparado o erro e volta para a verificação da repetição
            print("\nO valor final não pode ser menor que 2!")

    contador = 1                     #inicializa o contador com 1 para começar a calcular a raiz quadrada a partir de 1
    while contador <= a:
        raiz = raizQuad.RaizQuadrada(contador)      #instância o objeto da classe RaizQuadrada com o número atual do contador
        print(f"{contador:.1f}: {raiz.raiz_quadrada():.4f}")    #exibe o número atual do contador e a raiz quadrada do número atual do contador com 4 casas decimais
        
        contador = contador + 0.1        #incrementa o contador em 0.1 para calcular a raiz quadrada do próximo número
    

def fazNumerosDeFibonacci():   
    print("3 - Números de Fibonacci\n")

    n = -1                       #inicializa a variável n com um número não aceito para que seja pedido um novo valor
    while n < 1:
        n = int(input("Informe quantos números da sequência deseja saber: "))     #pede ao usuario um valor até que n seja digitado um número maior que 1
        if n < 1:                #caso não seja desparado o erro e volta para a verificação da repetição
            print("\nA quantidade não pode ser menor que 1!")

    contador = 0                #inicializa o contador com 0 para começar a calcular a sequência de Fibonacci a partir da primeira posição
    sequencia = numFibo.Fibonacci(n).fibo()     #instância o objeto da classe Fibonacci com o número atual do contador e chama o método fibo() para calcular a sequência de Fibonacci
    while contador < len(sequencia):       #enquanto o contador for menor que o tamanho da sequência de Fibonacci
        print(sequencia[contador], end=" ")   #exibe o número atual da sequência de Fibonacci e cocatena com o proximo
        
        contador += 1       #incrementa o contador para calcular o próximo número da sequência de Fibonacci


def fazProcessamentoDeDados():
    print("4 - Processamento de Dados\n")
    tiposDeArquivos = (                                     #tipos de arquivos aceitos para abrir
        ('Arquivos de texto', '*.TXT'),
        ('Arquivos JSON', '*.json'),
        ('Qualquer arquivo', '*.*')
    )
    nomeDoArquivo = filedialog.askopenfilename(             #abre a janela para selecionar o arquivo
                                title = 'Selecione o arquivo',
                                initialdir = r".\\",
                                multiple = False,
                                filetypes = tiposDeArquivos)
    if nomeDoArquivo != "" :                        #Se o nome do arquivo não é vazio
        arquivoDeEntrada = open(nomeDoArquivo, "r")       #abre o arquivo de entrada para leitura

        soma = som.Somatoria()                      #instância o objeto da classe Somatoria
        produt = prod.Produtorio()                  #instância o objeto da classe Produtorio
        linha ="-"                                  #inicializa a variável linha com um valor não aceito para que seja pedido um novo valor

        html = ""                                   #inicializa a variável html com uma string vazia
        html = f"<html> <table>"                    #cria a tabela no html

        html += f"<tr> <th>Valor</th> <th>Peso</th> </tr>"       #cria o cabeçalho da tabela no html
        
        while linha != "":                          #Concatena linhas de nota/peso na tabela
            linha = arquivoDeEntrada.readline()     #lê a linha do arquivo de entrada

            if linha != "":                         #se a linha não for vazia
                valor = float(linha[0:5])           #fatia a linha de dado no arquivo e transforma em float 
                peso = float(linha[6:10])           #fatia a linha de dado no arquivo e transforma em float

                html += f"<tr><td> {valor} </td> <td> {peso} </td></tr>"    #concatena os valores na tabela do html
                
                # chama os métodos de soma e produto
                soma.somar(valor)
                soma.somar_com_peso(valor, peso)
                produt.multiplicar(valor)
        html += "</table>"                          #fecha a tabela no html

        # concatena os paragrafos
        html += f"<h3>Resultados:</h3>"
        html += f"<p>Média aritimética: {soma.media_aritmetica():.2f} </p>"         
        html += f"<p>Raiz média quadratica: {soma.raiz_media_quadratica:.2f}</p>"   
        html += f"<p>Média ponderada: {soma.media_ponderada:.2f}</p>"  
        html += f"<p>Média geométrica: {produt.media_geometrica():.2f}</p>" 
        html += f"<p>Média harmônica: {soma.media_harmonica_dos_inversos():.2f} </p>" 
        html += f"<p>Maior valor: {produt._maior}</p>" 
        html += f"<p>Menor valor: {produt._menor}</p>" 
        html += "</body></html>"

        arquivoDeSaida = open("saida.html", "w")    #gera o arquivo de tipo html
        arquivoDeSaida.write(html)                  #grava a string com o código html no arquivo
        arquivoDeEntrada.close()                    #fecha o arquivo de entrada
        arquivoDeSaida.close()                      #fecha o arquivo se saida para salvar o que foi gravado

if __name__ == "__main__":      #executa o código
    seletorDeOpcoes()