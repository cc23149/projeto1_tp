import som, prod, os, raizQuad, numFibo
from tkinter import filedialog

def seletorDeOpcoes():
    opcao = -1
    while opcao != 0:
        os.system('cls') or None
        print("Seletor de Opções - Projeto 1")
        print("============= // =============\n")
        print("0 - Terminar Programa")
        print("1 - Primos")
        print("2 - Raiz Quadrada")
        print("3 - Números de Fibonacci")
        print("4 - Processamento de Dados")
        opcao = int(input("\nDigite a opção desejada: "))
        match opcao:
            case 1:
                os.system('cls') or None
                primos()
            case 2:
                os.system('cls') or None
                fazRaizQuadrada()
            case 3:
                os.system('cls') or None
                numerosDeFibonacci()
            case 4:
                os.system('cls') or None
                processamentoDeDados()

        if opcao != 0:
            input("\nTecle [Enter] para retornar ao seletor de opções: ")

def primos():
    print("1. Números primos num intervalo\n")

    valor_inicial = -1
    while valor_inicial <= 2:
        valor_inicial = int(input("Informe o valor inicial do intervalo: "))
        if valor_inicial <= 2:
            print("\nO valor inicial precisa ser maior que 2!")

    valor_final = int(input("Informe o valor final do intervalo : ")) 
    soma = som.Somatoria()

    contadorDeLinhas = 0
    print(f"\nOs primos nesse intervalo são: ")
    for numero in range(valor_inicial, valor_final + 1, 1):

        qts_divisores = 0
        metade = numero // 2
        for possivel_divisor in range(2, metade + 1, 1):
            if numero % possivel_divisor == 0:
                qts_divisores += 1

            possivel_divisor += 1

        
        if qts_divisores == 0:
            contadorDeLinhas += 1
              
            if numero < valor_final:
                if contadorDeLinhas >= 10:
                    print(numero,end=", \n")
                    soma.somar(numero)
                    contadorDeLinhas = 0
                else:
                    print(numero,end=", ")
                    soma.somar(numero)
            else:
                print(numero)
                soma.somar(numero)

        numero += 1

    print(f"\n\nA soma desses primos é: {soma.valor}")
    try:
        print(f"A média aritmética dos primos é: {soma.media_aritmetica():.2f}")
    except Exception as erro:
        print(erro)


def fazRaizQuadrada():
    print("2. Raiz Quadrada\n")

    a = -1
    while a < 2:
        a = float(input("Informe o valor final do intervalo: "))
        if a < 2:
            print("\nO valor final não pode ser menor que 2!")

    contador = 1
    while contador <= a:
        raiz = raizQuad.RaizQuadrada(contador)
        print(f"{contador:.1f}: {raiz.raiz_quadrada():.4f}")
        
        contador = contador + 0.1
    

def numerosDeFibonacci():
    print("3 - Números de Fibonacci\n")

    n = -1
    while n < 1:
        n = int(input("Informe quantos números da sequência deseja saber: "))
        if n < 1:
            print("\nA quantidade não pode ser menor que 1!")

    contador = 0
    sequencia = numFibo.Fibonacci(n).fibo()
    while contador < len(sequencia):
        print(sequencia[contador], end=" ")
        
        contador += 1


def processamentoDeDados():
    print("4 - Processamento de Dados\n")
    tiposDeArquivos = (
        ('Arquivos de texto', '*.TXT'),
        ('Arquivos JSON', '*.json'),
        ('Qualquer arquivo', '*.*')
    )
    nomeDoArquivo = filedialog.askopenfilename(
                                title = 'Selecione o arquivo',
                                initialdir = r".\\",
                                multiple = False,
                                filetypes = tiposDeArquivos)
    if nomeDoArquivo != "" :
        arquivoDeEntrada = open(nomeDoArquivo, "r")

        soma = som.Somatoria()
        produt = prod.Produtorio()
        linha ="-"

        html = ""
        html = f"<html> <table>"

        html += f"<tr style ='border: 1px solid black; border-collapse: collapse;'> <th>Valor</th> <th>Peso</th> </tr>"
        # while que concatena linhas de nota/peso na tabela
        while linha != "":
            linha = arquivoDeEntrada.readline()

            if linha != "":
                valor = float(linha[0:3]) 
                peso = float(linha[4:7])

                html += f"<tr><td> {valor} </td> <td> {peso} </td></tr>"

                soma.somar(valor)
                soma.somar_com_peso(valor, peso)
                produt.multiplicar(valor)
        html += "</table>"

            # cada print deve ser um <p> embaixo da tabela
        html += f"<h3>Resultados:</h3>"
        html += f"<p>Média aritimética: {soma.media_aritmetica():.2f} </p>"
        html += f"<p>Raiz média quadratica: {soma.raiz_media_quadratica:.2f}</p>"
        html += f"<p>Média ponderada: {soma.media_ponderada:.2f}</p>" 
        html += f"<p>Média geométrica: {produt.media_geometrica():.2f}</p>"
        html += f"<p>Média harmônica: {soma.media_harmonica_dos_inversos():.2f} </p>"
        html += f"<p>Maior valor: {produt._maior}</p>"
        html += f"<p>Menor valor: {produt._menor}</p>"
        html += "</body></html>"
        arquivoDeSaida = open("saida.html", "w")
        arquivoDeSaida.write(html)
        arquivoDeEntrada.close()
        arquivoDeSaida.close()

if __name__ == "__main__":
    seletorDeOpcoes()