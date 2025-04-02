import som, prod, os

def seletorDeOpcoes():
    opcao = -1
    while opcao != 0:
        os.system('cls') or None
        print("Seletor de Opções - Projeto 1")
        print("=========================//=========================")
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
                raizQuadrada()
            case 3:
                numerosDeFibonacci()
            case 4:
                processamentoDeDados()
            case 0:
                print("Finalizando...")
                break
        input("Digite [Enter] para prosseguir...")


def primos():
    print("1. Números primos num intervalo")
    numInicio = int(input("Informe o valor inicial do intervalo(valor > 2): "))
    while numInicio <= 2:
        print("O valor inicial precisa ser maior que 2!")
        numInicio = int(input("Informe o valor inicial do intervalo: "))
    numFim = int(input("Informe o valor final do intervalo : ")) 
    soma = som.Somatoria
    
    for i in range(numInicio, numFim+1, 1):
        pass

    print(f"Os primos entre {numInicio} e {numFim} são: {primo}")
    print(f"A soma dos primos é: {somaPrimos}")
    print(f"A média aritmética dos primos é: {media}")

def raizQuadrada():
    pass

def numerosDeFibonacci():
    pass

def processamentoDeDados():
    pass




if __name__ == "__main__":
    seletorDeOpcoes()