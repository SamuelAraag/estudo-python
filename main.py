##obter um nome aleatorio a partir de uma lista
import random

n1 = input("Digite um nome:")
n2 = input("Digite outro nome:")
n3 = input("Digite outro nome:")
n4 = input("Digite outro nome:")
n5 = input("Digite outro nome:")

nomes = [n1, n2, n3, n4, n5]

nomeEscolhido = random.choice(nomes)

print(nomeEscolhido)