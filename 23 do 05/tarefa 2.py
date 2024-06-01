# 2 - Elabore um script em linguagem Python que leia de 4 números
# reais, inserindo-os numa lista e ao final, mostre-os na ordem inversa.

lista = []

for x in range(4):
    numero = float(input("Numero == "))
    lista.append(numero)

lista.reverse()

print(lista)