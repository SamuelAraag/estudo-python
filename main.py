print("Tabuada")

num = int(input("Digite um número entre 1 e 10: "))

print("A tabuada do número {} é: ".format(num))

base = 11
i = 1

while i < base:
    print("{} x {} é igual a {}".format(num, i, num*i))
    i += 1

print("Obrigado por acessar a nossa calculadora.")
###
num = int(input("Digite um número: "))
prox = num + 1
anterior = num + -1

print("O número que você digitou foi: {}. O próximo número é {} e o anterior é {}".format(num, prox, anterior))

nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))

print("A média desse aluno foi: {}".format((nota1+nota2)/2))
