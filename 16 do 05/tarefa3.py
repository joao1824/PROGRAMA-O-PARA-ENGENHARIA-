# 3 – Elabore um script em linguagem Python que, dados dois inteiros x e y,
# retorna uma lista com todos os valores entre x e y (inclusive), considerando x <
# y

x = int(input("Valor x ==> "))
y = int(input("Valor y ==> "))
lista1 = []
if x < y:
    for num in range(x,y+1):
        lista1.append(num)    
if x > y:
    for num in range(x,y-1,-1):
        lista1.append(num)  

print(lista1)