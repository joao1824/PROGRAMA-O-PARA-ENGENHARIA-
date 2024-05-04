# Desenvolva um programa que leia 5 números e informe o maior número

aux1 = float(input("Número ==> "))
for x in range(4):
    numero = float(input("Número ==> "))
    if numero >= aux1:
        aux1 = numero
    

print(f"O maior é {aux1}")
    

