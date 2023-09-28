##Mostrar salário do funcionário com 15% de aumento
##60 reais por dia
##0,15 por KM

dias = int(input("Quantos dias você ficou com o carro: "))
km = int(input("Quantos kilometros você andou com o carro: "))

valor_total_dias = dias * 60
valor_total_km = km * 0.15

print("O total a pagar é: R${:.2f}".format(valor_total_km + valor_total_dias))
