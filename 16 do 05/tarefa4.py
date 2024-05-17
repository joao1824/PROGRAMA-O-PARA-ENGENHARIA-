# Em um script Python com duas listas de três elementos com números
# inteiros, crie uma nova lista onde cada elemento é a soma dos elementos de
# mesma posição nas duas primeiras listas.

lista1 = [5,2,3]
lista2 = [5,2,3]
lista_soma = []
y = 0
for x in lista1:
    num = x + lista2[y]
    y += 1
    lista_soma.append(num)

print(lista_soma)
    