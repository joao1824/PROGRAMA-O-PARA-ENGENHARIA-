# Desenvolva um script Python que lê vários números
# positivos via teclado. Quando o número lido for -1, o script
# deve parar e exibir a soma de todos os números positivos
# inseridos, a média desses números, o menor e o maior número
# digitado. No entanto, utilize uma lista para armazenar os
# números.

soma = 0
media = []
lista = []

while True:
    numero = float(input("Digite um Numero (-1 para cancelar) ==> "))
    if numero >= 0:
        media.append(numero)
        soma += numero
    if numero != -1:
        lista.append(numero)
    if numero == -1:
        break






print(f"soma = {soma}")
print(f"Média = {soma/len(media)}")
print(f"Marior numero é {max(lista)} e o menor numero é {min(lista)}")