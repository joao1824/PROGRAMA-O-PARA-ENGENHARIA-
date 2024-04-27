# 1) Desenvolva um script Python que lê vários números positivos via teclado. Quando o
# número lido for -1, o script deve parar e exibir a soma de todos os números positivos
# inseridos, a média desses números, o menor e o maior número digitado.

x = 0
y = 0
z = 0 
list = []
while x != -1:
    x = float(input("valor ==> "))
     
    if x != -1:
        list.append(x)
        z = x + z  
     
        

med = z/2
print(f"A soma de todos é {z}")
print(f"A media é {med}")
print(f" o numero maior é {max(list)}")
print(f" o numero menor é {min(list)}")