# Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles. Mostre no final a soma dos
# números.

numb1 = int(input("Numero (1) ==> "))
numb2 = int(input("Numero (2) ==> "))
numb1 += 1


if numb1 < numb2:
    print(list(range(numb1,numb2)))
if numb2 < numb1:
    print(list(range((numb2+1),(numb1-1))))