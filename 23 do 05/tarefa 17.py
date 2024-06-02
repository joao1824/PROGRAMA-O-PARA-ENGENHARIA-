# Escreva um algoritmo que leia um número inteiro entre 100 e 999 e
# imprima na saída cada um dos algarismo que compõem o número.

while True:
    numero = int(input("número inteiro entre 100 e 999 = "))
    if numero > 100 and numero < 999:
        break
    else:
        continue

lista = [10,100,1000]
aux = 1
for x in lista:
    alg = numero%x
    alg = alg//aux
    print(alg)
    aux =  aux*10