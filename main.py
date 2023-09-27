##Mostrar salário do funcionário com 15% de aumeto

import locale

aumento = 10
salario_base = int(input("Digite o seu salário atual: "))
valor_aumento = (salario_base * aumento) / 100
valor_total = salario_base + valor_aumento

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

salario_calculado = locale.currency(valor_total, grouping=True, symbol=None)

print("O seu novo salário será: R$:{}".format(salario_calculado))
