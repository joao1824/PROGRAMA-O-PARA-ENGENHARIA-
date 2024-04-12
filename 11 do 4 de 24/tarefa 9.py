#Desenvolva um script em linguagem Python que leia dois valores numéricos inteiros
#para duas variáveis e que troque o conteúdo dessas variáveis, visualizando o valor das
#mesmas antes e depois da troca.

x = int(input("Valor de x => "))
y = int(input("Valor de y => "))
print(f"{x}  x antes")
print(f"{y}  y antes")
c = y
y = x
x = c 

print(f"{x} x depois")
print(f"{y} y depois")
