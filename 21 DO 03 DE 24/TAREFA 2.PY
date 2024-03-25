#Uma imobiliária paga aos seus corretores um salário base de R$1.500,00. Além disso, uma comissão de R$ 200,00 por cada imóvel vendido e 5% do valor de cada venda.
#Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total de suas vendas.
#Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis.

nome = input("Digite seu nome = ")
imoveis_vendido = int(input("Quatidade de imóveis vendidos = "))
valo_total = int(input("Valor toal das vendas = "))

comis = imoveis_vendido * 200.00
comis_2 = valo_total * 0.05
salario = 1500                                                                      

sal_total = comis + comis_2 + salario

print((f"{nome} seu salário total com base nos dados fornecidos é {sal_total}"))

