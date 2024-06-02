# 20 – Faça um programa que receba 6 números inteiros e mostre:
# - Os números pares digitados
# - A soma dos números pares digitados
# - Os números ímpares digitados
# - A quantidade de números ímpares digitados

lista = []
pares = []
impares = []

for x in range(6):
    n = int(input("Numero inteiro = "))
    lista.append(n)

for numero in lista:
    par_impar = numero%2
    if par_impar == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Numero pares = {pares}")
print(f"Soma dos numeros pare = {sum(pares)}")
print(f"Numeros impares = {impares}")
print(f"Quantidade de numeros impares = {len(impares)}")
    