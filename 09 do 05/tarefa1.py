# 1) Elabore um script em linguagem Python que leia de 10 números reais,
# inserindo-os numa lista e ao final, mostre-os na ordem inversa.

numeros = []

for numero in range(5):
    numero = float(input("Numero ==> "))
    numeros.append(numero)

numeros.reverse()

print(numeros)
