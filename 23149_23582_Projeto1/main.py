import som, prod, os, pri

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
    numInicial = int(input("Informe o valor inicial do intervalo(valor > 2): "))
    while numInicial <= 2:
        print("O valor inicial precisa ser maior que 2!")
        numInicial = int(input("Informe o valor inicial do intervalo: "))
    numFim = int(input("Informe o valor final do intervalo : ")) 
    soma = som.Somatoria()
    primo = pri.Primo()

    print(f"Os primos entre {numInicial} e {numFim} são: ")

    for i in range(numInicial, numFim + 1):  #Enquanto esta dentro do perido
        if primo.ehPrimo(numInicial):
            print(numInicial, end=", ")
            soma.somar(numInicial)  #se o número não tiver nenhum divisor somanmos ele aos primos

        numInicial += 1        

    print(f"\nA soma dos primos é: {soma.valor}")
    print(f"A média aritmética dos primos é: {soma.media_aritmetica()}")

def raizQuadrada():
    pass

def numerosDeFibonacci():
    pass

def processamentoDeDados():
    pass




if __name__ == "__main__":
    seletorDeOpcoes()