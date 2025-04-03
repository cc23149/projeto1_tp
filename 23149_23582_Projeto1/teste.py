import som

def primos():
    print("1. Números primos numero intervalo")

    valor_inicial = int(input("Informe o valor inicial do intervalo: "))
    while valor_inicial <= 2:
        print("O valor inicial precisa ser maior que 2!")
        valor_inicial = int(input("Informe o valor inicial do intervalo: "))

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
            if numero == valor_inicial:
                print(f"{numero}",end="")
                soma.somar(numero)
            else:
                print(end=", " + f"{numero}")
                soma.somar(numero)
        
        numero += 1

    print(f"\nA soma desses primos é: {soma.valor}")
    try:
        print(f"A média aritmética dos primos é: {soma.media_aritmetica():5.2f}")
    except Exception as erro:
        print(erro)

if __name__ == "__main__":
    primos()