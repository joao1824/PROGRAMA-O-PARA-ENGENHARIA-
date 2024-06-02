# – Elabore um script em linguagem Python que, dados dois inteiros x e y,
# retorna uma lista com todos os valores entre x e y (inclusive), considerando x <
# y. Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6]

x = int(input("Valor de periodo (1)==> "))

y = int(input("Valor de periodo (2)==> "))

lista = []

if x < y:
    for x in range(x,y+1):
        lista.append(x)
if y < x:
    for x in range(x,y-1,-1):
        lista.append(x)

print(lista)