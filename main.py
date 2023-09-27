print("TABUADA")
num = int(input("Digite um número e dê enter para ver a tabuada5: "))

if num:
    print("A tabuada do número {} é: ".format(num))
    base = 11
    i = 1

    while i < base:
        print("{} x {} é igual a {}".format(num, i, num*i))
        i += 1

print("Obrigado por acessar a nossa calculadora.")
