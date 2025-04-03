import som, prod, os

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
                primos()
            case 2:
                fazRaizQuadrada()
            case 3:
                numerosDeFibonacci()
            case 4:
                processamentoDeDados()

        if opcao != 0:
            input("Tecle [Enter] para retornar ao seletor de opções: ")

def primos():
    print("\n1. Números primos numero intervalo\n")

    valor_inicial = -1
    while valor_inicial <= 2:
        valor_inicial = int(input("Informe o valor inicial do intervalo: "))
        if valor_inicial <= 2:
            print("O valor inicial precisa ser maior que 2!")

    valor_final = int(input("Informe o valor final do intervalo : ")) 
    soma = som.Somatoria()

    print(f"Os primos nesse intealo são: ")
    for numero in range(valor_inicial, valor_final + 1, 1):

        qts_divisores = 0
        metade = numero // 2
        for possivel_divisor in range(2, metade + 1, 1):
            if numero % possivel_divisor == 0:
                qts_divisores += 1

            possivel_divisor += 1

        if qts_divisores == 0:
            if numero > valor_final:
                print( numero,end=", ")
                soma.somar(numero)
            else:
                print(numero)
                soma.somar(numero)
        
        numero += 1

    print(f"\nA soma desses primos é: {soma.valor}")
    try:
        print(f"A média aritmética dos primos é: {soma.media_aritmetica():5.2f}")
    except Exception as erro:
        print(erro)


def fazRaizQuadrada():
    pass

def numerosDeFibonacci():
    pass

def processamentoDeDados():
    pass




if __name__ == "__main__":
    seletorDeOpcoes()