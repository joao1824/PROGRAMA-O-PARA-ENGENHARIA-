#3) Crie um script em linguagem Python que leia dois vetores com 5 elementos
#cada. Gere um terceiro vetor de 10 elementos, cujos valores deverão ser
#compostos pelos elementos intercalados dos dois outros vetores. Exibir na
#tela todos os vetores em linhas separadas.

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = []
for x in range(5):
    lista3.append(lista1[x])
    lista3.append(lista2[x])
    

print(lista3)