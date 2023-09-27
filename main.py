##Mostrar salário do funcionário com 15% de aumento

import locale

AUMENTO = 15
SALARIO_BASE = int(input("Digite o seu salário atual: "))
valor_aumento = (SALARIO_BASE * AUMENTO) / 100
valor_total = SALARIO_BASE + valor_aumento

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

salario_calculado = locale.currency(valor_total, grouping=True, symbol=None)

print("O seu novo salário será: R$:{}".format(salario_calculado))
