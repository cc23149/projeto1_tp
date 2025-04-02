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
    pass

def raizQuadrada():
    pass

def numerosDeFibonacci():
    pass

def processamentoDeDados():
    pass




if __name__ == "__main__":
    seletorDeOpcoes()