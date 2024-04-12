# Desenvolva um script em linguagem Python que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# • salário bruto.
# • quanto pagou ao INSS.
# • quanto pagou ao sindicato.
# • o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

hora = float(input("Quantos ganha por hora "))
horatr = float(input("Quantas horas trabalha "))

sal_bruto = hora * horatr
imposto_renda = sal_bruto *(11/100)
inss = sal_bruto *(8/100)
sindicato = sal_bruto *(5/100)
liquido = sal_bruto - imposto_renda - inss - sindicato 


print(f"Seu salario bruto é = {sal_bruto}\nImposto de renda = {imposto_renda}\nINSS = {inss}\nSindicato = {sindicato}\nSalario liquido = {liquido}")