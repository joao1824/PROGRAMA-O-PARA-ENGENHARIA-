# 19 – Leia um vetor com 4 número inteiros. Escreva os elementos do vetor
# eliminando elementos repetidos

lista = []

aux = 0
for p in range(4):
    n = int(input("Numero inteiro = "))

    lista.append(n)

for x in lista:
    contador = lista.count(x)
    print(contador)
    if contador != 1:
        lista.remove(x)


print(lista)
