#Crie um programa que peça um valor e imprima na tela se o valor é positivo, negativo ou ainda igual a zero.

numero = float(input("Digite um valor = "))

if numero < 0:
    print(f"O numero {numero} é negativo") 

elif numero > 0:
    print(f"O numero {numero} é positivo")

else:
    print(f"o numero {numero} é igual a zero")