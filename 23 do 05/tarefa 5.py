# 5 - Dada uma lista L de n valores inteiros, elabore um programa que remova
# todos os números ímpares da lista.

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in L:
    if numero % 2 != 0:
        L.remove(numero)

print(L)