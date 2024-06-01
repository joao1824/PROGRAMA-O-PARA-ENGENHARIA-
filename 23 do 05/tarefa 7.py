# 7 – De acordo com a tupla Vendas apresentada abaixo. Desenvolva um
# script em linguagem Python que calcule a média, a Variância, o Desvio
# Padrão, o menor valor e o maior Valor deste conjunto.
# Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)
# Media = Ʃi Vendasi
#             n
# Variância = Ʃi (Vendasi – Média)²
#                       n
# Desvio Padrão = √𝑉𝑎𝑟𝑖â𝑛𝑐𝑖a

import math


Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)
aux1 = 0
aux2 = 0

for venda in Vendas:
    aux1 += venda

print(f"Média = {round(aux1/12,2)}")

for venda in Vendas:
    aux2 += (venda - (aux1/12))**2

print(f"Variância = {round(aux2/12,2)}")

print(f"Desvio Padrão = {round(math.sqrt(aux2/12),2)}")

print(f"Menor Valor = {min(Vendas)}")

print(f"Maior Valor = {max(Vendas)}")



