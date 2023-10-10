from random import randint

computador = randint(0,5)
print('=' * 20)
print("Vou pensar em um número entre 0 e 5")
numDigitado = input("Digite um número e tente adivinhar em qual eu pensei: ")
print('=' * 20)

if computador == numDigitado:
    print("Uau, você conseguiu adivinhar! Eu realmente pensei em {}".format(computador))
else:
    print("Você errou, eu pensei no numero {}".format(computador))
