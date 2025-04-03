import som, prod, os, raizQuad

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

    print(f"\nOs primos nesse intealo são: ")
    for numero in range(valor_inicial, valor_final + 1, 1):

        qts_divisores = 0
        metade = numero // 2
        for possivel_divisor in range(2, metade + 1, 1):
            if numero % possivel_divisor == 0:
                qts_divisores += 1

            possivel_divisor += 1

        if qts_divisores == 0:
            if numero < valor_final:
                print(numero,end=", ")
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
    print("2. Raiz Quadrada de 1 a um valor\n")

    a = -1
    while a <= 1:
        a = float(input("Informe o valor inicial do intervalo: "))
        if a <= 1:
            print("\nO valor inicial precisa ser maior que 2!")

    contador = 1
    raiz = raizQuad.RaizQuadrada()
    while contador < a:
        print(contador + ":" + raiz.raiz_quadrada(contador))
        
        contador += 0.1
    

def numerosDeFibonacci():
    pass

def processamentoDeDados():
    pass




if __name__ == "__main__":
    seletorDeOpcoes()